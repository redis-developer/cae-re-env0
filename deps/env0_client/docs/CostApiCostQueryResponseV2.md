# CostApiCostQueryResponseV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_data_points** | [**List[CostApiGroupedCloudCost]**](CostApiGroupedCloudCost.md) |  | 
**errors** | [**List[CostApiCostError]**](CostApiCostError.md) |  | 

## Example

```python
from env0_client.models.cost_api_cost_query_response_v2 import CostApiCostQueryResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiCostQueryResponseV2 from a JSON string
cost_api_cost_query_response_v2_instance = CostApiCostQueryResponseV2.from_json(json)
# print the JSON string representation of the object
print(CostApiCostQueryResponseV2.to_json())

# convert the object into a dict
cost_api_cost_query_response_v2_dict = cost_api_cost_query_response_v2_instance.to_dict()
# create an instance of CostApiCostQueryResponseV2 from a dict
cost_api_cost_query_response_v2_from_dict = CostApiCostQueryResponseV2.from_dict(cost_api_cost_query_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


