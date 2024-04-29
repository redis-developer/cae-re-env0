# BulkOperationsApiBasePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_ids** | **List[str]** |  | 
**organization_id** | **str** |  | 

## Example

```python
from env0_client.models.bulk_operations_api_base_payload import BulkOperationsApiBasePayload

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOperationsApiBasePayload from a JSON string
bulk_operations_api_base_payload_instance = BulkOperationsApiBasePayload.from_json(json)
# print the JSON string representation of the object
print(BulkOperationsApiBasePayload.to_json())

# convert the object into a dict
bulk_operations_api_base_payload_dict = bulk_operations_api_base_payload_instance.to_dict()
# create an instance of BulkOperationsApiBasePayload from a dict
bulk_operations_api_base_payload_from_dict = BulkOperationsApiBasePayload.from_dict(bulk_operations_api_base_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


