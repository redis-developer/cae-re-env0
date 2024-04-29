# WorkflowSubEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from env0_client.models.workflow_sub_environment import WorkflowSubEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSubEnvironment from a JSON string
workflow_sub_environment_instance = WorkflowSubEnvironment.from_json(json)
# print the JSON string representation of the object
print(WorkflowSubEnvironment.to_json())

# convert the object into a dict
workflow_sub_environment_dict = workflow_sub_environment_instance.to_dict()
# create an instance of WorkflowSubEnvironment from a dict
workflow_sub_environment_from_dict = WorkflowSubEnvironment.from_dict(workflow_sub_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


