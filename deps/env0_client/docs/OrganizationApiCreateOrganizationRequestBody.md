# OrganizationApiCreateOrganizationRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 

## Example

```python
from env0_client.models.organization_api_create_organization_request_body import OrganizationApiCreateOrganizationRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationApiCreateOrganizationRequestBody from a JSON string
organization_api_create_organization_request_body_instance = OrganizationApiCreateOrganizationRequestBody.from_json(json)
# print the JSON string representation of the object
print(OrganizationApiCreateOrganizationRequestBody.to_json())

# convert the object into a dict
organization_api_create_organization_request_body_dict = organization_api_create_organization_request_body_instance.to_dict()
# create an instance of OrganizationApiCreateOrganizationRequestBody from a dict
organization_api_create_organization_request_body_from_dict = OrganizationApiCreateOrganizationRequestBody.from_dict(organization_api_create_organization_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


