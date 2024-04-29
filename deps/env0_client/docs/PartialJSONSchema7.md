# PartialJSONSchema7


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**enum** | **List[str]** |  | [optional] 
**format** | **str** |  | [optional] 

## Example

```python
from env0_client.models.partial_json_schema7 import PartialJSONSchema7

# TODO update the JSON string below
json = "{}"
# create an instance of PartialJSONSchema7 from a JSON string
partial_json_schema7_instance = PartialJSONSchema7.from_json(json)
# print the JSON string representation of the object
print(PartialJSONSchema7.to_json())

# convert the object into a dict
partial_json_schema7_dict = partial_json_schema7_instance.to_dict()
# create an instance of PartialJSONSchema7 from a dict
partial_json_schema7_from_dict = PartialJSONSchema7.from_dict(partial_json_schema7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


