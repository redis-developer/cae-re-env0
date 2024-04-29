# EnvironmentApiEnvironmentResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**type** | **str** |  | 
**name** | **str** |  | 
**module_name** | **str** |  | [optional] 

## Example

```python
from env0_client.models.environment_api_environment_resource import EnvironmentApiEnvironmentResource

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiEnvironmentResource from a JSON string
environment_api_environment_resource_instance = EnvironmentApiEnvironmentResource.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiEnvironmentResource.to_json())

# convert the object into a dict
environment_api_environment_resource_dict = environment_api_environment_resource_instance.to_dict()
# create an instance of EnvironmentApiEnvironmentResource from a dict
environment_api_environment_resource_from_dict = EnvironmentApiEnvironmentResource.from_dict(environment_api_environment_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


