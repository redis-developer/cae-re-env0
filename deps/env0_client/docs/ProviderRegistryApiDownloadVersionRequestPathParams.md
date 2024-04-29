# ProviderRegistryApiDownloadVersionRequestPathParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** |  | 
**type** | **str** |  | 
**version** | **str** |  | 
**os** | **str** |  | 
**architecture** | **str** |  | 

## Example

```python
from env0_client.models.provider_registry_api_download_version_request_path_params import ProviderRegistryApiDownloadVersionRequestPathParams

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRegistryApiDownloadVersionRequestPathParams from a JSON string
provider_registry_api_download_version_request_path_params_instance = ProviderRegistryApiDownloadVersionRequestPathParams.from_json(json)
# print the JSON string representation of the object
print(ProviderRegistryApiDownloadVersionRequestPathParams.to_json())

# convert the object into a dict
provider_registry_api_download_version_request_path_params_dict = provider_registry_api_download_version_request_path_params_instance.to_dict()
# create an instance of ProviderRegistryApiDownloadVersionRequestPathParams from a dict
provider_registry_api_download_version_request_path_params_from_dict = ProviderRegistryApiDownloadVersionRequestPathParams.from_dict(provider_registry_api_download_version_request_path_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


