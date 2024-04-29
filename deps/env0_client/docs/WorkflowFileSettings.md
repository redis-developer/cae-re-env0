# WorkflowFileSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_removal_strategy** | **object** |  | [optional] 

## Example

```python
from env0_client.models.workflow_file_settings import WorkflowFileSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowFileSettings from a JSON string
workflow_file_settings_instance = WorkflowFileSettings.from_json(json)
# print the JSON string representation of the object
print(WorkflowFileSettings.to_json())

# convert the object into a dict
workflow_file_settings_dict = workflow_file_settings_instance.to_dict()
# create an instance of WorkflowFileSettings from a dict
workflow_file_settings_from_dict = WorkflowFileSettings.from_dict(workflow_file_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


