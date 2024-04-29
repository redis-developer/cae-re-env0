# EnvironmentApiFindAllRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **str** |  | [optional] 
**offset** | **str** |  | [optional] 
**only_my** | **str** |  | [optional] 
**is_active** | **str** |  | [optional] 
**include_sub_environments** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**workspace_name** | **str** |  | [optional] 
**workspace_name_prefix** | **object** | filter by prefix of workspaceName, ignored when workspaceName is sent | [optional] 
**is_remote_backend** | **str** |  | [optional] 
**search_text** | **str** |  | [optional] 

## Example

```python
from env0_client.models.environment_api_find_all_request_query_params import EnvironmentApiFindAllRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiFindAllRequestQueryParams from a JSON string
environment_api_find_all_request_query_params_instance = EnvironmentApiFindAllRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiFindAllRequestQueryParams.to_json())

# convert the object into a dict
environment_api_find_all_request_query_params_dict = environment_api_find_all_request_query_params_instance.to_dict()
# create an instance of EnvironmentApiFindAllRequestQueryParams from a dict
environment_api_find_all_request_query_params_from_dict = EnvironmentApiFindAllRequestQueryParams.from_dict(environment_api_find_all_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


