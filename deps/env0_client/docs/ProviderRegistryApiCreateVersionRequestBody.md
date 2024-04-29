# ProviderRegistryApiCreateVersionRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | 
**gpg_key_id** | **str** |  | 

## Example

```python
from env0_client.models.provider_registry_api_create_version_request_body import ProviderRegistryApiCreateVersionRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRegistryApiCreateVersionRequestBody from a JSON string
provider_registry_api_create_version_request_body_instance = ProviderRegistryApiCreateVersionRequestBody.from_json(json)
# print the JSON string representation of the object
print(ProviderRegistryApiCreateVersionRequestBody.to_json())

# convert the object into a dict
provider_registry_api_create_version_request_body_dict = provider_registry_api_create_version_request_body_instance.to_dict()
# create an instance of ProviderRegistryApiCreateVersionRequestBody from a dict
provider_registry_api_create_version_request_body_from_dict = ProviderRegistryApiCreateVersionRequestBody.from_dict(provider_registry_api_create_version_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


