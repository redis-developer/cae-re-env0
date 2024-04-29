# CostApiGetAccumulatedProjectCostsResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**usage** | **float** |  | 

## Example

```python
from env0_client.models.cost_api_get_accumulated_project_costs_response_inner import CostApiGetAccumulatedProjectCostsResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiGetAccumulatedProjectCostsResponseInner from a JSON string
cost_api_get_accumulated_project_costs_response_inner_instance = CostApiGetAccumulatedProjectCostsResponseInner.from_json(json)
# print the JSON string representation of the object
print(CostApiGetAccumulatedProjectCostsResponseInner.to_json())

# convert the object into a dict
cost_api_get_accumulated_project_costs_response_inner_dict = cost_api_get_accumulated_project_costs_response_inner_instance.to_dict()
# create an instance of CostApiGetAccumulatedProjectCostsResponseInner from a dict
cost_api_get_accumulated_project_costs_response_inner_from_dict = CostApiGetAccumulatedProjectCostsResponseInner.from_dict(cost_api_get_accumulated_project_costs_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


