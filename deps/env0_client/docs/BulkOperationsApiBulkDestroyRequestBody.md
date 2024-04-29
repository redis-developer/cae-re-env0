# BulkOperationsApiBulkDestroyRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_ids** | **List[str]** |  | 
**organization_id** | **str** |  | 
**data** | [**BulkOperationsApiBulkDestroyRequestBodyData**](BulkOperationsApiBulkDestroyRequestBodyData.md) |  | 

## Example

```python
from env0_client.models.bulk_operations_api_bulk_destroy_request_body import BulkOperationsApiBulkDestroyRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOperationsApiBulkDestroyRequestBody from a JSON string
bulk_operations_api_bulk_destroy_request_body_instance = BulkOperationsApiBulkDestroyRequestBody.from_json(json)
# print the JSON string representation of the object
print(BulkOperationsApiBulkDestroyRequestBody.to_json())

# convert the object into a dict
bulk_operations_api_bulk_destroy_request_body_dict = bulk_operations_api_bulk_destroy_request_body_instance.to_dict()
# create an instance of BulkOperationsApiBulkDestroyRequestBody from a dict
bulk_operations_api_bulk_destroy_request_body_from_dict = BulkOperationsApiBulkDestroyRequestBody.from_dict(bulk_operations_api_bulk_destroy_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


