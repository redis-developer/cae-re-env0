# EnvironmentApiUpdateRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**requires_approval** | **bool** |  | [optional] 
**is_archived** | **bool** | Mark the environment as inactive | [optional] 
**continuous_deployment** | **bool** |  | [optional] 
**vcs_commands_alias** | **str** |  | [optional] 
**pull_request_plan_deployments** | **bool** |  | [optional] 
**auto_deploy_on_path_changes_only** | **bool** |  | [optional] 
**auto_deploy_by_custom_glob** | **str** |  | [optional] 
**is_remote_backend** | **bool** |  | [optional] 
**is_remote_apply_enabled** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.environment_api_update_request_body import EnvironmentApiUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiUpdateRequestBody from a JSON string
environment_api_update_request_body_instance = EnvironmentApiUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiUpdateRequestBody.to_json())

# convert the object into a dict
environment_api_update_request_body_dict = environment_api_update_request_body_instance.to_dict()
# create an instance of EnvironmentApiUpdateRequestBody from a dict
environment_api_update_request_body_from_dict = EnvironmentApiUpdateRequestBody.from_dict(environment_api_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


