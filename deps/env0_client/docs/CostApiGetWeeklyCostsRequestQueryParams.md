# CostApiGetWeeklyCostsRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_ids** | **str** |  | [optional] 
**project_ids** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 

## Example

```python
from env0_client.models.cost_api_get_weekly_costs_request_query_params import CostApiGetWeeklyCostsRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiGetWeeklyCostsRequestQueryParams from a JSON string
cost_api_get_weekly_costs_request_query_params_instance = CostApiGetWeeklyCostsRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(CostApiGetWeeklyCostsRequestQueryParams.to_json())

# convert the object into a dict
cost_api_get_weekly_costs_request_query_params_dict = cost_api_get_weekly_costs_request_query_params_instance.to_dict()
# create an instance of CostApiGetWeeklyCostsRequestQueryParams from a dict
cost_api_get_weekly_costs_request_query_params_from_dict = CostApiGetWeeklyCostsRequestQueryParams.from_dict(cost_api_get_weekly_costs_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


