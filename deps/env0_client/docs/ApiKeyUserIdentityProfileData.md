# ApiKeyUserIdentityProfileData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from env0_client.models.api_key_user_identity_profile_data import ApiKeyUserIdentityProfileData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyUserIdentityProfileData from a JSON string
api_key_user_identity_profile_data_instance = ApiKeyUserIdentityProfileData.from_json(json)
# print the JSON string representation of the object
print(ApiKeyUserIdentityProfileData.to_json())

# convert the object into a dict
api_key_user_identity_profile_data_dict = api_key_user_identity_profile_data_instance.to_dict()
# create an instance of ApiKeyUserIdentityProfileData from a dict
api_key_user_identity_profile_data_from_dict = ApiKeyUserIdentityProfileData.from_dict(api_key_user_identity_profile_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


