# EnvironmentApiDeploymentLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**type** | [**EnvironmentApiDeploymentType**](EnvironmentApiDeploymentType.md) |  | 
**started_by** | **str** |  | [optional] 
**queued_at** | **datetime** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**output** | [**EnvironmentApiDeploymentLogOutput**](EnvironmentApiDeploymentLogOutput.md) |  | [optional] 
**error** | **object** |  | [optional] 
**custom_env0_environment_variables** | [**CustomEnv0EnvironmentVariables**](CustomEnv0EnvironmentVariables.md) |  | [optional] 
**cost_estimation** | [**InfracostTotalOutput**](InfracostTotalOutput.md) |  | [optional] 
**status** | [**EnvironmentApiDeploymentLogStatus**](EnvironmentApiDeploymentLogStatus.md) |  | [optional] 
**blueprint_id** | **str** |  | [optional] 
**blueprint_name** | **str** |  | [optional] 
**blueprint_repository** | **str** |  | [optional] 
**blueprint_revision** | **str** |  | [optional] 
**blueprint_path** | **str** |  | [optional] 
**blueprint_type** | [**DeployableType**](DeployableType.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**resource_count** | **float** |  | [optional] 
**resources** | [**List[EnvironmentApiEnvironmentResource]**](EnvironmentApiEnvironmentResource.md) |  | [optional] 
**started_by_user** | [**User**](User.md) |  | [optional] 
**is_scheduled_run** | **bool** |  | [optional] 
**aborted_by** | **str** |  | [optional] 
**aborted_by_user** | [**User**](User.md) |  | [optional] 
**git_user** | **str** |  | [optional] 
**git_avatar_url** | **str** |  | [optional] 
**pr_number** | **str** |  | [optional] 
**trigger_name** | [**TriggerName**](TriggerName.md) |  | [optional] 
**drift_detected** | **bool** |  | [optional] 
**plan** | [**EnvironmentApiDeploymentLogPlan**](EnvironmentApiDeploymentLogPlan.md) |  | [optional] 
**plan_summary** | [**DeploymentApiPlanPlanSummary**](DeploymentApiPlanPlanSummary.md) |  | [optional] 
**is_skipped_apply** | **bool** |  | [optional] 
**workflow_deployment_id** | **str** |  | [optional] 
**workflow_file** | [**EnvironmentApiWorkflowEnvironmentsWorkflowFile**](EnvironmentApiWorkflowEnvironmentsWorkflowFile.md) |  | [optional] 
**workflow_deployment_options** | [**WorkflowDeploymentOptions**](WorkflowDeploymentOptions.md) |  | [optional] 
**state_version_id** | **str** |  | [optional] 
**reviewers_users** | [**List[EnvironmentApiReviewerUser]**](EnvironmentApiReviewerUser.md) |  | [optional] 
**reviewers** | [**List[EnvironmentApiReviewer]**](EnvironmentApiReviewer.md) |  | [optional] 
**reviewed_by** | **str** |  | [optional] 
**reviewed_by_user** | [**User**](User.md) |  | [optional] 
**targets** | **List[str]** |  | [optional] 

## Example

```python
from env0_client.models.environment_api_deployment_log import EnvironmentApiDeploymentLog

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiDeploymentLog from a JSON string
environment_api_deployment_log_instance = EnvironmentApiDeploymentLog.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiDeploymentLog.to_json())

# convert the object into a dict
environment_api_deployment_log_dict = environment_api_deployment_log_instance.to_dict()
# create an instance of EnvironmentApiDeploymentLog from a dict
environment_api_deployment_log_from_dict = EnvironmentApiDeploymentLog.from_dict(environment_api_deployment_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


