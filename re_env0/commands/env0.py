import json

import backoff
import typer
import uuid
import env0_client
from env0_client.rest import ApiException
from rich import print
from backoff import on_predicate


from ..console import console
from ..env import Env


def random_id():
    return str(uuid.uuid4())[:8]


def create_env0_api_client():
    env0_configuration = env0_client.Configuration(
        host="https://api.env0.com",
        username=Env.val(Env.ENV0_API_KEY),
        password=Env.val(Env.ENV0_API_KEY_SECRET),
    )
    return env0_client.ApiClient(env0_configuration)


def create_env(
    env_name: str,
    blueprint_id: str,
    template_parameters_path: str,
    ttl_hours: int = 3,
    env_output_path: str = "env_output.json",
):
    try:
        with open(template_parameters_path, "r") as json_file:
            template_parameters = json.load(json_file)
    except FileNotFoundError:
        print(f"SSH key file not found: {template_parameters_path}")
        raise typer.Exit(code=1)

    params = [
        env0_client.models.EnvironmentApiConfigurationPropertyChange(
            name=key,
            type=1,
            value=(
                json.dumps(value)
                if isinstance(value, dict) or isinstance(value, bool)
                else str(value)
            ),
            schema={"format": "JSON" if isinstance(value, dict) else None},
        )
        for key, value in template_parameters.items()
    ]

    new_env_request = env0_client.models.EnvironmentApiCreateEnvironmentRequest(
        name=f"{env_name}-{random_id()}",
        project_id=Env.val(Env.ENV0_PROJECT_ID),
        requiresApproval=False,
        ttl=env0_client.models.EnvironmentApiTTLRequest(
            type=env0_client.models.EnvironmentApiTTLType.HOURS,
            value=str(ttl_hours),
        ),
        deploy_request=env0_client.models.DeployRequest(
            blueprintId=blueprint_id,
        ),
        continuousDeployment=False,
        pullRequestPlanDeployments=False,
        terragruntWorkingDirectory="",
        driftDetectionRequest=env0_client.models.EnvironmentApiDriftDetectionRequest(
            enabled=False,
        ),
        configurationChanges=env0_client.models.EnvironmentApiConfigurationChanges(
            actual_instance=params,
        ),
    )

    with create_env0_api_client() as api_client:
        api_instance = env0_client.EnvironmentsApi(api_client)

        try:
            console.log("Creating environment")
            api_response = api_instance.environments_create(new_env_request)

            if (
                api_response.status
                != env0_client.models.EnvironmentApiEnvironmentStatus.CREATED
            ):
                console.log(f"Environment creation failed:", api_response)
                return

        except ApiException as e:
            console.log(f"create_env: {e}\n")
            raise typer.Exit(code=1)

        console.log(f"Waiting for environment {api_response.id} to be created")

        @on_predicate(backoff.constant, max_time=600, interval=30, jitter=None)
        def wait_for_env():
            env = api_instance.environments_find_by_id(api_response.id)
            console.log(f"Environment status: {env.status}")

            if env.status == env0_client.models.EnvironmentApiEnvironmentStatus.FAILED:
                raise ValueError(env.status)

            return (
                env.status == env0_client.models.EnvironmentApiEnvironmentStatus.ACTIVE
            )

        try:
            wait_for_env()
        except ValueError as e:
            console.log(f"Environment creation failed: {e}")
            raise typer.Exit(code=1)

        env = api_instance.environments_find_by_id(api_response.id)

        try:
            with open(env_output_path, "w") as json_file:
                json.dump(
                    env.latest_deployment_log.output.to_dict(), json_file, indent=4
                )
        except Exception as e:
            console.log(f"Failed to write environment output: {e}")
            raise typer.Exit(code=1)

        console.log(f"Environment output was saved to: {env_output_path}")


def get_env(environment_id: str):
    with create_env0_api_client() as api_client:
        api_instance = env0_client.EnvironmentsApi(api_client)

        try:
            env = api_instance.environments_find_by_id(environment_id)
            print(env)
        except ApiException as e:
            console.log(f"create_env: {e}\n")
            return
