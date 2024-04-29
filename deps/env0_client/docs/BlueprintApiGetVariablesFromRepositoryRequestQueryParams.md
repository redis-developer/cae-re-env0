# BlueprintApiGetVariablesFromRepositoryRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**repository** | **str** |  | 
**token_id** | **str** |  | [optional] 
**github_installation_id** | **str** |  | [optional] 
**ssh_key_ids** | **str** |  | [optional] 
**bitbucket_client_key** | **str** |  | [optional] 

## Example

```python
from env0_client.models.blueprint_api_get_variables_from_repository_request_query_params import BlueprintApiGetVariablesFromRepositoryRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiGetVariablesFromRepositoryRequestQueryParams from a JSON string
blueprint_api_get_variables_from_repository_request_query_params_instance = BlueprintApiGetVariablesFromRepositoryRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiGetVariablesFromRepositoryRequestQueryParams.to_json())

# convert the object into a dict
blueprint_api_get_variables_from_repository_request_query_params_dict = blueprint_api_get_variables_from_repository_request_query_params_instance.to_dict()
# create an instance of BlueprintApiGetVariablesFromRepositoryRequestQueryParams from a dict
blueprint_api_get_variables_from_repository_request_query_params_from_dict = BlueprintApiGetVariablesFromRepositoryRequestQueryParams.from_dict(blueprint_api_get_variables_from_repository_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


