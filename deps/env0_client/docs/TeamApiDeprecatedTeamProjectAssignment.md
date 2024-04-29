# TeamApiDeprecatedTeamProjectAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**team_id** | **str** |  | 
**project_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**project_role** | **str** |  | 

## Example

```python
from env0_client.models.team_api_deprecated_team_project_assignment import TeamApiDeprecatedTeamProjectAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of TeamApiDeprecatedTeamProjectAssignment from a JSON string
team_api_deprecated_team_project_assignment_instance = TeamApiDeprecatedTeamProjectAssignment.from_json(json)
# print the JSON string representation of the object
print(TeamApiDeprecatedTeamProjectAssignment.to_json())

# convert the object into a dict
team_api_deprecated_team_project_assignment_dict = team_api_deprecated_team_project_assignment_instance.to_dict()
# create an instance of TeamApiDeprecatedTeamProjectAssignment from a dict
team_api_deprecated_team_project_assignment_from_dict = TeamApiDeprecatedTeamProjectAssignment.from_dict(team_api_deprecated_team_project_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


