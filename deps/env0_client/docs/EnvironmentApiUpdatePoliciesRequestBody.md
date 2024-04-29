# EnvironmentApiUpdatePoliciesRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**number_of_environments** | **float** |  | [optional] 
**number_of_environments_total** | **float** |  | [optional] 
**max_ttl** | **str** | The maximum allowed TTL. Must be 6-h, 12-h, 1-d, 3-d, 1-w, 2-w, 1-M, inherit or explicit null which means infinite | [optional] 
**default_ttl** | **str** | The default TTL set when creating environments. Must be 6-h, 12-h, 1-d, 3-d, 1-w, 2-w, 1-M, inherit or explicit null which means infinite | [optional] 
**requires_approval_default** | **bool** |  | [optional] 
**include_cost_estimation** | **bool** |  | [optional] 
**skip_apply_when_plan_is_empty** | **bool** |  | [optional] 
**disable_destroy_environments** | **bool** |  | [optional] 
**skip_redundant_deployments** | **bool** |  | [optional] 
**run_pull_request_plan_default** | **bool** |  | [optional] 
**continuous_deployment_default** | **bool** |  | [optional] 
**force_remote_backend** | **bool** |  | [optional] 
**drift_detection_enabled** | **bool** |  | [optional] 
**drift_detection_cron** | **str** |  | [optional] 
**outputs_as_inputs_enabled** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.environment_api_update_policies_request_body import EnvironmentApiUpdatePoliciesRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiUpdatePoliciesRequestBody from a JSON string
environment_api_update_policies_request_body_instance = EnvironmentApiUpdatePoliciesRequestBody.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiUpdatePoliciesRequestBody.to_json())

# convert the object into a dict
environment_api_update_policies_request_body_dict = environment_api_update_policies_request_body_instance.to_dict()
# create an instance of EnvironmentApiUpdatePoliciesRequestBody from a dict
environment_api_update_policies_request_body_from_dict = EnvironmentApiUpdatePoliciesRequestBody.from_dict(environment_api_update_policies_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


