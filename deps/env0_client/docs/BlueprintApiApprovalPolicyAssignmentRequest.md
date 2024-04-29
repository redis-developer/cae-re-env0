# BlueprintApiApprovalPolicyAssignmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**BlueprintApiApprovalPolicyScope**](BlueprintApiApprovalPolicyScope.md) |  | 
**scope_id** | **str** |  | 
**blueprint_id** | **str** |  | 

## Example

```python
from env0_client.models.blueprint_api_approval_policy_assignment_request import BlueprintApiApprovalPolicyAssignmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiApprovalPolicyAssignmentRequest from a JSON string
blueprint_api_approval_policy_assignment_request_instance = BlueprintApiApprovalPolicyAssignmentRequest.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiApprovalPolicyAssignmentRequest.to_json())

# convert the object into a dict
blueprint_api_approval_policy_assignment_request_dict = blueprint_api_approval_policy_assignment_request_instance.to_dict()
# create an instance of BlueprintApiApprovalPolicyAssignmentRequest from a dict
blueprint_api_approval_policy_assignment_request_from_dict = BlueprintApiApprovalPolicyAssignmentRequest.from_dict(blueprint_api_approval_policy_assignment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


