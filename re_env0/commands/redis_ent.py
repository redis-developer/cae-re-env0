import json
import secrets
import enum

import backoff
import typer
from rich import print
from backoff import on_predicate
import requests

from ..console import console


class EndpointFormat(str, enum.Enum):
    redis_uri = "redis-uri"
    host_and_port = "host:port"


class RedisEnterpriseClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password

    def create_bdb(self, bdb_config):
        url = f"{self.base_url}/v1/bdbs"
        response = requests.post(
            url, auth=(self.username, self.password), json=bdb_config, verify=False
        )
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return response.json()

    def get_bdb(self, bdb_id):
        url = f"{self.base_url}/v1/bdbs/{bdb_id}"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.raise_for_status()
        return response.json()

    @on_predicate(
        backoff.constant,
        lambda b: b["status"] != "active",
        max_time=100,
        interval=10,
        jitter=None,
    )
    def wait_for_bdb(self, bdb_id):
        bdb = self.get_bdb(bdb_id)
        console.log(f"BDB {bdb_id} status: {bdb['status']}")
        return bdb

    def create_role(self, role_config):
        url = f"{self.base_url}/v1/roles"
        response = requests.post(
            url, auth=(self.username, self.password), json=role_config, verify=False
        )
        response.raise_for_status()
        return response.json()

    def get_roles(self):
        url = f"{self.base_url}/v1/roles"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.raise_for_status()
        return response.json()

    def create_user(self, user_config):
        url = f"{self.base_url}/v1/users"
        response = requests.post(
            url, auth=(self.username, self.password), json=user_config, verify=False
        )
        response.raise_for_status()
        return response.json()

    def create_acl(self, acl_config):
        url = f"{self.base_url}/redis_acls"
        response = requests.post(
            url, auth=(self.username, self.password), json=acl_config, verify=False
        )
        response.raise_for_status()
        return response.json()


def create_bdbs(
    env_config_path: str,
    bdb_config_path: str,
    cluster_index: int = 0,
    endpoint_format: EndpointFormat = EndpointFormat.redis_uri,
    endpoints_config_path: str = "endpoints.json",
):

    try:
        with open(env_config_path, "r") as f:
            env_config = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {env_config_path}")
        raise typer.Exit(code=1)

    if 'clusters' in env_config:
        try:
            env_config = env_config['clusters']['value'][cluster_index]
        except (IndexError, KeyError):
            print(f"Cluster index {cluster_index} is out of range or env0 output format is incorrect")
            raise typer.Exit(code=1)
    else:
        env_config = {key: output["value"] for key, output in env_config.items()}

    try:
        with open(bdb_config_path, "r") as f:
            bdb_configs = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {bdb_config_path}")
        raise typer.Exit(code=1)

    cluster_name = env_config["cluster_name"]

    api = RedisEnterpriseClient(
        f"https://{cluster_name}:9443",
        env_config["username"],
        env_config["password"],
    )

    created_endpoints = {}

    roles_to_users = {}

    if isinstance(bdb_configs, dict):
        roles = bdb_configs.pop("roles", None)
        users = bdb_configs.pop("users", None)
        acls = bdb_configs.pop("acls", None)
        bdb_configs = bdb_configs.pop("databases")

        if roles:
            for role in roles:
                try:
                    api.create_role(role)
                except requests.exceptions.RequestException as e:
                    print(f"Error creating role {role['name']}: {e}")
                    raise typer.Exit(code=1)

            print("Available roles: ", api.get_roles())

        if acls:
            for acl in acls:
                try:
                    api.create_acl(acl)
                except requests.exceptions.RequestException as e:
                    print(f"Error creating ACL {acl['name']}: {e}")
                    raise typer.Exit(code=1)

        if users:
            for user in users:
                try:
                    user["password"] = secrets.token_urlsafe(16)
                    api.create_user(user)

                    for role_id in user["role_uids"]:
                        roles_to_users[role_id] = {
                            "username": user["name"],
                            "password": user["password"],
                        }

                except requests.exceptions.RequestException as e:
                    print(f"Error creating user {user['name']}: {e}")
                    raise typer.Exit(code=1)

    for bdb_config in bdb_configs:
        console.log(f"Creating BDB: {bdb_config['name']}")

        if "roles_permissions" in bdb_config and bdb_config.get("default_user", True) is False:
            try:
                role_id = bdb_config["roles_permissions"][0]["role_uid"]
            except KeyError:
                print(f"Use 'role_permissions' to specify the role for the user")
                raise typer.Exit(code=1)
            try:
                user_name = roles_to_users[role_id]["username"]
                password = roles_to_users[role_id]["password"]
            except KeyError:
                print(
                    f"Role {role_id} is not defined in the roles section of the config file"
                )
                raise typer.Exit(code=1)
        else:
            user_name = "default"
            password = secrets.token_urlsafe(16)
            bdb_config["authentication_redis_pass"] = password

        try:
            bdb_object = api.create_bdb(bdb_config)

            created_endpoints[bdb_config["name"]] = {
                "bdb_id": bdb_object["uid"],
                "username": user_name,
                "password": password,
                "tls": bdb_object["ssl"],
            }

            console.log(
                f"Created BDB: {bdb_config['name']} with ID: {bdb_object['uid']}"
            )
        except requests.exceptions.RequestException as e:
            print(f"Error creating BDB {bdb_config['name']}: {e}")

    for bdb_name, bdb_obj in created_endpoints.items():
        bdb = api.wait_for_bdb(bdb_obj["bdb_id"])
        created_endpoints[bdb_name]["raw_endpoints"] = bdb["endpoints"]

        if endpoint_format == EndpointFormat.redis_uri:
            scheme = "rediss://" if bdb_obj["tls"] else "redis://"
        else:
            scheme = ""  # No scheme for host and port

        created_endpoints[bdb_name]["endpoints"] = [
            f"{scheme}{e['dns_name']}:{e['port']}" for e in bdb["endpoints"]
        ]

    try:
        with open(endpoints_config_path, "w") as json_file:
            json.dump(created_endpoints, json_file, indent=4)
    except Exception as e:
        console.log(f"Failed to write endpoints config: {e}")
        raise typer.Exit(code=1)

    console.log(f"Endpoint config was saved to: {endpoints_config_path}")
