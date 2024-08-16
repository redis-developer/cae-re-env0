import json

import typer
from rich import print

from ...console import console
from .client import RedisEnterpriseClient
from .provisioner import REProvisioner, EndpointFormat


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

    created_endpoints = manager.provision(bdb_configs, endpoint_format, clusters_config)

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

        if bdb['crdt']:
            # TODO: find a cleaner way to retrieve all endpoints
            crdb = api.get_crdb(bdb['crdt_guid'])
            crdb_endpoints = []

            for instance in crdb["instances"]:
                if instance['cluster']['name'] == cluster_name:
                    continue

                cluster_api = api_cache.get(
                    instance['cluster']['name'],
                    RedisEnterpriseClient(
                        instance['cluster']['url'],
                        env_config["username"],
                        env_config["password"],
                    )
                )
                crdb_obj = cluster_api.get_crdb(bdb['crdt_guid'])

                for local_bdb in crdb_obj['local_databases']:
                    local_bdb_object = cluster_api.wait_for_bdb(local_bdb['bdb_uid'])
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
