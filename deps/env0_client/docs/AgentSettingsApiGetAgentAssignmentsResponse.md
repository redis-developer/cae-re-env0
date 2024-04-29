# AgentSettingsApiGetAgentAssignmentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_agent** | **str** |  | 
**projects_agents** | **Dict[str, str]** |  | 

## Example

```python
from env0_client.models.agent_settings_api_get_agent_assignments_response import AgentSettingsApiGetAgentAssignmentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSettingsApiGetAgentAssignmentsResponse from a JSON string
agent_settings_api_get_agent_assignments_response_instance = AgentSettingsApiGetAgentAssignmentsResponse.from_json(json)
# print the JSON string representation of the object
print(AgentSettingsApiGetAgentAssignmentsResponse.to_json())

# convert the object into a dict
agent_settings_api_get_agent_assignments_response_dict = agent_settings_api_get_agent_assignments_response_instance.to_dict()
# create an instance of AgentSettingsApiGetAgentAssignmentsResponse from a dict
agent_settings_api_get_agent_assignments_response_from_dict = AgentSettingsApiGetAgentAssignmentsResponse.from_dict(agent_settings_api_get_agent_assignments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


