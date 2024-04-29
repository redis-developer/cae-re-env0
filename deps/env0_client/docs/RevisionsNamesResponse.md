# RevisionsNamesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**heads** | **List[str]** |  | 
**tags** | **List[str]** |  | 

## Example

```python
from env0_client.models.revisions_names_response import RevisionsNamesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RevisionsNamesResponse from a JSON string
revisions_names_response_instance = RevisionsNamesResponse.from_json(json)
# print the JSON string representation of the object
print(RevisionsNamesResponse.to_json())

# convert the object into a dict
revisions_names_response_dict = revisions_names_response_instance.to_dict()
# create an instance of RevisionsNamesResponse from a dict
revisions_names_response_from_dict = RevisionsNamesResponse.from_dict(revisions_names_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


