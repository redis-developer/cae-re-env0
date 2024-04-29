# RolesApiUpdateRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**permissions** | [**List[RBACPermission]**](RBACPermission.md) |  | [optional] 

## Example

```python
from env0_client.models.roles_api_update_request_body import RolesApiUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of RolesApiUpdateRequestBody from a JSON string
roles_api_update_request_body_instance = RolesApiUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print(RolesApiUpdateRequestBody.to_json())

# convert the object into a dict
roles_api_update_request_body_dict = roles_api_update_request_body_instance.to_dict()
# create an instance of RolesApiUpdateRequestBody from a dict
roles_api_update_request_body_from_dict = RolesApiUpdateRequestBody.from_dict(roles_api_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


