# BulkOperationsApiBaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BulkOperationsApiSingleResult]**](BulkOperationsApiSingleResult.md) |  | 
**organization_id** | **str** |  | 

## Example

```python
from env0_client.models.bulk_operations_api_base_response import BulkOperationsApiBaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOperationsApiBaseResponse from a JSON string
bulk_operations_api_base_response_instance = BulkOperationsApiBaseResponse.from_json(json)
# print the JSON string representation of the object
print(BulkOperationsApiBaseResponse.to_json())

# convert the object into a dict
bulk_operations_api_base_response_dict = bulk_operations_api_base_response_instance.to_dict()
# create an instance of BulkOperationsApiBaseResponse from a dict
bulk_operations_api_base_response_from_dict = BulkOperationsApiBaseResponse.from_dict(bulk_operations_api_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


