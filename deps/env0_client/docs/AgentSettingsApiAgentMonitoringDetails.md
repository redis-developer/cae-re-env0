# AgentSettingsApiAgentMonitoringDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_key** | **str** |  | 
**status** | [**AgentSettingsApiAgentStatus**](AgentSettingsApiAgentStatus.md) |  | 
**version** | **str** |  | [optional] 

## Example

```python
from env0_client.models.agent_settings_api_agent_monitoring_details import AgentSettingsApiAgentMonitoringDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSettingsApiAgentMonitoringDetails from a JSON string
agent_settings_api_agent_monitoring_details_instance = AgentSettingsApiAgentMonitoringDetails.from_json(json)
# print the JSON string representation of the object
print(AgentSettingsApiAgentMonitoringDetails.to_json())

# convert the object into a dict
agent_settings_api_agent_monitoring_details_dict = agent_settings_api_agent_monitoring_details_instance.to_dict()
# create an instance of AgentSettingsApiAgentMonitoringDetails from a dict
agent_settings_api_agent_monitoring_details_from_dict = AgentSettingsApiAgentMonitoringDetails.from_dict(agent_settings_api_agent_monitoring_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


