# OrganizationApiOrganizationLimitsEnvironments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** |  | [optional] 
**amount** | **float** |  | [optional] 
**limit_reached** | **bool** |  | 

## Example

```python
from env0_client.models.organization_api_organization_limits_environments import OrganizationApiOrganizationLimitsEnvironments

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationApiOrganizationLimitsEnvironments from a JSON string
organization_api_organization_limits_environments_instance = OrganizationApiOrganizationLimitsEnvironments.from_json(json)
# print the JSON string representation of the object
print(OrganizationApiOrganizationLimitsEnvironments.to_json())

# convert the object into a dict
organization_api_organization_limits_environments_dict = organization_api_organization_limits_environments_instance.to_dict()
# create an instance of OrganizationApiOrganizationLimitsEnvironments from a dict
organization_api_organization_limits_environments_from_dict = OrganizationApiOrganizationLimitsEnvironments.from_dict(organization_api_organization_limits_environments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


