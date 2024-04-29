# ConfigurationSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**assignment_scope_id** | **str** |  | 
**assignment_scope** | [**ConfigurationSetAssignmentScope**](ConfigurationSetAssignmentScope.md) |  | [optional] 
**creation_scope_id** | **str** |  | 
**creation_scope** | [**SetCreationScope**](SetCreationScope.md) |  | 
**organization_id** | **str** |  | 
**created_by** | **str** |  | 
**created_by_user** | [**User**](User.md) |  | [optional] 
**to_delete** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from env0_client.models.configuration_set import ConfigurationSet

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationSet from a JSON string
configuration_set_instance = ConfigurationSet.from_json(json)
# print the JSON string representation of the object
print(ConfigurationSet.to_json())

# convert the object into a dict
configuration_set_dict = configuration_set_instance.to_dict()
# create an instance of ConfigurationSet from a dict
configuration_set_from_dict = ConfigurationSet.from_dict(configuration_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


