# BulkOperationsApiBulkDestroyRequestBodyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_state_refresh** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from env0_client.models.bulk_operations_api_bulk_destroy_request_body_data import BulkOperationsApiBulkDestroyRequestBodyData

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOperationsApiBulkDestroyRequestBodyData from a JSON string
bulk_operations_api_bulk_destroy_request_body_data_instance = BulkOperationsApiBulkDestroyRequestBodyData.from_json(json)
# print the JSON string representation of the object
print(BulkOperationsApiBulkDestroyRequestBodyData.to_json())

# convert the object into a dict
bulk_operations_api_bulk_destroy_request_body_data_dict = bulk_operations_api_bulk_destroy_request_body_data_instance.to_dict()
# create an instance of BulkOperationsApiBulkDestroyRequestBodyData from a dict
bulk_operations_api_bulk_destroy_request_body_data_from_dict = BulkOperationsApiBulkDestroyRequestBodyData.from_dict(bulk_operations_api_bulk_destroy_request_body_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


