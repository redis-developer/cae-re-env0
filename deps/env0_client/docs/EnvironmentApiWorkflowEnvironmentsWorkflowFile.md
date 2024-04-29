# EnvironmentApiWorkflowEnvironmentsWorkflowFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**WorkflowFileSettings**](WorkflowFileSettings.md) |  | [optional] 
**environments** | [**Dict[str, EnvironmentApiWorkflowEnvironmentsWorkflowSubEnvironment]**](EnvironmentApiWorkflowEnvironmentsWorkflowSubEnvironment.md) |  | 

## Example

```python
from env0_client.models.environment_api_workflow_environments_workflow_file import EnvironmentApiWorkflowEnvironmentsWorkflowFile

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiWorkflowEnvironmentsWorkflowFile from a JSON string
environment_api_workflow_environments_workflow_file_instance = EnvironmentApiWorkflowEnvironmentsWorkflowFile.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiWorkflowEnvironmentsWorkflowFile.to_json())

# convert the object into a dict
environment_api_workflow_environments_workflow_file_dict = environment_api_workflow_environments_workflow_file_instance.to_dict()
# create an instance of EnvironmentApiWorkflowEnvironmentsWorkflowFile from a dict
environment_api_workflow_environments_workflow_file_from_dict = EnvironmentApiWorkflowEnvironmentsWorkflowFile.from_dict(environment_api_workflow_environments_workflow_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


