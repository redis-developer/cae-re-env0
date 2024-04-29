# TeamApiTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**organization_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**users** | [**List[User]**](User.md) |  | [optional] 
**created_by_user** | [**User**](User.md) |  | [optional] 
**is_default_team** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.team_api_team import TeamApiTeam

# TODO update the JSON string below
json = "{}"
# create an instance of TeamApiTeam from a JSON string
team_api_team_instance = TeamApiTeam.from_json(json)
# print the JSON string representation of the object
print(TeamApiTeam.to_json())

# convert the object into a dict
team_api_team_dict = team_api_team_instance.to_dict()
# create an instance of TeamApiTeam from a dict
team_api_team_from_dict = TeamApiTeam.from_dict(team_api_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


