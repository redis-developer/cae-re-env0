# CostApiWeeklyCostEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** |  | 
**error** | **str** |  | [optional] 

## Example

```python
from env0_client.models.cost_api_weekly_cost_entry import CostApiWeeklyCostEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiWeeklyCostEntry from a JSON string
cost_api_weekly_cost_entry_instance = CostApiWeeklyCostEntry.from_json(json)
# print the JSON string representation of the object
print(CostApiWeeklyCostEntry.to_json())

# convert the object into a dict
cost_api_weekly_cost_entry_dict = cost_api_weekly_cost_entry_instance.to_dict()
# create an instance of CostApiWeeklyCostEntry from a dict
cost_api_weekly_cost_entry_from_dict = CostApiWeeklyCostEntry.from_dict(cost_api_weekly_cost_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


