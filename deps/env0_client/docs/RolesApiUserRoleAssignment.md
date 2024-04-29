# RolesApiUserRoleAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**role** | [**RolesApiRBACPermissionRole**](RolesApiRBACPermissionRole.md) |  | [optional] 
**organization_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from env0_client.models.roles_api_user_role_assignment import RolesApiUserRoleAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of RolesApiUserRoleAssignment from a JSON string
roles_api_user_role_assignment_instance = RolesApiUserRoleAssignment.from_json(json)
# print the JSON string representation of the object
print(RolesApiUserRoleAssignment.to_json())

# convert the object into a dict
roles_api_user_role_assignment_dict = roles_api_user_role_assignment_instance.to_dict()
# create an instance of RolesApiUserRoleAssignment from a dict
roles_api_user_role_assignment_from_dict = RolesApiUserRoleAssignment.from_dict(roles_api_user_role_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


