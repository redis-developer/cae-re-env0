# env0_client.BulkOperationsApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_operations_bulk_approve**](BulkOperationsApi.md#bulk_operations_bulk_approve) | **POST** /bulk-operations/approve | Bulk approve
[**bulk_operations_bulk_archive**](BulkOperationsApi.md#bulk_operations_bulk_archive) | **POST** /bulk-operations/archive | Bulk archive
[**bulk_operations_bulk_cancel**](BulkOperationsApi.md#bulk_operations_bulk_cancel) | **POST** /bulk-operations/cancel | Bulk deploy
[**bulk_operations_bulk_cancel_queued_deployments**](BulkOperationsApi.md#bulk_operations_bulk_cancel_queued_deployments) | **POST** /bulk-operations/cancel-queued-deployments | Bulk cancel queued deployments
[**bulk_operations_bulk_deploy**](BulkOperationsApi.md#bulk_operations_bulk_deploy) | **POST** /bulk-operations/deploy | Bulk deploy
[**bulk_operations_bulk_destroy**](BulkOperationsApi.md#bulk_operations_bulk_destroy) | **POST** /bulk-operations/destroy | Bulk destroy
[**bulk_operations_bulk_lock**](BulkOperationsApi.md#bulk_operations_bulk_lock) | **POST** /bulk-operations/lock | Bulk lock
[**bulk_operations_bulk_run_task**](BulkOperationsApi.md#bulk_operations_bulk_run_task) | **POST** /bulk-operations/run-task | Bulk run task
[**bulk_operations_bulk_unlock**](BulkOperationsApi.md#bulk_operations_bulk_unlock) | **POST** /bulk-operations/unlock | Bulk unlock


# **bulk_operations_bulk_approve**
> BulkOperationsApiBaseResponse bulk_operations_bulk_approve(bulk_operations_api_base_payload=bulk_operations_api_base_payload)

Bulk approve

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.bulk_operations_api_base_payload import BulkOperationsApiBasePayload
from env0_client.models.bulk_operations_api_base_response import BulkOperationsApiBaseResponse
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
    api_instance = env0_client.BulkOperationsApi(api_client)
    bulk_operations_api_base_payload = env0_client.BulkOperationsApiBasePayload() # BulkOperationsApiBasePayload |  (optional)

    try:
        # Bulk approve
        api_response = api_instance.bulk_operations_bulk_approve(bulk_operations_api_base_payload=bulk_operations_api_base_payload)
        print("The response of BulkOperationsApi->bulk_operations_bulk_approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkOperationsApi->bulk_operations_bulk_approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_operations_api_base_payload** | [**BulkOperationsApiBasePayload**](BulkOperationsApiBasePayload.md)|  | [optional] 

### Return type

[**BulkOperationsApiBaseResponse**](BulkOperationsApiBaseResponse.md)

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

# **bulk_operations_bulk_archive**
> BulkOperationsApiBaseResponse bulk_operations_bulk_archive(bulk_operations_api_base_payload=bulk_operations_api_base_payload)

Bulk archive

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.bulk_operations_api_base_payload import BulkOperationsApiBasePayload
from env0_client.models.bulk_operations_api_base_response import BulkOperationsApiBaseResponse
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
    api_instance = env0_client.BulkOperationsApi(api_client)
    bulk_operations_api_base_payload = env0_client.BulkOperationsApiBasePayload() # BulkOperationsApiBasePayload |  (optional)

    try:
        # Bulk archive
        api_response = api_instance.bulk_operations_bulk_archive(bulk_operations_api_base_payload=bulk_operations_api_base_payload)
        print("The response of BulkOperationsApi->bulk_operations_bulk_archive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkOperationsApi->bulk_operations_bulk_archive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_operations_api_base_payload** | [**BulkOperationsApiBasePayload**](BulkOperationsApiBasePayload.md)|  | [optional] 

### Return type

[**BulkOperationsApiBaseResponse**](BulkOperationsApiBaseResponse.md)

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

# **bulk_operations_bulk_cancel**
> BulkOperationsApiBaseResponse bulk_operations_bulk_cancel(bulk_operations_api_base_payload=bulk_operations_api_base_payload)

Bulk deploy

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.bulk_operations_api_base_payload import BulkOperationsApiBasePayload
from env0_client.models.bulk_operations_api_base_response import BulkOperationsApiBaseResponse
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
    api_instance = env0_client.BulkOperationsApi(api_client)
    bulk_operations_api_base_payload = env0_client.BulkOperationsApiBasePayload() # BulkOperationsApiBasePayload |  (optional)

    try:
        # Bulk deploy
        api_response = api_instance.bulk_operations_bulk_cancel(bulk_operations_api_base_payload=bulk_operations_api_base_payload)
        print("The response of BulkOperationsApi->bulk_operations_bulk_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkOperationsApi->bulk_operations_bulk_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_operations_api_base_payload** | [**BulkOperationsApiBasePayload**](BulkOperationsApiBasePayload.md)|  | [optional] 

### Return type

[**BulkOperationsApiBaseResponse**](BulkOperationsApiBaseResponse.md)

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

# **bulk_operations_bulk_cancel_queued_deployments**
> BulkOperationsApiBaseResponse bulk_operations_bulk_cancel_queued_deployments(bulk_operations_api_base_payload=bulk_operations_api_base_payload)

Bulk cancel queued deployments

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.bulk_operations_api_base_payload import BulkOperationsApiBasePayload
from env0_client.models.bulk_operations_api_base_response import BulkOperationsApiBaseResponse
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
    api_instance = env0_client.BulkOperationsApi(api_client)
    bulk_operations_api_base_payload = env0_client.BulkOperationsApiBasePayload() # BulkOperationsApiBasePayload |  (optional)

    try:
        # Bulk cancel queued deployments
        api_response = api_instance.bulk_operations_bulk_cancel_queued_deployments(bulk_operations_api_base_payload=bulk_operations_api_base_payload)
        print("The response of BulkOperationsApi->bulk_operations_bulk_cancel_queued_deployments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkOperationsApi->bulk_operations_bulk_cancel_queued_deployments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_operations_api_base_payload** | [**BulkOperationsApiBasePayload**](BulkOperationsApiBasePayload.md)|  | [optional] 

### Return type

[**BulkOperationsApiBaseResponse**](BulkOperationsApiBaseResponse.md)

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

# **bulk_operations_bulk_deploy**
> BulkOperationsApiBaseResponse bulk_operations_bulk_deploy(bulk_operations_api_bulk_deploy_request_body=bulk_operations_api_bulk_deploy_request_body)

Bulk deploy

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.bulk_operations_api_base_response import BulkOperationsApiBaseResponse
from env0_client.models.bulk_operations_api_bulk_deploy_request_body import BulkOperationsApiBulkDeployRequestBody
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
    api_instance = env0_client.BulkOperationsApi(api_client)
    bulk_operations_api_bulk_deploy_request_body = env0_client.BulkOperationsApiBulkDeployRequestBody() # BulkOperationsApiBulkDeployRequestBody |  (optional)

    try:
        # Bulk deploy
        api_response = api_instance.bulk_operations_bulk_deploy(bulk_operations_api_bulk_deploy_request_body=bulk_operations_api_bulk_deploy_request_body)
        print("The response of BulkOperationsApi->bulk_operations_bulk_deploy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkOperationsApi->bulk_operations_bulk_deploy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_operations_api_bulk_deploy_request_body** | [**BulkOperationsApiBulkDeployRequestBody**](BulkOperationsApiBulkDeployRequestBody.md)|  | [optional] 

### Return type

[**BulkOperationsApiBaseResponse**](BulkOperationsApiBaseResponse.md)

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

# **bulk_operations_bulk_destroy**
> BulkOperationsApiBaseResponse bulk_operations_bulk_destroy(bulk_operations_api_bulk_destroy_request_body=bulk_operations_api_bulk_destroy_request_body)

Bulk destroy

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.bulk_operations_api_base_response import BulkOperationsApiBaseResponse
from env0_client.models.bulk_operations_api_bulk_destroy_request_body import BulkOperationsApiBulkDestroyRequestBody
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
    api_instance = env0_client.BulkOperationsApi(api_client)
    bulk_operations_api_bulk_destroy_request_body = env0_client.BulkOperationsApiBulkDestroyRequestBody() # BulkOperationsApiBulkDestroyRequestBody |  (optional)

    try:
        # Bulk destroy
        api_response = api_instance.bulk_operations_bulk_destroy(bulk_operations_api_bulk_destroy_request_body=bulk_operations_api_bulk_destroy_request_body)
        print("The response of BulkOperationsApi->bulk_operations_bulk_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkOperationsApi->bulk_operations_bulk_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_operations_api_bulk_destroy_request_body** | [**BulkOperationsApiBulkDestroyRequestBody**](BulkOperationsApiBulkDestroyRequestBody.md)|  | [optional] 

### Return type

[**BulkOperationsApiBaseResponse**](BulkOperationsApiBaseResponse.md)

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

# **bulk_operations_bulk_lock**
> BulkOperationsApiBaseResponse bulk_operations_bulk_lock(bulk_operations_api_bulk_lock_request_body=bulk_operations_api_bulk_lock_request_body)

Bulk lock

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.bulk_operations_api_base_response import BulkOperationsApiBaseResponse
from env0_client.models.bulk_operations_api_bulk_lock_request_body import BulkOperationsApiBulkLockRequestBody
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
    api_instance = env0_client.BulkOperationsApi(api_client)
    bulk_operations_api_bulk_lock_request_body = env0_client.BulkOperationsApiBulkLockRequestBody() # BulkOperationsApiBulkLockRequestBody |  (optional)

    try:
        # Bulk lock
        api_response = api_instance.bulk_operations_bulk_lock(bulk_operations_api_bulk_lock_request_body=bulk_operations_api_bulk_lock_request_body)
        print("The response of BulkOperationsApi->bulk_operations_bulk_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkOperationsApi->bulk_operations_bulk_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_operations_api_bulk_lock_request_body** | [**BulkOperationsApiBulkLockRequestBody**](BulkOperationsApiBulkLockRequestBody.md)|  | [optional] 

### Return type

[**BulkOperationsApiBaseResponse**](BulkOperationsApiBaseResponse.md)

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

# **bulk_operations_bulk_run_task**
> BulkOperationsApiBaseResponse bulk_operations_bulk_run_task(bulk_operations_api_bulk_run_task_request_body=bulk_operations_api_bulk_run_task_request_body)

Bulk run task

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.bulk_operations_api_base_response import BulkOperationsApiBaseResponse
from env0_client.models.bulk_operations_api_bulk_run_task_request_body import BulkOperationsApiBulkRunTaskRequestBody
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
    api_instance = env0_client.BulkOperationsApi(api_client)
    bulk_operations_api_bulk_run_task_request_body = env0_client.BulkOperationsApiBulkRunTaskRequestBody() # BulkOperationsApiBulkRunTaskRequestBody |  (optional)

    try:
        # Bulk run task
        api_response = api_instance.bulk_operations_bulk_run_task(bulk_operations_api_bulk_run_task_request_body=bulk_operations_api_bulk_run_task_request_body)
        print("The response of BulkOperationsApi->bulk_operations_bulk_run_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkOperationsApi->bulk_operations_bulk_run_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_operations_api_bulk_run_task_request_body** | [**BulkOperationsApiBulkRunTaskRequestBody**](BulkOperationsApiBulkRunTaskRequestBody.md)|  | [optional] 

### Return type

[**BulkOperationsApiBaseResponse**](BulkOperationsApiBaseResponse.md)

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

# **bulk_operations_bulk_unlock**
> BulkOperationsApiBaseResponse bulk_operations_bulk_unlock(bulk_operations_api_base_payload=bulk_operations_api_base_payload)

Bulk unlock

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.bulk_operations_api_base_payload import BulkOperationsApiBasePayload
from env0_client.models.bulk_operations_api_base_response import BulkOperationsApiBaseResponse
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
    api_instance = env0_client.BulkOperationsApi(api_client)
    bulk_operations_api_base_payload = env0_client.BulkOperationsApiBasePayload() # BulkOperationsApiBasePayload |  (optional)

    try:
        # Bulk unlock
        api_response = api_instance.bulk_operations_bulk_unlock(bulk_operations_api_base_payload=bulk_operations_api_base_payload)
        print("The response of BulkOperationsApi->bulk_operations_bulk_unlock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkOperationsApi->bulk_operations_bulk_unlock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_operations_api_base_payload** | [**BulkOperationsApiBasePayload**](BulkOperationsApiBasePayload.md)|  | [optional] 

### Return type

[**BulkOperationsApiBaseResponse**](BulkOperationsApiBaseResponse.md)

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

