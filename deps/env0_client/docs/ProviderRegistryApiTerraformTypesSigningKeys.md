# ProviderRegistryApiTerraformTypesSigningKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpg_public_keys** | [**List[ProviderRegistryApiTerraformTypesGpgPublicKeys]**](ProviderRegistryApiTerraformTypesGpgPublicKeys.md) |  | 

## Example

```python
from env0_client.models.provider_registry_api_terraform_types_signing_keys import ProviderRegistryApiTerraformTypesSigningKeys

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRegistryApiTerraformTypesSigningKeys from a JSON string
provider_registry_api_terraform_types_signing_keys_instance = ProviderRegistryApiTerraformTypesSigningKeys.from_json(json)
# print the JSON string representation of the object
print(ProviderRegistryApiTerraformTypesSigningKeys.to_json())

# convert the object into a dict
provider_registry_api_terraform_types_signing_keys_dict = provider_registry_api_terraform_types_signing_keys_instance.to_dict()
# create an instance of ProviderRegistryApiTerraformTypesSigningKeys from a dict
provider_registry_api_terraform_types_signing_keys_from_dict = ProviderRegistryApiTerraformTypesSigningKeys.from_dict(provider_registry_api_terraform_types_signing_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


