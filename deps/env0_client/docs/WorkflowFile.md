# WorkflowFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environments** | [**Dict[str, WorkflowSubEnvironment]**](WorkflowSubEnvironment.md) |  | 
**settings** | [**WorkflowFileSettings**](WorkflowFileSettings.md) |  | [optional] 

## Example

```python
from env0_client.models.workflow_file import WorkflowFile

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowFile from a JSON string
workflow_file_instance = WorkflowFile.from_json(json)
# print the JSON string representation of the object
print(WorkflowFile.to_json())

# convert the object into a dict
workflow_file_dict = workflow_file_instance.to_dict()
# create an instance of WorkflowFile from a dict
workflow_file_from_dict = WorkflowFile.from_dict(workflow_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


