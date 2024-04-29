# BulkOperationsApiSingleResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_id** | **str** |  | 
**status** | **str** |  | 
**error** | **str** |  | [optional] 

## Example

```python
from env0_client.models.bulk_operations_api_single_result import BulkOperationsApiSingleResult

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOperationsApiSingleResult from a JSON string
bulk_operations_api_single_result_instance = BulkOperationsApiSingleResult.from_json(json)
# print the JSON string representation of the object
print(BulkOperationsApiSingleResult.to_json())

# convert the object into a dict
bulk_operations_api_single_result_dict = bulk_operations_api_single_result_instance.to_dict()
# create an instance of BulkOperationsApiSingleResult from a dict
bulk_operations_api_single_result_from_dict = BulkOperationsApiSingleResult.from_dict(bulk_operations_api_single_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


