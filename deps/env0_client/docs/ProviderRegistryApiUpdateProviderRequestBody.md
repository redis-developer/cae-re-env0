# ProviderRegistryApiUpdateProviderRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 

## Example

```python
from env0_client.models.provider_registry_api_update_provider_request_body import ProviderRegistryApiUpdateProviderRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRegistryApiUpdateProviderRequestBody from a JSON string
provider_registry_api_update_provider_request_body_instance = ProviderRegistryApiUpdateProviderRequestBody.from_json(json)
# print the JSON string representation of the object
print(ProviderRegistryApiUpdateProviderRequestBody.to_json())

# convert the object into a dict
provider_registry_api_update_provider_request_body_dict = provider_registry_api_update_provider_request_body_instance.to_dict()
# create an instance of ProviderRegistryApiUpdateProviderRequestBody from a dict
provider_registry_api_update_provider_request_body_from_dict = ProviderRegistryApiUpdateProviderRequestBody.from_dict(provider_registry_api_update_provider_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


