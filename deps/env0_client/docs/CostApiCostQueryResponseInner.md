# CostApiCostQueryResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**total** | [**CostApiCostQueryResponseInnerTotal**](CostApiCostQueryResponseInnerTotal.md) |  | 
**id** | **str** |  | [optional] 

## Example

```python
from env0_client.models.cost_api_cost_query_response_inner import CostApiCostQueryResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiCostQueryResponseInner from a JSON string
cost_api_cost_query_response_inner_instance = CostApiCostQueryResponseInner.from_json(json)
# print the JSON string representation of the object
print(CostApiCostQueryResponseInner.to_json())

# convert the object into a dict
cost_api_cost_query_response_inner_dict = cost_api_cost_query_response_inner_instance.to_dict()
# create an instance of CostApiCostQueryResponseInner from a dict
cost_api_cost_query_response_inner_from_dict = CostApiCostQueryResponseInner.from_dict(cost_api_cost_query_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


