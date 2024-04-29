# EnvironmentApiWorkflowEnvironmentsWorkflowSubEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_id** | **str** |  | [optional] 
**to_destroy** | **bool** |  | [optional] 
**is_remote_backend** | **bool** |  | [optional] 
**k8s_namespace** | **str** |  | [optional] 
**name** | **str** |  | 
**template_name** | **str** |  | 
**template_id** | **str** |  | 
**template_type** | [**IacType**](IacType.md) |  | 
**revision** | **str** |  | [optional] 
**workspace** | **str** |  | [optional] 
**needs** | **List[str]** |  | [optional] 
**terragrunt_working_directory** | **str** |  | [optional] 
**disabled** | [**WorkflowSubEnvironmentDisabled**](WorkflowSubEnvironmentDisabled.md) |  | [optional] 

## Example

```python
from env0_client.models.environment_api_workflow_environments_workflow_sub_environment import EnvironmentApiWorkflowEnvironmentsWorkflowSubEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiWorkflowEnvironmentsWorkflowSubEnvironment from a JSON string
environment_api_workflow_environments_workflow_sub_environment_instance = EnvironmentApiWorkflowEnvironmentsWorkflowSubEnvironment.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiWorkflowEnvironmentsWorkflowSubEnvironment.to_json())

# convert the object into a dict
environment_api_workflow_environments_workflow_sub_environment_dict = environment_api_workflow_environments_workflow_sub_environment_instance.to_dict()
# create an instance of EnvironmentApiWorkflowEnvironmentsWorkflowSubEnvironment from a dict
environment_api_workflow_environments_workflow_sub_environment_from_dict = EnvironmentApiWorkflowEnvironmentsWorkflowSubEnvironment.from_dict(environment_api_workflow_environments_workflow_sub_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


