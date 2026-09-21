# RE Env0 Toolbox

CLI tool for creating RE clusters with env0.

## Installation

1. Install Python3 and pip

2. Install the package using pip:
```bash
pip install git+https://github.com/redis-developer/cae-re-env0.git
```

## Usage

Define the following environment variables:
```bash
export ENV0_API_KEY = "..."
export ENV0_API_KEY_SECRET = "..."
export ENV0_PROJECT_ID = "..."
```

### Creating a new environment using the template/blueprint

1. Define all required template parameters in the `params.json` file.
2. Run the following command:
```bash
re-env0 create-env NAME_HERE ENV0_TEMPLATE_ID params.json
```
3. The command will same the env0 output file as `env_output.json`


### Creating BDBs in RE
Once the environment is created, you can create BDBs.

1. Define all required BDBs parameters in the `bdbs.json` file.
2. Run the following command:
```bash
re-env create-bdbs env_output.json bdbs.json
```
3. The command will save the created endpoints to `endpoints.json`

Each database entry also carries a `discovery_endpoints` list with the address of the Redis
Enterprise discovery service (Sentinel-compatible API) on every cluster node:

```json
"discovery_endpoints": [
    "34.244.146.73:8001",
    "18.201.54.148:8001",
    "54.78.167.171:8001"
]
```

Clients that discover a database through that service need one address per node: the service runs
on all of them and keeps answering after a database endpoint moves to another node. The external
node address is used when there is one, the internal address otherwise. The field is omitted when
the cluster nodes cannot be read.


### Uploading TLS certificates
```bash
re-env upload-certificate [OPTIONS] ENV_CONFIG_PATH CERTIFICATE_PATH
```

**Arguments**:

* `ENV_CONFIG_PATH`: [required]
* `CERTIFICATE_PATH`: [required]

**Options**:

* `--private-key-path TEXT`
* `--certificate-type [proxy|api|cm|ldap_client|metrics_exporter|syncer]`: [default: proxy]
* `--cluster-index INTEGER`: [default: 0]
