# OrganizationApiOrganizationLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environments** | [**OrganizationApiOrganizationLimitsEnvironments**](OrganizationApiOrganizationLimitsEnvironments.md) |  | 

## Example

```python
from env0_client.models.organization_api_organization_limits import OrganizationApiOrganizationLimits

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationApiOrganizationLimits from a JSON string
organization_api_organization_limits_instance = OrganizationApiOrganizationLimits.from_json(json)
# print the JSON string representation of the object
print(OrganizationApiOrganizationLimits.to_json())

# convert the object into a dict
organization_api_organization_limits_dict = organization_api_organization_limits_instance.to_dict()
# create an instance of OrganizationApiOrganizationLimits from a dict
organization_api_organization_limits_from_dict = OrganizationApiOrganizationLimits.from_dict(organization_api_organization_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


