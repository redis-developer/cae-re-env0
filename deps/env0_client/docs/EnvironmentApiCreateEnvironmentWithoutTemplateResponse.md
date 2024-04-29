# EnvironmentApiCreateEnvironmentWithoutTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blueprint_id** | **str** |  | 
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
from env0_client.models.environment_api_create_environment_without_template_response import EnvironmentApiCreateEnvironmentWithoutTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiCreateEnvironmentWithoutTemplateResponse from a JSON string
environment_api_create_environment_without_template_response_instance = EnvironmentApiCreateEnvironmentWithoutTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiCreateEnvironmentWithoutTemplateResponse.to_json())

# convert the object into a dict
environment_api_create_environment_without_template_response_dict = environment_api_create_environment_without_template_response_instance.to_dict()
# create an instance of EnvironmentApiCreateEnvironmentWithoutTemplateResponse from a dict
environment_api_create_environment_without_template_response_from_dict = EnvironmentApiCreateEnvironmentWithoutTemplateResponse.from_dict(environment_api_create_environment_without_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


