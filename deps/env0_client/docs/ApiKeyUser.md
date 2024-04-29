# ApiKeyUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**app_metadata** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**last_login** | **str** |  | [optional] 
**blocked** | **bool** |  | [optional] 
**identities** | [**List[ApiKeyUserIdentity]**](ApiKeyUserIdentity.md) |  | [optional] 

## Example

```python
from env0_client.models.api_key_user import ApiKeyUser

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyUser from a JSON string
api_key_user_instance = ApiKeyUser.from_json(json)
# print the JSON string representation of the object
print(ApiKeyUser.to_json())

# convert the object into a dict
api_key_user_dict = api_key_user_instance.to_dict()
# create an instance of ApiKeyUser from a dict
api_key_user_from_dict = ApiKeyUser.from_dict(api_key_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


