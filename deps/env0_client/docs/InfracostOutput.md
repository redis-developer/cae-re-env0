# InfracostOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | **List[object]** |  | [optional] 
**total_hourly_cost** | **str** |  | [optional] 
**total_monthly_cost** | **str** |  | [optional] 

## Example

```python
from env0_client.models.infracost_output import InfracostOutput

# TODO update the JSON string below
json = "{}"
# create an instance of InfracostOutput from a JSON string
infracost_output_instance = InfracostOutput.from_json(json)
# print the JSON string representation of the object
print(InfracostOutput.to_json())

# convert the object into a dict
infracost_output_dict = infracost_output_instance.to_dict()
# create an instance of InfracostOutput from a dict
infracost_output_from_dict = InfracostOutput.from_dict(infracost_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


