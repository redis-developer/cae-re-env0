# CostApiGroupedCloudCostProvidersCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws** | **object** |  | [optional] 
**gcp** | **object** |  | [optional] 
**azure** | **object** |  | [optional] 

## Example

```python
from env0_client.models.cost_api_grouped_cloud_cost_providers_cost import CostApiGroupedCloudCostProvidersCost

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiGroupedCloudCostProvidersCost from a JSON string
cost_api_grouped_cloud_cost_providers_cost_instance = CostApiGroupedCloudCostProvidersCost.from_json(json)
# print the JSON string representation of the object
print(CostApiGroupedCloudCostProvidersCost.to_json())

# convert the object into a dict
cost_api_grouped_cloud_cost_providers_cost_dict = cost_api_grouped_cloud_cost_providers_cost_instance.to_dict()
# create an instance of CostApiGroupedCloudCostProvidersCost from a dict
cost_api_grouped_cloud_cost_providers_cost_from_dict = CostApiGroupedCloudCostProvidersCost.from_dict(cost_api_grouped_cloud_cost_providers_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


