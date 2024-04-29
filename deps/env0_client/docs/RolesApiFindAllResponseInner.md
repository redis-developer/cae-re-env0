# RolesApiFindAllResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**permissions** | [**List[RBACPermission]**](RBACPermission.md) |  | 
**is_default_role** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.roles_api_find_all_response_inner import RolesApiFindAllResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RolesApiFindAllResponseInner from a JSON string
roles_api_find_all_response_inner_instance = RolesApiFindAllResponseInner.from_json(json)
# print the JSON string representation of the object
print(RolesApiFindAllResponseInner.to_json())

# convert the object into a dict
roles_api_find_all_response_inner_dict = roles_api_find_all_response_inner_instance.to_dict()
# create an instance of RolesApiFindAllResponseInner from a dict
roles_api_find_all_response_inner_from_dict = RolesApiFindAllResponseInner.from_dict(roles_api_find_all_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


