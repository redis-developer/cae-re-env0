# RolesApiGetRoleAssignmentsRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 

## Example

```python
from env0_client.models.roles_api_get_role_assignments_request_query_params import RolesApiGetRoleAssignmentsRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of RolesApiGetRoleAssignmentsRequestQueryParams from a JSON string
roles_api_get_role_assignments_request_query_params_instance = RolesApiGetRoleAssignmentsRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(RolesApiGetRoleAssignmentsRequestQueryParams.to_json())

# convert the object into a dict
roles_api_get_role_assignments_request_query_params_dict = roles_api_get_role_assignments_request_query_params_instance.to_dict()
# create an instance of RolesApiGetRoleAssignmentsRequestQueryParams from a dict
roles_api_get_role_assignments_request_query_params_from_dict = RolesApiGetRoleAssignmentsRequestQueryParams.from_dict(roles_api_get_role_assignments_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


