# BulkOperationsApiBulkDeployRequestBodyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_requires_approval** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from env0_client.models.bulk_operations_api_bulk_deploy_request_body_data import BulkOperationsApiBulkDeployRequestBodyData

# TODO update the JSON string below
json = "{}"
# create an instance of BulkOperationsApiBulkDeployRequestBodyData from a JSON string
bulk_operations_api_bulk_deploy_request_body_data_instance = BulkOperationsApiBulkDeployRequestBodyData.from_json(json)
# print the JSON string representation of the object
print(BulkOperationsApiBulkDeployRequestBodyData.to_json())

# convert the object into a dict
bulk_operations_api_bulk_deploy_request_body_data_dict = bulk_operations_api_bulk_deploy_request_body_data_instance.to_dict()
# create an instance of BulkOperationsApiBulkDeployRequestBodyData from a dict
bulk_operations_api_bulk_deploy_request_body_data_from_dict = BulkOperationsApiBulkDeployRequestBodyData.from_dict(bulk_operations_api_bulk_deploy_request_body_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


