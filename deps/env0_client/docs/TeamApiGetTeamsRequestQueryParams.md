# TeamApiGetTeamsRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **str** |  | [optional] 
**offset** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from env0_client.models.team_api_get_teams_request_query_params import TeamApiGetTeamsRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of TeamApiGetTeamsRequestQueryParams from a JSON string
team_api_get_teams_request_query_params_instance = TeamApiGetTeamsRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(TeamApiGetTeamsRequestQueryParams.to_json())

# convert the object into a dict
team_api_get_teams_request_query_params_dict = team_api_get_teams_request_query_params_instance.to_dict()
# create an instance of TeamApiGetTeamsRequestQueryParams from a dict
team_api_get_teams_request_query_params_from_dict = TeamApiGetTeamsRequestQueryParams.from_dict(team_api_get_teams_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


