# BulkOperationsApiBulkRunTaskRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_ids** | **List[str]** |  | 
**organization_id** | **str** |  | 
**data** | [**BulkOperationsApiBulkRunTaskRequestBodyData**](BulkOperationsApiBulkRunTaskRequestBodyData.md) |  | 

## Example

```python
from env0_client.models.bulk_operations_api_bulk_run_task_request_body import BulkOperationsApiBulkRunTaskRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOperationsApiBulkRunTaskRequestBody from a JSON string
bulk_operations_api_bulk_run_task_request_body_instance = BulkOperationsApiBulkRunTaskRequestBody.from_json(json)
# print the JSON string representation of the object
print(BulkOperationsApiBulkRunTaskRequestBody.to_json())

# convert the object into a dict
bulk_operations_api_bulk_run_task_request_body_dict = bulk_operations_api_bulk_run_task_request_body_instance.to_dict()
# create an instance of BulkOperationsApiBulkRunTaskRequestBody from a dict
bulk_operations_api_bulk_run_task_request_body_from_dict = BulkOperationsApiBulkRunTaskRequestBody.from_dict(bulk_operations_api_bulk_run_task_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


