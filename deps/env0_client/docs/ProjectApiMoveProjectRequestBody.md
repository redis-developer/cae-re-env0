# ProjectApiMoveProjectRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_project_id** | **str** |  | 

## Example

```python
from env0_client.models.project_api_move_project_request_body import ProjectApiMoveProjectRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectApiMoveProjectRequestBody from a JSON string
project_api_move_project_request_body_instance = ProjectApiMoveProjectRequestBody.from_json(json)
# print the JSON string representation of the object
print(ProjectApiMoveProjectRequestBody.to_json())

# convert the object into a dict
project_api_move_project_request_body_dict = project_api_move_project_request_body_instance.to_dict()
# create an instance of ProjectApiMoveProjectRequestBody from a dict
project_api_move_project_request_body_from_dict = ProjectApiMoveProjectRequestBody.from_dict(project_api_move_project_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


