# ProjectApiProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**organization_id** | **str** |  | 
**parent_project_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**created_by** | **str** |  | 
**created_by_user** | [**User**](User.md) |  | [optional] 
**is_archived** | **bool** |  | [optional] 
**hierarchy** | **str** |  | 

## Example

```python
from env0_client.models.project_api_project import ProjectApiProject

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectApiProject from a JSON string
project_api_project_instance = ProjectApiProject.from_json(json)
# print the JSON string representation of the object
print(ProjectApiProject.to_json())

# convert the object into a dict
project_api_project_dict = project_api_project_instance.to_dict()
# create an instance of ProjectApiProject from a dict
project_api_project_from_dict = ProjectApiProject.from_dict(project_api_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


