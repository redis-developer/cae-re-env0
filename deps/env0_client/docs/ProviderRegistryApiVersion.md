# ProviderRegistryApiVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**provider_id** | **str** |  | 
**version** | **str** |  | 
**gpg_key_id** | **str** |  | 
**platform** | **str** |  | 
**shasum** | **str** |  | [optional] 
**is_archived** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.provider_registry_api_version import ProviderRegistryApiVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRegistryApiVersion from a JSON string
provider_registry_api_version_instance = ProviderRegistryApiVersion.from_json(json)
# print the JSON string representation of the object
print(ProviderRegistryApiVersion.to_json())

# convert the object into a dict
provider_registry_api_version_dict = provider_registry_api_version_instance.to_dict()
# create an instance of ProviderRegistryApiVersion from a dict
provider_registry_api_version_from_dict = ProviderRegistryApiVersion.from_dict(provider_registry_api_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


