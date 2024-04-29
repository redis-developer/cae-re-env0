# ConfigurationApiFindVariablesByScopeRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | [optional] 
**set_id** | **str** |  | [optional] 
**blueprint_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**workflow_environment_id** | **str** |  | [optional] 
**deployment_log_id** | **str** |  | [optional] 
**workflow_blueprint_id** | **str** |  | [optional] 

## Example

```python
from env0_client.models.configuration_api_find_variables_by_scope_request_query_params import ConfigurationApiFindVariablesByScopeRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationApiFindVariablesByScopeRequestQueryParams from a JSON string
configuration_api_find_variables_by_scope_request_query_params_instance = ConfigurationApiFindVariablesByScopeRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(ConfigurationApiFindVariablesByScopeRequestQueryParams.to_json())

# convert the object into a dict
configuration_api_find_variables_by_scope_request_query_params_dict = configuration_api_find_variables_by_scope_request_query_params_instance.to_dict()
# create an instance of ConfigurationApiFindVariablesByScopeRequestQueryParams from a dict
configuration_api_find_variables_by_scope_request_query_params_from_dict = ConfigurationApiFindVariablesByScopeRequestQueryParams.from_dict(configuration_api_find_variables_by_scope_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


