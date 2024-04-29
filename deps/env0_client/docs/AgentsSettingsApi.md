# env0_client.AgentsSettingsApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agents_settings_assign_agents**](AgentsSettingsApi.md#agents_settings_assign_agents) | **POST** /agents/projects-assignments | Assign agents to projects
[**agents_settings_get_agent_assignments**](AgentsSettingsApi.md#agents_settings_get_agent_assignments) | **GET** /agents/projects-assignments | Get agent assignments of projects
[**agents_settings_get_agent_values**](AgentsSettingsApi.md#agents_settings_get_agent_values) | **GET** /agents/{agentKey}/values | Get agent values file content
[**agents_settings_get_docker_agent_dot_env**](AgentsSettingsApi.md#agents_settings_get_docker_agent_dot_env) | **GET** /agents/{agentKey}/dotenv | Get agent .env file content
[**agents_settings_list_agents**](AgentsSettingsApi.md#agents_settings_list_agents) | **GET** /agents | List agents


# **agents_settings_assign_agents**
> AgentSettingsApiGetAgentAssignmentsResponse agents_settings_assign_agents(organization_id, request_body=request_body)

Assign agents to projects

gets a map of project ids to agent-key assignments

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.agent_settings_api_get_agent_assignments_response import AgentSettingsApiGetAgentAssignmentsResponse
from env0_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.env0.com
# See configuration.py for a list of all supported configuration parameters.
configuration = env0_client.Configuration(
    host = "https://api.env0.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: env0_API_Key
configuration = env0_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with env0_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = env0_client.AgentsSettingsApi(api_client)
    organization_id = 'organization_id_example' # str | 
    request_body = {'key': 'request_body_example'} # Dict[str, str] |  (optional)

    try:
        # Assign agents to projects
        api_response = api_instance.agents_settings_assign_agents(organization_id, request_body=request_body)
        print("The response of AgentsSettingsApi->agents_settings_assign_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsSettingsApi->agents_settings_assign_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **request_body** | [**Dict[str, str]**](str.md)|  | [optional] 

### Return type

[**AgentSettingsApiGetAgentAssignmentsResponse**](AgentSettingsApiGetAgentAssignmentsResponse.md)

### Authorization

[env0_API_Key](../README.md#env0_API_Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agents_settings_get_agent_assignments**
> AgentSettingsApiGetAgentAssignmentsResponse agents_settings_get_agent_assignments(organization_id)

Get agent assignments of projects

returns the current default agent key and a map of project ids to agent key assignments

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.agent_settings_api_get_agent_assignments_response import AgentSettingsApiGetAgentAssignmentsResponse
from env0_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.env0.com
# See configuration.py for a list of all supported configuration parameters.
configuration = env0_client.Configuration(
    host = "https://api.env0.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: env0_API_Key
configuration = env0_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with env0_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = env0_client.AgentsSettingsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Get agent assignments of projects
        api_response = api_instance.agents_settings_get_agent_assignments(organization_id)
        print("The response of AgentsSettingsApi->agents_settings_get_agent_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsSettingsApi->agents_settings_get_agent_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**AgentSettingsApiGetAgentAssignmentsResponse**](AgentSettingsApiGetAgentAssignmentsResponse.md)

### Authorization

[env0_API_Key](../README.md#env0_API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agents_settings_get_agent_values**
> str agents_settings_get_agent_values(agent_key)

Get agent values file content

Save it to a yaml file for helm

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.env0.com
# See configuration.py for a list of all supported configuration parameters.
configuration = env0_client.Configuration(
    host = "https://api.env0.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: env0_API_Key
configuration = env0_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with env0_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = env0_client.AgentsSettingsApi(api_client)
    agent_key = 'agent_key_example' # str | 

    try:
        # Get agent values file content
        api_response = api_instance.agents_settings_get_agent_values(agent_key)
        print("The response of AgentsSettingsApi->agents_settings_get_agent_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsSettingsApi->agents_settings_get_agent_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_key** | **str**|  | 

### Return type

**str**

### Authorization

[env0_API_Key](../README.md#env0_API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agents_settings_get_docker_agent_dot_env**
> str agents_settings_get_docker_agent_dot_env(agent_key)

Get agent .env file content

Save it to a bash file for docker

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.env0.com
# See configuration.py for a list of all supported configuration parameters.
configuration = env0_client.Configuration(
    host = "https://api.env0.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: env0_API_Key
configuration = env0_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with env0_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = env0_client.AgentsSettingsApi(api_client)
    agent_key = 'agent_key_example' # str | 

    try:
        # Get agent .env file content
        api_response = api_instance.agents_settings_get_docker_agent_dot_env(agent_key)
        print("The response of AgentsSettingsApi->agents_settings_get_docker_agent_dot_env:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsSettingsApi->agents_settings_get_docker_agent_dot_env: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_key** | **str**|  | 

### Return type

**str**

### Authorization

[env0_API_Key](../README.md#env0_API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agents_settings_list_agents**
> List[AgentSettingsApiAgentMonitoringDetails] agents_settings_list_agents(organization_id)

List agents

Get a list of the organization agents

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.agent_settings_api_agent_monitoring_details import AgentSettingsApiAgentMonitoringDetails
from env0_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.env0.com
# See configuration.py for a list of all supported configuration parameters.
configuration = env0_client.Configuration(
    host = "https://api.env0.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: env0_API_Key
configuration = env0_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with env0_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = env0_client.AgentsSettingsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # List agents
        api_response = api_instance.agents_settings_list_agents(organization_id)
        print("The response of AgentsSettingsApi->agents_settings_list_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsSettingsApi->agents_settings_list_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**List[AgentSettingsApiAgentMonitoringDetails]**](AgentSettingsApiAgentMonitoringDetails.md)

### Authorization

[env0_API_Key](../README.md#env0_API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

