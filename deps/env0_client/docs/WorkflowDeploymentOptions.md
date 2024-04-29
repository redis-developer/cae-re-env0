# WorkflowDeploymentOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **str** |  | 
**operation** | [**WorkflowPartialDeployOperation**](WorkflowPartialDeployOperation.md) |  | 

## Example

```python
from env0_client.models.workflow_deployment_options import WorkflowDeploymentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowDeploymentOptions from a JSON string
workflow_deployment_options_instance = WorkflowDeploymentOptions.from_json(json)
# print the JSON string representation of the object
print(WorkflowDeploymentOptions.to_json())

# convert the object into a dict
workflow_deployment_options_dict = workflow_deployment_options_instance.to_dict()
# create an instance of WorkflowDeploymentOptions from a dict
workflow_deployment_options_from_dict = WorkflowDeploymentOptions.from_dict(workflow_deployment_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


