# CostApiProjectBudgetSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**usage** | **float** |  | 
**amount** | **float** |  | 
**renewed_at** | **datetime** |  | 

## Example

```python
from env0_client.models.cost_api_project_budget_summary import CostApiProjectBudgetSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiProjectBudgetSummary from a JSON string
cost_api_project_budget_summary_instance = CostApiProjectBudgetSummary.from_json(json)
# print the JSON string representation of the object
print(CostApiProjectBudgetSummary.to_json())

# convert the object into a dict
cost_api_project_budget_summary_dict = cost_api_project_budget_summary_instance.to_dict()
# create an instance of CostApiProjectBudgetSummary from a dict
cost_api_project_budget_summary_from_dict = CostApiProjectBudgetSummary.from_dict(cost_api_project_budget_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


