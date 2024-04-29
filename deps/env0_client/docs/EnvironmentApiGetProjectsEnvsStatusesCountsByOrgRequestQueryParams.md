# EnvironmentApiGetProjectsEnvsStatusesCountsByOrgRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**status** | **str** |  | [optional] 
**is_active** | **str** |  | [optional] 
**drift_status** | **str** |  | [optional] 

## Example

```python
from env0_client.models.environment_api_get_projects_envs_statuses_counts_by_org_request_query_params import EnvironmentApiGetProjectsEnvsStatusesCountsByOrgRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiGetProjectsEnvsStatusesCountsByOrgRequestQueryParams from a JSON string
environment_api_get_projects_envs_statuses_counts_by_org_request_query_params_instance = EnvironmentApiGetProjectsEnvsStatusesCountsByOrgRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiGetProjectsEnvsStatusesCountsByOrgRequestQueryParams.to_json())

# convert the object into a dict
environment_api_get_projects_envs_statuses_counts_by_org_request_query_params_dict = environment_api_get_projects_envs_statuses_counts_by_org_request_query_params_instance.to_dict()
# create an instance of EnvironmentApiGetProjectsEnvsStatusesCountsByOrgRequestQueryParams from a dict
environment_api_get_projects_envs_statuses_counts_by_org_request_query_params_from_dict = EnvironmentApiGetProjectsEnvsStatusesCountsByOrgRequestQueryParams.from_dict(environment_api_get_projects_envs_statuses_counts_by_org_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


