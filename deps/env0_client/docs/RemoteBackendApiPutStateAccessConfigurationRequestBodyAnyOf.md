# RemoteBackendApiPutStateAccessConfigurationRequestBodyAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessible_from_entire_organization** | **bool** |  | 
**allowed_project_ids** | **List[str]** |  | 

## Example

```python
from env0_client.models.remote_backend_api_put_state_access_configuration_request_body_any_of import RemoteBackendApiPutStateAccessConfigurationRequestBodyAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteBackendApiPutStateAccessConfigurationRequestBodyAnyOf from a JSON string
remote_backend_api_put_state_access_configuration_request_body_any_of_instance = RemoteBackendApiPutStateAccessConfigurationRequestBodyAnyOf.from_json(json)
# print the JSON string representation of the object
print(RemoteBackendApiPutStateAccessConfigurationRequestBodyAnyOf.to_json())

# convert the object into a dict
remote_backend_api_put_state_access_configuration_request_body_any_of_dict = remote_backend_api_put_state_access_configuration_request_body_any_of_instance.to_dict()
# create an instance of RemoteBackendApiPutStateAccessConfigurationRequestBodyAnyOf from a dict
remote_backend_api_put_state_access_configuration_request_body_any_of_from_dict = RemoteBackendApiPutStateAccessConfigurationRequestBodyAnyOf.from_dict(remote_backend_api_put_state_access_configuration_request_body_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


