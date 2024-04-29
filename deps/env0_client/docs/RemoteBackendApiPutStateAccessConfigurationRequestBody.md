# RemoteBackendApiPutStateAccessConfigurationRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessible_from_entire_organization** | **bool** |  | 
**allowed_project_ids** | **List[object]** |  | 

## Example

```python
from env0_client.models.remote_backend_api_put_state_access_configuration_request_body import RemoteBackendApiPutStateAccessConfigurationRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteBackendApiPutStateAccessConfigurationRequestBody from a JSON string
remote_backend_api_put_state_access_configuration_request_body_instance = RemoteBackendApiPutStateAccessConfigurationRequestBody.from_json(json)
# print the JSON string representation of the object
print(RemoteBackendApiPutStateAccessConfigurationRequestBody.to_json())

# convert the object into a dict
remote_backend_api_put_state_access_configuration_request_body_dict = remote_backend_api_put_state_access_configuration_request_body_instance.to_dict()
# create an instance of RemoteBackendApiPutStateAccessConfigurationRequestBody from a dict
remote_backend_api_put_state_access_configuration_request_body_from_dict = RemoteBackendApiPutStateAccessConfigurationRequestBody.from_dict(remote_backend_api_put_state_access_configuration_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


