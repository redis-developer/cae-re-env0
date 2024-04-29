# CredentialsApiCreateApiKeyRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**organization_id** | **str** |  | 
**permissions** | [**OrganizationApiPermissions**](OrganizationApiPermissions.md) |  | [optional] 

## Example

```python
from env0_client.models.credentials_api_create_api_key_request_body import CredentialsApiCreateApiKeyRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsApiCreateApiKeyRequestBody from a JSON string
credentials_api_create_api_key_request_body_instance = CredentialsApiCreateApiKeyRequestBody.from_json(json)
# print the JSON string representation of the object
print(CredentialsApiCreateApiKeyRequestBody.to_json())

# convert the object into a dict
credentials_api_create_api_key_request_body_dict = credentials_api_create_api_key_request_body_instance.to_dict()
# create an instance of CredentialsApiCreateApiKeyRequestBody from a dict
credentials_api_create_api_key_request_body_from_dict = CredentialsApiCreateApiKeyRequestBody.from_dict(credentials_api_create_api_key_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


