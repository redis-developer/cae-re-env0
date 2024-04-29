# CredentialsApiApiKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**api_key_id** | **str** |  | 
**last_used_at** | **str** |  | 
**organization_id** | **str** |  | 
**created_at** | **str** |  | 
**created_by** | **str** |  | 
**created_by_user** | [**ApiKeyUser**](ApiKeyUser.md) |  | [optional] 
**api_key_secret** | **str** |  | [optional] 
**organization_role** | **str** |  | 
**is_blocked** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.credentials_api_api_key import CredentialsApiApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsApiApiKey from a JSON string
credentials_api_api_key_instance = CredentialsApiApiKey.from_json(json)
# print the JSON string representation of the object
print(CredentialsApiApiKey.to_json())

# convert the object into a dict
credentials_api_api_key_dict = credentials_api_api_key_instance.to_dict()
# create an instance of CredentialsApiApiKey from a dict
credentials_api_api_key_from_dict = CredentialsApiApiKey.from_dict(credentials_api_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


