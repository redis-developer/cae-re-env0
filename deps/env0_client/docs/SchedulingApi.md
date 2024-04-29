# env0_client.SchedulingApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scheduling_get_drift_detection_by_environment_id**](SchedulingApi.md#scheduling_get_drift_detection_by_environment_id) | **GET** /scheduling/drift-detection/environments/{id} | Get Drift Detection Environment Scheduling
[**scheduling_get_schedule_by_environment_id**](SchedulingApi.md#scheduling_get_schedule_by_environment_id) | **GET** /scheduling/environments/{id} | Get Environment Scheduling
[**scheduling_get_schedule_by_project_id**](SchedulingApi.md#scheduling_get_schedule_by_project_id) | **GET** /scheduling/projects/{id} | Get Project Scheduling
[**scheduling_set_drift_detection**](SchedulingApi.md#scheduling_set_drift_detection) | **PATCH** /scheduling/drift-detection/environments/{id} | Set Drift Detection Environment Scheduling
[**scheduling_set_environment_schedule**](SchedulingApi.md#scheduling_set_environment_schedule) | **PUT** /scheduling/environments/{id} | Set Environment Scheduling


# **scheduling_get_drift_detection_by_environment_id**
> SchedulingApiScheduledAction scheduling_get_drift_detection_by_environment_id(id)

Get Drift Detection Environment Scheduling

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.scheduling_api_scheduled_action import SchedulingApiScheduledAction
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
    api_instance = env0_client.SchedulingApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Drift Detection Environment Scheduling
        api_response = api_instance.scheduling_get_drift_detection_by_environment_id(id)
        print("The response of SchedulingApi->scheduling_get_drift_detection_by_environment_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_get_drift_detection_by_environment_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SchedulingApiScheduledAction**](SchedulingApiScheduledAction.md)

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

# **scheduling_get_schedule_by_environment_id**
> SchedulingApiGetScheduleByEnvironmentIdResponse scheduling_get_schedule_by_environment_id(id)

Get Environment Scheduling

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.scheduling_api_get_schedule_by_environment_id_response import SchedulingApiGetScheduleByEnvironmentIdResponse
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
    api_instance = env0_client.SchedulingApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Environment Scheduling
        api_response = api_instance.scheduling_get_schedule_by_environment_id(id)
        print("The response of SchedulingApi->scheduling_get_schedule_by_environment_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_get_schedule_by_environment_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SchedulingApiGetScheduleByEnvironmentIdResponse**](SchedulingApiGetScheduleByEnvironmentIdResponse.md)

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

# **scheduling_get_schedule_by_project_id**
> List[SchedulingApiGetScheduleByEnvironmentIdResponse] scheduling_get_schedule_by_project_id(id)

Get Project Scheduling

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.scheduling_api_get_schedule_by_environment_id_response import SchedulingApiGetScheduleByEnvironmentIdResponse
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
    api_instance = env0_client.SchedulingApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Project Scheduling
        api_response = api_instance.scheduling_get_schedule_by_project_id(id)
        print("The response of SchedulingApi->scheduling_get_schedule_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_get_schedule_by_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[SchedulingApiGetScheduleByEnvironmentIdResponse]**](SchedulingApiGetScheduleByEnvironmentIdResponse.md)

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

# **scheduling_set_drift_detection**
> SchedulingApiScheduledAction scheduling_set_drift_detection(id, scheduling_api_set_drift_detection_request_scheduled_action=scheduling_api_set_drift_detection_request_scheduled_action)

Set Drift Detection Environment Scheduling

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.scheduling_api_scheduled_action import SchedulingApiScheduledAction
from env0_client.models.scheduling_api_set_drift_detection_request_scheduled_action import SchedulingApiSetDriftDetectionRequestScheduledAction
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
    api_instance = env0_client.SchedulingApi(api_client)
    id = 'id_example' # str | 
    scheduling_api_set_drift_detection_request_scheduled_action = env0_client.SchedulingApiSetDriftDetectionRequestScheduledAction() # SchedulingApiSetDriftDetectionRequestScheduledAction |  (optional)

    try:
        # Set Drift Detection Environment Scheduling
        api_response = api_instance.scheduling_set_drift_detection(id, scheduling_api_set_drift_detection_request_scheduled_action=scheduling_api_set_drift_detection_request_scheduled_action)
        print("The response of SchedulingApi->scheduling_set_drift_detection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_set_drift_detection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **scheduling_api_set_drift_detection_request_scheduled_action** | [**SchedulingApiSetDriftDetectionRequestScheduledAction**](SchedulingApiSetDriftDetectionRequestScheduledAction.md)|  | [optional] 

### Return type

[**SchedulingApiScheduledAction**](SchedulingApiScheduledAction.md)

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

# **scheduling_set_environment_schedule**
> SchedulingApiGetScheduleByEnvironmentIdResponse scheduling_set_environment_schedule(id, scheduling_api_set_environment_schedule_request_body=scheduling_api_set_environment_schedule_request_body)

Set Environment Scheduling

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.scheduling_api_get_schedule_by_environment_id_response import SchedulingApiGetScheduleByEnvironmentIdResponse
from env0_client.models.scheduling_api_set_environment_schedule_request_body import SchedulingApiSetEnvironmentScheduleRequestBody
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
    api_instance = env0_client.SchedulingApi(api_client)
    id = 'id_example' # str | 
    scheduling_api_set_environment_schedule_request_body = env0_client.SchedulingApiSetEnvironmentScheduleRequestBody() # SchedulingApiSetEnvironmentScheduleRequestBody |  (optional)

    try:
        # Set Environment Scheduling
        api_response = api_instance.scheduling_set_environment_schedule(id, scheduling_api_set_environment_schedule_request_body=scheduling_api_set_environment_schedule_request_body)
        print("The response of SchedulingApi->scheduling_set_environment_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_set_environment_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **scheduling_api_set_environment_schedule_request_body** | [**SchedulingApiSetEnvironmentScheduleRequestBody**](SchedulingApiSetEnvironmentScheduleRequestBody.md)|  | [optional] 

### Return type

[**SchedulingApiGetScheduleByEnvironmentIdResponse**](SchedulingApiGetScheduleByEnvironmentIdResponse.md)

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

