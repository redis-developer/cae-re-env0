# BlueprintApiApprovalPolicyQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**BlueprintApiApprovalPolicyScope**](BlueprintApiApprovalPolicyScope.md) |  | 
**scope_id** | **str** |  | 

## Example

```python
from env0_client.models.blueprint_api_approval_policy_query import BlueprintApiApprovalPolicyQuery

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiApprovalPolicyQuery from a JSON string
blueprint_api_approval_policy_query_instance = BlueprintApiApprovalPolicyQuery.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiApprovalPolicyQuery.to_json())

# convert the object into a dict
blueprint_api_approval_policy_query_dict = blueprint_api_approval_policy_query_instance.to_dict()
# create an instance of BlueprintApiApprovalPolicyQuery from a dict
blueprint_api_approval_policy_query_from_dict = BlueprintApiApprovalPolicyQuery.from_dict(blueprint_api_approval_policy_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


