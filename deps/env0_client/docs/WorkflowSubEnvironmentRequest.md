# WorkflowSubEnvironmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **str** |  | [optional] 
**workspace_name** | **str** |  | [optional] 
**k8s_namespace** | **str** |  | [optional] 
**terragrunt_working_directory** | **str** |  | [optional] 
**configuration_changes** | [**EnvironmentApiConfigurationChanges**](EnvironmentApiConfigurationChanges.md) |  | [optional] 
**is_remote_backend** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.workflow_sub_environment_request import WorkflowSubEnvironmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSubEnvironmentRequest from a JSON string
workflow_sub_environment_request_instance = WorkflowSubEnvironmentRequest.from_json(json)
# print the JSON string representation of the object
print(WorkflowSubEnvironmentRequest.to_json())

# convert the object into a dict
workflow_sub_environment_request_dict = workflow_sub_environment_request_instance.to_dict()
# create an instance of WorkflowSubEnvironmentRequest from a dict
workflow_sub_environment_request_from_dict = WorkflowSubEnvironmentRequest.from_dict(workflow_sub_environment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


