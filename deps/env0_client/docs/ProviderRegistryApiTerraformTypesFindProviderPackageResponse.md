# ProviderRegistryApiTerraformTypesFindProviderPackageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocols** | **List[str]** |  | 
**os** | **str** |  | 
**arch** | **str** |  | 
**filename** | **str** |  | 
**download_url** | **str** |  | 
**shasums_url** | **str** |  | 
**shasums_signature_url** | **str** |  | 
**shasum** | **str** |  | 
**signing_keys** | [**ProviderRegistryApiTerraformTypesSigningKeys**](ProviderRegistryApiTerraformTypesSigningKeys.md) |  | 

## Example

```python
from env0_client.models.provider_registry_api_terraform_types_find_provider_package_response import ProviderRegistryApiTerraformTypesFindProviderPackageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRegistryApiTerraformTypesFindProviderPackageResponse from a JSON string
provider_registry_api_terraform_types_find_provider_package_response_instance = ProviderRegistryApiTerraformTypesFindProviderPackageResponse.from_json(json)
# print the JSON string representation of the object
print(ProviderRegistryApiTerraformTypesFindProviderPackageResponse.to_json())

# convert the object into a dict
provider_registry_api_terraform_types_find_provider_package_response_dict = provider_registry_api_terraform_types_find_provider_package_response_instance.to_dict()
# create an instance of ProviderRegistryApiTerraformTypesFindProviderPackageResponse from a dict
provider_registry_api_terraform_types_find_provider_package_response_from_dict = ProviderRegistryApiTerraformTypesFindProviderPackageResponse.from_dict(provider_registry_api_terraform_types_find_provider_package_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


