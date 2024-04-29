# RolesApiUpsertUserRoleAssignmentRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**role** | [**RolesApiRBACPermissionRole**](RolesApiRBACPermissionRole.md) |  | 
**environment_id** | **str** |  | 

## Example

```python
from env0_client.models.roles_api_upsert_user_role_assignment_request_body import RolesApiUpsertUserRoleAssignmentRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of RolesApiUpsertUserRoleAssignmentRequestBody from a JSON string
roles_api_upsert_user_role_assignment_request_body_instance = RolesApiUpsertUserRoleAssignmentRequestBody.from_json(json)
# print the JSON string representation of the object
print(RolesApiUpsertUserRoleAssignmentRequestBody.to_json())

# convert the object into a dict
roles_api_upsert_user_role_assignment_request_body_dict = roles_api_upsert_user_role_assignment_request_body_instance.to_dict()
# create an instance of RolesApiUpsertUserRoleAssignmentRequestBody from a dict
roles_api_upsert_user_role_assignment_request_body_from_dict = RolesApiUpsertUserRoleAssignmentRequestBody.from_dict(roles_api_upsert_user_role_assignment_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


