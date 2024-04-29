# env0_client.DeploymentLogsApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deployment_logs_find_by_deployment_log_id**](DeploymentLogsApi.md#deployment_logs_find_by_deployment_log_id) | **GET** /deployments/{deploymentLogId}/steps | Find all steps by Deployment Id
[**deployment_logs_find_step_log**](DeploymentLogsApi.md#deployment_logs_find_step_log) | **GET** /deployments/{deploymentLogId}/steps/{name}/log | Get logs for specific step


# **deployment_logs_find_by_deployment_log_id**
> List[DeploymentStepApiFindByDeploymentLogIdResponseInner] deployment_logs_find_by_deployment_log_id(deployment_log_id)

Find all steps by Deployment Id

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.deployment_step_api_find_by_deployment_log_id_response_inner import DeploymentStepApiFindByDeploymentLogIdResponseInner
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
    api_instance = env0_client.DeploymentLogsApi(api_client)
    deployment_log_id = 'deployment_log_id_example' # str | 

    try:
        # Find all steps by Deployment Id
        api_response = api_instance.deployment_logs_find_by_deployment_log_id(deployment_log_id)
        print("The response of DeploymentLogsApi->deployment_logs_find_by_deployment_log_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentLogsApi->deployment_logs_find_by_deployment_log_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_log_id** | **str**|  | 

### Return type

[**List[DeploymentStepApiFindByDeploymentLogIdResponseInner]**](DeploymentStepApiFindByDeploymentLogIdResponseInner.md)

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

# **deployment_logs_find_step_log**
> DeploymentStepApiFindStepLogResponse deployment_logs_find_step_log(name, deployment_log_id)

Get logs for specific step

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.deployment_step_api_find_step_log_response import DeploymentStepApiFindStepLogResponse
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
    api_instance = env0_client.DeploymentLogsApi(api_client)
    name = 'name_example' # str | In order to fetch the available step names first use deployments/{deploymentLogId}/steps end point
    deployment_log_id = 'deployment_log_id_example' # str | 

    try:
        # Get logs for specific step
        api_response = api_instance.deployment_logs_find_step_log(name, deployment_log_id)
        print("The response of DeploymentLogsApi->deployment_logs_find_step_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentLogsApi->deployment_logs_find_step_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| In order to fetch the available step names first use deployments/{deploymentLogId}/steps end point | 
 **deployment_log_id** | **str**|  | 

### Return type

[**DeploymentStepApiFindStepLogResponse**](DeploymentStepApiFindStepLogResponse.md)

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

