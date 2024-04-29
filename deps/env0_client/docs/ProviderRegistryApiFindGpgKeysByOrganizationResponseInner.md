# ProviderRegistryApiFindGpgKeysByOrganizationResponseInner


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
from env0_client.models.provider_registry_api_find_gpg_keys_by_organization_response_inner import ProviderRegistryApiFindGpgKeysByOrganizationResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRegistryApiFindGpgKeysByOrganizationResponseInner from a JSON string
provider_registry_api_find_gpg_keys_by_organization_response_inner_instance = ProviderRegistryApiFindGpgKeysByOrganizationResponseInner.from_json(json)
# print the JSON string representation of the object
print(ProviderRegistryApiFindGpgKeysByOrganizationResponseInner.to_json())

# convert the object into a dict
provider_registry_api_find_gpg_keys_by_organization_response_inner_dict = provider_registry_api_find_gpg_keys_by_organization_response_inner_instance.to_dict()
# create an instance of ProviderRegistryApiFindGpgKeysByOrganizationResponseInner from a dict
provider_registry_api_find_gpg_keys_by_organization_response_inner_from_dict = ProviderRegistryApiFindGpgKeysByOrganizationResponseInner.from_dict(provider_registry_api_find_gpg_keys_by_organization_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


