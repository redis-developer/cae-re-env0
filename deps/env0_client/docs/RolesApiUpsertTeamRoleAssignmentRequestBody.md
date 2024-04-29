# RolesApiUpsertTeamRoleAssignmentRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** |  | 
**role** | [**RolesApiRBACPermissionRole**](RolesApiRBACPermissionRole.md) |  | 
**environment_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 

## Example

```python
from env0_client.models.roles_api_upsert_team_role_assignment_request_body import RolesApiUpsertTeamRoleAssignmentRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of RolesApiUpsertTeamRoleAssignmentRequestBody from a JSON string
roles_api_upsert_team_role_assignment_request_body_instance = RolesApiUpsertTeamRoleAssignmentRequestBody.from_json(json)
# print the JSON string representation of the object
print(RolesApiUpsertTeamRoleAssignmentRequestBody.to_json())

# convert the object into a dict
roles_api_upsert_team_role_assignment_request_body_dict = roles_api_upsert_team_role_assignment_request_body_instance.to_dict()
# create an instance of RolesApiUpsertTeamRoleAssignmentRequestBody from a dict
roles_api_upsert_team_role_assignment_request_body_from_dict = RolesApiUpsertTeamRoleAssignmentRequestBody.from_dict(roles_api_upsert_team_role_assignment_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


