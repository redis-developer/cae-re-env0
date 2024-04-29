# env0_client.TemplatesApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**templates_add_blueprint_to_project**](TemplatesApi.md#templates_add_blueprint_to_project) | **PATCH** /blueprints/{id}/projects | Add Template to Project
[**templates_create_blueprint**](TemplatesApi.md#templates_create_blueprint) | **POST** /blueprints | Create Template
[**templates_delete_environment_discovery**](TemplatesApi.md#templates_delete_environment_discovery) | **DELETE** /environment-discovery/projects/{projectId} | Delete Environment Discovery Configuration for a Project
[**templates_enable_environment_discovery**](TemplatesApi.md#templates_enable_environment_discovery) | **PUT** /environment-discovery/projects/{projectId} | Enable/Update Environment Discovery Configuration
[**templates_find_all**](TemplatesApi.md#templates_find_all) | **GET** /blueprints | List Templates
[**templates_get_blueprint_by_id**](TemplatesApi.md#templates_get_blueprint_by_id) | **GET** /blueprints/{id} | Get Template by ID
[**templates_get_environment_discovery**](TemplatesApi.md#templates_get_environment_discovery) | **GET** /environment-discovery/projects/{projectId} | Get Environment Discovery Configuration for a Project
[**templates_get_variables_from_repository**](TemplatesApi.md#templates_get_variables_from_repository) | **GET** /blueprints/variables-from-repository | Generate Terraform Variables from Repository
[**templates_get_vcs_repository_revisions**](TemplatesApi.md#templates_get_vcs_repository_revisions) | **GET** /blueprints/vcs-revisions | List git repository revisions
[**templates_get_workflow_file**](TemplatesApi.md#templates_get_workflow_file) | **GET** /workflowFile | Get workflow file representation
[**templates_module_registry_download_source**](TemplatesApi.md#templates_module_registry_download_source) | **GET** /modules/v1/{organizationId}/{moduleName}/{providerName}/{version}/download | Download Terraform module
[**templates_remove_blueprint_by_id**](TemplatesApi.md#templates_remove_blueprint_by_id) | **DELETE** /blueprints/{id} | Delete Template
[**templates_remove_blueprint_from_project**](TemplatesApi.md#templates_remove_blueprint_from_project) | **DELETE** /blueprints/{id}/projects/{projectId} | Remove Template from Project
[**templates_update_blueprint**](TemplatesApi.md#templates_update_blueprint) | **PUT** /blueprints/{id} | Update Template


# **templates_add_blueprint_to_project**
> BlueprintApiBlueprint templates_add_blueprint_to_project(id, blueprint_api_add_blueprint_to_project_request_body=blueprint_api_add_blueprint_to_project_request_body)

Add Template to Project

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_add_blueprint_to_project_request_body import BlueprintApiAddBlueprintToProjectRequestBody
from env0_client.models.blueprint_api_blueprint import BlueprintApiBlueprint
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
    api_instance = env0_client.TemplatesApi(api_client)
    id = 'id_example' # str | 
    blueprint_api_add_blueprint_to_project_request_body = env0_client.BlueprintApiAddBlueprintToProjectRequestBody() # BlueprintApiAddBlueprintToProjectRequestBody |  (optional)

    try:
        # Add Template to Project
        api_response = api_instance.templates_add_blueprint_to_project(id, blueprint_api_add_blueprint_to_project_request_body=blueprint_api_add_blueprint_to_project_request_body)
        print("The response of TemplatesApi->templates_add_blueprint_to_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_add_blueprint_to_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **blueprint_api_add_blueprint_to_project_request_body** | [**BlueprintApiAddBlueprintToProjectRequestBody**](BlueprintApiAddBlueprintToProjectRequestBody.md)|  | [optional] 

### Return type

[**BlueprintApiBlueprint**](BlueprintApiBlueprint.md)

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

# **templates_create_blueprint**
> BlueprintApiBlueprint templates_create_blueprint(blueprint_api_create_blueprint_request_body=blueprint_api_create_blueprint_request_body)

Create Template

Please note, you can only have 1 ssh key per template

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_blueprint import BlueprintApiBlueprint
from env0_client.models.blueprint_api_create_blueprint_request_body import BlueprintApiCreateBlueprintRequestBody
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
    api_instance = env0_client.TemplatesApi(api_client)
    blueprint_api_create_blueprint_request_body = env0_client.BlueprintApiCreateBlueprintRequestBody() # BlueprintApiCreateBlueprintRequestBody |  (optional)

    try:
        # Create Template
        api_response = api_instance.templates_create_blueprint(blueprint_api_create_blueprint_request_body=blueprint_api_create_blueprint_request_body)
        print("The response of TemplatesApi->templates_create_blueprint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_create_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_api_create_blueprint_request_body** | [**BlueprintApiCreateBlueprintRequestBody**](BlueprintApiCreateBlueprintRequestBody.md)|  | [optional] 

### Return type

[**BlueprintApiBlueprint**](BlueprintApiBlueprint.md)

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

# **templates_delete_environment_discovery**
> templates_delete_environment_discovery(project_id)

Delete Environment Discovery Configuration for a Project

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
    api_instance = env0_client.TemplatesApi(api_client)
    project_id = 'project_id_example' # str | The Project ID to delete environment discovery configuration for

    try:
        # Delete Environment Discovery Configuration for a Project
        api_instance.templates_delete_environment_discovery(project_id)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_delete_environment_discovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The Project ID to delete environment discovery configuration for | 

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

# **templates_enable_environment_discovery**
> BlueprintApiEnvironmentDiscoveryResponse templates_enable_environment_discovery(project_id, blueprint_api_environment_discovery=blueprint_api_environment_discovery)

Enable/Update Environment Discovery Configuration

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_environment_discovery import BlueprintApiEnvironmentDiscovery
from env0_client.models.blueprint_api_environment_discovery_response import BlueprintApiEnvironmentDiscoveryResponse
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
    api_instance = env0_client.TemplatesApi(api_client)
    project_id = 'project_id_example' # str | The Project ID to enable environment discovery for
    blueprint_api_environment_discovery = env0_client.BlueprintApiEnvironmentDiscovery() # BlueprintApiEnvironmentDiscovery |  (optional)

    try:
        # Enable/Update Environment Discovery Configuration
        api_response = api_instance.templates_enable_environment_discovery(project_id, blueprint_api_environment_discovery=blueprint_api_environment_discovery)
        print("The response of TemplatesApi->templates_enable_environment_discovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_enable_environment_discovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The Project ID to enable environment discovery for | 
 **blueprint_api_environment_discovery** | [**BlueprintApiEnvironmentDiscovery**](BlueprintApiEnvironmentDiscovery.md)|  | [optional] 

### Return type

[**BlueprintApiEnvironmentDiscoveryResponse**](BlueprintApiEnvironmentDiscoveryResponse.md)

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

# **templates_find_all**
> List[BlueprintApiBlueprint] templates_find_all(organization_id=organization_id, project_id=project_id)

List Templates

Returns all Templates associated with either an Organization or Project. At least one of these must be set.

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_blueprint import BlueprintApiBlueprint
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
    api_instance = env0_client.TemplatesApi(api_client)
    organization_id = 'organization_id_example' # str | An Organization ID to filter by (optional)
    project_id = 'project_id_example' # str | A Project ID to filter by (optional)

    try:
        # List Templates
        api_response = api_instance.templates_find_all(organization_id=organization_id, project_id=project_id)
        print("The response of TemplatesApi->templates_find_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_find_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| An Organization ID to filter by | [optional] 
 **project_id** | **str**| A Project ID to filter by | [optional] 

### Return type

[**List[BlueprintApiBlueprint]**](BlueprintApiBlueprint.md)

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

# **templates_get_blueprint_by_id**
> BlueprintApiBlueprint templates_get_blueprint_by_id(id)

Get Template by ID

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_blueprint import BlueprintApiBlueprint
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
    api_instance = env0_client.TemplatesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Template by ID
        api_response = api_instance.templates_get_blueprint_by_id(id)
        print("The response of TemplatesApi->templates_get_blueprint_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_get_blueprint_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BlueprintApiBlueprint**](BlueprintApiBlueprint.md)

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

# **templates_get_environment_discovery**
> BlueprintApiEnvironmentDiscoveryResponse templates_get_environment_discovery(project_id)

Get Environment Discovery Configuration for a Project

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_environment_discovery_response import BlueprintApiEnvironmentDiscoveryResponse
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
    api_instance = env0_client.TemplatesApi(api_client)
    project_id = 'project_id_example' # str | The Project ID to fetch environment discovery configuration for

    try:
        # Get Environment Discovery Configuration for a Project
        api_response = api_instance.templates_get_environment_discovery(project_id)
        print("The response of TemplatesApi->templates_get_environment_discovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_get_environment_discovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The Project ID to fetch environment discovery configuration for | 

### Return type

[**BlueprintApiEnvironmentDiscoveryResponse**](BlueprintApiEnvironmentDiscoveryResponse.md)

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

# **templates_get_variables_from_repository**
> List[BlueprintApiGetVariablesFromRepositoryRepositoryVariable] templates_get_variables_from_repository(repository, revision=revision, path=path, token_id=token_id, ssh_key_ids=ssh_key_ids, github_installation_id=github_installation_id, bitbucket_client_key=bitbucket_client_key)

Generate Terraform Variables from Repository

Clones and searches through a Template git repository for any Terraform variable blocks and returns a set of env0 Terraform Configuration Variables that may be added to env0 via the Configuration API

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_get_variables_from_repository_repository_variable import BlueprintApiGetVariablesFromRepositoryRepositoryVariable
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
    api_instance = env0_client.TemplatesApi(api_client)
    repository = 'repository_example' # str | 
    revision = 'revision_example' # str |  (optional)
    path = 'path_example' # str |  (optional)
    token_id = 'token_id_example' # str |  (optional)
    ssh_key_ids = 'ssh_key_ids_example' # str |  (optional)
    github_installation_id = 'github_installation_id_example' # str |  (optional)
    bitbucket_client_key = 'bitbucket_client_key_example' # str |  (optional)

    try:
        # Generate Terraform Variables from Repository
        api_response = api_instance.templates_get_variables_from_repository(repository, revision=revision, path=path, token_id=token_id, ssh_key_ids=ssh_key_ids, github_installation_id=github_installation_id, bitbucket_client_key=bitbucket_client_key)
        print("The response of TemplatesApi->templates_get_variables_from_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_get_variables_from_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**|  | 
 **revision** | **str**|  | [optional] 
 **path** | **str**|  | [optional] 
 **token_id** | **str**|  | [optional] 
 **ssh_key_ids** | **str**|  | [optional] 
 **github_installation_id** | **str**|  | [optional] 
 **bitbucket_client_key** | **str**|  | [optional] 

### Return type

[**List[BlueprintApiGetVariablesFromRepositoryRepositoryVariable]**](BlueprintApiGetVariablesFromRepositoryRepositoryVariable.md)

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

# **templates_get_vcs_repository_revisions**
> RevisionsNamesResponse templates_get_vcs_repository_revisions(repository, token_id=token_id, ssh_key_ids=ssh_key_ids, github_installation_id=github_installation_id, bitbucket_client_key=bitbucket_client_key)

List git repository revisions

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.revisions_names_response import RevisionsNamesResponse
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
    api_instance = env0_client.TemplatesApi(api_client)
    repository = 'repository_example' # str | 
    token_id = 'token_id_example' # str |  (optional)
    ssh_key_ids = 'ssh_key_ids_example' # str |  (optional)
    github_installation_id = 'github_installation_id_example' # str |  (optional)
    bitbucket_client_key = 'bitbucket_client_key_example' # str |  (optional)

    try:
        # List git repository revisions
        api_response = api_instance.templates_get_vcs_repository_revisions(repository, token_id=token_id, ssh_key_ids=ssh_key_ids, github_installation_id=github_installation_id, bitbucket_client_key=bitbucket_client_key)
        print("The response of TemplatesApi->templates_get_vcs_repository_revisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_get_vcs_repository_revisions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**|  | 
 **token_id** | **str**|  | [optional] 
 **ssh_key_ids** | **str**|  | [optional] 
 **github_installation_id** | **str**|  | [optional] 
 **bitbucket_client_key** | **str**|  | [optional] 

### Return type

[**RevisionsNamesResponse**](RevisionsNamesResponse.md)

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

# **templates_get_workflow_file**
> WorkflowFile templates_get_workflow_file(blueprint_id, revision=revision)

Get workflow file representation

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.workflow_file import WorkflowFile
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
    api_instance = env0_client.TemplatesApi(api_client)
    blueprint_id = 'blueprint_id_example' # str | 
    revision = 'revision_example' # str |  (optional)

    try:
        # Get workflow file representation
        api_response = api_instance.templates_get_workflow_file(blueprint_id, revision=revision)
        print("The response of TemplatesApi->templates_get_workflow_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_get_workflow_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_id** | **str**|  | 
 **revision** | **str**|  | [optional] 

### Return type

[**WorkflowFile**](WorkflowFile.md)

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

# **templates_module_registry_download_source**
> object templates_module_registry_download_source(organization_id, module_name, provider_name, version)

Download Terraform module

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
    api_instance = env0_client.TemplatesApi(api_client)
    organization_id = 'organization_id_example' # str | 
    module_name = 'module_name_example' # str | 
    provider_name = 'provider_name_example' # str | 
    version = 'version_example' # str | 

    try:
        # Download Terraform module
        api_response = api_instance.templates_module_registry_download_source(organization_id, module_name, provider_name, version)
        print("The response of TemplatesApi->templates_module_registry_download_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_module_registry_download_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **module_name** | **str**|  | 
 **provider_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

**object**

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

# **templates_remove_blueprint_by_id**
> templates_remove_blueprint_by_id(id)

Delete Template

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
    api_instance = env0_client.TemplatesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Template
        api_instance.templates_remove_blueprint_by_id(id)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_remove_blueprint_by_id: %s\n" % e)
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

# **templates_remove_blueprint_from_project**
> templates_remove_blueprint_from_project(id, project_id)

Remove Template from Project

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
    api_instance = env0_client.TemplatesApi(api_client)
    id = 'id_example' # str | 
    project_id = 'project_id_example' # str | 

    try:
        # Remove Template from Project
        api_instance.templates_remove_blueprint_from_project(id, project_id)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_remove_blueprint_from_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **project_id** | **str**|  | 

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

# **templates_update_blueprint**
> BlueprintApiBlueprint templates_update_blueprint(id, blueprint_api_blueprint_user_fields=blueprint_api_blueprint_user_fields)

Update Template

Please note, you can only have 1 ssh key per template

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_blueprint import BlueprintApiBlueprint
from env0_client.models.blueprint_api_blueprint_user_fields import BlueprintApiBlueprintUserFields
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
    api_instance = env0_client.TemplatesApi(api_client)
    id = 'id_example' # str | 
    blueprint_api_blueprint_user_fields = env0_client.BlueprintApiBlueprintUserFields() # BlueprintApiBlueprintUserFields |  (optional)

    try:
        # Update Template
        api_response = api_instance.templates_update_blueprint(id, blueprint_api_blueprint_user_fields=blueprint_api_blueprint_user_fields)
        print("The response of TemplatesApi->templates_update_blueprint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_update_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **blueprint_api_blueprint_user_fields** | [**BlueprintApiBlueprintUserFields**](BlueprintApiBlueprintUserFields.md)|  | [optional] 

### Return type

[**BlueprintApiBlueprint**](BlueprintApiBlueprint.md)

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

