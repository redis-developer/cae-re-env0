# CostApiGroupedCloudCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**providers_cost** | [**CostApiGroupedCloudCostProvidersCost**](CostApiGroupedCloudCostProvidersCost.md) |  | 
**group_key** | **str** |  | 

## Example

```python
from env0_client.models.cost_api_grouped_cloud_cost import CostApiGroupedCloudCost

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiGroupedCloudCost from a JSON string
cost_api_grouped_cloud_cost_instance = CostApiGroupedCloudCost.from_json(json)
# print the JSON string representation of the object
print(CostApiGroupedCloudCost.to_json())

# convert the object into a dict
cost_api_grouped_cloud_cost_dict = cost_api_grouped_cloud_cost_instance.to_dict()
# create an instance of CostApiGroupedCloudCost from a dict
cost_api_grouped_cloud_cost_from_dict = CostApiGroupedCloudCost.from_dict(cost_api_grouped_cloud_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


