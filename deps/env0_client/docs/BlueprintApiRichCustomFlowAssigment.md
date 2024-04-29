# BlueprintApiRichCustomFlowAssigment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_id** | **str** |  | 
**blueprint_id** | **str** |  | 
**hash** | **str** |  | [optional] 
**scope** | [**Scope**](Scope.md) |  | 
**organization_id** | **str** |  | 
**order** | **float** |  | [optional] 
**custom_flow_template** | [**BlueprintApiCustomFlowTemplate**](BlueprintApiCustomFlowTemplate.md) |  | 

## Example

```python
from env0_client.models.blueprint_api_rich_custom_flow_assigment import BlueprintApiRichCustomFlowAssigment

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiRichCustomFlowAssigment from a JSON string
blueprint_api_rich_custom_flow_assigment_instance = BlueprintApiRichCustomFlowAssigment.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiRichCustomFlowAssigment.to_json())

# convert the object into a dict
blueprint_api_rich_custom_flow_assigment_dict = blueprint_api_rich_custom_flow_assigment_instance.to_dict()
# create an instance of BlueprintApiRichCustomFlowAssigment from a dict
blueprint_api_rich_custom_flow_assigment_from_dict = BlueprintApiRichCustomFlowAssigment.from_dict(blueprint_api_rich_custom_flow_assigment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


