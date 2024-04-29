# EnvironmentApiPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**updated_by** | **str** |  | 
**project_id** | **str** |  | 
**number_of_environments** | **float** |  | 
**number_of_environments_total** | **float** |  | 
**max_ttl** | **str** |  | 
**default_ttl** | **str** |  | 
**requires_approval_default** | **bool** |  | 
**include_cost_estimation** | **bool** |  | 
**skip_apply_when_plan_is_empty** | **bool** |  | 
**disable_destroy_environments** | **bool** |  | 
**skip_redundant_deployments** | **bool** |  | 
**run_pull_request_plan_default** | **bool** |  | 
**continuous_deployment_default** | **bool** |  | 
**force_remote_backend** | **bool** |  | 
**drift_detection_enabled** | **bool** |  | [optional] 
**drift_detection_cron** | **str** |  | [optional] 
**outputs_as_inputs_enabled** | **bool** |  | 

## Example

```python
from env0_client.models.environment_api_policy import EnvironmentApiPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiPolicy from a JSON string
environment_api_policy_instance = EnvironmentApiPolicy.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiPolicy.to_json())

# convert the object into a dict
environment_api_policy_dict = environment_api_policy_instance.to_dict()
# create an instance of EnvironmentApiPolicy from a dict
environment_api_policy_from_dict = EnvironmentApiPolicy.from_dict(environment_api_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


