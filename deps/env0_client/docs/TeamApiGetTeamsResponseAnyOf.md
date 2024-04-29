# TeamApiGetTeamsResponseAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[TeamApiTeam]**](TeamApiTeam.md) |  | 
**next_page_key** | **str** |  | [optional] 

## Example

```python
from env0_client.models.team_api_get_teams_response_any_of import TeamApiGetTeamsResponseAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of TeamApiGetTeamsResponseAnyOf from a JSON string
team_api_get_teams_response_any_of_instance = TeamApiGetTeamsResponseAnyOf.from_json(json)
# print the JSON string representation of the object
print(TeamApiGetTeamsResponseAnyOf.to_json())

# convert the object into a dict
team_api_get_teams_response_any_of_dict = team_api_get_teams_response_any_of_instance.to_dict()
# create an instance of TeamApiGetTeamsResponseAnyOf from a dict
team_api_get_teams_response_any_of_from_dict = TeamApiGetTeamsResponseAnyOf.from_dict(team_api_get_teams_response_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


