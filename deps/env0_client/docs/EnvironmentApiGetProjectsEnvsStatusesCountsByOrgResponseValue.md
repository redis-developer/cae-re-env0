# EnvironmentApiGetProjectsEnvsStatusesCountsByOrgResponseValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drift_status** | [**EnvironmentApiGetProjectsEnvsStatusesCountsByOrgResponseValueDriftStatus**](EnvironmentApiGetProjectsEnvsStatusesCountsByOrgResponseValueDriftStatus.md) |  | 
**created** | **float** |  | [optional] 
**inactive** | **float** |  | [optional] 
**active** | **float** |  | [optional] 
**failed** | **float** |  | [optional] 
**timeout** | **float** |  | [optional] 
**waiting_for_user** | **float** |  | [optional] 
**deploy_in_progress** | **float** |  | [optional] 
**destroy_in_progress** | **float** |  | [optional] 
**pr_plan_in_progress** | **float** |  | [optional] 
**remote_plan_in_progress** | **float** |  | [optional] 
**drift_detection_in_progress** | **float** |  | [optional] 
**task_in_progress** | **float** |  | [optional] 
**aborting** | **float** |  | [optional] 
**aborted** | **float** |  | [optional] 
**never_deployed** | **float** |  | [optional] 
**drifted** | **float** |  | [optional] 
**total** | **float** |  | 

## Example

```python
from env0_client.models.environment_api_get_projects_envs_statuses_counts_by_org_response_value import EnvironmentApiGetProjectsEnvsStatusesCountsByOrgResponseValue

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiGetProjectsEnvsStatusesCountsByOrgResponseValue from a JSON string
environment_api_get_projects_envs_statuses_counts_by_org_response_value_instance = EnvironmentApiGetProjectsEnvsStatusesCountsByOrgResponseValue.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiGetProjectsEnvsStatusesCountsByOrgResponseValue.to_json())

# convert the object into a dict
environment_api_get_projects_envs_statuses_counts_by_org_response_value_dict = environment_api_get_projects_envs_statuses_counts_by_org_response_value_instance.to_dict()
# create an instance of EnvironmentApiGetProjectsEnvsStatusesCountsByOrgResponseValue from a dict
environment_api_get_projects_envs_statuses_counts_by_org_response_value_from_dict = EnvironmentApiGetProjectsEnvsStatusesCountsByOrgResponseValue.from_dict(environment_api_get_projects_envs_statuses_counts_by_org_response_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


