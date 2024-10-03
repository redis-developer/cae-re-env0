import json

import typer
from requests import HTTPError
from rich import print

from ..console import console
from re_fault_injector.deps.re_env0.re_env0.re_utils.client import RedisEnterpriseClient, CertificateType
from re_fault_injector.deps.re_env0.re_env0.re_utils.provisioner import REProvisioner, EndpointFormat


def create_bdbs(
    env_config_path: str,
    bdb_config_path: str,
    cluster_index: int = 0,
    endpoint_format: EndpointFormat = EndpointFormat.redis_uri,
    endpoints_config_path: str = "endpoints.json",
):
    env_config, clusters_config = parse_env_config(env_config_path, cluster_index)

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

    manager = REProvisioner(api)

    try:
        created_endpoints = manager.provision(bdb_configs, endpoint_format, clusters_config)
    except RuntimeError as e:
        console.log(f"Failed to create databases: {e}")
        raise typer.Exit(code=1)

    api_cache = {}

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

        if bdb["crdt"]:
            # TODO: find a cleaner way to retrieve all endpoints
            crdb = api.get_crdb(bdb["crdt_guid"])
            crdb_endpoints = []

            for instance in crdb["instances"]:
                if instance["cluster"]["name"] == cluster_name:
                    continue

                cluster_api = api_cache.get(
                    instance["cluster"]["name"],
                    RedisEnterpriseClient(
                        instance["cluster"]["url"],
                        env_config["username"],
                        env_config["password"],
                    ),
                )
                crdb_obj = cluster_api.get_crdb(bdb["crdt_guid"])

                for local_bdb in crdb_obj["local_databases"]:
                    local_bdb_object = cluster_api.wait_for_bdb(local_bdb["bdb_uid"])
                    crdb_endpoints.extend(
                        [
                            f"{scheme}{e['dns_name']}:{e['port']}"
                            for e in local_bdb_object["endpoints"]
                        ]
                    )

            created_endpoints[bdb_name]["endpoints"].extend(crdb_endpoints)

    try:
        with open(endpoints_config_path, "w") as json_file:
            json.dump(created_endpoints, json_file, indent=4)
    except Exception as e:
        console.log(f"Failed to write endpoints config: {e}")
        raise typer.Exit(code=1)

    console.log(f"Endpoint config was saved to: {endpoints_config_path}")


def upload_certificate(
    env_config_path: str,
    certificate_path: str,
    private_key_path: str = "",
    certificate_type: CertificateType = CertificateType.proxy,
    cluster_index: int = 0,
):
    env_config, clusters_config = parse_env_config(env_config_path, cluster_index)

    private_key = None

    if private_key_path:
        with open(private_key_path, "r") as f:
            private_key = f.read()

    with open(certificate_path, "r") as f:
        certificate = f.read()

    api = RedisEnterpriseClient(
        f"https://{env_config['cluster_name']}:9443",
        env_config["username"],
        env_config["password"],
    )

    try:
        api.update_tls_certificate(certificate_type, certificate, private_key)
    except HTTPError as e:
        console.log(f"Failed to update certificate: {e}")
        raise typer.Exit(code=1)

    console.log(f"Certificate was updated")


def parse_env_config(env_config_path: str, cluster_index: int = 0):
    try:
        with open(env_config_path, "r") as f:
            env_config = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {env_config_path}")
        raise typer.Exit(code=1)

    clusters_config = None

    if "clusters" in env_config:
        try:
            clusters_config = env_config["clusters"]["value"]
            env_config = clusters_config[cluster_index]
        except (IndexError, KeyError):
            print(
                f"Cluster index {cluster_index} is out of range or env0 output format is incorrect"
            )
            raise typer.Exit(code=1)
    else:
        env_config = {key: output["value"] for key, output in env_config.items()}

    return env_config, clusters_config
