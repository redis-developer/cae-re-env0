# RolesApiCreateRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**permissions** | [**List[RBACPermission]**](RBACPermission.md) |  | [optional] 

## Example

```python
from env0_client.models.roles_api_create_request_body import RolesApiCreateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of RolesApiCreateRequestBody from a JSON string
roles_api_create_request_body_instance = RolesApiCreateRequestBody.from_json(json)
# print the JSON string representation of the object
print(RolesApiCreateRequestBody.to_json())

# convert the object into a dict
roles_api_create_request_body_dict = roles_api_create_request_body_instance.to_dict()
# create an instance of RolesApiCreateRequestBody from a dict
roles_api_create_request_body_from_dict = RolesApiCreateRequestBody.from_dict(roles_api_create_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


