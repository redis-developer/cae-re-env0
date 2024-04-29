# OrganizationApiPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_role** | **str** |  | 
**projects_permissions** | [**List[OrganizationApiProjectPermission]**](OrganizationApiProjectPermission.md) |  | [optional] 

## Example

```python
from env0_client.models.organization_api_permissions import OrganizationApiPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationApiPermissions from a JSON string
organization_api_permissions_instance = OrganizationApiPermissions.from_json(json)
# print the JSON string representation of the object
print(OrganizationApiPermissions.to_json())

# convert the object into a dict
organization_api_permissions_dict = organization_api_permissions_instance.to_dict()
# create an instance of OrganizationApiPermissions from a dict
organization_api_permissions_from_dict = OrganizationApiPermissions.from_dict(organization_api_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


