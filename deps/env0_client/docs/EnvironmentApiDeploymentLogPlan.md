# EnvironmentApiDeploymentLogPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_changes** | [**List[DeploymentApiPlanPlanResourceChange]**](DeploymentApiPlanPlanResourceChange.md) |  | 
**output_changes** | [**List[DeploymentApiPlanPlanOutputChange]**](DeploymentApiPlanPlanOutputChange.md) |  | 

## Example

```python
from env0_client.models.environment_api_deployment_log_plan import EnvironmentApiDeploymentLogPlan

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiDeploymentLogPlan from a JSON string
environment_api_deployment_log_plan_instance = EnvironmentApiDeploymentLogPlan.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiDeploymentLogPlan.to_json())

# convert the object into a dict
environment_api_deployment_log_plan_dict = environment_api_deployment_log_plan_instance.to_dict()
# create an instance of EnvironmentApiDeploymentLogPlan from a dict
environment_api_deployment_log_plan_from_dict = EnvironmentApiDeploymentLogPlan.from_dict(environment_api_deployment_log_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


