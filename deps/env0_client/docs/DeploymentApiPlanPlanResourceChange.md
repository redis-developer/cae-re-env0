# DeploymentApiPlanPlanResourceChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**provider_name** | **str** |  | 
**type** | **str** |  | 
**path** | **str** |  | 
**action** | [**DeploymentApiPlanChangeAction**](DeploymentApiPlanChangeAction.md) |  | 
**attributes** | [**List[DeploymentApiPlanAttributeChange]**](DeploymentApiPlanAttributeChange.md) |  | 
**importing** | [**DeploymentApiPlanResourceImportData**](DeploymentApiPlanResourceImportData.md) |  | [optional] 
**previous_address** | **str** |  | [optional] 

## Example

```python
from env0_client.models.deployment_api_plan_plan_resource_change import DeploymentApiPlanPlanResourceChange

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentApiPlanPlanResourceChange from a JSON string
deployment_api_plan_plan_resource_change_instance = DeploymentApiPlanPlanResourceChange.from_json(json)
# print the JSON string representation of the object
print(DeploymentApiPlanPlanResourceChange.to_json())

# convert the object into a dict
deployment_api_plan_plan_resource_change_dict = deployment_api_plan_plan_resource_change_instance.to_dict()
# create an instance of DeploymentApiPlanPlanResourceChange from a dict
deployment_api_plan_plan_resource_change_from_dict = DeploymentApiPlanPlanResourceChange.from_dict(deployment_api_plan_plan_resource_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


