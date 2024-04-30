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


def create_bdbs(
    env_config_path: str,
    bdb_config_path: str,
    endpoint_format: EndpointFormat = EndpointFormat.redis_uri,
    endpoints_config_path: str = "endpoints.json",
):

    try:
        with open(env_config_path, "r") as f:
            env_config = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {env_config_path}")
        raise typer.Exit(code=1)

    try:
        with open(bdb_config_path, "r") as f:
            bdb_configs = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {bdb_config_path}")
        raise typer.Exit(code=1)

    cluster_name = env_config["cluster_name"]["value"]

    api = RedisEnterpriseClient(
        f"https://{cluster_name}:9443",
        env_config["username"]["value"],
        env_config["password"]["value"],
    )

    created_endpoints = {}

    for bdb_config in bdb_configs:
        console.log(f"Creating BDB: {bdb_config['name']}")

        password = secrets.token_urlsafe(16)
        bdb_config["authentication_redis_pass"] = password

        try:
            bdb_object = api.create_bdb(bdb_config)

            created_endpoints[bdb_config["name"]] = {
                "bdb_id": bdb_object["uid"],
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
