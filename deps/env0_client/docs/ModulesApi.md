# env0_client.ModulesApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modules_get_module_test_run_by_id**](ModulesApi.md#modules_get_module_test_run_by_id) | **GET** /module/tests/{testRunId} | Get Module Test Run by ID
[**modules_get_module_test_runs**](ModulesApi.md#modules_get_module_test_runs) | **GET** /module/{moduleId}/tests | List Module Test Runs
[**modules_trigger_module_test_run**](ModulesApi.md#modules_trigger_module_test_run) | **POST** /module/{moduleId}/test | Trigger Module Test Run
[**templates_create_module**](ModulesApi.md#templates_create_module) | **POST** /modules | Create module
[**templates_delete_module_by_id**](ModulesApi.md#templates_delete_module_by_id) | **DELETE** /modules/{id} | Delete module
[**templates_find_all_modules**](ModulesApi.md#templates_find_all_modules) | **GET** /modules | List Modules
[**templates_get_module**](ModulesApi.md#templates_get_module) | **GET** /modules/{id} | Get module
[**templates_get_module_readme**](ModulesApi.md#templates_get_module_readme) | **GET** /modules/{id}/versions/{releaseId} | Get Module README
[**templates_get_module_versions**](ModulesApi.md#templates_get_module_versions) | **GET** /modules/{id}/versions | List Module Versions
[**templates_update_module**](ModulesApi.md#templates_update_module) | **PATCH** /modules/{id} | Update module


# **modules_get_module_test_run_by_id**
> ModuleTestingApiFullModuleTestRun modules_get_module_test_run_by_id(test_run_id)

Get Module Test Run by ID

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.module_testing_api_full_module_test_run import ModuleTestingApiFullModuleTestRun
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
    api_instance = env0_client.ModulesApi(api_client)
    test_run_id = 'test_run_id_example' # str | 

    try:
        # Get Module Test Run by ID
        api_response = api_instance.modules_get_module_test_run_by_id(test_run_id)
        print("The response of ModulesApi->modules_get_module_test_run_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModulesApi->modules_get_module_test_run_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_id** | **str**|  | 

### Return type

[**ModuleTestingApiFullModuleTestRun**](ModuleTestingApiFullModuleTestRun.md)

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

# **modules_get_module_test_runs**
> List[ModuleTestingApiFullModuleTestRun] modules_get_module_test_runs(module_id, limit=limit, offset=offset)

List Module Test Runs

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.module_testing_api_full_module_test_run import ModuleTestingApiFullModuleTestRun
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
    api_instance = env0_client.ModulesApi(api_client)
    module_id = 'module_id_example' # str | 
    limit = 'limit_example' # str | Number of test runs per page. The maximum is 100, with the default value is set to maximum (optional)
    offset = 'offset_example' # str | The offset of the first test returned. Defaults to 0 (optional)

    try:
        # List Module Test Runs
        api_response = api_instance.modules_get_module_test_runs(module_id, limit=limit, offset=offset)
        print("The response of ModulesApi->modules_get_module_test_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModulesApi->modules_get_module_test_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 
 **limit** | **str**| Number of test runs per page. The maximum is 100, with the default value is set to maximum | [optional] 
 **offset** | **str**| The offset of the first test returned. Defaults to 0 | [optional] 

### Return type

[**List[ModuleTestingApiFullModuleTestRun]**](ModuleTestingApiFullModuleTestRun.md)

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

# **modules_trigger_module_test_run**
> object modules_trigger_module_test_run(module_id, body=body)

Trigger Module Test Run

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
    api_instance = env0_client.ModulesApi(api_client)
    module_id = 'module_id_example' # str | 
    body = None # object |  (optional)

    try:
        # Trigger Module Test Run
        api_response = api_instance.modules_trigger_module_test_run(module_id, body=body)
        print("The response of ModulesApi->modules_trigger_module_test_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModulesApi->modules_trigger_module_test_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_id** | **str**|  | 
 **body** | **object**|  | [optional] 

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

# **templates_create_module**
> BlueprintApiExistingModule templates_create_module(blueprint_api_create_module_request_body=blueprint_api_create_module_request_body)

Create module

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_create_module_request_body import BlueprintApiCreateModuleRequestBody
from env0_client.models.blueprint_api_existing_module import BlueprintApiExistingModule
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
    api_instance = env0_client.ModulesApi(api_client)
    blueprint_api_create_module_request_body = env0_client.BlueprintApiCreateModuleRequestBody() # BlueprintApiCreateModuleRequestBody |  (optional)

    try:
        # Create module
        api_response = api_instance.templates_create_module(blueprint_api_create_module_request_body=blueprint_api_create_module_request_body)
        print("The response of ModulesApi->templates_create_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModulesApi->templates_create_module: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_api_create_module_request_body** | [**BlueprintApiCreateModuleRequestBody**](BlueprintApiCreateModuleRequestBody.md)|  | [optional] 

### Return type

[**BlueprintApiExistingModule**](BlueprintApiExistingModule.md)

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

# **templates_delete_module_by_id**
> templates_delete_module_by_id(id)

Delete module

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
    api_instance = env0_client.ModulesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete module
        api_instance.templates_delete_module_by_id(id)
    except Exception as e:
        print("Exception when calling ModulesApi->templates_delete_module_by_id: %s\n" % e)
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

# **templates_find_all_modules**
> List[BlueprintApiExistingModule] templates_find_all_modules(organization_id=organization_id)

List Modules

Returns all modules associated with an organization.

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_existing_module import BlueprintApiExistingModule
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
    api_instance = env0_client.ModulesApi(api_client)
    organization_id = 'organization_id_example' # str | An Organization ID to filter by (optional)

    try:
        # List Modules
        api_response = api_instance.templates_find_all_modules(organization_id=organization_id)
        print("The response of ModulesApi->templates_find_all_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModulesApi->templates_find_all_modules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| An Organization ID to filter by | [optional] 

### Return type

[**List[BlueprintApiExistingModule]**](BlueprintApiExistingModule.md)

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

# **templates_get_module**
> BlueprintApiModule templates_get_module(id)

Get module

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_module import BlueprintApiModule
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
    api_instance = env0_client.ModulesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get module
        api_response = api_instance.templates_get_module(id)
        print("The response of ModulesApi->templates_get_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModulesApi->templates_get_module: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BlueprintApiModule**](BlueprintApiModule.md)

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

# **templates_get_module_readme**
> str templates_get_module_readme(id, release_id)

Get Module README

Returns the Module README.md file content from a specific version

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
    api_instance = env0_client.ModulesApi(api_client)
    id = 'id_example' # str | The Module Id
    release_id = 'release_id_example' # str | The release based on the tag of the module

    try:
        # Get Module README
        api_response = api_instance.templates_get_module_readme(id, release_id)
        print("The response of ModulesApi->templates_get_module_readme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModulesApi->templates_get_module_readme: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Module Id | 
 **release_id** | **str**| The release based on the tag of the module | 

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

# **templates_get_module_versions**
> List[BlueprintApiGetModuleVersionsModuleVersionMetadata] templates_get_module_versions(id)

List Module Versions

Returns all versions of the module.

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_get_module_versions_module_version_metadata import BlueprintApiGetModuleVersionsModuleVersionMetadata
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
    api_instance = env0_client.ModulesApi(api_client)
    id = 'id_example' # str | The Module Id

    try:
        # List Module Versions
        api_response = api_instance.templates_get_module_versions(id)
        print("The response of ModulesApi->templates_get_module_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModulesApi->templates_get_module_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Module Id | 

### Return type

[**List[BlueprintApiGetModuleVersionsModuleVersionMetadata]**](BlueprintApiGetModuleVersionsModuleVersionMetadata.md)

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

# **templates_update_module**
> BlueprintApiExistingModule templates_update_module(id, blueprint_api_module_user_fields=blueprint_api_module_user_fields)

Update module

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_existing_module import BlueprintApiExistingModule
from env0_client.models.blueprint_api_module_user_fields import BlueprintApiModuleUserFields
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
    api_instance = env0_client.ModulesApi(api_client)
    id = 'id_example' # str | 
    blueprint_api_module_user_fields = env0_client.BlueprintApiModuleUserFields() # BlueprintApiModuleUserFields |  (optional)

    try:
        # Update module
        api_response = api_instance.templates_update_module(id, blueprint_api_module_user_fields=blueprint_api_module_user_fields)
        print("The response of ModulesApi->templates_update_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModulesApi->templates_update_module: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **blueprint_api_module_user_fields** | [**BlueprintApiModuleUserFields**](BlueprintApiModuleUserFields.md)|  | [optional] 

### Return type

[**BlueprintApiExistingModule**](BlueprintApiExistingModule.md)

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

