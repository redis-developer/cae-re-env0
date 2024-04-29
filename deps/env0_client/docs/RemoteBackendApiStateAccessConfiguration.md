# RemoteBackendApiStateAccessConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**accessible_from_entire_organization** | **bool** |  | 
**allowed_project_ids** | **List[str]** |  | [optional] 
**environment_id** | **str** |  | 

## Example

```python
from env0_client.models.remote_backend_api_state_access_configuration import RemoteBackendApiStateAccessConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteBackendApiStateAccessConfiguration from a JSON string
remote_backend_api_state_access_configuration_instance = RemoteBackendApiStateAccessConfiguration.from_json(json)
# print the JSON string representation of the object
print(RemoteBackendApiStateAccessConfiguration.to_json())

# convert the object into a dict
remote_backend_api_state_access_configuration_dict = remote_backend_api_state_access_configuration_instance.to_dict()
# create an instance of RemoteBackendApiStateAccessConfiguration from a dict
remote_backend_api_state_access_configuration_from_dict = RemoteBackendApiStateAccessConfiguration.from_dict(remote_backend_api_state_access_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


