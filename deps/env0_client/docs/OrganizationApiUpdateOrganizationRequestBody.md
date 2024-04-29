# OrganizationApiUpdateOrganizationRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**photo_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from env0_client.models.organization_api_update_organization_request_body import OrganizationApiUpdateOrganizationRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationApiUpdateOrganizationRequestBody from a JSON string
organization_api_update_organization_request_body_instance = OrganizationApiUpdateOrganizationRequestBody.from_json(json)
# print the JSON string representation of the object
print(OrganizationApiUpdateOrganizationRequestBody.to_json())

# convert the object into a dict
organization_api_update_organization_request_body_dict = organization_api_update_organization_request_body_instance.to_dict()
# create an instance of OrganizationApiUpdateOrganizationRequestBody from a dict
organization_api_update_organization_request_body_from_dict = OrganizationApiUpdateOrganizationRequestBody.from_dict(organization_api_update_organization_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


