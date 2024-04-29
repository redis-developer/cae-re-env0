# env0_client.CustomFlowApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**templates_assign_custom_flow**](CustomFlowApi.md#templates_assign_custom_flow) | **POST** /custom-flow/assign | Assign Custom Flow
[**templates_create_custom_flow**](CustomFlowApi.md#templates_create_custom_flow) | **POST** /custom-flow | Create Custom Flow
[**templates_delete_custom_flow**](CustomFlowApi.md#templates_delete_custom_flow) | **DELETE** /custom-flow/{id} | Delete Custom Flow
[**templates_find_custom_flows**](CustomFlowApi.md#templates_find_custom_flows) | **GET** /custom-flows | Find Custom Flows
[**templates_get_custom_flow_assignments**](CustomFlowApi.md#templates_get_custom_flow_assignments) | **POST** /custom-flow/get-assignments | Get Custom Flow Assignments
[**templates_unassign_custom_flow**](CustomFlowApi.md#templates_unassign_custom_flow) | **POST** /custom-flow/unassign | Unassign Custom Flow
[**templates_update_custom_flow**](CustomFlowApi.md#templates_update_custom_flow) | **PUT** /custom-flow | Update Custom Flow


# **templates_assign_custom_flow**
> object templates_assign_custom_flow(blueprint_api_custom_flow_assignment_request=blueprint_api_custom_flow_assignment_request)

Assign Custom Flow

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_custom_flow_assignment_request import BlueprintApiCustomFlowAssignmentRequest
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
    api_instance = env0_client.CustomFlowApi(api_client)
    blueprint_api_custom_flow_assignment_request = [env0_client.BlueprintApiCustomFlowAssignmentRequest()] # List[BlueprintApiCustomFlowAssignmentRequest] |  (optional)

    try:
        # Assign Custom Flow
        api_response = api_instance.templates_assign_custom_flow(blueprint_api_custom_flow_assignment_request=blueprint_api_custom_flow_assignment_request)
        print("The response of CustomFlowApi->templates_assign_custom_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFlowApi->templates_assign_custom_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_api_custom_flow_assignment_request** | [**List[BlueprintApiCustomFlowAssignmentRequest]**](BlueprintApiCustomFlowAssignmentRequest.md)|  | [optional] 

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

# **templates_create_custom_flow**
> BlueprintApiCustomFlowTemplate templates_create_custom_flow(blueprint_api_create_configuration_template=blueprint_api_create_configuration_template)

Create Custom Flow

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_create_configuration_template import BlueprintApiCreateConfigurationTemplate
from env0_client.models.blueprint_api_custom_flow_template import BlueprintApiCustomFlowTemplate
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
    api_instance = env0_client.CustomFlowApi(api_client)
    blueprint_api_create_configuration_template = env0_client.BlueprintApiCreateConfigurationTemplate() # BlueprintApiCreateConfigurationTemplate |  (optional)

    try:
        # Create Custom Flow
        api_response = api_instance.templates_create_custom_flow(blueprint_api_create_configuration_template=blueprint_api_create_configuration_template)
        print("The response of CustomFlowApi->templates_create_custom_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFlowApi->templates_create_custom_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_api_create_configuration_template** | [**BlueprintApiCreateConfigurationTemplate**](BlueprintApiCreateConfigurationTemplate.md)|  | [optional] 

### Return type

[**BlueprintApiCustomFlowTemplate**](BlueprintApiCustomFlowTemplate.md)

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

# **templates_delete_custom_flow**
> templates_delete_custom_flow(id)

Delete Custom Flow

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
    api_instance = env0_client.CustomFlowApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Custom Flow
        api_instance.templates_delete_custom_flow(id)
    except Exception as e:
        print("Exception when calling CustomFlowApi->templates_delete_custom_flow: %s\n" % e)
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

# **templates_find_custom_flows**
> List[BlueprintApiCustomFlowTemplate] templates_find_custom_flows(organization_id, name)

Find Custom Flows

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_custom_flow_template import BlueprintApiCustomFlowTemplate
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
    api_instance = env0_client.CustomFlowApi(api_client)
    organization_id = 'organization_id_example' # str | 
    name = 'name_example' # str | 

    try:
        # Find Custom Flows
        api_response = api_instance.templates_find_custom_flows(organization_id, name)
        print("The response of CustomFlowApi->templates_find_custom_flows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFlowApi->templates_find_custom_flows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**List[BlueprintApiCustomFlowTemplate]**](BlueprintApiCustomFlowTemplate.md)

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

# **templates_get_custom_flow_assignments**
> List[BlueprintApiRichCustomFlowAssigment] templates_get_custom_flow_assignments(blueprint_api_get_custom_flow_assignments_request_body_inner=blueprint_api_get_custom_flow_assignments_request_body_inner)

Get Custom Flow Assignments

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_get_custom_flow_assignments_request_body_inner import BlueprintApiGetCustomFlowAssignmentsRequestBodyInner
from env0_client.models.blueprint_api_rich_custom_flow_assigment import BlueprintApiRichCustomFlowAssigment
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
    api_instance = env0_client.CustomFlowApi(api_client)
    blueprint_api_get_custom_flow_assignments_request_body_inner = [env0_client.BlueprintApiGetCustomFlowAssignmentsRequestBodyInner()] # List[BlueprintApiGetCustomFlowAssignmentsRequestBodyInner] |  (optional)

    try:
        # Get Custom Flow Assignments
        api_response = api_instance.templates_get_custom_flow_assignments(blueprint_api_get_custom_flow_assignments_request_body_inner=blueprint_api_get_custom_flow_assignments_request_body_inner)
        print("The response of CustomFlowApi->templates_get_custom_flow_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFlowApi->templates_get_custom_flow_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_api_get_custom_flow_assignments_request_body_inner** | [**List[BlueprintApiGetCustomFlowAssignmentsRequestBodyInner]**](BlueprintApiGetCustomFlowAssignmentsRequestBodyInner.md)|  | [optional] 

### Return type

[**List[BlueprintApiRichCustomFlowAssigment]**](BlueprintApiRichCustomFlowAssigment.md)

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

# **templates_unassign_custom_flow**
> object templates_unassign_custom_flow(blueprint_api_custom_flow_assignment_request=blueprint_api_custom_flow_assignment_request)

Unassign Custom Flow

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_custom_flow_assignment_request import BlueprintApiCustomFlowAssignmentRequest
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
    api_instance = env0_client.CustomFlowApi(api_client)
    blueprint_api_custom_flow_assignment_request = [env0_client.BlueprintApiCustomFlowAssignmentRequest()] # List[BlueprintApiCustomFlowAssignmentRequest] |  (optional)

    try:
        # Unassign Custom Flow
        api_response = api_instance.templates_unassign_custom_flow(blueprint_api_custom_flow_assignment_request=blueprint_api_custom_flow_assignment_request)
        print("The response of CustomFlowApi->templates_unassign_custom_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFlowApi->templates_unassign_custom_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_api_custom_flow_assignment_request** | [**List[BlueprintApiCustomFlowAssignmentRequest]**](BlueprintApiCustomFlowAssignmentRequest.md)|  | [optional] 

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

# **templates_update_custom_flow**
> BlueprintApiCustomFlowTemplate templates_update_custom_flow(blueprint_api_update_configuration_template_body=blueprint_api_update_configuration_template_body)

Update Custom Flow

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_custom_flow_template import BlueprintApiCustomFlowTemplate
from env0_client.models.blueprint_api_update_configuration_template_body import BlueprintApiUpdateConfigurationTemplateBody
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
    api_instance = env0_client.CustomFlowApi(api_client)
    blueprint_api_update_configuration_template_body = env0_client.BlueprintApiUpdateConfigurationTemplateBody() # BlueprintApiUpdateConfigurationTemplateBody |  (optional)

    try:
        # Update Custom Flow
        api_response = api_instance.templates_update_custom_flow(blueprint_api_update_configuration_template_body=blueprint_api_update_configuration_template_body)
        print("The response of CustomFlowApi->templates_update_custom_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFlowApi->templates_update_custom_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_api_update_configuration_template_body** | [**BlueprintApiUpdateConfigurationTemplateBody**](BlueprintApiUpdateConfigurationTemplateBody.md)|  | [optional] 

### Return type

[**BlueprintApiCustomFlowTemplate**](BlueprintApiCustomFlowTemplate.md)

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

