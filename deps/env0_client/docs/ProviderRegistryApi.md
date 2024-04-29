# env0_client.ProviderRegistryApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**provider_registry_create_gpg_key**](ProviderRegistryApi.md#provider_registry_create_gpg_key) | **POST** /gpg-keys | Create a new GPG key
[**provider_registry_create_provider**](ProviderRegistryApi.md#provider_registry_create_provider) | **POST** /providers | Create a new provider
[**provider_registry_create_version**](ProviderRegistryApi.md#provider_registry_create_version) | **POST** /providers/{providerId}/versions | Create a new provider version
[**provider_registry_delete_gpg_key**](ProviderRegistryApi.md#provider_registry_delete_gpg_key) | **DELETE** /gpg-keys/{id} | Delete a GPG key
[**provider_registry_delete_provider**](ProviderRegistryApi.md#provider_registry_delete_provider) | **DELETE** /providers/{providerId} | Delete a provider
[**provider_registry_download_version**](ProviderRegistryApi.md#provider_registry_download_version) | **GET** /providers/v1/{namespace}/{type}/{version}/download/{os}/{architecture} | Get a download url for a specific version
[**provider_registry_find_gpg_keys_by_organization**](ProviderRegistryApi.md#provider_registry_find_gpg_keys_by_organization) | **GET** /gpg-keys | List all available GPG keys
[**provider_registry_find_provider_by_id**](ProviderRegistryApi.md#provider_registry_find_provider_by_id) | **GET** /providers/{providerId} | Find a provider by id
[**provider_registry_find_provider_by_type**](ProviderRegistryApi.md#provider_registry_find_provider_by_type) | **GET** /providers/v1/{namespace}/{type}/versions | Find a provider by type
[**provider_registry_find_providers_by_organization_id**](ProviderRegistryApi.md#provider_registry_find_providers_by_organization_id) | **GET** /providers | Find all providers in an organization
[**provider_registry_update_provider**](ProviderRegistryApi.md#provider_registry_update_provider) | **PUT** /providers/{providerId} | Update a provider


# **provider_registry_create_gpg_key**
> ProviderRegistryApiCreateGpgKeyResponse provider_registry_create_gpg_key(provider_registry_api_create_gpg_key_request_body=provider_registry_api_create_gpg_key_request_body)

Create a new GPG key

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.provider_registry_api_create_gpg_key_request_body import ProviderRegistryApiCreateGpgKeyRequestBody
from env0_client.models.provider_registry_api_create_gpg_key_response import ProviderRegistryApiCreateGpgKeyResponse
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
    api_instance = env0_client.ProviderRegistryApi(api_client)
    provider_registry_api_create_gpg_key_request_body = env0_client.ProviderRegistryApiCreateGpgKeyRequestBody() # ProviderRegistryApiCreateGpgKeyRequestBody |  (optional)

    try:
        # Create a new GPG key
        api_response = api_instance.provider_registry_create_gpg_key(provider_registry_api_create_gpg_key_request_body=provider_registry_api_create_gpg_key_request_body)
        print("The response of ProviderRegistryApi->provider_registry_create_gpg_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderRegistryApi->provider_registry_create_gpg_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_registry_api_create_gpg_key_request_body** | [**ProviderRegistryApiCreateGpgKeyRequestBody**](ProviderRegistryApiCreateGpgKeyRequestBody.md)|  | [optional] 

### Return type

[**ProviderRegistryApiCreateGpgKeyResponse**](ProviderRegistryApiCreateGpgKeyResponse.md)

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

# **provider_registry_create_provider**
> ProviderRegistryApiProvider provider_registry_create_provider(provider_registry_api_create_provider_request_body=provider_registry_api_create_provider_request_body)

Create a new provider

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.provider_registry_api_create_provider_request_body import ProviderRegistryApiCreateProviderRequestBody
from env0_client.models.provider_registry_api_provider import ProviderRegistryApiProvider
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
    api_instance = env0_client.ProviderRegistryApi(api_client)
    provider_registry_api_create_provider_request_body = env0_client.ProviderRegistryApiCreateProviderRequestBody() # ProviderRegistryApiCreateProviderRequestBody |  (optional)

    try:
        # Create a new provider
        api_response = api_instance.provider_registry_create_provider(provider_registry_api_create_provider_request_body=provider_registry_api_create_provider_request_body)
        print("The response of ProviderRegistryApi->provider_registry_create_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderRegistryApi->provider_registry_create_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_registry_api_create_provider_request_body** | [**ProviderRegistryApiCreateProviderRequestBody**](ProviderRegistryApiCreateProviderRequestBody.md)|  | [optional] 

### Return type

[**ProviderRegistryApiProvider**](ProviderRegistryApiProvider.md)

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

# **provider_registry_create_version**
> ProviderRegistryApiCreateVersionResponse provider_registry_create_version(provider_id, provider_registry_api_create_version_request_body=provider_registry_api_create_version_request_body)

Create a new provider version

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.provider_registry_api_create_version_request_body import ProviderRegistryApiCreateVersionRequestBody
from env0_client.models.provider_registry_api_create_version_response import ProviderRegistryApiCreateVersionResponse
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
    api_instance = env0_client.ProviderRegistryApi(api_client)
    provider_id = 'provider_id_example' # str | 
    provider_registry_api_create_version_request_body = env0_client.ProviderRegistryApiCreateVersionRequestBody() # ProviderRegistryApiCreateVersionRequestBody |  (optional)

    try:
        # Create a new provider version
        api_response = api_instance.provider_registry_create_version(provider_id, provider_registry_api_create_version_request_body=provider_registry_api_create_version_request_body)
        print("The response of ProviderRegistryApi->provider_registry_create_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderRegistryApi->provider_registry_create_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **provider_registry_api_create_version_request_body** | [**ProviderRegistryApiCreateVersionRequestBody**](ProviderRegistryApiCreateVersionRequestBody.md)|  | [optional] 

### Return type

[**ProviderRegistryApiCreateVersionResponse**](ProviderRegistryApiCreateVersionResponse.md)

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

# **provider_registry_delete_gpg_key**
> provider_registry_delete_gpg_key(id)

Delete a GPG key

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
    api_instance = env0_client.ProviderRegistryApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a GPG key
        api_instance.provider_registry_delete_gpg_key(id)
    except Exception as e:
        print("Exception when calling ProviderRegistryApi->provider_registry_delete_gpg_key: %s\n" % e)
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

# **provider_registry_delete_provider**
> provider_registry_delete_provider(provider_id)

Delete a provider

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
    api_instance = env0_client.ProviderRegistryApi(api_client)
    provider_id = 'provider_id_example' # str | 

    try:
        # Delete a provider
        api_instance.provider_registry_delete_provider(provider_id)
    except Exception as e:
        print("Exception when calling ProviderRegistryApi->provider_registry_delete_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 

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

# **provider_registry_download_version**
> ProviderRegistryApiTerraformTypesFindProviderPackageResponse provider_registry_download_version(namespace, type, version, os, architecture)

Get a download url for a specific version

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.provider_registry_api_terraform_types_find_provider_package_response import ProviderRegistryApiTerraformTypesFindProviderPackageResponse
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
    api_instance = env0_client.ProviderRegistryApi(api_client)
    namespace = 'namespace_example' # str | 
    type = 'type_example' # str | 
    version = 'version_example' # str | 
    os = 'os_example' # str | 
    architecture = 'architecture_example' # str | 

    try:
        # Get a download url for a specific version
        api_response = api_instance.provider_registry_download_version(namespace, type, version, os, architecture)
        print("The response of ProviderRegistryApi->provider_registry_download_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderRegistryApi->provider_registry_download_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **type** | **str**|  | 
 **version** | **str**|  | 
 **os** | **str**|  | 
 **architecture** | **str**|  | 

### Return type

[**ProviderRegistryApiTerraformTypesFindProviderPackageResponse**](ProviderRegistryApiTerraformTypesFindProviderPackageResponse.md)

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

# **provider_registry_find_gpg_keys_by_organization**
> List[ProviderRegistryApiFindGpgKeysByOrganizationResponseInner] provider_registry_find_gpg_keys_by_organization(organization_id)

List all available GPG keys

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.provider_registry_api_find_gpg_keys_by_organization_response_inner import ProviderRegistryApiFindGpgKeysByOrganizationResponseInner
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
    api_instance = env0_client.ProviderRegistryApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # List all available GPG keys
        api_response = api_instance.provider_registry_find_gpg_keys_by_organization(organization_id)
        print("The response of ProviderRegistryApi->provider_registry_find_gpg_keys_by_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderRegistryApi->provider_registry_find_gpg_keys_by_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**List[ProviderRegistryApiFindGpgKeysByOrganizationResponseInner]**](ProviderRegistryApiFindGpgKeysByOrganizationResponseInner.md)

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

# **provider_registry_find_provider_by_id**
> ProviderRegistryApiProviderWithVersions provider_registry_find_provider_by_id(provider_id)

Find a provider by id

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.provider_registry_api_provider_with_versions import ProviderRegistryApiProviderWithVersions
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
    api_instance = env0_client.ProviderRegistryApi(api_client)
    provider_id = 'provider_id_example' # str | 

    try:
        # Find a provider by id
        api_response = api_instance.provider_registry_find_provider_by_id(provider_id)
        print("The response of ProviderRegistryApi->provider_registry_find_provider_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderRegistryApi->provider_registry_find_provider_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 

### Return type

[**ProviderRegistryApiProviderWithVersions**](ProviderRegistryApiProviderWithVersions.md)

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

# **provider_registry_find_provider_by_type**
> ProviderRegistryApiTerraformTypesProviderVersions provider_registry_find_provider_by_type(namespace, type)

Find a provider by type

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.provider_registry_api_terraform_types_provider_versions import ProviderRegistryApiTerraformTypesProviderVersions
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
    api_instance = env0_client.ProviderRegistryApi(api_client)
    namespace = 'namespace_example' # str | 
    type = 'type_example' # str | 

    try:
        # Find a provider by type
        api_response = api_instance.provider_registry_find_provider_by_type(namespace, type)
        print("The response of ProviderRegistryApi->provider_registry_find_provider_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderRegistryApi->provider_registry_find_provider_by_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **type** | **str**|  | 

### Return type

[**ProviderRegistryApiTerraformTypesProviderVersions**](ProviderRegistryApiTerraformTypesProviderVersions.md)

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

# **provider_registry_find_providers_by_organization_id**
> List[ProviderRegistryApiProvider] provider_registry_find_providers_by_organization_id(organization_id)

Find all providers in an organization

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.provider_registry_api_provider import ProviderRegistryApiProvider
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
    api_instance = env0_client.ProviderRegistryApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # Find all providers in an organization
        api_response = api_instance.provider_registry_find_providers_by_organization_id(organization_id)
        print("The response of ProviderRegistryApi->provider_registry_find_providers_by_organization_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderRegistryApi->provider_registry_find_providers_by_organization_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**List[ProviderRegistryApiProvider]**](ProviderRegistryApiProvider.md)

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

# **provider_registry_update_provider**
> ProviderRegistryApiProvider provider_registry_update_provider(provider_id, provider_registry_api_update_provider_request_body=provider_registry_api_update_provider_request_body)

Update a provider

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.provider_registry_api_provider import ProviderRegistryApiProvider
from env0_client.models.provider_registry_api_update_provider_request_body import ProviderRegistryApiUpdateProviderRequestBody
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
    api_instance = env0_client.ProviderRegistryApi(api_client)
    provider_id = 'provider_id_example' # str | 
    provider_registry_api_update_provider_request_body = env0_client.ProviderRegistryApiUpdateProviderRequestBody() # ProviderRegistryApiUpdateProviderRequestBody |  (optional)

    try:
        # Update a provider
        api_response = api_instance.provider_registry_update_provider(provider_id, provider_registry_api_update_provider_request_body=provider_registry_api_update_provider_request_body)
        print("The response of ProviderRegistryApi->provider_registry_update_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderRegistryApi->provider_registry_update_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **provider_registry_api_update_provider_request_body** | [**ProviderRegistryApiUpdateProviderRequestBody**](ProviderRegistryApiUpdateProviderRequestBody.md)|  | [optional] 

### Return type

[**ProviderRegistryApiProvider**](ProviderRegistryApiProvider.md)

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

