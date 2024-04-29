# InfracostTotalOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**projects** | [**List[InfracostTotalOutputProjectsInner]**](InfracostTotalOutputProjectsInner.md) |  | [optional] 
**time_generated** | **str** |  | [optional] 
**summary** | [**InfracostTotalOutputSummary**](InfracostTotalOutputSummary.md) |  | [optional] 
**resources** | **List[object]** |  | [optional] 
**total_hourly_cost** | **str** |  | [optional] 
**total_monthly_cost** | **str** |  | [optional] 

## Example

```python
from env0_client.models.infracost_total_output import InfracostTotalOutput

# TODO update the JSON string below
json = "{}"
# create an instance of InfracostTotalOutput from a JSON string
infracost_total_output_instance = InfracostTotalOutput.from_json(json)
# print the JSON string representation of the object
print(InfracostTotalOutput.to_json())

# convert the object into a dict
infracost_total_output_dict = infracost_total_output_instance.to_dict()
# create an instance of InfracostTotalOutput from a dict
infracost_total_output_from_dict = InfracostTotalOutput.from_dict(infracost_total_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


