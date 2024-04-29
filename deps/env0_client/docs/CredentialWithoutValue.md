# CredentialWithoutValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**organization_id** | **str** |  | 
**value** | **object** |  | 
**encryption_method** | **str** |  | [optional] 
**type** | [**CredentialType**](CredentialType.md) |  | 
**created_by_user** | [**User**](User.md) |  | [optional] 
**updated_at** | **datetime** |  | 

## Example

```python
from env0_client.models.credential_without_value import CredentialWithoutValue

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialWithoutValue from a JSON string
credential_without_value_instance = CredentialWithoutValue.from_json(json)
# print the JSON string representation of the object
print(CredentialWithoutValue.to_json())

# convert the object into a dict
credential_without_value_dict = credential_without_value_instance.to_dict()
# create an instance of CredentialWithoutValue from a dict
credential_without_value_from_dict = CredentialWithoutValue.from_dict(credential_without_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


