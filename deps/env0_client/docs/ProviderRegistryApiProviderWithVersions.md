# ProviderRegistryApiProviderWithVersions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | [**List[ProviderRegistryApiVersion]**](ProviderRegistryApiVersion.md) |  | 
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**organization_id** | **str** |  | 
**description** | **str** |  | [optional] 
**created_by** | **str** |  | 
**created_by_user** | [**User**](User.md) |  | [optional] 

## Example

```python
from env0_client.models.provider_registry_api_provider_with_versions import ProviderRegistryApiProviderWithVersions

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRegistryApiProviderWithVersions from a JSON string
provider_registry_api_provider_with_versions_instance = ProviderRegistryApiProviderWithVersions.from_json(json)
# print the JSON string representation of the object
print(ProviderRegistryApiProviderWithVersions.to_json())

# convert the object into a dict
provider_registry_api_provider_with_versions_dict = provider_registry_api_provider_with_versions_instance.to_dict()
# create an instance of ProviderRegistryApiProviderWithVersions from a dict
provider_registry_api_provider_with_versions_from_dict = ProviderRegistryApiProviderWithVersions.from_dict(provider_registry_api_provider_with_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


