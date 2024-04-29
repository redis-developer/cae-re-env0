# env0_client.AuditEventsApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audit_events_fetch_audit_logs**](AuditEventsApi.md#audit_events_fetch_audit_logs) | **GET** /audit/events | Fetch Audit Logs


# **audit_events_fetch_audit_logs**
> AuditEventApiFetchAuditLogsResponse audit_events_fetch_audit_logs(organization_id, limit=limit, offset=offset, var_from=var_from, to=to)

Fetch Audit Logs

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.audit_event_api_fetch_audit_logs_response import AuditEventApiFetchAuditLogsResponse
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
    api_instance = env0_client.AuditEventsApi(api_client)
    organization_id = 'organization_id_example' # str | 
    limit = 'limit_example' # str | Number of audit logs per page. The maximum is 1000, the default is 50 (optional)
    offset = 'offset_example' # str | An audit log's id from which the page will start (optional)
    var_from = 'var_from_example' # str |  (optional)
    to = 'to_example' # str |  (optional)

    try:
        # Fetch Audit Logs
        api_response = api_instance.audit_events_fetch_audit_logs(organization_id, limit=limit, offset=offset, var_from=var_from, to=to)
        print("The response of AuditEventsApi->audit_events_fetch_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditEventsApi->audit_events_fetch_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **limit** | **str**| Number of audit logs per page. The maximum is 1000, the default is 50 | [optional] 
 **offset** | **str**| An audit log&#39;s id from which the page will start | [optional] 
 **var_from** | **str**|  | [optional] 
 **to** | **str**|  | [optional] 

### Return type

[**AuditEventApiFetchAuditLogsResponse**](AuditEventApiFetchAuditLogsResponse.md)

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

