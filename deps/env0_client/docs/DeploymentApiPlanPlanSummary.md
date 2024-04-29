# DeploymentApiPlanPlanSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added** | **float** |  | 
**changed** | **float** |  | 
**destroyed** | **float** |  | 
**imported** | **float** |  | [optional] 

## Example

```python
from env0_client.models.deployment_api_plan_plan_summary import DeploymentApiPlanPlanSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentApiPlanPlanSummary from a JSON string
deployment_api_plan_plan_summary_instance = DeploymentApiPlanPlanSummary.from_json(json)
# print the JSON string representation of the object
print(DeploymentApiPlanPlanSummary.to_json())

# convert the object into a dict
deployment_api_plan_plan_summary_dict = deployment_api_plan_plan_summary_instance.to_dict()
# create an instance of DeploymentApiPlanPlanSummary from a dict
deployment_api_plan_plan_summary_from_dict = DeploymentApiPlanPlanSummary.from_dict(deployment_api_plan_plan_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


