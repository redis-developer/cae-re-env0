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
