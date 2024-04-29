# ProviderRegistryApiTerraformTypesVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**platforms** | [**List[ProviderRegistryApiTerraformTypesPlatform]**](ProviderRegistryApiTerraformTypesPlatform.md) |  | 

## Example

```python
from env0_client.models.provider_registry_api_terraform_types_version import ProviderRegistryApiTerraformTypesVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRegistryApiTerraformTypesVersion from a JSON string
provider_registry_api_terraform_types_version_instance = ProviderRegistryApiTerraformTypesVersion.from_json(json)
# print the JSON string representation of the object
print(ProviderRegistryApiTerraformTypesVersion.to_json())

# convert the object into a dict
provider_registry_api_terraform_types_version_dict = provider_registry_api_terraform_types_version_instance.to_dict()
# create an instance of ProviderRegistryApiTerraformTypesVersion from a dict
provider_registry_api_terraform_types_version_from_dict = ProviderRegistryApiTerraformTypesVersion.from_dict(provider_registry_api_terraform_types_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


