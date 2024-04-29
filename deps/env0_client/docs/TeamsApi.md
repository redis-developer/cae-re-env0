# env0_client.TeamsApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_create_team**](TeamsApi.md#teams_create_team) | **POST** /teams | Create Team
[**teams_delete_team**](TeamsApi.md#teams_delete_team) | **DELETE** /teams/{teamId} | Delete Team
[**teams_deprecated_create_or_update_single_assignment**](TeamsApi.md#teams_deprecated_create_or_update_single_assignment) | **POST** /teams/assignments | Create or Update a single Team to Project Assignment
[**teams_deprecated_delete_single_assignment**](TeamsApi.md#teams_deprecated_delete_single_assignment) | **DELETE** /teams/assignments/{assignmentId} | Delete a single Team to Project Assignment
[**teams_deprecated_get_assignments**](TeamsApi.md#teams_deprecated_get_assignments) | **GET** /teams/assignments | List Project Teams Permissions
[**teams_deprecated_update_assignments**](TeamsApi.md#teams_deprecated_update_assignments) | **PUT** /teams/assignments | Update Teams Assignments
[**teams_get_team**](TeamsApi.md#teams_get_team) | **GET** /teams/{teamId} | Get Team
[**teams_get_teams**](TeamsApi.md#teams_get_teams) | **GET** /teams/organizations/{organizationId} | List Teams
[**teams_update_team**](TeamsApi.md#teams_update_team) | **PUT** /teams/{teamId} | Update Team


# **teams_create_team**
> TeamApiTeam teams_create_team(team_api_create_team_request_body=team_api_create_team_request_body)

Create Team

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.team_api_create_team_request_body import TeamApiCreateTeamRequestBody
from env0_client.models.team_api_team import TeamApiTeam
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
    api_instance = env0_client.TeamsApi(api_client)
    team_api_create_team_request_body = env0_client.TeamApiCreateTeamRequestBody() # TeamApiCreateTeamRequestBody |  (optional)

    try:
        # Create Team
        api_response = api_instance.teams_create_team(team_api_create_team_request_body=team_api_create_team_request_body)
        print("The response of TeamsApi->teams_create_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_create_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_api_create_team_request_body** | [**TeamApiCreateTeamRequestBody**](TeamApiCreateTeamRequestBody.md)|  | [optional] 

### Return type

[**TeamApiTeam**](TeamApiTeam.md)

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

# **teams_delete_team**
> teams_delete_team(team_id)

Delete Team

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
    api_instance = env0_client.TeamsApi(api_client)
    team_id = 'team_id_example' # str | 

    try:
        # Delete Team
        api_instance.teams_delete_team(team_id)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_delete_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[env0_API_Key](../README.md#env0_API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Status 204 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_deprecated_create_or_update_single_assignment**
> TeamApiDeprecatedTeamProjectAssignment teams_deprecated_create_or_update_single_assignment(team_api_deprecated_create_or_update_single_assignment_request_body=team_api_deprecated_create_or_update_single_assignment_request_body)

Create or Update a single Team to Project Assignment

This API is deprecated. Please use \"Create or Update a Role Assignment for a Team\" instead.

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.team_api_deprecated_create_or_update_single_assignment_request_body import TeamApiDeprecatedCreateOrUpdateSingleAssignmentRequestBody
from env0_client.models.team_api_deprecated_team_project_assignment import TeamApiDeprecatedTeamProjectAssignment
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
    api_instance = env0_client.TeamsApi(api_client)
    team_api_deprecated_create_or_update_single_assignment_request_body = env0_client.TeamApiDeprecatedCreateOrUpdateSingleAssignmentRequestBody() # TeamApiDeprecatedCreateOrUpdateSingleAssignmentRequestBody |  (optional)

    try:
        # Create or Update a single Team to Project Assignment
        api_response = api_instance.teams_deprecated_create_or_update_single_assignment(team_api_deprecated_create_or_update_single_assignment_request_body=team_api_deprecated_create_or_update_single_assignment_request_body)
        print("The response of TeamsApi->teams_deprecated_create_or_update_single_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_deprecated_create_or_update_single_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_api_deprecated_create_or_update_single_assignment_request_body** | [**TeamApiDeprecatedCreateOrUpdateSingleAssignmentRequestBody**](TeamApiDeprecatedCreateOrUpdateSingleAssignmentRequestBody.md)|  | [optional] 

### Return type

[**TeamApiDeprecatedTeamProjectAssignment**](TeamApiDeprecatedTeamProjectAssignment.md)

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

# **teams_deprecated_delete_single_assignment**
> teams_deprecated_delete_single_assignment(assignment_id)

Delete a single Team to Project Assignment

This API is deprecated. Please use \"Remove a Role Assignment for a Team\" instead.

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
    api_instance = env0_client.TeamsApi(api_client)
    assignment_id = 'assignment_id_example' # str | 

    try:
        # Delete a single Team to Project Assignment
        api_instance.teams_deprecated_delete_single_assignment(assignment_id)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_deprecated_delete_single_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[env0_API_Key](../README.md#env0_API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Status 204 Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_deprecated_get_assignments**
> List[TeamApiDeprecatedTeamProjectAssignment] teams_deprecated_get_assignments(project_id)

List Project Teams Permissions

This API is deprecated. Please use \"Get Team Role Assignments\" instead.

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.team_api_deprecated_team_project_assignment import TeamApiDeprecatedTeamProjectAssignment
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
    api_instance = env0_client.TeamsApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # List Project Teams Permissions
        api_response = api_instance.teams_deprecated_get_assignments(project_id)
        print("The response of TeamsApi->teams_deprecated_get_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_deprecated_get_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**List[TeamApiDeprecatedTeamProjectAssignment]**](TeamApiDeprecatedTeamProjectAssignment.md)

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

# **teams_deprecated_update_assignments**
> List[TeamApiDeprecatedTeamProjectAssignment] teams_deprecated_update_assignments(team_api_deprecated_update_assignments_request_body=team_api_deprecated_update_assignments_request_body)

Update Teams Assignments

This API is deprecated. Please use \"Create or Update a Role Assignment for a Team\" instead.

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.team_api_deprecated_team_project_assignment import TeamApiDeprecatedTeamProjectAssignment
from env0_client.models.team_api_deprecated_update_assignments_request_body import TeamApiDeprecatedUpdateAssignmentsRequestBody
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
    api_instance = env0_client.TeamsApi(api_client)
    team_api_deprecated_update_assignments_request_body = env0_client.TeamApiDeprecatedUpdateAssignmentsRequestBody() # TeamApiDeprecatedUpdateAssignmentsRequestBody |  (optional)

    try:
        # Update Teams Assignments
        api_response = api_instance.teams_deprecated_update_assignments(team_api_deprecated_update_assignments_request_body=team_api_deprecated_update_assignments_request_body)
        print("The response of TeamsApi->teams_deprecated_update_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_deprecated_update_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_api_deprecated_update_assignments_request_body** | [**TeamApiDeprecatedUpdateAssignmentsRequestBody**](TeamApiDeprecatedUpdateAssignmentsRequestBody.md)|  | [optional] 

### Return type

[**List[TeamApiDeprecatedTeamProjectAssignment]**](TeamApiDeprecatedTeamProjectAssignment.md)

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

# **teams_get_team**
> TeamApiTeam teams_get_team(team_id)

Get Team

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.team_api_team import TeamApiTeam
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
    api_instance = env0_client.TeamsApi(api_client)
    team_id = 'team_id_example' # str | 

    try:
        # Get Team
        api_response = api_instance.teams_get_team(team_id)
        print("The response of TeamsApi->teams_get_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_get_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**TeamApiTeam**](TeamApiTeam.md)

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

# **teams_get_teams**
> TeamApiGetTeamsResponse teams_get_teams(organization_id, limit=limit, offset=offset)

List Teams

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.team_api_get_teams_response import TeamApiGetTeamsResponse
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
    api_instance = env0_client.TeamsApi(api_client)
    organization_id = 'organization_id_example' # str | 
    limit = 'limit_example' # str | Number of teams per page. The maximum is 1000, the default is 50 (optional)
    offset = 'offset_example' # str | The nextPageKey returned in the previous request (optional)

    try:
        # List Teams
        api_response = api_instance.teams_get_teams(organization_id, limit=limit, offset=offset)
        print("The response of TeamsApi->teams_get_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_get_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **limit** | **str**| Number of teams per page. The maximum is 1000, the default is 50 | [optional] 
 **offset** | **str**| The nextPageKey returned in the previous request | [optional] 

### Return type

[**TeamApiGetTeamsResponse**](TeamApiGetTeamsResponse.md)

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

# **teams_update_team**
> TeamApiTeam teams_update_team(team_id, team_api_update_team_request_body=team_api_update_team_request_body)

Update Team

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.team_api_team import TeamApiTeam
from env0_client.models.team_api_update_team_request_body import TeamApiUpdateTeamRequestBody
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
    api_instance = env0_client.TeamsApi(api_client)
    team_id = 'team_id_example' # str | 
    team_api_update_team_request_body = env0_client.TeamApiUpdateTeamRequestBody() # TeamApiUpdateTeamRequestBody |  (optional)

    try:
        # Update Team
        api_response = api_instance.teams_update_team(team_id, team_api_update_team_request_body=team_api_update_team_request_body)
        print("The response of TeamsApi->teams_update_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_update_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **team_api_update_team_request_body** | [**TeamApiUpdateTeamRequestBody**](TeamApiUpdateTeamRequestBody.md)|  | [optional] 

### Return type

[**TeamApiTeam**](TeamApiTeam.md)

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

