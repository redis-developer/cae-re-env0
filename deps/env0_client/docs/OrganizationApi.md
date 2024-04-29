# env0_client.OrganizationApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_create_invite**](OrganizationApi.md#organization_create_invite) | **POST** /invites | Invite User
[**organization_create_organization**](OrganizationApi.md#organization_create_organization) | **POST** /organizations | Create a new Organization
[**organization_find_organization_by_id**](OrganizationApi.md#organization_find_organization_by_id) | **GET** /organizations/{id} | Get Organization
[**organization_find_organizations**](OrganizationApi.md#organization_find_organizations) | **GET** /organizations | List Organizations
[**organization_get_organization_limits**](OrganizationApi.md#organization_get_organization_limits) | **GET** /organizations/{id}/limits | Get Organization Limits
[**organization_get_users**](OrganizationApi.md#organization_get_users) | **GET** /organizations/{id}/users | List Users
[**organization_remove_user_from_organization**](OrganizationApi.md#organization_remove_user_from_organization) | **DELETE** /organizations/{id}/users/{userId} | Remove User
[**organization_update_organization**](OrganizationApi.md#organization_update_organization) | **PUT** /organizations/{id} | Update Organization
[**organization_update_policy**](OrganizationApi.md#organization_update_policy) | **POST** /organizations/{id}/policies | Update Policy
[**organization_update_role**](OrganizationApi.md#organization_update_role) | **PUT** /organizations/{id}/users/{userId}/role | Update User&#39;s Organization Role Assignment


# **organization_create_invite**
> OrganizationApiCreateInviteResponse organization_create_invite(organization_api_create_invite_request_body=organization_api_create_invite_request_body)

Invite User

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.organization_api_create_invite_request_body import OrganizationApiCreateInviteRequestBody
from env0_client.models.organization_api_create_invite_response import OrganizationApiCreateInviteResponse
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
    api_instance = env0_client.OrganizationApi(api_client)
    organization_api_create_invite_request_body = env0_client.OrganizationApiCreateInviteRequestBody() # OrganizationApiCreateInviteRequestBody |  (optional)

    try:
        # Invite User
        api_response = api_instance.organization_create_invite(organization_api_create_invite_request_body=organization_api_create_invite_request_body)
        print("The response of OrganizationApi->organization_create_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_create_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_api_create_invite_request_body** | [**OrganizationApiCreateInviteRequestBody**](OrganizationApiCreateInviteRequestBody.md)|  | [optional] 

### Return type

[**OrganizationApiCreateInviteResponse**](OrganizationApiCreateInviteResponse.md)

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

# **organization_create_organization**
> OrganizationApiOrganizationModel organization_create_organization(organization_api_create_organization_request_body=organization_api_create_organization_request_body)

Create a new Organization

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.organization_api_create_organization_request_body import OrganizationApiCreateOrganizationRequestBody
from env0_client.models.organization_api_organization_model import OrganizationApiOrganizationModel
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
    api_instance = env0_client.OrganizationApi(api_client)
    organization_api_create_organization_request_body = env0_client.OrganizationApiCreateOrganizationRequestBody() # OrganizationApiCreateOrganizationRequestBody |  (optional)

    try:
        # Create a new Organization
        api_response = api_instance.organization_create_organization(organization_api_create_organization_request_body=organization_api_create_organization_request_body)
        print("The response of OrganizationApi->organization_create_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_create_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_api_create_organization_request_body** | [**OrganizationApiCreateOrganizationRequestBody**](OrganizationApiCreateOrganizationRequestBody.md)|  | [optional] 

### Return type

[**OrganizationApiOrganizationModel**](OrganizationApiOrganizationModel.md)

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

# **organization_find_organization_by_id**
> OrganizationApiOrganization organization_find_organization_by_id(id)

Get Organization

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.organization_api_organization import OrganizationApiOrganization
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
    api_instance = env0_client.OrganizationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Organization
        api_response = api_instance.organization_find_organization_by_id(id)
        print("The response of OrganizationApi->organization_find_organization_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_find_organization_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OrganizationApiOrganization**](OrganizationApiOrganization.md)

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

# **organization_find_organizations**
> List[OrganizationApiOrganization] organization_find_organizations()

List Organizations

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.organization_api_organization import OrganizationApiOrganization
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
    api_instance = env0_client.OrganizationApi(api_client)

    try:
        # List Organizations
        api_response = api_instance.organization_find_organizations()
        print("The response of OrganizationApi->organization_find_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_find_organizations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OrganizationApiOrganization]**](OrganizationApiOrganization.md)

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

# **organization_get_organization_limits**
> OrganizationApiOrganizationLimits organization_get_organization_limits(id)

Get Organization Limits

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.organization_api_organization_limits import OrganizationApiOrganizationLimits
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
    api_instance = env0_client.OrganizationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Organization Limits
        api_response = api_instance.organization_get_organization_limits(id)
        print("The response of OrganizationApi->organization_get_organization_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_get_organization_limits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OrganizationApiOrganizationLimits**](OrganizationApiOrganizationLimits.md)

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

# **organization_get_users**
> List[OrganizationUser] organization_get_users(id, include_api_keys=include_api_keys, query=query)

List Users

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.organization_user import OrganizationUser
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
    api_instance = env0_client.OrganizationApi(api_client)
    id = 'id_example' # str | 
    include_api_keys = 'include_api_keys_example' # str |  (optional)
    query = 'query_example' # str |  (optional)

    try:
        # List Users
        api_response = api_instance.organization_get_users(id, include_api_keys=include_api_keys, query=query)
        print("The response of OrganizationApi->organization_get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **include_api_keys** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 

### Return type

[**List[OrganizationUser]**](OrganizationUser.md)

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

# **organization_remove_user_from_organization**
> organization_remove_user_from_organization(id, user_id)

Remove User

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
    api_instance = env0_client.OrganizationApi(api_client)
    id = 'id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Remove User
        api_instance.organization_remove_user_from_organization(id, user_id)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_remove_user_from_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **organization_update_organization**
> OrganizationApiOrganization organization_update_organization(id, organization_api_update_organization_request_body=organization_api_update_organization_request_body)

Update Organization

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.organization_api_organization import OrganizationApiOrganization
from env0_client.models.organization_api_update_organization_request_body import OrganizationApiUpdateOrganizationRequestBody
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
    api_instance = env0_client.OrganizationApi(api_client)
    id = 'id_example' # str | 
    organization_api_update_organization_request_body = env0_client.OrganizationApiUpdateOrganizationRequestBody() # OrganizationApiUpdateOrganizationRequestBody |  (optional)

    try:
        # Update Organization
        api_response = api_instance.organization_update_organization(id, organization_api_update_organization_request_body=organization_api_update_organization_request_body)
        print("The response of OrganizationApi->organization_update_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_update_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **organization_api_update_organization_request_body** | [**OrganizationApiUpdateOrganizationRequestBody**](OrganizationApiUpdateOrganizationRequestBody.md)|  | [optional] 

### Return type

[**OrganizationApiOrganization**](OrganizationApiOrganization.md)

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

# **organization_update_policy**
> OrganizationApiOrganization organization_update_policy(id, organization_api_organization_policy=organization_api_organization_policy)

Update Policy

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.organization_api_organization import OrganizationApiOrganization
from env0_client.models.organization_api_organization_policy import OrganizationApiOrganizationPolicy
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
    api_instance = env0_client.OrganizationApi(api_client)
    id = 'id_example' # str | 
    organization_api_organization_policy = env0_client.OrganizationApiOrganizationPolicy() # OrganizationApiOrganizationPolicy |  (optional)

    try:
        # Update Policy
        api_response = api_instance.organization_update_policy(id, organization_api_organization_policy=organization_api_organization_policy)
        print("The response of OrganizationApi->organization_update_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_update_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **organization_api_organization_policy** | [**OrganizationApiOrganizationPolicy**](OrganizationApiOrganizationPolicy.md)|  | [optional] 

### Return type

[**OrganizationApiOrganization**](OrganizationApiOrganization.md)

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

# **organization_update_role**
> object organization_update_role(id, user_id, body=body)

Update User's Organization Role Assignment

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
    api_instance = env0_client.OrganizationApi(api_client)
    id = 'id_example' # str | 
    user_id = 'user_id_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update User's Organization Role Assignment
        api_response = api_instance.organization_update_role(id, user_id, body=body)
        print("The response of OrganizationApi->organization_update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_update_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_id** | **str**|  | 
 **body** | **str**|  | [optional] 

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

