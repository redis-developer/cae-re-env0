# ProjectApiUpdateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from env0_client.models.project_api_update_project_request import ProjectApiUpdateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectApiUpdateProjectRequest from a JSON string
project_api_update_project_request_instance = ProjectApiUpdateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectApiUpdateProjectRequest.to_json())

# convert the object into a dict
project_api_update_project_request_dict = project_api_update_project_request_instance.to_dict()
# create an instance of ProjectApiUpdateProjectRequest from a dict
project_api_update_project_request_from_dict = ProjectApiUpdateProjectRequest.from_dict(project_api_update_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


