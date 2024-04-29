# TeamApiGetTeamsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[TeamApiTeam]**](TeamApiTeam.md) |  | 
**next_page_key** | **str** |  | [optional] 

## Example

```python
from env0_client.models.team_api_get_teams_response import TeamApiGetTeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TeamApiGetTeamsResponse from a JSON string
team_api_get_teams_response_instance = TeamApiGetTeamsResponse.from_json(json)
# print the JSON string representation of the object
print(TeamApiGetTeamsResponse.to_json())

# convert the object into a dict
team_api_get_teams_response_dict = team_api_get_teams_response_instance.to_dict()
# create an instance of TeamApiGetTeamsResponse from a dict
team_api_get_teams_response_from_dict = TeamApiGetTeamsResponse.from_dict(team_api_get_teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


