# CostApiCostQueryResponseInnerTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws** | **float** |  | [optional] 
**gcp** | **float** |  | [optional] 
**azure** | **float** |  | [optional] 

## Example

```python
from env0_client.models.cost_api_cost_query_response_inner_total import CostApiCostQueryResponseInnerTotal

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiCostQueryResponseInnerTotal from a JSON string
cost_api_cost_query_response_inner_total_instance = CostApiCostQueryResponseInnerTotal.from_json(json)
# print the JSON string representation of the object
print(CostApiCostQueryResponseInnerTotal.to_json())

# convert the object into a dict
cost_api_cost_query_response_inner_total_dict = cost_api_cost_query_response_inner_total_instance.to_dict()
# create an instance of CostApiCostQueryResponseInnerTotal from a dict
cost_api_cost_query_response_inner_total_from_dict = CostApiCostQueryResponseInnerTotal.from_dict(cost_api_cost_query_response_inner_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


