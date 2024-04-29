# CostApiBudget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**project_id** | **str** |  | 
**amount** | **float** |  | 
**timeframe** | [**CostApiBudgetTimeframe**](CostApiBudgetTimeframe.md) |  | 
**thresholds** | **List[float]** |  | 

## Example

```python
from env0_client.models.cost_api_budget import CostApiBudget

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiBudget from a JSON string
cost_api_budget_instance = CostApiBudget.from_json(json)
# print the JSON string representation of the object
print(CostApiBudget.to_json())

# convert the object into a dict
cost_api_budget_dict = cost_api_budget_instance.to_dict()
# create an instance of CostApiBudget from a dict
cost_api_budget_from_dict = CostApiBudget.from_dict(cost_api_budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


