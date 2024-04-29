# EnvironmentApiEnvironmentLockStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**updated_by** | **str** |  | 
**updated_by_user** | [**User**](User.md) |  | [optional] 
**updated_at** | **datetime** |  | 

## Example

```python
from env0_client.models.environment_api_environment_lock_status import EnvironmentApiEnvironmentLockStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiEnvironmentLockStatus from a JSON string
environment_api_environment_lock_status_instance = EnvironmentApiEnvironmentLockStatus.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiEnvironmentLockStatus.to_json())

# convert the object into a dict
environment_api_environment_lock_status_dict = environment_api_environment_lock_status_instance.to_dict()
# create an instance of EnvironmentApiEnvironmentLockStatus from a dict
environment_api_environment_lock_status_from_dict = EnvironmentApiEnvironmentLockStatus.from_dict(environment_api_environment_lock_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


