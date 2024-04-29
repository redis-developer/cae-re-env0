# env0_client.RemoteBackendServiceApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remote_backend_service_delete_state_access_configuration**](RemoteBackendServiceApi.md#remote_backend_service_delete_state_access_configuration) | **DELETE** /remote-backend/states/{environmentId}/access-control | Delete remote state access configuration
[**remote_backend_service_get_state_access_configuration**](RemoteBackendServiceApi.md#remote_backend_service_get_state_access_configuration) | **GET** /remote-backend/states/{environmentId}/access-control | Get remote state access configuration
[**remote_backend_service_put_state_access_configuration**](RemoteBackendServiceApi.md#remote_backend_service_put_state_access_configuration) | **PUT** /remote-backend/states/{environmentId}/access-control | Create remote state access configuration


# **remote_backend_service_delete_state_access_configuration**
> remote_backend_service_delete_state_access_configuration(environment_id)

Delete remote state access configuration

Deletes an existing environment state access configuration

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
    api_instance = env0_client.RemoteBackendServiceApi(api_client)
    environment_id = 'environment_id_example' # str | 

    try:
        # Delete remote state access configuration
        api_instance.remote_backend_service_delete_state_access_configuration(environment_id)
    except Exception as e:
        print("Exception when calling RemoteBackendServiceApi->remote_backend_service_delete_state_access_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  | 

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

# **remote_backend_service_get_state_access_configuration**
> RemoteBackendApiStateAccessConfiguration remote_backend_service_get_state_access_configuration(environment_id)

Get remote state access configuration

Describe which environments, or projects in the organization may access a given environment's state

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.remote_backend_api_state_access_configuration import RemoteBackendApiStateAccessConfiguration
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
    api_instance = env0_client.RemoteBackendServiceApi(api_client)
    environment_id = 'environment_id_example' # str | 

    try:
        # Get remote state access configuration
        api_response = api_instance.remote_backend_service_get_state_access_configuration(environment_id)
        print("The response of RemoteBackendServiceApi->remote_backend_service_get_state_access_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteBackendServiceApi->remote_backend_service_get_state_access_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  | 

### Return type

[**RemoteBackendApiStateAccessConfiguration**](RemoteBackendApiStateAccessConfiguration.md)

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

# **remote_backend_service_put_state_access_configuration**
> RemoteBackendApiStateAccessConfiguration remote_backend_service_put_state_access_configuration(environment_id, remote_backend_api_put_state_access_configuration_request_body=remote_backend_api_put_state_access_configuration_request_body)

Create remote state access configuration

Creates configuration describing which environments, or projects in the organization may access a given environment's state

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.remote_backend_api_put_state_access_configuration_request_body import RemoteBackendApiPutStateAccessConfigurationRequestBody
from env0_client.models.remote_backend_api_state_access_configuration import RemoteBackendApiStateAccessConfiguration
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
    api_instance = env0_client.RemoteBackendServiceApi(api_client)
    environment_id = 'environment_id_example' # str | 
    remote_backend_api_put_state_access_configuration_request_body = env0_client.RemoteBackendApiPutStateAccessConfigurationRequestBody() # RemoteBackendApiPutStateAccessConfigurationRequestBody |  (optional)

    try:
        # Create remote state access configuration
        api_response = api_instance.remote_backend_service_put_state_access_configuration(environment_id, remote_backend_api_put_state_access_configuration_request_body=remote_backend_api_put_state_access_configuration_request_body)
        print("The response of RemoteBackendServiceApi->remote_backend_service_put_state_access_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteBackendServiceApi->remote_backend_service_put_state_access_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  | 
 **remote_backend_api_put_state_access_configuration_request_body** | [**RemoteBackendApiPutStateAccessConfigurationRequestBody**](RemoteBackendApiPutStateAccessConfigurationRequestBody.md)|  | [optional] 

### Return type

[**RemoteBackendApiStateAccessConfiguration**](RemoteBackendApiStateAccessConfiguration.md)

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

