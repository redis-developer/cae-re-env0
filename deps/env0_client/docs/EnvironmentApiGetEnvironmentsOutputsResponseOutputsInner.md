# EnvironmentApiGetEnvironmentsOutputsResponseOutputsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**environment_id** | **str** |  | 
**name** | **str** |  | 
**is_sensitive** | **bool** |  | 
**environment_name** | **str** |  | 

## Example

```python
from env0_client.models.environment_api_get_environments_outputs_response_outputs_inner import EnvironmentApiGetEnvironmentsOutputsResponseOutputsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiGetEnvironmentsOutputsResponseOutputsInner from a JSON string
environment_api_get_environments_outputs_response_outputs_inner_instance = EnvironmentApiGetEnvironmentsOutputsResponseOutputsInner.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiGetEnvironmentsOutputsResponseOutputsInner.to_json())

# convert the object into a dict
environment_api_get_environments_outputs_response_outputs_inner_dict = environment_api_get_environments_outputs_response_outputs_inner_instance.to_dict()
# create an instance of EnvironmentApiGetEnvironmentsOutputsResponseOutputsInner from a dict
environment_api_get_environments_outputs_response_outputs_inner_from_dict = EnvironmentApiGetEnvironmentsOutputsResponseOutputsInner.from_dict(environment_api_get_environments_outputs_response_outputs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


