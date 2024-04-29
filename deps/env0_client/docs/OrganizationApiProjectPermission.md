# OrganizationApiProjectPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**project_role** | **str** |  | 

## Example

```python
from env0_client.models.organization_api_project_permission import OrganizationApiProjectPermission

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationApiProjectPermission from a JSON string
organization_api_project_permission_instance = OrganizationApiProjectPermission.from_json(json)
# print the JSON string representation of the object
print(OrganizationApiProjectPermission.to_json())

# convert the object into a dict
organization_api_project_permission_dict = organization_api_project_permission_instance.to_dict()
# create an instance of OrganizationApiProjectPermission from a dict
organization_api_project_permission_from_dict = OrganizationApiProjectPermission.from_dict(organization_api_project_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


