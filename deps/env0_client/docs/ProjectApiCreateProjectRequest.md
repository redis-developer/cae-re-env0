# ProjectApiCreateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**organization_id** | **str** |  | 
**parent_project_id** | **str** |  | [optional] 

## Example

```python
from env0_client.models.project_api_create_project_request import ProjectApiCreateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectApiCreateProjectRequest from a JSON string
project_api_create_project_request_instance = ProjectApiCreateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectApiCreateProjectRequest.to_json())

# convert the object into a dict
project_api_create_project_request_dict = project_api_create_project_request_instance.to_dict()
# create an instance of ProjectApiCreateProjectRequest from a dict
project_api_create_project_request_from_dict = ProjectApiCreateProjectRequest.from_dict(project_api_create_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


