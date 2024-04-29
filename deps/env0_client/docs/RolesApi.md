# env0_client.RolesApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roles_create**](RolesApi.md#roles_create) | **POST** /roles | Create a Role
[**roles_delete**](RolesApi.md#roles_delete) | **DELETE** /roles/{id} | Delete a Role
[**roles_find_all**](RolesApi.md#roles_find_all) | **GET** /roles | Get All Roles
[**roles_find_by_id**](RolesApi.md#roles_find_by_id) | **GET** /roles/{id} | Get a Role
[**roles_get_team_role_assignments**](RolesApi.md#roles_get_team_role_assignments) | **GET** /roles/assignments/teams | Get Team Role Assignments
[**roles_get_user_role_assignments**](RolesApi.md#roles_get_user_role_assignments) | **GET** /roles/assignments/users | Get User Role Assignments
[**roles_remove_team_role_assignment**](RolesApi.md#roles_remove_team_role_assignment) | **DELETE** /roles/assignments/teams | Remove a Role Assignment for a Team
[**roles_remove_user_role_assignment**](RolesApi.md#roles_remove_user_role_assignment) | **DELETE** /roles/assignments/users | Remove a Role Assignment for a User
[**roles_update**](RolesApi.md#roles_update) | **PUT** /roles/{id} | Update a Role
[**roles_upsert_team_role_assignment**](RolesApi.md#roles_upsert_team_role_assignment) | **PUT** /roles/assignments/teams | Create or Update a Role Assignment for a Team
[**roles_upsert_user_role_assignment**](RolesApi.md#roles_upsert_user_role_assignment) | **PUT** /roles/assignments/users | Create or Update a Role Assignment for a User


# **roles_create**
> RolesApiRole roles_create(roles_api_create_request_body=roles_api_create_request_body)

Create a Role

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.roles_api_create_request_body import RolesApiCreateRequestBody
from env0_client.models.roles_api_role import RolesApiRole
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
    api_instance = env0_client.RolesApi(api_client)
    roles_api_create_request_body = env0_client.RolesApiCreateRequestBody() # RolesApiCreateRequestBody |  (optional)

    try:
        # Create a Role
        api_response = api_instance.roles_create(roles_api_create_request_body=roles_api_create_request_body)
        print("The response of RolesApi->roles_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->roles_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roles_api_create_request_body** | [**RolesApiCreateRequestBody**](RolesApiCreateRequestBody.md)|  | [optional] 

### Return type

[**RolesApiRole**](RolesApiRole.md)

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

# **roles_delete**
> roles_delete(id)

Delete a Role

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
    api_instance = env0_client.RolesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a Role
        api_instance.roles_delete(id)
    except Exception as e:
        print("Exception when calling RolesApi->roles_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **roles_find_all**
> List[RolesApiFindAllResponseInner] roles_find_all(organization_id)

Get All Roles

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.roles_api_find_all_response_inner import RolesApiFindAllResponseInner
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
    api_instance = env0_client.RolesApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Get All Roles
        api_response = api_instance.roles_find_all(organization_id)
        print("The response of RolesApi->roles_find_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->roles_find_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**List[RolesApiFindAllResponseInner]**](RolesApiFindAllResponseInner.md)

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

# **roles_find_by_id**
> RolesApiRole roles_find_by_id(id)

Get a Role

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.roles_api_role import RolesApiRole
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
    api_instance = env0_client.RolesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a Role
        api_response = api_instance.roles_find_by_id(id)
        print("The response of RolesApi->roles_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->roles_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RolesApiRole**](RolesApiRole.md)

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

# **roles_get_team_role_assignments**
> List[RolesApiTeamRoleAssignment] roles_get_team_role_assignments(organization_id=organization_id, project_id=project_id, environment_id=environment_id)

Get Team Role Assignments

Specifying `environmentId`, `projectId` or `organizationId` is required.

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.roles_api_team_role_assignment import RolesApiTeamRoleAssignment
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
    api_instance = env0_client.RolesApi(api_client)
    organization_id = 'organization_id_example' # str | ID of an organization to fetch its team role assignments (optional)
    project_id = 'project_id_example' # str | ID of a project to fetch its team role assignments (optional)
    environment_id = 'environment_id_example' # str | ID of an environment to fetch its team role assignments (optional)

    try:
        # Get Team Role Assignments
        api_response = api_instance.roles_get_team_role_assignments(organization_id=organization_id, project_id=project_id, environment_id=environment_id)
        print("The response of RolesApi->roles_get_team_role_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->roles_get_team_role_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| ID of an organization to fetch its team role assignments | [optional] 
 **project_id** | **str**| ID of a project to fetch its team role assignments | [optional] 
 **environment_id** | **str**| ID of an environment to fetch its team role assignments | [optional] 

### Return type

[**List[RolesApiTeamRoleAssignment]**](RolesApiTeamRoleAssignment.md)

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

# **roles_get_user_role_assignments**
> List[RolesApiUserRoleAssignment] roles_get_user_role_assignments(environment_id)

Get User Role Assignments

Currently supports environment scope assignments only.

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.roles_api_user_role_assignment import RolesApiUserRoleAssignment
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
    api_instance = env0_client.RolesApi(api_client)
    environment_id = 'environment_id_example' # str | ID of an environment to fetch its user role assignments

    try:
        # Get User Role Assignments
        api_response = api_instance.roles_get_user_role_assignments(environment_id)
        print("The response of RolesApi->roles_get_user_role_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->roles_get_user_role_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| ID of an environment to fetch its user role assignments | 

### Return type

[**List[RolesApiUserRoleAssignment]**](RolesApiUserRoleAssignment.md)

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

# **roles_remove_team_role_assignment**
> roles_remove_team_role_assignment(team_id, organization_id=organization_id, project_id=project_id, environment_id=environment_id)

Remove a Role Assignment for a Team

Specifying `environmentId`, `projectId` or `organizationId` is required.

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
    api_instance = env0_client.RolesApi(api_client)
    team_id = 'team_id_example' # str | 
    organization_id = 'organization_id_example' # str |  (optional)
    project_id = 'project_id_example' # str |  (optional)
    environment_id = 'environment_id_example' # str |  (optional)

    try:
        # Remove a Role Assignment for a Team
        api_instance.roles_remove_team_role_assignment(team_id, organization_id=organization_id, project_id=project_id, environment_id=environment_id)
    except Exception as e:
        print("Exception when calling RolesApi->roles_remove_team_role_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **organization_id** | **str**|  | [optional] 
 **project_id** | **str**|  | [optional] 
 **environment_id** | **str**|  | [optional] 

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

# **roles_remove_user_role_assignment**
> roles_remove_user_role_assignment(environment_id, user_id)

Remove a Role Assignment for a User

Currently supports environment scope assignments only.

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
    api_instance = env0_client.RolesApi(api_client)
    environment_id = 'environment_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Remove a Role Assignment for a User
        api_instance.roles_remove_user_role_assignment(environment_id, user_id)
    except Exception as e:
        print("Exception when calling RolesApi->roles_remove_user_role_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  | 
 **user_id** | **str**|  | 

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

# **roles_update**
> RolesApiRole roles_update(id, roles_api_update_request_body=roles_api_update_request_body)

Update a Role

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.roles_api_role import RolesApiRole
from env0_client.models.roles_api_update_request_body import RolesApiUpdateRequestBody
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
    api_instance = env0_client.RolesApi(api_client)
    id = 'id_example' # str | 
    roles_api_update_request_body = env0_client.RolesApiUpdateRequestBody() # RolesApiUpdateRequestBody |  (optional)

    try:
        # Update a Role
        api_response = api_instance.roles_update(id, roles_api_update_request_body=roles_api_update_request_body)
        print("The response of RolesApi->roles_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->roles_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **roles_api_update_request_body** | [**RolesApiUpdateRequestBody**](RolesApiUpdateRequestBody.md)|  | [optional] 

### Return type

[**RolesApiRole**](RolesApiRole.md)

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

# **roles_upsert_team_role_assignment**
> RolesApiTeamRoleAssignment roles_upsert_team_role_assignment(roles_api_upsert_team_role_assignment_request_body=roles_api_upsert_team_role_assignment_request_body)

Create or Update a Role Assignment for a Team

Currently supports organization or environment scope assignments only. Specifying `environmentId` or `organizationId` is required.

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.roles_api_team_role_assignment import RolesApiTeamRoleAssignment
from env0_client.models.roles_api_upsert_team_role_assignment_request_body import RolesApiUpsertTeamRoleAssignmentRequestBody
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
    api_instance = env0_client.RolesApi(api_client)
    roles_api_upsert_team_role_assignment_request_body = env0_client.RolesApiUpsertTeamRoleAssignmentRequestBody() # RolesApiUpsertTeamRoleAssignmentRequestBody |  (optional)

    try:
        # Create or Update a Role Assignment for a Team
        api_response = api_instance.roles_upsert_team_role_assignment(roles_api_upsert_team_role_assignment_request_body=roles_api_upsert_team_role_assignment_request_body)
        print("The response of RolesApi->roles_upsert_team_role_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->roles_upsert_team_role_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roles_api_upsert_team_role_assignment_request_body** | [**RolesApiUpsertTeamRoleAssignmentRequestBody**](RolesApiUpsertTeamRoleAssignmentRequestBody.md)|  | [optional] 

### Return type

[**RolesApiTeamRoleAssignment**](RolesApiTeamRoleAssignment.md)

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

# **roles_upsert_user_role_assignment**
> RolesApiUserRoleAssignment roles_upsert_user_role_assignment(roles_api_upsert_user_role_assignment_request_body=roles_api_upsert_user_role_assignment_request_body)

Create or Update a Role Assignment for a User

Currently supports environment scope assignments only.

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.roles_api_upsert_user_role_assignment_request_body import RolesApiUpsertUserRoleAssignmentRequestBody
from env0_client.models.roles_api_user_role_assignment import RolesApiUserRoleAssignment
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
    api_instance = env0_client.RolesApi(api_client)
    roles_api_upsert_user_role_assignment_request_body = env0_client.RolesApiUpsertUserRoleAssignmentRequestBody() # RolesApiUpsertUserRoleAssignmentRequestBody |  (optional)

    try:
        # Create or Update a Role Assignment for a User
        api_response = api_instance.roles_upsert_user_role_assignment(roles_api_upsert_user_role_assignment_request_body=roles_api_upsert_user_role_assignment_request_body)
        print("The response of RolesApi->roles_upsert_user_role_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->roles_upsert_user_role_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roles_api_upsert_user_role_assignment_request_body** | [**RolesApiUpsertUserRoleAssignmentRequestBody**](RolesApiUpsertUserRoleAssignmentRequestBody.md)|  | [optional] 

### Return type

[**RolesApiUserRoleAssignment**](RolesApiUserRoleAssignment.md)

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

