# env0_client.UsersApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_create_vcs_provider_user_mapping**](UsersApi.md#users_create_vcs_provider_user_mapping) | **POST** /users/me/vcs-provider-user-mappings | Create VCS Provider User Mapping
[**users_get_vcs_provider_user_mappings**](UsersApi.md#users_get_vcs_provider_user_mappings) | **GET** /users/me/vcs-provider-user-mappings | List User&#39;s VCS ID Mappings
[**users_update_vcs_provider_user_mappings**](UsersApi.md#users_update_vcs_provider_user_mappings) | **PUT** /vcs-provider-user-mappings/{mappingId} | Update a User&#39;s VCS ID Mapping


# **users_create_vcs_provider_user_mapping**
> AccountApiVcsProviderUserMapping users_create_vcs_provider_user_mapping(account_api_create_vcs_provider_user_mapping_request_body=account_api_create_vcs_provider_user_mapping_request_body)

Create VCS Provider User Mapping

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.account_api_create_vcs_provider_user_mapping_request_body import AccountApiCreateVcsProviderUserMappingRequestBody
from env0_client.models.account_api_vcs_provider_user_mapping import AccountApiVcsProviderUserMapping
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
    api_instance = env0_client.UsersApi(api_client)
    account_api_create_vcs_provider_user_mapping_request_body = env0_client.AccountApiCreateVcsProviderUserMappingRequestBody() # AccountApiCreateVcsProviderUserMappingRequestBody |  (optional)

    try:
        # Create VCS Provider User Mapping
        api_response = api_instance.users_create_vcs_provider_user_mapping(account_api_create_vcs_provider_user_mapping_request_body=account_api_create_vcs_provider_user_mapping_request_body)
        print("The response of UsersApi->users_create_vcs_provider_user_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_create_vcs_provider_user_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_api_create_vcs_provider_user_mapping_request_body** | [**AccountApiCreateVcsProviderUserMappingRequestBody**](AccountApiCreateVcsProviderUserMappingRequestBody.md)|  | [optional] 

### Return type

[**AccountApiVcsProviderUserMapping**](AccountApiVcsProviderUserMapping.md)

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

# **users_get_vcs_provider_user_mappings**
> List[AccountApiVcsProviderUserMapping] users_get_vcs_provider_user_mappings()

List User's VCS ID Mappings

Returns the user's account ids for all mapped vcs-es.

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.account_api_vcs_provider_user_mapping import AccountApiVcsProviderUserMapping
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
    api_instance = env0_client.UsersApi(api_client)

    try:
        # List User's VCS ID Mappings
        api_response = api_instance.users_get_vcs_provider_user_mappings()
        print("The response of UsersApi->users_get_vcs_provider_user_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_vcs_provider_user_mappings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AccountApiVcsProviderUserMapping]**](AccountApiVcsProviderUserMapping.md)

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

# **users_update_vcs_provider_user_mappings**
> AccountApiVcsProviderUserMapping users_update_vcs_provider_user_mappings(mapping_id, account_api_update_vcs_provider_user_mappings_request_body=account_api_update_vcs_provider_user_mappings_request_body)

Update a User's VCS ID Mapping

Updates a user's VCS ID mapping, and returns the updated value.

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.account_api_update_vcs_provider_user_mappings_request_body import AccountApiUpdateVcsProviderUserMappingsRequestBody
from env0_client.models.account_api_vcs_provider_user_mapping import AccountApiVcsProviderUserMapping
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
    api_instance = env0_client.UsersApi(api_client)
    mapping_id = 'mapping_id_example' # str | 
    account_api_update_vcs_provider_user_mappings_request_body = env0_client.AccountApiUpdateVcsProviderUserMappingsRequestBody() # AccountApiUpdateVcsProviderUserMappingsRequestBody |  (optional)

    try:
        # Update a User's VCS ID Mapping
        api_response = api_instance.users_update_vcs_provider_user_mappings(mapping_id, account_api_update_vcs_provider_user_mappings_request_body=account_api_update_vcs_provider_user_mappings_request_body)
        print("The response of UsersApi->users_update_vcs_provider_user_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_update_vcs_provider_user_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **str**|  | 
 **account_api_update_vcs_provider_user_mappings_request_body** | [**AccountApiUpdateVcsProviderUserMappingsRequestBody**](AccountApiUpdateVcsProviderUserMappingsRequestBody.md)|  | [optional] 

### Return type

[**AccountApiVcsProviderUserMapping**](AccountApiVcsProviderUserMapping.md)

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

