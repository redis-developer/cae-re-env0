# BlueprintApiApprovalPolicyTemplateWithScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**scope** | [**BlueprintApiApprovalPolicyScope**](BlueprintApiApprovalPolicyScope.md) |  | 
**scope_id** | **str** |  | 
**blueprint** | [**BlueprintApiApprovalPolicyTemplate**](BlueprintApiApprovalPolicyTemplate.md) |  | 
**created_at** | **str** |  | 

## Example

```python
from env0_client.models.blueprint_api_approval_policy_template_with_scope import BlueprintApiApprovalPolicyTemplateWithScope

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiApprovalPolicyTemplateWithScope from a JSON string
blueprint_api_approval_policy_template_with_scope_instance = BlueprintApiApprovalPolicyTemplateWithScope.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiApprovalPolicyTemplateWithScope.to_json())

# convert the object into a dict
blueprint_api_approval_policy_template_with_scope_dict = blueprint_api_approval_policy_template_with_scope_instance.to_dict()
# create an instance of BlueprintApiApprovalPolicyTemplateWithScope from a dict
blueprint_api_approval_policy_template_with_scope_from_dict = BlueprintApiApprovalPolicyTemplateWithScope.from_dict(blueprint_api_approval_policy_template_with_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


