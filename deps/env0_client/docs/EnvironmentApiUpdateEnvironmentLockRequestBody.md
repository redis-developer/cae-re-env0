# EnvironmentApiUpdateEnvironmentLockRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_locked** | **bool** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from env0_client.models.environment_api_update_environment_lock_request_body import EnvironmentApiUpdateEnvironmentLockRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiUpdateEnvironmentLockRequestBody from a JSON string
environment_api_update_environment_lock_request_body_instance = EnvironmentApiUpdateEnvironmentLockRequestBody.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiUpdateEnvironmentLockRequestBody.to_json())

# convert the object into a dict
environment_api_update_environment_lock_request_body_dict = environment_api_update_environment_lock_request_body_instance.to_dict()
# create an instance of EnvironmentApiUpdateEnvironmentLockRequestBody from a dict
environment_api_update_environment_lock_request_body_from_dict = EnvironmentApiUpdateEnvironmentLockRequestBody.from_dict(environment_api_update_environment_lock_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


