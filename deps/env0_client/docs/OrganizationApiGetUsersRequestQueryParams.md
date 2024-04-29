# OrganizationApiGetUsersRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_api_keys** | **str** |  | [optional] 
**query** | **str** |  | [optional] 

## Example

```python
from env0_client.models.organization_api_get_users_request_query_params import OrganizationApiGetUsersRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationApiGetUsersRequestQueryParams from a JSON string
organization_api_get_users_request_query_params_instance = OrganizationApiGetUsersRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(OrganizationApiGetUsersRequestQueryParams.to_json())

# convert the object into a dict
organization_api_get_users_request_query_params_dict = organization_api_get_users_request_query_params_instance.to_dict()
# create an instance of OrganizationApiGetUsersRequestQueryParams from a dict
organization_api_get_users_request_query_params_from_dict = OrganizationApiGetUsersRequestQueryParams.from_dict(organization_api_get_users_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


