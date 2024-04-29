# BlueprintApiModuleRegistryDownloadSourceRequestPathParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**module_name** | **str** |  | 
**provider_name** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from env0_client.models.blueprint_api_module_registry_download_source_request_path_params import BlueprintApiModuleRegistryDownloadSourceRequestPathParams

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiModuleRegistryDownloadSourceRequestPathParams from a JSON string
blueprint_api_module_registry_download_source_request_path_params_instance = BlueprintApiModuleRegistryDownloadSourceRequestPathParams.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiModuleRegistryDownloadSourceRequestPathParams.to_json())

# convert the object into a dict
blueprint_api_module_registry_download_source_request_path_params_dict = blueprint_api_module_registry_download_source_request_path_params_instance.to_dict()
# create an instance of BlueprintApiModuleRegistryDownloadSourceRequestPathParams from a dict
blueprint_api_module_registry_download_source_request_path_params_from_dict = BlueprintApiModuleRegistryDownloadSourceRequestPathParams.from_dict(blueprint_api_module_registry_download_source_request_path_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


