# EnvironmentApiCreateEnvironmentWithoutTemplateRequestBodyDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_deployment_id** | **str** |  | [optional] 
**deployment_type** | **object** |  | [optional] 
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

## Example

```python
from env0_client.models.environment_api_create_environment_without_template_request_body_deploy_request import EnvironmentApiCreateEnvironmentWithoutTemplateRequestBodyDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiCreateEnvironmentWithoutTemplateRequestBodyDeployRequest from a JSON string
environment_api_create_environment_without_template_request_body_deploy_request_instance = EnvironmentApiCreateEnvironmentWithoutTemplateRequestBodyDeployRequest.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiCreateEnvironmentWithoutTemplateRequestBodyDeployRequest.to_json())

# convert the object into a dict
environment_api_create_environment_without_template_request_body_deploy_request_dict = environment_api_create_environment_without_template_request_body_deploy_request_instance.to_dict()
# create an instance of EnvironmentApiCreateEnvironmentWithoutTemplateRequestBodyDeployRequest from a dict
environment_api_create_environment_without_template_request_body_deploy_request_from_dict = EnvironmentApiCreateEnvironmentWithoutTemplateRequestBodyDeployRequest.from_dict(environment_api_create_environment_without_template_request_body_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


