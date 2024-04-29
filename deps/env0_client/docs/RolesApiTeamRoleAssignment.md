# RolesApiTeamRoleAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**role** | [**RolesApiRBACPermissionRole**](RolesApiRBACPermissionRole.md) |  | [optional] 
**organization_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from env0_client.models.roles_api_team_role_assignment import RolesApiTeamRoleAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of RolesApiTeamRoleAssignment from a JSON string
roles_api_team_role_assignment_instance = RolesApiTeamRoleAssignment.from_json(json)
# print the JSON string representation of the object
print(RolesApiTeamRoleAssignment.to_json())

# convert the object into a dict
roles_api_team_role_assignment_dict = roles_api_team_role_assignment_instance.to_dict()
# create an instance of RolesApiTeamRoleAssignment from a dict
roles_api_team_role_assignment_from_dict = RolesApiTeamRoleAssignment.from_dict(roles_api_team_role_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


