# CostApiGetCostsRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timespan** | [**CostApiTimespan**](CostApiTimespan.md) |  | [optional] 
**granularity** | [**CostApiGranularity**](CostApiGranularity.md) |  | [optional] 

## Example

```python
from env0_client.models.cost_api_get_costs_request_query_params import CostApiGetCostsRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiGetCostsRequestQueryParams from a JSON string
cost_api_get_costs_request_query_params_instance = CostApiGetCostsRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(CostApiGetCostsRequestQueryParams.to_json())

# convert the object into a dict
cost_api_get_costs_request_query_params_dict = cost_api_get_costs_request_query_params_instance.to_dict()
# create an instance of CostApiGetCostsRequestQueryParams from a dict
cost_api_get_costs_request_query_params_from_dict = CostApiGetCostsRequestQueryParams.from_dict(cost_api_get_costs_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


