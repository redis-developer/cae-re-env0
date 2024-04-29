# TeamApiUpdateTeamRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 

## Example

```python
from env0_client.models.team_api_update_team_request_body import TeamApiUpdateTeamRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of TeamApiUpdateTeamRequestBody from a JSON string
team_api_update_team_request_body_instance = TeamApiUpdateTeamRequestBody.from_json(json)
# print the JSON string representation of the object
print(TeamApiUpdateTeamRequestBody.to_json())

# convert the object into a dict
team_api_update_team_request_body_dict = team_api_update_team_request_body_instance.to_dict()
# create an instance of TeamApiUpdateTeamRequestBody from a dict
team_api_update_team_request_body_from_dict = TeamApiUpdateTeamRequestBody.from_dict(team_api_update_team_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


