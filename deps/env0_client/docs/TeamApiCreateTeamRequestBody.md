# TeamApiCreateTeamRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**is_default_team** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.team_api_create_team_request_body import TeamApiCreateTeamRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of TeamApiCreateTeamRequestBody from a JSON string
team_api_create_team_request_body_instance = TeamApiCreateTeamRequestBody.from_json(json)
# print the JSON string representation of the object
print(TeamApiCreateTeamRequestBody.to_json())

# convert the object into a dict
team_api_create_team_request_body_dict = team_api_create_team_request_body_instance.to_dict()
# create an instance of TeamApiCreateTeamRequestBody from a dict
team_api_create_team_request_body_from_dict = TeamApiCreateTeamRequestBody.from_dict(team_api_create_team_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


