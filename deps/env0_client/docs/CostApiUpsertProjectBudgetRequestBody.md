# CostApiUpsertProjectBudgetRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | 
**timeframe** | [**CostApiBudgetTimeframe**](CostApiBudgetTimeframe.md) |  | 
**thresholds** | **List[float]** |  | 

## Example

```python
from env0_client.models.cost_api_upsert_project_budget_request_body import CostApiUpsertProjectBudgetRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiUpsertProjectBudgetRequestBody from a JSON string
cost_api_upsert_project_budget_request_body_instance = CostApiUpsertProjectBudgetRequestBody.from_json(json)
# print the JSON string representation of the object
print(CostApiUpsertProjectBudgetRequestBody.to_json())

# convert the object into a dict
cost_api_upsert_project_budget_request_body_dict = cost_api_upsert_project_budget_request_body_instance.to_dict()
# create an instance of CostApiUpsertProjectBudgetRequestBody from a dict
cost_api_upsert_project_budget_request_body_from_dict = CostApiUpsertProjectBudgetRequestBody.from_dict(cost_api_upsert_project_budget_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


