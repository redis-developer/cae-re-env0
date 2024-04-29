# BulkOperationsApiBulkDeployRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_ids** | **List[str]** |  | 
**organization_id** | **str** |  | 
**data** | [**BulkOperationsApiBulkDeployRequestBodyData**](BulkOperationsApiBulkDeployRequestBodyData.md) |  | 

## Example

```python
from env0_client.models.bulk_operations_api_bulk_deploy_request_body import BulkOperationsApiBulkDeployRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOperationsApiBulkDeployRequestBody from a JSON string
bulk_operations_api_bulk_deploy_request_body_instance = BulkOperationsApiBulkDeployRequestBody.from_json(json)
# print the JSON string representation of the object
print(BulkOperationsApiBulkDeployRequestBody.to_json())

# convert the object into a dict
bulk_operations_api_bulk_deploy_request_body_dict = bulk_operations_api_bulk_deploy_request_body_instance.to_dict()
# create an instance of BulkOperationsApiBulkDeployRequestBody from a dict
bulk_operations_api_bulk_deploy_request_body_from_dict = BulkOperationsApiBulkDeployRequestBody.from_dict(bulk_operations_api_bulk_deploy_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


