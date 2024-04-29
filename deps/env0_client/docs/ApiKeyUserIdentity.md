# ApiKeyUserIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**profile_data** | [**ApiKeyUserIdentityProfileData**](ApiKeyUserIdentityProfileData.md) |  | [optional] 
**blocked** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.api_key_user_identity import ApiKeyUserIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyUserIdentity from a JSON string
api_key_user_identity_instance = ApiKeyUserIdentity.from_json(json)
# print the JSON string representation of the object
print(ApiKeyUserIdentity.to_json())

# convert the object into a dict
api_key_user_identity_dict = api_key_user_identity_instance.to_dict()
# create an instance of ApiKeyUserIdentity from a dict
api_key_user_identity_from_dict = ApiKeyUserIdentity.from_dict(api_key_user_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


