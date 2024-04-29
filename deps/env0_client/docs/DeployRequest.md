# DeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_deployment_id** | **str** |  | [optional] 
**deployment_type** | **str** |  | [optional] 
**blueprint_id** | **str** |  | [optional] 
**blueprint_revision** | **str** |  | [optional] 
**blueprint_repository** | **str** |  | [optional] 
**configuration_changes** | [**EnvironmentApiConfigurationChanges**](EnvironmentApiConfigurationChanges.md) |  | [optional] 
**ttl** | [**EnvironmentApiTTLRequest**](EnvironmentApiTTLRequest.md) |  | [optional] 
**env_name** | **str** |  | [optional] 
**user_requires_approval** | **bool** |  | [optional] 
**targets** | **List[str]** |  | [optional] 
**custom_env0_environment_variables** | [**CustomEnv0EnvironmentVariables**](CustomEnv0EnvironmentVariables.md) |  | [optional] 
**git_user_data** | [**GitUserData**](GitUserData.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**trigger_name** | [**TriggerName**](TriggerName.md) |  | [optional] 
**upstream_environment_id** | **str** |  | [optional] 
**task_payload** | **str** |  | [optional] 
**sub_environments** | [**Dict[str, WorkflowSubEnvironmentRequest]**](WorkflowSubEnvironmentRequest.md) |  | [optional] 
**workflow_deployment_options** | [**WorkflowDeploymentOptions**](WorkflowDeploymentOptions.md) | [Optional] Only applicable when running a Workflow Environment. Allows to run a partial Workflow, starting from a specific point in the pipeline. Or run a single sub-environment deploy/destroy. | [optional] 

## Example

```python
from env0_client.models.deploy_request import DeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeployRequest from a JSON string
deploy_request_instance = DeployRequest.from_json(json)
# print the JSON string representation of the object
print(DeployRequest.to_json())

# convert the object into a dict
deploy_request_dict = deploy_request_instance.to_dict()
# create an instance of DeployRequest from a dict
deploy_request_from_dict = DeployRequest.from_dict(deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


