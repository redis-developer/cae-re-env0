# ProviderRegistryApiCreateProviderRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**organization_id** | **str** |  | 
**description** | **str** |  | [optional] 
**created_by_user** | [**User**](User.md) |  | [optional] 

## Example

```python
from env0_client.models.provider_registry_api_create_provider_request_body import ProviderRegistryApiCreateProviderRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRegistryApiCreateProviderRequestBody from a JSON string
provider_registry_api_create_provider_request_body_instance = ProviderRegistryApiCreateProviderRequestBody.from_json(json)
# print the JSON string representation of the object
print(ProviderRegistryApiCreateProviderRequestBody.to_json())

# convert the object into a dict
provider_registry_api_create_provider_request_body_dict = provider_registry_api_create_provider_request_body_instance.to_dict()
# create an instance of ProviderRegistryApiCreateProviderRequestBody from a dict
provider_registry_api_create_provider_request_body_from_dict = ProviderRegistryApiCreateProviderRequestBody.from_dict(provider_registry_api_create_provider_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


