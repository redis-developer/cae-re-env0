# PaginationQueryStringParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **str** |  | [optional] 
**offset** | **str** |  | [optional] 

## Example

```python
from env0_client.models.pagination_query_string_params import PaginationQueryStringParams

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationQueryStringParams from a JSON string
pagination_query_string_params_instance = PaginationQueryStringParams.from_json(json)
# print the JSON string representation of the object
print(PaginationQueryStringParams.to_json())

# convert the object into a dict
pagination_query_string_params_dict = pagination_query_string_params_instance.to_dict()
# create an instance of PaginationQueryStringParams from a dict
pagination_query_string_params_from_dict = PaginationQueryStringParams.from_dict(pagination_query_string_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


