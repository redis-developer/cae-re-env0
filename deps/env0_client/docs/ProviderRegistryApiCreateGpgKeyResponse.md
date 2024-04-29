# ProviderRegistryApiCreateGpgKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**key_id** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**created_by_user** | [**User**](User.md) |  | [optional] 

## Example

```python
from env0_client.models.provider_registry_api_create_gpg_key_response import ProviderRegistryApiCreateGpgKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRegistryApiCreateGpgKeyResponse from a JSON string
provider_registry_api_create_gpg_key_response_instance = ProviderRegistryApiCreateGpgKeyResponse.from_json(json)
# print the JSON string representation of the object
print(ProviderRegistryApiCreateGpgKeyResponse.to_json())

# convert the object into a dict
provider_registry_api_create_gpg_key_response_dict = provider_registry_api_create_gpg_key_response_instance.to_dict()
# create an instance of ProviderRegistryApiCreateGpgKeyResponse from a dict
provider_registry_api_create_gpg_key_response_from_dict = ProviderRegistryApiCreateGpgKeyResponse.from_dict(provider_registry_api_create_gpg_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


