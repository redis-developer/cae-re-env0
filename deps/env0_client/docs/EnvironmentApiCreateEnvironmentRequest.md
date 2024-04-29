# EnvironmentApiCreateEnvironmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**project_id** | **str** |  | 
**workspace_name** | **str** |  | [optional] 
**requires_approval** | **bool** |  | [optional] 
**ttl** | [**EnvironmentApiTTLRequest**](EnvironmentApiTTLRequest.md) |  | [optional] 
**configuration_changes** | [**EnvironmentApiConfigurationChanges**](EnvironmentApiConfigurationChanges.md) |  | [optional] 
**vcs_commands_alias** | **str** |  | [optional] 
**deploy_request** | [**DeployRequest**](DeployRequest.md) |  | 
**continuous_deployment** | **bool** |  | [optional] 
**pull_request_plan_deployments** | **bool** |  | [optional] 
**drift_detection_request** | [**EnvironmentApiDriftDetectionRequest**](EnvironmentApiDriftDetectionRequest.md) |  | [optional] 
**auto_deploy_on_path_changes_only** | **bool** |  | [optional] 
**auto_deploy_by_custom_glob** | **str** |  | [optional] 
**terragrunt_working_directory** | **str** |  | [optional] 
**is_remote_backend** | **bool** |  | [optional] 
**k8s_namespace** | **str** |  | [optional] 
**prevent_auto_deploy** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.environment_api_create_environment_request import EnvironmentApiCreateEnvironmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiCreateEnvironmentRequest from a JSON string
environment_api_create_environment_request_instance = EnvironmentApiCreateEnvironmentRequest.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiCreateEnvironmentRequest.to_json())

# convert the object into a dict
environment_api_create_environment_request_dict = environment_api_create_environment_request_instance.to_dict()
# create an instance of EnvironmentApiCreateEnvironmentRequest from a dict
environment_api_create_environment_request_from_dict = EnvironmentApiCreateEnvironmentRequest.from_dict(environment_api_create_environment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


