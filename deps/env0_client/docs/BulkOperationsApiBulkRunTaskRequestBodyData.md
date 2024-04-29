# BulkOperationsApiBulkRunTaskRequestBodyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**task_payload** | **str** |  | [optional] 

## Example

```python
from env0_client.models.bulk_operations_api_bulk_run_task_request_body_data import BulkOperationsApiBulkRunTaskRequestBodyData

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOperationsApiBulkRunTaskRequestBodyData from a JSON string
bulk_operations_api_bulk_run_task_request_body_data_instance = BulkOperationsApiBulkRunTaskRequestBodyData.from_json(json)
# print the JSON string representation of the object
print(BulkOperationsApiBulkRunTaskRequestBodyData.to_json())

# convert the object into a dict
bulk_operations_api_bulk_run_task_request_body_data_dict = bulk_operations_api_bulk_run_task_request_body_data_instance.to_dict()
# create an instance of BulkOperationsApiBulkRunTaskRequestBodyData from a dict
bulk_operations_api_bulk_run_task_request_body_data_from_dict = BulkOperationsApiBulkRunTaskRequestBodyData.from_dict(bulk_operations_api_bulk_run_task_request_body_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


