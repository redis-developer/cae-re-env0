# EnvironmentApiEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**name** | **str** |  | 
**organization_id** | **str** |  | 
**project_id** | **str** |  | 
**user_id** | **str** |  | 
**workspace_name** | **str** |  | 
**user** | [**User**](User.md) |  | [optional] 
**requires_approval** | **bool** |  | 
**status** | [**EnvironmentApiEnvironmentStatus**](EnvironmentApiEnvironmentStatus.md) |  | 
**latest_deployment_log_id** | **str** |  | 
**latest_deployment_log** | [**EnvironmentApiDeploymentLog**](EnvironmentApiDeploymentLog.md) |  | 
**lifespan_end_at** | **datetime** |  | 
**marked_for_auto_destroy** | [**AutoDestroyStatus**](AutoDestroyStatus.md) |  | 
**is_archived** | **bool** | Mark the environment as inactive | 
**next_scheduled_dates** | [**EnvironmentApiEnvironmentNextScheduledDates**](EnvironmentApiEnvironmentNextScheduledDates.md) |  | [optional] 
**vcs_commands_alias** | **str** |  | [optional] 
**continuous_deployment** | **bool** |  | 
**pull_request_plan_deployments** | **bool** |  | 
**auto_deploy_on_path_changes_only** | **bool** |  | 
**auto_deploy_by_custom_glob** | **str** |  | [optional] 
**terragrunt_working_directory** | **str** |  | [optional] 
**is_single_use_blueprint** | **bool** |  | [optional] 
**workflow_environment_id** | **str** |  | [optional] 
**is_remote_backend** | **bool** |  | 
**is_locked** | **bool** |  | 
**lock_status** | [**EnvironmentApiEnvironmentLockStatus**](EnvironmentApiEnvironmentLockStatus.md) |  | [optional] 
**k8s_namespace** | **str** |  | [optional] 
**is_remote_apply_enabled** | **bool** |  | [optional] 
**drift_status** | [**EnvironmentApiDriftStatus**](EnvironmentApiDriftStatus.md) |  | 

## Example

```python
from env0_client.models.environment_api_environment import EnvironmentApiEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiEnvironment from a JSON string
environment_api_environment_instance = EnvironmentApiEnvironment.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiEnvironment.to_json())

# convert the object into a dict
environment_api_environment_dict = environment_api_environment_instance.to_dict()
# create an instance of EnvironmentApiEnvironment from a dict
environment_api_environment_from_dict = EnvironmentApiEnvironment.from_dict(environment_api_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


