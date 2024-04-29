# CredentialsApiPersonalApiKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**api_key_id** | **str** |  | 
**api_key_secret** | **str** |  | [optional] 
**is_blocked** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.credentials_api_personal_api_key import CredentialsApiPersonalApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsApiPersonalApiKey from a JSON string
credentials_api_personal_api_key_instance = CredentialsApiPersonalApiKey.from_json(json)
# print the JSON string representation of the object
print(CredentialsApiPersonalApiKey.to_json())

# convert the object into a dict
credentials_api_personal_api_key_dict = credentials_api_personal_api_key_instance.to_dict()
# create an instance of CredentialsApiPersonalApiKey from a dict
credentials_api_personal_api_key_from_dict = CredentialsApiPersonalApiKey.from_dict(credentials_api_personal_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


