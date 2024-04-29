# TeamApiDeprecatedUpdateAssignmentsRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**assignments** | [**List[TeamApiDeprecatedUpdateAssignmentsTeamRoleTuple]**](TeamApiDeprecatedUpdateAssignmentsTeamRoleTuple.md) |  | 

## Example

```python
from env0_client.models.team_api_deprecated_update_assignments_request_body import TeamApiDeprecatedUpdateAssignmentsRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of TeamApiDeprecatedUpdateAssignmentsRequestBody from a JSON string
team_api_deprecated_update_assignments_request_body_instance = TeamApiDeprecatedUpdateAssignmentsRequestBody.from_json(json)
# print the JSON string representation of the object
print(TeamApiDeprecatedUpdateAssignmentsRequestBody.to_json())

# convert the object into a dict
team_api_deprecated_update_assignments_request_body_dict = team_api_deprecated_update_assignments_request_body_instance.to_dict()
# create an instance of TeamApiDeprecatedUpdateAssignmentsRequestBody from a dict
team_api_deprecated_update_assignments_request_body_from_dict = TeamApiDeprecatedUpdateAssignmentsRequestBody.from_dict(team_api_deprecated_update_assignments_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


