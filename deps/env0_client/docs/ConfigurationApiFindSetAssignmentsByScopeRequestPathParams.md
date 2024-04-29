# ConfigurationApiFindSetAssignmentsByScopeRequestPathParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**ConfigurationSetAssignmentScope**](ConfigurationSetAssignmentScope.md) |  | 
**scope_id** | **str** |  | 

## Example

```python
from env0_client.models.configuration_api_find_set_assignments_by_scope_request_path_params import ConfigurationApiFindSetAssignmentsByScopeRequestPathParams

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationApiFindSetAssignmentsByScopeRequestPathParams from a JSON string
configuration_api_find_set_assignments_by_scope_request_path_params_instance = ConfigurationApiFindSetAssignmentsByScopeRequestPathParams.from_json(json)
# print the JSON string representation of the object
print(ConfigurationApiFindSetAssignmentsByScopeRequestPathParams.to_json())

# convert the object into a dict
configuration_api_find_set_assignments_by_scope_request_path_params_dict = configuration_api_find_set_assignments_by_scope_request_path_params_instance.to_dict()
# create an instance of ConfigurationApiFindSetAssignmentsByScopeRequestPathParams from a dict
configuration_api_find_set_assignments_by_scope_request_path_params_from_dict = ConfigurationApiFindSetAssignmentsByScopeRequestPathParams.from_dict(configuration_api_find_set_assignments_by_scope_request_path_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


