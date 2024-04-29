# env0_client.DashboardApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboard_query**](DashboardApi.md#dashboard_query) | **GET** /dashboards | Get query result


# **dashboard_query**
> DashboardApiQueryResponse dashboard_query(query_name, organization_id)

Get query result

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.dashboard_api_query_response import DashboardApiQueryResponse
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
    api_instance = env0_client.DashboardApi(api_client)
    query_name = 'query_name_example' # str | the query to trigger
    organization_id = 'organization_id_example' # str | 

    try:
        # Get query result
        api_response = api_instance.dashboard_query(query_name, organization_id)
        print("The response of DashboardApi->dashboard_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->dashboard_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_name** | **str**| the query to trigger | 
 **organization_id** | **str**|  | 

### Return type

[**DashboardApiQueryResponse**](DashboardApiQueryResponse.md)

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

