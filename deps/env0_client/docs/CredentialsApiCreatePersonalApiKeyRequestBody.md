# CredentialsApiCreatePersonalApiKeyRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from env0_client.models.credentials_api_create_personal_api_key_request_body import CredentialsApiCreatePersonalApiKeyRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsApiCreatePersonalApiKeyRequestBody from a JSON string
credentials_api_create_personal_api_key_request_body_instance = CredentialsApiCreatePersonalApiKeyRequestBody.from_json(json)
# print the JSON string representation of the object
print(CredentialsApiCreatePersonalApiKeyRequestBody.to_json())

# convert the object into a dict
credentials_api_create_personal_api_key_request_body_dict = credentials_api_create_personal_api_key_request_body_instance.to_dict()
# create an instance of CredentialsApiCreatePersonalApiKeyRequestBody from a dict
credentials_api_create_personal_api_key_request_body_from_dict = CredentialsApiCreatePersonalApiKeyRequestBody.from_dict(credentials_api_create_personal_api_key_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


