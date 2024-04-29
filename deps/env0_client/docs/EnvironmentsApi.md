# env0_client.EnvironmentsApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**environments_abort**](EnvironmentsApi.md#environments_abort) | **POST** /environments/deployments/{id}/abort | Abort Deployment
[**environments_batch_cancel**](EnvironmentsApi.md#environments_batch_cancel) | **PUT** /environments/{id}/deployments/cancel | Batch Cancel Deployments
[**environments_cancel**](EnvironmentsApi.md#environments_cancel) | **PUT** /environments/deployments/{id}/cancel | Cancel Deployment
[**environments_check_limit**](EnvironmentsApi.md#environments_check_limit) | **GET** /policies/limits/check | Check Environment meets Project limits
[**environments_count_by_project**](EnvironmentsApi.md#environments_count_by_project) | **GET** /environments/count | Count Environments
[**environments_create**](EnvironmentsApi.md#environments_create) | **POST** /environments | Create Environment
[**environments_create_environment_without_template**](EnvironmentsApi.md#environments_create_environment_without_template) | **POST** /environments/without-template | Create an Environment Without Template
[**environments_deploy**](EnvironmentsApi.md#environments_deploy) | **POST** /environments/{id}/deployments | Deploy Environment
[**environments_destroy**](EnvironmentsApi.md#environments_destroy) | **POST** /environments/{id}/destroy | Destroy Environment
[**environments_find_all**](EnvironmentsApi.md#environments_find_all) | **GET** /environments | List Environments
[**environments_find_by_id**](EnvironmentsApi.md#environments_find_by_id) | **GET** /environments/{id} | Get Environment
[**environments_find_deployment_log_by_id**](EnvironmentsApi.md#environments_find_deployment_log_by_id) | **GET** /environments/deployments/{id} | Get Deployment
[**environments_find_deployment_logs_by_environment_id**](EnvironmentsApi.md#environments_find_deployment_logs_by_environment_id) | **GET** /environments/{id}/deployments | List Deployments
[**environments_find_downstream_environments**](EnvironmentsApi.md#environments_find_downstream_environments) | **GET** /environments/{id}/downstream | Get downstream environments that will be triggered by this environment deployment
[**environments_find_resources**](EnvironmentsApi.md#environments_find_resources) | **GET** /environments/deployments/{id}/resources | List Resources
[**environments_find_sub_deployment_log**](EnvironmentsApi.md#environments_find_sub_deployment_log) | **GET** /workflow-deployments/{workflowDeploymentId}/sub-environments/{subEnvironmentId}/deployment | Get Sub Deployment Log In A Workflow By Workflow Deployment Id And Environment Id
[**environments_get_environments_outputs**](EnvironmentsApi.md#environments_get_environments_outputs) | **GET** /environment-outputs | Get Environments Outputs
[**environments_get_projects_envs_statuses_counts_by_org**](EnvironmentsApi.md#environments_get_projects_envs_statuses_counts_by_org) | **GET** /environments/statuses/counts | Counts all selected statuses of organization projects
[**environments_rerun_deployment**](EnvironmentsApi.md#environments_rerun_deployment) | **POST** /environments/deployments/{id}/rerun | Rerun PR plan
[**environments_resume**](EnvironmentsApi.md#environments_resume) | **PUT** /environments/deployments/{id} | Resume Deployment
[**environments_save_as_template**](EnvironmentsApi.md#environments_save_as_template) | **PUT** /environments/{id}/template | Save VCS environment as a template
[**environments_subscribe_downstream_environments**](EnvironmentsApi.md#environments_subscribe_downstream_environments) | **POST** /environments/{id}/downstream/subscribe | Subscribe environments as workflow-trigger
[**environments_ttl**](EnvironmentsApi.md#environments_ttl) | **PUT** /environments/{id}/ttl | Update Environment TTL
[**environments_unsubscribe_downstream_environments**](EnvironmentsApi.md#environments_unsubscribe_downstream_environments) | **POST** /environments/{id}/downstream/unsubscribe | Unsubscribe environments as workflow-trigger
[**environments_update**](EnvironmentsApi.md#environments_update) | **PUT** /environments/{id} | Update Environment
[**environments_update_downstream_environments**](EnvironmentsApi.md#environments_update_downstream_environments) | **PUT** /environments/{id}/downstream | Create or Update Workflow Trigger
[**environments_update_environment_lock**](EnvironmentsApi.md#environments_update_environment_lock) | **PUT** /environments/{id}/lock | Lock/Unlock environment


# **environments_abort**
> object environments_abort(id, body=body)

Abort Deployment

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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    body = None # object |  (optional)

    try:
        # Abort Deployment
        api_response = api_instance.environments_abort(id, body=body)
        print("The response of EnvironmentsApi->environments_abort:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_abort: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **environments_batch_cancel**
> EnvironmentApiBatchCancelResponse environments_batch_cancel(id, status, body=body)

Batch Cancel Deployments

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_batch_cancel_response import EnvironmentApiBatchCancelResponse
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    status = 'status_example' # str | Cancel deployments with this status
    body = None # object |  (optional)

    try:
        # Batch Cancel Deployments
        api_response = api_instance.environments_batch_cancel(id, status, body=body)
        print("The response of EnvironmentsApi->environments_batch_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_batch_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **status** | **str**| Cancel deployments with this status | 
 **body** | **object**|  | [optional] 

### Return type

[**EnvironmentApiBatchCancelResponse**](EnvironmentApiBatchCancelResponse.md)

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

# **environments_cancel**
> EnvironmentApiCancelResponse environments_cancel(id, body=body)

Cancel Deployment

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_cancel_response import EnvironmentApiCancelResponse
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    body = None # object |  (optional)

    try:
        # Cancel Deployment
        api_response = api_instance.environments_cancel(id, body=body)
        print("The response of EnvironmentsApi->environments_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | [optional] 

### Return type

[**EnvironmentApiCancelResponse**](EnvironmentApiCancelResponse.md)

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

# **environments_check_limit**
> EnvironmentApiCheckLimitResponse environments_check_limit(project_id)

Check Environment meets Project limits

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_check_limit_response import EnvironmentApiCheckLimitResponse
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Check Environment meets Project limits
        api_response = api_instance.environments_check_limit(project_id)
        print("The response of EnvironmentsApi->environments_check_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_check_limit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**EnvironmentApiCheckLimitResponse**](EnvironmentApiCheckLimitResponse.md)

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

# **environments_count_by_project**
> float environments_count_by_project(project_id, is_active=is_active, status=status)

Count Environments

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
    api_instance = env0_client.EnvironmentsApi(api_client)
    project_id = 'project_id_example' # str | 
    is_active = 'is_active_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        # Count Environments
        api_response = api_instance.environments_count_by_project(project_id, is_active=is_active, status=status)
        print("The response of EnvironmentsApi->environments_count_by_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_count_by_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **is_active** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

**float**

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

# **environments_create**
> EnvironmentApiEnvironment environments_create(environment_api_create_environment_request=environment_api_create_environment_request)

Create Environment

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_create_environment_request import EnvironmentApiCreateEnvironmentRequest
from env0_client.models.environment_api_environment import EnvironmentApiEnvironment
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    environment_api_create_environment_request = env0_client.EnvironmentApiCreateEnvironmentRequest() # EnvironmentApiCreateEnvironmentRequest |  (optional)

    try:
        # Create Environment
        api_response = api_instance.environments_create(environment_api_create_environment_request=environment_api_create_environment_request)
        print("The response of EnvironmentsApi->environments_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_api_create_environment_request** | [**EnvironmentApiCreateEnvironmentRequest**](EnvironmentApiCreateEnvironmentRequest.md)|  | [optional] 

### Return type

[**EnvironmentApiEnvironment**](EnvironmentApiEnvironment.md)

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

# **environments_create_environment_without_template**
> EnvironmentApiCreateEnvironmentWithoutTemplateResponse environments_create_environment_without_template(environment_api_create_environment_without_template_request_body=environment_api_create_environment_without_template_request_body)

Create an Environment Without Template

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_create_environment_without_template_request_body import EnvironmentApiCreateEnvironmentWithoutTemplateRequestBody
from env0_client.models.environment_api_create_environment_without_template_response import EnvironmentApiCreateEnvironmentWithoutTemplateResponse
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    environment_api_create_environment_without_template_request_body = env0_client.EnvironmentApiCreateEnvironmentWithoutTemplateRequestBody() # EnvironmentApiCreateEnvironmentWithoutTemplateRequestBody |  (optional)

    try:
        # Create an Environment Without Template
        api_response = api_instance.environments_create_environment_without_template(environment_api_create_environment_without_template_request_body=environment_api_create_environment_without_template_request_body)
        print("The response of EnvironmentsApi->environments_create_environment_without_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_create_environment_without_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_api_create_environment_without_template_request_body** | [**EnvironmentApiCreateEnvironmentWithoutTemplateRequestBody**](EnvironmentApiCreateEnvironmentWithoutTemplateRequestBody.md)|  | [optional] 

### Return type

[**EnvironmentApiCreateEnvironmentWithoutTemplateResponse**](EnvironmentApiCreateEnvironmentWithoutTemplateResponse.md)

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

# **environments_deploy**
> DeployResult environments_deploy(id, deploy_request=deploy_request)

Deploy Environment

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.deploy_request import DeployRequest
from env0_client.models.deploy_result import DeployResult
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    deploy_request = env0_client.DeployRequest() # DeployRequest |  (optional)

    try:
        # Deploy Environment
        api_response = api_instance.environments_deploy(id, deploy_request=deploy_request)
        print("The response of EnvironmentsApi->environments_deploy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_deploy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **deploy_request** | [**DeployRequest**](DeployRequest.md)|  | [optional] 

### Return type

[**DeployResult**](DeployResult.md)

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

# **environments_destroy**
> EnvironmentApiDestroyResponse environments_destroy(id, checkout_updated_code=checkout_updated_code, is_scheduled_run=is_scheduled_run, skip_state_refresh=skip_state_refresh, revision=revision, environment_api_destroy_request_body=environment_api_destroy_request_body)

Destroy Environment

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_destroy_request_body import EnvironmentApiDestroyRequestBody
from env0_client.models.environment_api_destroy_response import EnvironmentApiDestroyResponse
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    checkout_updated_code = 'checkout_updated_code_example' # str | Checkout updated code (optional)
    is_scheduled_run = 'is_scheduled_run_example' # str | Is scheduled run (optional)
    skip_state_refresh = 'skip_state_refresh_example' # str | Skip automatic state refresh (optional)
    revision = 'revision_example' # str | Revision (optional)
    environment_api_destroy_request_body = env0_client.EnvironmentApiDestroyRequestBody() # EnvironmentApiDestroyRequestBody |  (optional)

    try:
        # Destroy Environment
        api_response = api_instance.environments_destroy(id, checkout_updated_code=checkout_updated_code, is_scheduled_run=is_scheduled_run, skip_state_refresh=skip_state_refresh, revision=revision, environment_api_destroy_request_body=environment_api_destroy_request_body)
        print("The response of EnvironmentsApi->environments_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **checkout_updated_code** | **str**| Checkout updated code | [optional] 
 **is_scheduled_run** | **str**| Is scheduled run | [optional] 
 **skip_state_refresh** | **str**| Skip automatic state refresh | [optional] 
 **revision** | **str**| Revision | [optional] 
 **environment_api_destroy_request_body** | [**EnvironmentApiDestroyRequestBody**](EnvironmentApiDestroyRequestBody.md)|  | [optional] 

### Return type

[**EnvironmentApiDestroyResponse**](EnvironmentApiDestroyResponse.md)

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

# **environments_find_all**
> List[EnvironmentApiEnvironment] environments_find_all(limit=limit, offset=offset, organization_id=organization_id, project_id=project_id, only_my=only_my, is_active=is_active, name=name, is_remote_backend=is_remote_backend, workspace_name=workspace_name, workspace_name_prefix=workspace_name_prefix, include_sub_environments=include_sub_environments, search_text=search_text)

List Environments

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_environment import EnvironmentApiEnvironment
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    limit = 'limit_example' # str | Number of environments per page. The maximum is 100, with the default value is set to maximum (optional)
    offset = 'offset_example' # str | The offset of the first environment returned. Defaults to 0 (optional)
    organization_id = 'organization_id_example' # str |  (optional)
    project_id = 'project_id_example' # str |  (optional)
    only_my = 'only_my_example' # str |  (optional)
    is_active = 'is_active_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    is_remote_backend = 'is_remote_backend_example' # str |  (optional)
    workspace_name = 'workspace_name_example' # str |  (optional)
    workspace_name_prefix = 'workspace_name_prefix_example' # str |  (optional)
    include_sub_environments = 'include_sub_environments_example' # str |  (optional)
    search_text = 'search_text_example' # str |  (optional)

    try:
        # List Environments
        api_response = api_instance.environments_find_all(limit=limit, offset=offset, organization_id=organization_id, project_id=project_id, only_my=only_my, is_active=is_active, name=name, is_remote_backend=is_remote_backend, workspace_name=workspace_name, workspace_name_prefix=workspace_name_prefix, include_sub_environments=include_sub_environments, search_text=search_text)
        print("The response of EnvironmentsApi->environments_find_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_find_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Number of environments per page. The maximum is 100, with the default value is set to maximum | [optional] 
 **offset** | **str**| The offset of the first environment returned. Defaults to 0 | [optional] 
 **organization_id** | **str**|  | [optional] 
 **project_id** | **str**|  | [optional] 
 **only_my** | **str**|  | [optional] 
 **is_active** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **is_remote_backend** | **str**|  | [optional] 
 **workspace_name** | **str**|  | [optional] 
 **workspace_name_prefix** | **str**|  | [optional] 
 **include_sub_environments** | **str**|  | [optional] 
 **search_text** | **str**|  | [optional] 

### Return type

[**List[EnvironmentApiEnvironment]**](EnvironmentApiEnvironment.md)

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

# **environments_find_by_id**
> EnvironmentApiEnvironment environments_find_by_id(id)

Get Environment

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_environment import EnvironmentApiEnvironment
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Environment
        api_response = api_instance.environments_find_by_id(id)
        print("The response of EnvironmentsApi->environments_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**EnvironmentApiEnvironment**](EnvironmentApiEnvironment.md)

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

# **environments_find_deployment_log_by_id**
> EnvironmentApiDeploymentLog environments_find_deployment_log_by_id(id)

Get Deployment

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_deployment_log import EnvironmentApiDeploymentLog
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Deployment
        api_response = api_instance.environments_find_deployment_log_by_id(id)
        print("The response of EnvironmentsApi->environments_find_deployment_log_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_find_deployment_log_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**EnvironmentApiDeploymentLog**](EnvironmentApiDeploymentLog.md)

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

# **environments_find_deployment_logs_by_environment_id**
> List[EnvironmentApiDeploymentLog] environments_find_deployment_logs_by_environment_id(id, limit=limit, offset=offset, from_date=from_date, to_date=to_date, deployment_types=deployment_types, statuses=statuses)

List Deployments

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_deployment_log import EnvironmentApiDeploymentLog
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    limit = 'limit_example' # str | Number of deployments per page. The maximum is 100, with the default value is set to maximum (optional)
    offset = 'offset_example' # str | The offset of the first deployment returned. Defaults to 0 (optional)
    from_date = 'from_date_example' # str | The start date of the first deployment log in the response. Must be provided with toDate and in the following format YYYY-MM-DDTHH:mm:ss.sssZ (optional)
    to_date = 'to_date_example' # str | The start date of the last deployment log in the response. Must be provided with fromDate and in the following format YYYY-MM-DDTHH:mm:ss.sssZ (optional)
    deployment_types = 'deployment_types_example' # str | The types of the deployment logs in the response. The types should be in Camel case and separated by commas. For example: deploymentTypes=deploy,prPlan,driftDetection (optional)
    statuses = 'statuses_example' # str | The statuses of the deployment logs in the response. The statuses should be separated by commas. (optional)

    try:
        # List Deployments
        api_response = api_instance.environments_find_deployment_logs_by_environment_id(id, limit=limit, offset=offset, from_date=from_date, to_date=to_date, deployment_types=deployment_types, statuses=statuses)
        print("The response of EnvironmentsApi->environments_find_deployment_logs_by_environment_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_find_deployment_logs_by_environment_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **str**| Number of deployments per page. The maximum is 100, with the default value is set to maximum | [optional] 
 **offset** | **str**| The offset of the first deployment returned. Defaults to 0 | [optional] 
 **from_date** | **str**| The start date of the first deployment log in the response. Must be provided with toDate and in the following format YYYY-MM-DDTHH:mm:ss.sssZ | [optional] 
 **to_date** | **str**| The start date of the last deployment log in the response. Must be provided with fromDate and in the following format YYYY-MM-DDTHH:mm:ss.sssZ | [optional] 
 **deployment_types** | **str**| The types of the deployment logs in the response. The types should be in Camel case and separated by commas. For example: deploymentTypes&#x3D;deploy,prPlan,driftDetection | [optional] 
 **statuses** | **str**| The statuses of the deployment logs in the response. The statuses should be separated by commas. | [optional] 

### Return type

[**List[EnvironmentApiDeploymentLog]**](EnvironmentApiDeploymentLog.md)

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

# **environments_find_downstream_environments**
> List[EnvironmentApiDownstreamEnvironment] environments_find_downstream_environments(id)

Get downstream environments that will be triggered by this environment deployment

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_downstream_environment import EnvironmentApiDownstreamEnvironment
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get downstream environments that will be triggered by this environment deployment
        api_response = api_instance.environments_find_downstream_environments(id)
        print("The response of EnvironmentsApi->environments_find_downstream_environments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_find_downstream_environments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[EnvironmentApiDownstreamEnvironment]**](EnvironmentApiDownstreamEnvironment.md)

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

# **environments_find_resources**
> List[EnvironmentApiEnvironmentResource] environments_find_resources(id)

List Resources

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_environment_resource import EnvironmentApiEnvironmentResource
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 

    try:
        # List Resources
        api_response = api_instance.environments_find_resources(id)
        print("The response of EnvironmentsApi->environments_find_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_find_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[EnvironmentApiEnvironmentResource]**](EnvironmentApiEnvironmentResource.md)

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

# **environments_find_sub_deployment_log**
> EnvironmentApiDeploymentLog environments_find_sub_deployment_log(sub_environment_id, workflow_deployment_id)

Get Sub Deployment Log In A Workflow By Workflow Deployment Id And Environment Id

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_deployment_log import EnvironmentApiDeploymentLog
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    sub_environment_id = 'sub_environment_id_example' # str | 
    workflow_deployment_id = 'workflow_deployment_id_example' # str | 

    try:
        # Get Sub Deployment Log In A Workflow By Workflow Deployment Id And Environment Id
        api_response = api_instance.environments_find_sub_deployment_log(sub_environment_id, workflow_deployment_id)
        print("The response of EnvironmentsApi->environments_find_sub_deployment_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_find_sub_deployment_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_environment_id** | **str**|  | 
 **workflow_deployment_id** | **str**|  | 

### Return type

[**EnvironmentApiDeploymentLog**](EnvironmentApiDeploymentLog.md)

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

# **environments_get_environments_outputs**
> EnvironmentApiGetEnvironmentsOutputsResponse environments_get_environments_outputs(project_id)

Get Environments Outputs

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_get_environments_outputs_response import EnvironmentApiGetEnvironmentsOutputsResponse
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Get Environments Outputs
        api_response = api_instance.environments_get_environments_outputs(project_id)
        print("The response of EnvironmentsApi->environments_get_environments_outputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_get_environments_outputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**EnvironmentApiGetEnvironmentsOutputsResponse**](EnvironmentApiGetEnvironmentsOutputsResponse.md)

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

# **environments_get_projects_envs_statuses_counts_by_org**
> object environments_get_projects_envs_statuses_counts_by_org(organization_id)

Counts all selected statuses of organization projects

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
    api_instance = env0_client.EnvironmentsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Counts all selected statuses of organization projects
        api_response = api_instance.environments_get_projects_envs_statuses_counts_by_org(organization_id)
        print("The response of EnvironmentsApi->environments_get_projects_envs_statuses_counts_by_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_get_projects_envs_statuses_counts_by_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

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

# **environments_rerun_deployment**
> object environments_rerun_deployment(id, body=body)

Rerun PR plan

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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    body = None # object |  (optional)

    try:
        # Rerun PR plan
        api_response = api_instance.environments_rerun_deployment(id, body=body)
        print("The response of EnvironmentsApi->environments_rerun_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_rerun_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **environments_resume**
> EnvironmentApiResumeResponse environments_resume(id, body=body)

Resume Deployment

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_resume_response import EnvironmentApiResumeResponse
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    body = None # object |  (optional)

    try:
        # Resume Deployment
        api_response = api_instance.environments_resume(id, body=body)
        print("The response of EnvironmentsApi->environments_resume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_resume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | [optional] 

### Return type

[**EnvironmentApiResumeResponse**](EnvironmentApiResumeResponse.md)

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

# **environments_save_as_template**
> EnvironmentApiEnvironment environments_save_as_template(id, environment_api_save_as_template_request_body=environment_api_save_as_template_request_body)

Save VCS environment as a template

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_environment import EnvironmentApiEnvironment
from env0_client.models.environment_api_save_as_template_request_body import EnvironmentApiSaveAsTemplateRequestBody
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    environment_api_save_as_template_request_body = env0_client.EnvironmentApiSaveAsTemplateRequestBody() # EnvironmentApiSaveAsTemplateRequestBody |  (optional)

    try:
        # Save VCS environment as a template
        api_response = api_instance.environments_save_as_template(id, environment_api_save_as_template_request_body=environment_api_save_as_template_request_body)
        print("The response of EnvironmentsApi->environments_save_as_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_save_as_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **environment_api_save_as_template_request_body** | [**EnvironmentApiSaveAsTemplateRequestBody**](EnvironmentApiSaveAsTemplateRequestBody.md)|  | [optional] 

### Return type

[**EnvironmentApiEnvironment**](EnvironmentApiEnvironment.md)

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

# **environments_subscribe_downstream_environments**
> object environments_subscribe_downstream_environments(id, environment_api_subscribe_downstream_environments_request_body=environment_api_subscribe_downstream_environments_request_body)

Subscribe environments as workflow-trigger

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_subscribe_downstream_environments_request_body import EnvironmentApiSubscribeDownstreamEnvironmentsRequestBody
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    environment_api_subscribe_downstream_environments_request_body = env0_client.EnvironmentApiSubscribeDownstreamEnvironmentsRequestBody() # EnvironmentApiSubscribeDownstreamEnvironmentsRequestBody |  (optional)

    try:
        # Subscribe environments as workflow-trigger
        api_response = api_instance.environments_subscribe_downstream_environments(id, environment_api_subscribe_downstream_environments_request_body=environment_api_subscribe_downstream_environments_request_body)
        print("The response of EnvironmentsApi->environments_subscribe_downstream_environments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_subscribe_downstream_environments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **environment_api_subscribe_downstream_environments_request_body** | [**EnvironmentApiSubscribeDownstreamEnvironmentsRequestBody**](EnvironmentApiSubscribeDownstreamEnvironmentsRequestBody.md)|  | [optional] 

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

# **environments_ttl**
> EnvironmentApiEnvironment environments_ttl(id, environment_api_ttl_request=environment_api_ttl_request)

Update Environment TTL

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_environment import EnvironmentApiEnvironment
from env0_client.models.environment_api_ttl_request import EnvironmentApiTTLRequest
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    environment_api_ttl_request = env0_client.EnvironmentApiTTLRequest() # EnvironmentApiTTLRequest |  (optional)

    try:
        # Update Environment TTL
        api_response = api_instance.environments_ttl(id, environment_api_ttl_request=environment_api_ttl_request)
        print("The response of EnvironmentsApi->environments_ttl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_ttl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **environment_api_ttl_request** | [**EnvironmentApiTTLRequest**](EnvironmentApiTTLRequest.md)|  | [optional] 

### Return type

[**EnvironmentApiEnvironment**](EnvironmentApiEnvironment.md)

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

# **environments_unsubscribe_downstream_environments**
> object environments_unsubscribe_downstream_environments(id, environment_api_unsubscribe_downstream_environments_request_body=environment_api_unsubscribe_downstream_environments_request_body)

Unsubscribe environments as workflow-trigger

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_unsubscribe_downstream_environments_request_body import EnvironmentApiUnsubscribeDownstreamEnvironmentsRequestBody
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    environment_api_unsubscribe_downstream_environments_request_body = env0_client.EnvironmentApiUnsubscribeDownstreamEnvironmentsRequestBody() # EnvironmentApiUnsubscribeDownstreamEnvironmentsRequestBody |  (optional)

    try:
        # Unsubscribe environments as workflow-trigger
        api_response = api_instance.environments_unsubscribe_downstream_environments(id, environment_api_unsubscribe_downstream_environments_request_body=environment_api_unsubscribe_downstream_environments_request_body)
        print("The response of EnvironmentsApi->environments_unsubscribe_downstream_environments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_unsubscribe_downstream_environments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **environment_api_unsubscribe_downstream_environments_request_body** | [**EnvironmentApiUnsubscribeDownstreamEnvironmentsRequestBody**](EnvironmentApiUnsubscribeDownstreamEnvironmentsRequestBody.md)|  | [optional] 

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

# **environments_update**
> EnvironmentApiEnvironment environments_update(id, environment_api_update_request_body=environment_api_update_request_body)

Update Environment

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_environment import EnvironmentApiEnvironment
from env0_client.models.environment_api_update_request_body import EnvironmentApiUpdateRequestBody
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    environment_api_update_request_body = env0_client.EnvironmentApiUpdateRequestBody() # EnvironmentApiUpdateRequestBody |  (optional)

    try:
        # Update Environment
        api_response = api_instance.environments_update(id, environment_api_update_request_body=environment_api_update_request_body)
        print("The response of EnvironmentsApi->environments_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **environment_api_update_request_body** | [**EnvironmentApiUpdateRequestBody**](EnvironmentApiUpdateRequestBody.md)|  | [optional] 

### Return type

[**EnvironmentApiEnvironment**](EnvironmentApiEnvironment.md)

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

# **environments_update_downstream_environments**
> List[EnvironmentApiDownstreamEnvironment] environments_update_downstream_environments(id, environment_api_update_downstream_environments_request_body=environment_api_update_downstream_environments_request_body)

Create or Update Workflow Trigger

Env0 allows you to configure chained dependent environments to your current environment. Using workflow triggers, you can define which environments would trigger a deployment downstream in response to a deployment of your current environment. This allows you to configure a cascading series of environment deployments.\" More on https://docs.env0.com/docs/workflow-triggers 

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_downstream_environment import EnvironmentApiDownstreamEnvironment
from env0_client.models.environment_api_update_downstream_environments_request_body import EnvironmentApiUpdateDownstreamEnvironmentsRequestBody
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    environment_api_update_downstream_environments_request_body = env0_client.EnvironmentApiUpdateDownstreamEnvironmentsRequestBody() # EnvironmentApiUpdateDownstreamEnvironmentsRequestBody |  (optional)

    try:
        # Create or Update Workflow Trigger
        api_response = api_instance.environments_update_downstream_environments(id, environment_api_update_downstream_environments_request_body=environment_api_update_downstream_environments_request_body)
        print("The response of EnvironmentsApi->environments_update_downstream_environments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_update_downstream_environments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **environment_api_update_downstream_environments_request_body** | [**EnvironmentApiUpdateDownstreamEnvironmentsRequestBody**](EnvironmentApiUpdateDownstreamEnvironmentsRequestBody.md)|  | [optional] 

### Return type

[**List[EnvironmentApiDownstreamEnvironment]**](EnvironmentApiDownstreamEnvironment.md)

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

# **environments_update_environment_lock**
> EnvironmentApiEnvironmentLockStatus environments_update_environment_lock(id, environment_api_update_environment_lock_request_body=environment_api_update_environment_lock_request_body)

Lock/Unlock environment

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.environment_api_environment_lock_status import EnvironmentApiEnvironmentLockStatus
from env0_client.models.environment_api_update_environment_lock_request_body import EnvironmentApiUpdateEnvironmentLockRequestBody
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
    api_instance = env0_client.EnvironmentsApi(api_client)
    id = 'id_example' # str | 
    environment_api_update_environment_lock_request_body = env0_client.EnvironmentApiUpdateEnvironmentLockRequestBody() # EnvironmentApiUpdateEnvironmentLockRequestBody |  (optional)

    try:
        # Lock/Unlock environment
        api_response = api_instance.environments_update_environment_lock(id, environment_api_update_environment_lock_request_body=environment_api_update_environment_lock_request_body)
        print("The response of EnvironmentsApi->environments_update_environment_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->environments_update_environment_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **environment_api_update_environment_lock_request_body** | [**EnvironmentApiUpdateEnvironmentLockRequestBody**](EnvironmentApiUpdateEnvironmentLockRequestBody.md)|  | [optional] 

### Return type

[**EnvironmentApiEnvironmentLockStatus**](EnvironmentApiEnvironmentLockStatus.md)

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

