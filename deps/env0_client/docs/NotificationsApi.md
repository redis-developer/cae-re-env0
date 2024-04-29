# env0_client.NotificationsApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notifications_create_notification_endpoint**](NotificationsApi.md#notifications_create_notification_endpoint) | **POST** /notifications/endpoints | Create Notification Endpoint
[**notifications_delete_notification_endpoint**](NotificationsApi.md#notifications_delete_notification_endpoint) | **DELETE** /notifications/endpoints/{endpointId} | Delete Notification Endpoint
[**notifications_find_notification_endpoints**](NotificationsApi.md#notifications_find_notification_endpoints) | **GET** /notifications/endpoints | List Notification Endpoints
[**notifications_find_project_notification_settings**](NotificationsApi.md#notifications_find_project_notification_settings) | **GET** /notifications/projects/{projectId} | Get Notification Endpoint settings
[**notifications_update_notification_endpoint**](NotificationsApi.md#notifications_update_notification_endpoint) | **PATCH** /notifications/endpoints/{endpointId} | Update Notification Endpoint
[**notifications_update_project_notification_settings**](NotificationsApi.md#notifications_update_project_notification_settings) | **PUT** /notifications/projects/{projectId}/endpoints/{endpointId} | Update Notification Settings


# **notifications_create_notification_endpoint**
> NotificationsApiNotificationEndpoint notifications_create_notification_endpoint(notifications_api_notification_endpoint_model=notifications_api_notification_endpoint_model)

Create Notification Endpoint

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.notifications_api_notification_endpoint import NotificationsApiNotificationEndpoint
from env0_client.models.notifications_api_notification_endpoint_model import NotificationsApiNotificationEndpointModel
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
    api_instance = env0_client.NotificationsApi(api_client)
    notifications_api_notification_endpoint_model = env0_client.NotificationsApiNotificationEndpointModel() # NotificationsApiNotificationEndpointModel |  (optional)

    try:
        # Create Notification Endpoint
        api_response = api_instance.notifications_create_notification_endpoint(notifications_api_notification_endpoint_model=notifications_api_notification_endpoint_model)
        print("The response of NotificationsApi->notifications_create_notification_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->notifications_create_notification_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notifications_api_notification_endpoint_model** | [**NotificationsApiNotificationEndpointModel**](NotificationsApiNotificationEndpointModel.md)|  | [optional] 

### Return type

[**NotificationsApiNotificationEndpoint**](NotificationsApiNotificationEndpoint.md)

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

# **notifications_delete_notification_endpoint**
> notifications_delete_notification_endpoint(endpoint_id)

Delete Notification Endpoint

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
    api_instance = env0_client.NotificationsApi(api_client)
    endpoint_id = 'endpoint_id_example' # str | 

    try:
        # Delete Notification Endpoint
        api_instance.notifications_delete_notification_endpoint(endpoint_id)
    except Exception as e:
        print("Exception when calling NotificationsApi->notifications_delete_notification_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **str**|  | 

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

# **notifications_find_notification_endpoints**
> List[NotificationsApiNotificationEndpoint] notifications_find_notification_endpoints(organization_id)

List Notification Endpoints

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.notifications_api_notification_endpoint import NotificationsApiNotificationEndpoint
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
    api_instance = env0_client.NotificationsApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # List Notification Endpoints
        api_response = api_instance.notifications_find_notification_endpoints(organization_id)
        print("The response of NotificationsApi->notifications_find_notification_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->notifications_find_notification_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**List[NotificationsApiNotificationEndpoint]**](NotificationsApiNotificationEndpoint.md)

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

# **notifications_find_project_notification_settings**
> List[NotificationsApiProjectNotificationSetting] notifications_find_project_notification_settings(project_id)

Get Notification Endpoint settings

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.notifications_api_project_notification_setting import NotificationsApiProjectNotificationSetting
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
    api_instance = env0_client.NotificationsApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Get Notification Endpoint settings
        api_response = api_instance.notifications_find_project_notification_settings(project_id)
        print("The response of NotificationsApi->notifications_find_project_notification_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->notifications_find_project_notification_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**List[NotificationsApiProjectNotificationSetting]**](NotificationsApiProjectNotificationSetting.md)

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

# **notifications_update_notification_endpoint**
> NotificationsApiNotificationEndpoint notifications_update_notification_endpoint(endpoint_id, notifications_api_update_notification_endpoint_request_body=notifications_api_update_notification_endpoint_request_body)

Update Notification Endpoint

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.notifications_api_notification_endpoint import NotificationsApiNotificationEndpoint
from env0_client.models.notifications_api_update_notification_endpoint_request_body import NotificationsApiUpdateNotificationEndpointRequestBody
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
    api_instance = env0_client.NotificationsApi(api_client)
    endpoint_id = 'endpoint_id_example' # str | 
    notifications_api_update_notification_endpoint_request_body = env0_client.NotificationsApiUpdateNotificationEndpointRequestBody() # NotificationsApiUpdateNotificationEndpointRequestBody |  (optional)

    try:
        # Update Notification Endpoint
        api_response = api_instance.notifications_update_notification_endpoint(endpoint_id, notifications_api_update_notification_endpoint_request_body=notifications_api_update_notification_endpoint_request_body)
        print("The response of NotificationsApi->notifications_update_notification_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->notifications_update_notification_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **str**|  | 
 **notifications_api_update_notification_endpoint_request_body** | [**NotificationsApiUpdateNotificationEndpointRequestBody**](NotificationsApiUpdateNotificationEndpointRequestBody.md)|  | [optional] 

### Return type

[**NotificationsApiNotificationEndpoint**](NotificationsApiNotificationEndpoint.md)

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

# **notifications_update_project_notification_settings**
> NotificationsApiProjectNotificationSetting notifications_update_project_notification_settings(project_id, endpoint_id, notifications_api_update_project_notification_settings_request_body=notifications_api_update_project_notification_settings_request_body)

Update Notification Settings

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.notifications_api_project_notification_setting import NotificationsApiProjectNotificationSetting
from env0_client.models.notifications_api_update_project_notification_settings_request_body import NotificationsApiUpdateProjectNotificationSettingsRequestBody
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
    api_instance = env0_client.NotificationsApi(api_client)
    project_id = 'project_id_example' # str | 
    endpoint_id = 'endpoint_id_example' # str | 
    notifications_api_update_project_notification_settings_request_body = env0_client.NotificationsApiUpdateProjectNotificationSettingsRequestBody() # NotificationsApiUpdateProjectNotificationSettingsRequestBody |  (optional)

    try:
        # Update Notification Settings
        api_response = api_instance.notifications_update_project_notification_settings(project_id, endpoint_id, notifications_api_update_project_notification_settings_request_body=notifications_api_update_project_notification_settings_request_body)
        print("The response of NotificationsApi->notifications_update_project_notification_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->notifications_update_project_notification_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **endpoint_id** | **str**|  | 
 **notifications_api_update_project_notification_settings_request_body** | [**NotificationsApiUpdateProjectNotificationSettingsRequestBody**](NotificationsApiUpdateProjectNotificationSettingsRequestBody.md)|  | [optional] 

### Return type

[**NotificationsApiProjectNotificationSetting**](NotificationsApiProjectNotificationSetting.md)

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

