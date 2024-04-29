# ProviderRegistryApiProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**organization_id** | **str** |  | 
**description** | **str** |  | [optional] 
**created_by** | **str** |  | 
**created_by_user** | [**User**](User.md) |  | [optional] 

## Example

```python
from env0_client.models.provider_registry_api_provider import ProviderRegistryApiProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRegistryApiProvider from a JSON string
provider_registry_api_provider_instance = ProviderRegistryApiProvider.from_json(json)
# print the JSON string representation of the object
print(ProviderRegistryApiProvider.to_json())

# convert the object into a dict
provider_registry_api_provider_dict = provider_registry_api_provider_instance.to_dict()
# create an instance of ProviderRegistryApiProvider from a dict
provider_registry_api_provider_from_dict = ProviderRegistryApiProvider.from_dict(provider_registry_api_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


