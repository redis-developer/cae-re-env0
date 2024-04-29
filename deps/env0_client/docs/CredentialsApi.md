# env0_client.CredentialsApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credentials_create_api_key**](CredentialsApi.md#credentials_create_api_key) | **POST** /api-keys | Create API Key
[**credentials_create_personal_api_key**](CredentialsApi.md#credentials_create_personal_api_key) | **POST** /personal-api-keys | Create personal API Key
[**credentials_delete_api_key**](CredentialsApi.md#credentials_delete_api_key) | **DELETE** /api-keys/{id} | Delete an API Key
[**credentials_delete_personal_api_key**](CredentialsApi.md#credentials_delete_personal_api_key) | **DELETE** /personal-api-keys/{id} | Delete a User&#39;s personal API Key endpoint
[**credentials_find_all_api_keys**](CredentialsApi.md#credentials_find_all_api_keys) | **GET** /api-keys | List Organization API Keys
[**credentials_find_all_personal_api_keys**](CredentialsApi.md#credentials_find_all_personal_api_keys) | **GET** /personal-api-keys | List User&#39;s personal API Keys endpoint


# **credentials_create_api_key**
> CredentialsApiApiKey credentials_create_api_key(credentials_api_create_api_key_request_body=credentials_api_create_api_key_request_body)

Create API Key

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.credentials_api_api_key import CredentialsApiApiKey
from env0_client.models.credentials_api_create_api_key_request_body import CredentialsApiCreateApiKeyRequestBody
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
    api_instance = env0_client.CredentialsApi(api_client)
    credentials_api_create_api_key_request_body = env0_client.CredentialsApiCreateApiKeyRequestBody() # CredentialsApiCreateApiKeyRequestBody |  (optional)

    try:
        # Create API Key
        api_response = api_instance.credentials_create_api_key(credentials_api_create_api_key_request_body=credentials_api_create_api_key_request_body)
        print("The response of CredentialsApi->credentials_create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->credentials_create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_api_create_api_key_request_body** | [**CredentialsApiCreateApiKeyRequestBody**](CredentialsApiCreateApiKeyRequestBody.md)|  | [optional] 

### Return type

[**CredentialsApiApiKey**](CredentialsApiApiKey.md)

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

# **credentials_create_personal_api_key**
> CredentialsApiPersonalApiKey credentials_create_personal_api_key(credentials_api_create_personal_api_key_request_body=credentials_api_create_personal_api_key_request_body)

Create personal API Key

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.credentials_api_create_personal_api_key_request_body import CredentialsApiCreatePersonalApiKeyRequestBody
from env0_client.models.credentials_api_personal_api_key import CredentialsApiPersonalApiKey
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
    api_instance = env0_client.CredentialsApi(api_client)
    credentials_api_create_personal_api_key_request_body = env0_client.CredentialsApiCreatePersonalApiKeyRequestBody() # CredentialsApiCreatePersonalApiKeyRequestBody |  (optional)

    try:
        # Create personal API Key
        api_response = api_instance.credentials_create_personal_api_key(credentials_api_create_personal_api_key_request_body=credentials_api_create_personal_api_key_request_body)
        print("The response of CredentialsApi->credentials_create_personal_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->credentials_create_personal_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_api_create_personal_api_key_request_body** | [**CredentialsApiCreatePersonalApiKeyRequestBody**](CredentialsApiCreatePersonalApiKeyRequestBody.md)|  | [optional] 

### Return type

[**CredentialsApiPersonalApiKey**](CredentialsApiPersonalApiKey.md)

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

# **credentials_delete_api_key**
> credentials_delete_api_key(id)

Delete an API Key

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
    api_instance = env0_client.CredentialsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete an API Key
        api_instance.credentials_delete_api_key(id)
    except Exception as e:
        print("Exception when calling CredentialsApi->credentials_delete_api_key: %s\n" % e)
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

# **credentials_delete_personal_api_key**
> credentials_delete_personal_api_key(id)

Delete a User's personal API Key endpoint

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
    api_instance = env0_client.CredentialsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a User's personal API Key endpoint
        api_instance.credentials_delete_personal_api_key(id)
    except Exception as e:
        print("Exception when calling CredentialsApi->credentials_delete_personal_api_key: %s\n" % e)
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

# **credentials_find_all_api_keys**
> List[CredentialsApiApiKey] credentials_find_all_api_keys(organization_id)

List Organization API Keys

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.credentials_api_api_key import CredentialsApiApiKey
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
    api_instance = env0_client.CredentialsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # List Organization API Keys
        api_response = api_instance.credentials_find_all_api_keys(organization_id)
        print("The response of CredentialsApi->credentials_find_all_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->credentials_find_all_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**List[CredentialsApiApiKey]**](CredentialsApiApiKey.md)

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

# **credentials_find_all_personal_api_keys**
> List[CredentialsApiPersonalApiKey] credentials_find_all_personal_api_keys()

List User's personal API Keys endpoint

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.credentials_api_personal_api_key import CredentialsApiPersonalApiKey
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
    api_instance = env0_client.CredentialsApi(api_client)

    try:
        # List User's personal API Keys endpoint
        api_response = api_instance.credentials_find_all_personal_api_keys()
        print("The response of CredentialsApi->credentials_find_all_personal_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->credentials_find_all_personal_api_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CredentialsApiPersonalApiKey]**](CredentialsApiPersonalApiKey.md)

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

