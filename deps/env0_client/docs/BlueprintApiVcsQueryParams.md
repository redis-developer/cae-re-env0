# BlueprintApiVcsQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** |  | 
**token_id** | **str** |  | [optional] 
**github_installation_id** | **str** |  | [optional] 
**ssh_key_ids** | **str** |  | [optional] 
**bitbucket_client_key** | **str** |  | [optional] 

## Example

```python
from env0_client.models.blueprint_api_vcs_query_params import BlueprintApiVcsQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiVcsQueryParams from a JSON string
blueprint_api_vcs_query_params_instance = BlueprintApiVcsQueryParams.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiVcsQueryParams.to_json())

# convert the object into a dict
blueprint_api_vcs_query_params_dict = blueprint_api_vcs_query_params_instance.to_dict()
# create an instance of BlueprintApiVcsQueryParams from a dict
blueprint_api_vcs_query_params_from_dict = BlueprintApiVcsQueryParams.from_dict(blueprint_api_vcs_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


