# BlueprintApiCustomFlowTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**BlueprintApiCustomFlowTemplateType**](BlueprintApiCustomFlowTemplateType.md) |  | 
**name** | **str** |  | 
**repository** | **str** |  | 
**revision** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**token_name** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**github_installation_id** | **float** |  | [optional] 
**bitbucket_client_key** | **str** |  | [optional] 
**is_bitbucket_server** | **bool** |  | [optional] 
**is_git_lab_enterprise** | **bool** |  | [optional] 
**is_git_hub_enterprise** | **bool** |  | [optional] 
**is_git_lab** | **bool** |  | [optional] 
**is_azure_dev_ops** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**author** | [**User**](User.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**author_id** | **str** |  | [optional] 
**organization_id** | **str** |  | 
**project_id** | **str** |  | [optional] 

## Example

```python
from env0_client.models.blueprint_api_custom_flow_template import BlueprintApiCustomFlowTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiCustomFlowTemplate from a JSON string
blueprint_api_custom_flow_template_instance = BlueprintApiCustomFlowTemplate.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiCustomFlowTemplate.to_json())

# convert the object into a dict
blueprint_api_custom_flow_template_dict = blueprint_api_custom_flow_template_instance.to_dict()
# create an instance of BlueprintApiCustomFlowTemplate from a dict
blueprint_api_custom_flow_template_from_dict = BlueprintApiCustomFlowTemplate.from_dict(blueprint_api_custom_flow_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


