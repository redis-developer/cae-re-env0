# CostApiGetBudgetSummaryRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **str** |  | 

## Example

```python
from env0_client.models.cost_api_get_budget_summary_request_query_params import CostApiGetBudgetSummaryRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiGetBudgetSummaryRequestQueryParams from a JSON string
cost_api_get_budget_summary_request_query_params_instance = CostApiGetBudgetSummaryRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(CostApiGetBudgetSummaryRequestQueryParams.to_json())

# convert the object into a dict
cost_api_get_budget_summary_request_query_params_dict = cost_api_get_budget_summary_request_query_params_instance.to_dict()
# create an instance of CostApiGetBudgetSummaryRequestQueryParams from a dict
cost_api_get_budget_summary_request_query_params_from_dict = CostApiGetBudgetSummaryRequestQueryParams.from_dict(cost_api_get_budget_summary_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


