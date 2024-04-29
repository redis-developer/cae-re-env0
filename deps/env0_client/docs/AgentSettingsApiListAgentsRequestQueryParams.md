# AgentSettingsApiListAgentsRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 

## Example

```python
from env0_client.models.agent_settings_api_list_agents_request_query_params import AgentSettingsApiListAgentsRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSettingsApiListAgentsRequestQueryParams from a JSON string
agent_settings_api_list_agents_request_query_params_instance = AgentSettingsApiListAgentsRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(AgentSettingsApiListAgentsRequestQueryParams.to_json())

# convert the object into a dict
agent_settings_api_list_agents_request_query_params_dict = agent_settings_api_list_agents_request_query_params_instance.to_dict()
# create an instance of AgentSettingsApiListAgentsRequestQueryParams from a dict
agent_settings_api_list_agents_request_query_params_from_dict = AgentSettingsApiListAgentsRequestQueryParams.from_dict(agent_settings_api_list_agents_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


