# RolesApiRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**organization_id** | **str** |  | [optional] 
**permissions** | [**List[RBACPermission]**](RBACPermission.md) |  | 
**is_default_role** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.roles_api_role import RolesApiRole

# TODO update the JSON string below
json = "{}"
# create an instance of RolesApiRole from a JSON string
roles_api_role_instance = RolesApiRole.from_json(json)
# print the JSON string representation of the object
print(RolesApiRole.to_json())

# convert the object into a dict
roles_api_role_dict = roles_api_role_instance.to_dict()
# create an instance of RolesApiRole from a dict
roles_api_role_from_dict = RolesApiRole.from_dict(roles_api_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


