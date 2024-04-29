# ModuleTestingApiFullModuleTestRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**EnvironmentApiDeploymentLogStatus**](EnvironmentApiDeploymentLogStatus.md) |  | [optional] 
**blueprint_revision** | **str** |  | [optional] 
**pr_number** | **str** |  | [optional] 
**started_by** | **str** |  | [optional] 
**started_by_user** | [**User**](User.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**queued_at** | **datetime** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**error** | **object** |  | [optional] 
**custom_env0_environment_variables** | [**CustomEnv0EnvironmentVariables**](CustomEnv0EnvironmentVariables.md) |  | [optional] 
**git_avatar_url** | **str** |  | [optional] 
**git_user** | **str** |  | [optional] 
**blueprint_repository** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**deployment_log_id** | **str** |  | 
**environment_id** | **str** |  | 
**organization_id** | **str** |  | 
**trigger_name** | [**TriggerName**](TriggerName.md) |  | [optional] 
**test_summary** | [**ModuleTestingApiTestFileSummary**](ModuleTestingApiTestFileSummary.md) |  | [optional] 
**test_files_results** | [**Dict[str, ModuleTestingApiTestFileResult]**](ModuleTestingApiTestFileResult.md) |  | [optional] 
**module_id** | **str** |  | [optional] 

## Example

```python
from env0_client.models.module_testing_api_full_module_test_run import ModuleTestingApiFullModuleTestRun

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleTestingApiFullModuleTestRun from a JSON string
module_testing_api_full_module_test_run_instance = ModuleTestingApiFullModuleTestRun.from_json(json)
# print the JSON string representation of the object
print(ModuleTestingApiFullModuleTestRun.to_json())

# convert the object into a dict
module_testing_api_full_module_test_run_dict = module_testing_api_full_module_test_run_instance.to_dict()
# create an instance of ModuleTestingApiFullModuleTestRun from a dict
module_testing_api_full_module_test_run_from_dict = ModuleTestingApiFullModuleTestRun.from_dict(module_testing_api_full_module_test_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


