# DeploymentApiPlanAttributeChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**before** | **object** |  | [optional] 
**after** | **object** |  | [optional] 

## Example

```python
from env0_client.models.deployment_api_plan_attribute_change import DeploymentApiPlanAttributeChange

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentApiPlanAttributeChange from a JSON string
deployment_api_plan_attribute_change_instance = DeploymentApiPlanAttributeChange.from_json(json)
# print the JSON string representation of the object
print(DeploymentApiPlanAttributeChange.to_json())

# convert the object into a dict
deployment_api_plan_attribute_change_dict = deployment_api_plan_attribute_change_instance.to_dict()
# create an instance of DeploymentApiPlanAttributeChange from a dict
deployment_api_plan_attribute_change_from_dict = DeploymentApiPlanAttributeChange.from_dict(deployment_api_plan_attribute_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


