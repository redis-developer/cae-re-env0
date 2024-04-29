# InfracostTotalOutputProjectsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**past_breakdown** | [**InfracostOutput**](InfracostOutput.md) |  | [optional] 
**breakdown** | [**InfracostOutput**](InfracostOutput.md) |  | [optional] 
**diff** | [**InfracostOutput**](InfracostOutput.md) |  | [optional] 

## Example

```python
from env0_client.models.infracost_total_output_projects_inner import InfracostTotalOutputProjectsInner

# TODO update the JSON string below
json = "{}"
# create an instance of InfracostTotalOutputProjectsInner from a JSON string
infracost_total_output_projects_inner_instance = InfracostTotalOutputProjectsInner.from_json(json)
# print the JSON string representation of the object
print(InfracostTotalOutputProjectsInner.to_json())

# convert the object into a dict
infracost_total_output_projects_inner_dict = infracost_total_output_projects_inner_instance.to_dict()
# create an instance of InfracostTotalOutputProjectsInner from a dict
infracost_total_output_projects_inner_from_dict = InfracostTotalOutputProjectsInner.from_dict(infracost_total_output_projects_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


