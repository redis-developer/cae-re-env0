# BlueprintApiCustomFlowAssignmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**Scope**](Scope.md) |  | 
**order** | **float** | Determines the execution order of the assigned custom flow, with lower numbers being executed first. If not provided, the assigned custom flow will be executed last. If multiple assignments have the same order number, their custom flows execution order is chosen randomly. | [optional] 
**scope_id** | **str** |  | 
**blueprint_id** | **str** |  | 

## Example

```python
from env0_client.models.blueprint_api_custom_flow_assignment_request import BlueprintApiCustomFlowAssignmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiCustomFlowAssignmentRequest from a JSON string
blueprint_api_custom_flow_assignment_request_instance = BlueprintApiCustomFlowAssignmentRequest.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiCustomFlowAssignmentRequest.to_json())

# convert the object into a dict
blueprint_api_custom_flow_assignment_request_dict = blueprint_api_custom_flow_assignment_request_instance.to_dict()
# create an instance of BlueprintApiCustomFlowAssignmentRequest from a dict
blueprint_api_custom_flow_assignment_request_from_dict = BlueprintApiCustomFlowAssignmentRequest.from_dict(blueprint_api_custom_flow_assignment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


