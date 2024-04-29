# env0_client.ProjectsApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**environments_get_policies**](ProjectsApi.md#environments_get_policies) | **GET** /policies | Get Policy
[**environments_update_policies**](ProjectsApi.md#environments_update_policies) | **PUT** /policies | Update Policy
[**projects_archive**](ProjectsApi.md#projects_archive) | **DELETE** /projects/{id} | Archive a Project
[**projects_create_project**](ProjectsApi.md#projects_create_project) | **POST** /projects | Create a new Project
[**projects_find_by_id**](ProjectsApi.md#projects_find_by_id) | **GET** /projects/{id} | Get a Project By ID
[**projects_find_by_organization_id**](ProjectsApi.md#projects_find_by_organization_id) | **GET** /projects | List Projects
[**projects_get_modules_testing_project**](ProjectsApi.md#projects_get_modules_testing_project) | **GET** /projects/modules/testing/{organizationId} | Get Modules Testing Project for Organization
[**projects_move_project**](ProjectsApi.md#projects_move_project) | **POST** /projects/{id}/move | Move a project to be a sub-project of another project
[**projects_update**](ProjectsApi.md#projects_update) | **PUT** /projects/{id} | Update a Project


# **environments_get_policies**
> EnvironmentApiPolicy environments_get_policies(project_id)

Get Policy

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_policy import EnvironmentApiPolicy
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
    api_instance = env0_client.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Get Policy
        api_response = api_instance.environments_get_policies(project_id)
        print("The response of ProjectsApi->environments_get_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->environments_get_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**EnvironmentApiPolicy**](EnvironmentApiPolicy.md)

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

# **environments_update_policies**
> EnvironmentApiPolicy environments_update_policies(environment_api_update_policies_request_body=environment_api_update_policies_request_body)

Update Policy

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_policy import EnvironmentApiPolicy
from env0_client.models.environment_api_update_policies_request_body import EnvironmentApiUpdatePoliciesRequestBody
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
    api_instance = env0_client.ProjectsApi(api_client)
    environment_api_update_policies_request_body = env0_client.EnvironmentApiUpdatePoliciesRequestBody() # EnvironmentApiUpdatePoliciesRequestBody |  (optional)

    try:
        # Update Policy
        api_response = api_instance.environments_update_policies(environment_api_update_policies_request_body=environment_api_update_policies_request_body)
        print("The response of ProjectsApi->environments_update_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->environments_update_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_api_update_policies_request_body** | [**EnvironmentApiUpdatePoliciesRequestBody**](EnvironmentApiUpdatePoliciesRequestBody.md)|  | [optional] 

### Return type

[**EnvironmentApiPolicy**](EnvironmentApiPolicy.md)

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

# **projects_archive**
> projects_archive(id)

Archive a Project

This can not be undone. Running Environments will NOT be destroyed and continuous and scheduled Deployments will NOT continue to occur.

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
    api_instance = env0_client.ProjectsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive a Project
        api_instance.projects_archive(id)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_archive: %s\n" % e)
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

# **projects_create_project**
> ProjectApiProject projects_create_project(project_api_create_project_request=project_api_create_project_request)

Create a new Project

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.project_api_create_project_request import ProjectApiCreateProjectRequest
from env0_client.models.project_api_project import ProjectApiProject
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
    api_instance = env0_client.ProjectsApi(api_client)
    project_api_create_project_request = env0_client.ProjectApiCreateProjectRequest() # ProjectApiCreateProjectRequest |  (optional)

    try:
        # Create a new Project
        api_response = api_instance.projects_create_project(project_api_create_project_request=project_api_create_project_request)
        print("The response of ProjectsApi->projects_create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_api_create_project_request** | [**ProjectApiCreateProjectRequest**](ProjectApiCreateProjectRequest.md)|  | [optional] 

### Return type

[**ProjectApiProject**](ProjectApiProject.md)

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

# **projects_find_by_id**
> ProjectApiProject projects_find_by_id(id)

Get a Project By ID

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.project_api_project import ProjectApiProject
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
    api_instance = env0_client.ProjectsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a Project By ID
        api_response = api_instance.projects_find_by_id(id)
        print("The response of ProjectsApi->projects_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProjectApiProject**](ProjectApiProject.md)

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

# **projects_find_by_organization_id**
> List[ProjectApiProject] projects_find_by_organization_id(organization_id)

List Projects

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.project_api_project import ProjectApiProject
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
    api_instance = env0_client.ProjectsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # List Projects
        api_response = api_instance.projects_find_by_organization_id(organization_id)
        print("The response of ProjectsApi->projects_find_by_organization_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_find_by_organization_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**List[ProjectApiProject]**](ProjectApiProject.md)

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

# **projects_get_modules_testing_project**
> ProjectApiProject projects_get_modules_testing_project(organization_id)

Get Modules Testing Project for Organization

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.project_api_project import ProjectApiProject
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
    api_instance = env0_client.ProjectsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Get Modules Testing Project for Organization
        api_response = api_instance.projects_get_modules_testing_project(organization_id)
        print("The response of ProjectsApi->projects_get_modules_testing_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_get_modules_testing_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**ProjectApiProject**](ProjectApiProject.md)

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

# **projects_move_project**
> object projects_move_project(id, project_api_move_project_request_body=project_api_move_project_request_body)

Move a project to be a sub-project of another project

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.project_api_move_project_request_body import ProjectApiMoveProjectRequestBody
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
    api_instance = env0_client.ProjectsApi(api_client)
    id = 'id_example' # str | 
    project_api_move_project_request_body = env0_client.ProjectApiMoveProjectRequestBody() # ProjectApiMoveProjectRequestBody |  (optional)

    try:
        # Move a project to be a sub-project of another project
        api_response = api_instance.projects_move_project(id, project_api_move_project_request_body=project_api_move_project_request_body)
        print("The response of ProjectsApi->projects_move_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_move_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **project_api_move_project_request_body** | [**ProjectApiMoveProjectRequestBody**](ProjectApiMoveProjectRequestBody.md)|  | [optional] 

### Return type

**object**

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

# **projects_update**
> ProjectApiProject projects_update(id, project_api_update_project_request=project_api_update_project_request)

Update a Project

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.project_api_project import ProjectApiProject
from env0_client.models.project_api_update_project_request import ProjectApiUpdateProjectRequest
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
    api_instance = env0_client.ProjectsApi(api_client)
    id = 'id_example' # str | 
    project_api_update_project_request = env0_client.ProjectApiUpdateProjectRequest() # ProjectApiUpdateProjectRequest |  (optional)

    try:
        # Update a Project
        api_response = api_instance.projects_update(id, project_api_update_project_request=project_api_update_project_request)
        print("The response of ProjectsApi->projects_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **project_api_update_project_request** | [**ProjectApiUpdateProjectRequest**](ProjectApiUpdateProjectRequest.md)|  | [optional] 

### Return type

[**ProjectApiProject**](ProjectApiProject.md)

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

