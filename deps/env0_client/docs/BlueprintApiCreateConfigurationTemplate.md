# BlueprintApiCreateConfigurationTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**repository** | **str** |  | 
**revision** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**organization_id** | **str** |  | 
**token_name** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**github_installation_id** | **float** |  | [optional] 
**bitbucket_client_key** | **str** |  | [optional] 
**is_bitbucket_server** | **bool** |  | [optional] 
**is_git_lab_enterprise** | **bool** |  | [optional] 
**is_git_hub_enterprise** | **bool** |  | [optional] 
**is_git_lab** | **bool** |  | [optional] 
**is_azure_dev_ops** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.blueprint_api_create_configuration_template import BlueprintApiCreateConfigurationTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiCreateConfigurationTemplate from a JSON string
blueprint_api_create_configuration_template_instance = BlueprintApiCreateConfigurationTemplate.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiCreateConfigurationTemplate.to_json())

# convert the object into a dict
blueprint_api_create_configuration_template_dict = blueprint_api_create_configuration_template_instance.to_dict()
# create an instance of BlueprintApiCreateConfigurationTemplate from a dict
blueprint_api_create_configuration_template_from_dict = BlueprintApiCreateConfigurationTemplate.from_dict(blueprint_api_create_configuration_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


