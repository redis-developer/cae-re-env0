# BlueprintApiExistingModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_name** | **str** | Module Name. Can be made of up to 64 characters, containing alphanumeric, hyphens and underscores. Must not contain leading/trailing hyphens/underscores. | 
**module_provider** | **str** | Module Provider. Can be made of up to 64 characters, containing lowercase alphanumeric characters only. | 
**module_test_enabled** | **bool** |  | [optional] 
**repository** | **str** |  | 
**description** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**token_name** | **str** |  | [optional] 
**github_installation_id** | **float** |  | [optional] 
**bitbucket_client_key** | **str** |  | [optional] 
**is_git_lab** | **bool** |  | [optional] 
**is_azure_dev_ops** | **bool** |  | [optional] 
**is_bitbucket_server** | **bool** |  | [optional] 
**is_git_hub_enterprise** | **bool** |  | [optional] 
**gitlab_project_id** | **float** |  | [optional] 
**path** | **str** |  | [optional] 
**run_tests_on_pull_request** | **bool** |  | [optional] 
**opentofu_version** | **str** |  | [optional] 
**tag_prefix** | **str** |  | [optional] 
**type** | **str** |  | 
**testing_environment_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**organization_id** | **str** |  | 
**author** | [**User**](User.md) |  | [optional] 
**author_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.blueprint_api_existing_module import BlueprintApiExistingModule

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiExistingModule from a JSON string
blueprint_api_existing_module_instance = BlueprintApiExistingModule.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiExistingModule.to_json())

# convert the object into a dict
blueprint_api_existing_module_dict = blueprint_api_existing_module_instance.to_dict()
# create an instance of BlueprintApiExistingModule from a dict
blueprint_api_existing_module_from_dict = BlueprintApiExistingModule.from_dict(blueprint_api_existing_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


