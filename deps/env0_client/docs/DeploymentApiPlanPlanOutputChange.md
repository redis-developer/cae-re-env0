# DeploymentApiPlanPlanOutputChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**action** | [**DeploymentApiPlanChangeAction**](DeploymentApiPlanChangeAction.md) |  | 
**attributes** | [**List[DeploymentApiPlanAttributeChange]**](DeploymentApiPlanAttributeChange.md) |  | 

## Example

```python
from env0_client.models.deployment_api_plan_plan_output_change import DeploymentApiPlanPlanOutputChange

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentApiPlanPlanOutputChange from a JSON string
deployment_api_plan_plan_output_change_instance = DeploymentApiPlanPlanOutputChange.from_json(json)
# print the JSON string representation of the object
print(DeploymentApiPlanPlanOutputChange.to_json())

# convert the object into a dict
deployment_api_plan_plan_output_change_dict = deployment_api_plan_plan_output_change_instance.to_dict()
# create an instance of DeploymentApiPlanPlanOutputChange from a dict
deployment_api_plan_plan_output_change_from_dict = DeploymentApiPlanPlanOutputChange.from_dict(deployment_api_plan_plan_output_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


