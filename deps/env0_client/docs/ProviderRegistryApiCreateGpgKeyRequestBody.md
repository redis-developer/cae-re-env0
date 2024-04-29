# ProviderRegistryApiCreateGpgKeyRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**organization_id** | **str** |  | 
**key_id** | **str** |  | 
**content** | **str** |  | 

## Example

```python
from env0_client.models.provider_registry_api_create_gpg_key_request_body import ProviderRegistryApiCreateGpgKeyRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRegistryApiCreateGpgKeyRequestBody from a JSON string
provider_registry_api_create_gpg_key_request_body_instance = ProviderRegistryApiCreateGpgKeyRequestBody.from_json(json)
# print the JSON string representation of the object
print(ProviderRegistryApiCreateGpgKeyRequestBody.to_json())

# convert the object into a dict
provider_registry_api_create_gpg_key_request_body_dict = provider_registry_api_create_gpg_key_request_body_instance.to_dict()
# create an instance of ProviderRegistryApiCreateGpgKeyRequestBody from a dict
provider_registry_api_create_gpg_key_request_body_from_dict = ProviderRegistryApiCreateGpgKeyRequestBody.from_dict(provider_registry_api_create_gpg_key_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


