# EnvironmentApiGetEnvironmentsOutputsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outputs** | [**List[EnvironmentApiGetEnvironmentsOutputsResponseOutputsInner]**](EnvironmentApiGetEnvironmentsOutputsResponseOutputsInner.md) |  | 

## Example

```python
from env0_client.models.environment_api_get_environments_outputs_response import EnvironmentApiGetEnvironmentsOutputsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiGetEnvironmentsOutputsResponse from a JSON string
environment_api_get_environments_outputs_response_instance = EnvironmentApiGetEnvironmentsOutputsResponse.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiGetEnvironmentsOutputsResponse.to_json())

# convert the object into a dict
environment_api_get_environments_outputs_response_dict = environment_api_get_environments_outputs_response_instance.to_dict()
# create an instance of EnvironmentApiGetEnvironmentsOutputsResponse from a dict
environment_api_get_environments_outputs_response_from_dict = EnvironmentApiGetEnvironmentsOutputsResponse.from_dict(environment_api_get_environments_outputs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


