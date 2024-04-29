# BulkOperationsApiBulkLockRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_ids** | **List[str]** |  | 
**organization_id** | **str** |  | 
**data** | [**BulkOperationsApiBulkLockRequestBodyData**](BulkOperationsApiBulkLockRequestBodyData.md) |  | 

## Example

```python
from env0_client.models.bulk_operations_api_bulk_lock_request_body import BulkOperationsApiBulkLockRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOperationsApiBulkLockRequestBody from a JSON string
bulk_operations_api_bulk_lock_request_body_instance = BulkOperationsApiBulkLockRequestBody.from_json(json)
# print the JSON string representation of the object
print(BulkOperationsApiBulkLockRequestBody.to_json())

# convert the object into a dict
bulk_operations_api_bulk_lock_request_body_dict = bulk_operations_api_bulk_lock_request_body_instance.to_dict()
# create an instance of BulkOperationsApiBulkLockRequestBody from a dict
bulk_operations_api_bulk_lock_request_body_from_dict = BulkOperationsApiBulkLockRequestBody.from_dict(bulk_operations_api_bulk_lock_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


