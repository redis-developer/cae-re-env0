# BlueprintApiApprovalPolicyAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_id** | **str** |  | 
**blueprint_id** | **str** |  | 
**hash** | **str** |  | [optional] 
**scope** | [**BlueprintApiApprovalPolicyScope**](BlueprintApiApprovalPolicyScope.md) |  | 

## Example

```python
from env0_client.models.blueprint_api_approval_policy_assignment import BlueprintApiApprovalPolicyAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiApprovalPolicyAssignment from a JSON string
blueprint_api_approval_policy_assignment_instance = BlueprintApiApprovalPolicyAssignment.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiApprovalPolicyAssignment.to_json())

# convert the object into a dict
blueprint_api_approval_policy_assignment_dict = blueprint_api_approval_policy_assignment_instance.to_dict()
# create an instance of BlueprintApiApprovalPolicyAssignment from a dict
blueprint_api_approval_policy_assignment_from_dict = BlueprintApiApprovalPolicyAssignment.from_dict(blueprint_api_approval_policy_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


