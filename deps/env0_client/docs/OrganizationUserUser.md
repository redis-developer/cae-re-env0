# OrganizationUserUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**last_login** | **str** |  | [optional] 
**picture** | **str** |  | [optional] 
**given_name** | **str** |  | [optional] 
**family_name** | **str** |  | [optional] 
**app_metadata** | [**OrganizationUserUserAppMetadata**](OrganizationUserUserAppMetadata.md) |  | [optional] 

## Example

```python
from env0_client.models.organization_user_user import OrganizationUserUser

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUserUser from a JSON string
organization_user_user_instance = OrganizationUserUser.from_json(json)
# print the JSON string representation of the object
print(OrganizationUserUser.to_json())

# convert the object into a dict
organization_user_user_dict = organization_user_user_instance.to_dict()
# create an instance of OrganizationUserUser from a dict
organization_user_user_from_dict = OrganizationUserUser.from_dict(organization_user_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


