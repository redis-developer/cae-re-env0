# CostApiCostError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CostApiCloudType**](CostApiCloudType.md) |  | 
**error_message** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from env0_client.models.cost_api_cost_error import CostApiCostError

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiCostError from a JSON string
cost_api_cost_error_instance = CostApiCostError.from_json(json)
# print the JSON string representation of the object
print(CostApiCostError.to_json())

# convert the object into a dict
cost_api_cost_error_dict = cost_api_cost_error_instance.to_dict()
# create an instance of CostApiCostError from a dict
cost_api_cost_error_from_dict = CostApiCostError.from_dict(cost_api_cost_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


