# env0_client.ApprovalPolicyApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**templates_assign_approval_policy**](ApprovalPolicyApi.md#templates_assign_approval_policy) | **POST** /approval-policy/assignment | Assign Approval Policy To Scope
[**templates_create_approval_policy**](ApprovalPolicyApi.md#templates_create_approval_policy) | **POST** /approval-policy | Create Approval Policy
[**templates_delete_approval_policy**](ApprovalPolicyApi.md#templates_delete_approval_policy) | **DELETE** /approval-policy/delete/{id} | Delete Approval Policy
[**templates_get_approval_policy_by_name**](ApprovalPolicyApi.md#templates_get_approval_policy_by_name) | **GET** /approval-policy | Get Approval Policy By Name
[**templates_get_approval_policy_by_scope**](ApprovalPolicyApi.md#templates_get_approval_policy_by_scope) | **GET** /approval-policy/{scope}/{scopeId} | Get Approval Policy Assignments By Scope
[**templates_unassign_approval_policy**](ApprovalPolicyApi.md#templates_unassign_approval_policy) | **DELETE** /approval-policy/assignment/{scope}/{scopeId} | Unassign Approval Policy From Scope
[**templates_unassign_approval_policy_by_id**](ApprovalPolicyApi.md#templates_unassign_approval_policy_by_id) | **DELETE** /approval-policy/assignment | Unassign Approval Policy by assignment id
[**templates_update_approval_policy**](ApprovalPolicyApi.md#templates_update_approval_policy) | **PUT** /approval-policy | Update Existing Approval Policy


# **templates_assign_approval_policy**
> BlueprintApiApprovalPolicyAssignment templates_assign_approval_policy(blueprint_api_approval_policy_assignment_request=blueprint_api_approval_policy_assignment_request)

Assign Approval Policy To Scope

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_approval_policy_assignment import BlueprintApiApprovalPolicyAssignment
from env0_client.models.blueprint_api_approval_policy_assignment_request import BlueprintApiApprovalPolicyAssignmentRequest
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
    api_instance = env0_client.ApprovalPolicyApi(api_client)
    blueprint_api_approval_policy_assignment_request = env0_client.BlueprintApiApprovalPolicyAssignmentRequest() # BlueprintApiApprovalPolicyAssignmentRequest |  (optional)

    try:
        # Assign Approval Policy To Scope
        api_response = api_instance.templates_assign_approval_policy(blueprint_api_approval_policy_assignment_request=blueprint_api_approval_policy_assignment_request)
        print("The response of ApprovalPolicyApi->templates_assign_approval_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalPolicyApi->templates_assign_approval_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_api_approval_policy_assignment_request** | [**BlueprintApiApprovalPolicyAssignmentRequest**](BlueprintApiApprovalPolicyAssignmentRequest.md)|  | [optional] 

### Return type

[**BlueprintApiApprovalPolicyAssignment**](BlueprintApiApprovalPolicyAssignment.md)

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

# **templates_create_approval_policy**
> BlueprintApiApprovalPolicyTemplate templates_create_approval_policy(blueprint_api_create_configuration_template=blueprint_api_create_configuration_template)

Create Approval Policy

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_approval_policy_template import BlueprintApiApprovalPolicyTemplate
from env0_client.models.blueprint_api_create_configuration_template import BlueprintApiCreateConfigurationTemplate
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
    api_instance = env0_client.ApprovalPolicyApi(api_client)
    blueprint_api_create_configuration_template = env0_client.BlueprintApiCreateConfigurationTemplate() # BlueprintApiCreateConfigurationTemplate |  (optional)

    try:
        # Create Approval Policy
        api_response = api_instance.templates_create_approval_policy(blueprint_api_create_configuration_template=blueprint_api_create_configuration_template)
        print("The response of ApprovalPolicyApi->templates_create_approval_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalPolicyApi->templates_create_approval_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_api_create_configuration_template** | [**BlueprintApiCreateConfigurationTemplate**](BlueprintApiCreateConfigurationTemplate.md)|  | [optional] 

### Return type

[**BlueprintApiApprovalPolicyTemplate**](BlueprintApiApprovalPolicyTemplate.md)

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

# **templates_delete_approval_policy**
> templates_delete_approval_policy(id)

Delete Approval Policy

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
    api_instance = env0_client.ApprovalPolicyApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Approval Policy
        api_instance.templates_delete_approval_policy(id)
    except Exception as e:
        print("Exception when calling ApprovalPolicyApi->templates_delete_approval_policy: %s\n" % e)
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

# **templates_get_approval_policy_by_name**
> List[BlueprintApiApprovalPolicyTemplate] templates_get_approval_policy_by_name(organization_id, name)

Get Approval Policy By Name

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_approval_policy_template import BlueprintApiApprovalPolicyTemplate
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
    api_instance = env0_client.ApprovalPolicyApi(api_client)
    organization_id = 'organization_id_example' # str | 
    name = 'name_example' # str | 

    try:
        # Get Approval Policy By Name
        api_response = api_instance.templates_get_approval_policy_by_name(organization_id, name)
        print("The response of ApprovalPolicyApi->templates_get_approval_policy_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalPolicyApi->templates_get_approval_policy_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**List[BlueprintApiApprovalPolicyTemplate]**](BlueprintApiApprovalPolicyTemplate.md)

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

# **templates_get_approval_policy_by_scope**
> List[BlueprintApiApprovalPolicyTemplateWithScope] templates_get_approval_policy_by_scope(scope, scope_id)

Get Approval Policy Assignments By Scope

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_approval_policy_template_with_scope import BlueprintApiApprovalPolicyTemplateWithScope
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
    api_instance = env0_client.ApprovalPolicyApi(api_client)
    scope = 'scope_example' # str | 
    scope_id = 'scope_id_example' # str | 

    try:
        # Get Approval Policy Assignments By Scope
        api_response = api_instance.templates_get_approval_policy_by_scope(scope, scope_id)
        print("The response of ApprovalPolicyApi->templates_get_approval_policy_by_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalPolicyApi->templates_get_approval_policy_by_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **scope_id** | **str**|  | 

### Return type

[**List[BlueprintApiApprovalPolicyTemplateWithScope]**](BlueprintApiApprovalPolicyTemplateWithScope.md)

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

# **templates_unassign_approval_policy**
> templates_unassign_approval_policy(scope, scope_id)

Unassign Approval Policy From Scope

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
    api_instance = env0_client.ApprovalPolicyApi(api_client)
    scope = 'scope_example' # str | 
    scope_id = 'scope_id_example' # str | 

    try:
        # Unassign Approval Policy From Scope
        api_instance.templates_unassign_approval_policy(scope, scope_id)
    except Exception as e:
        print("Exception when calling ApprovalPolicyApi->templates_unassign_approval_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **scope_id** | **str**|  | 

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

# **templates_unassign_approval_policy_by_id**
> templates_unassign_approval_policy_by_id(id)

Unassign Approval Policy by assignment id

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
    api_instance = env0_client.ApprovalPolicyApi(api_client)
    id = 'id_example' # str | 

    try:
        # Unassign Approval Policy by assignment id
        api_instance.templates_unassign_approval_policy_by_id(id)
    except Exception as e:
        print("Exception when calling ApprovalPolicyApi->templates_unassign_approval_policy_by_id: %s\n" % e)
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

# **templates_update_approval_policy**
> BlueprintApiApprovalPolicyTemplate templates_update_approval_policy(blueprint_api_update_configuration_template_body=blueprint_api_update_configuration_template_body)

Update Existing Approval Policy

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.blueprint_api_approval_policy_template import BlueprintApiApprovalPolicyTemplate
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
    api_instance = env0_client.ApprovalPolicyApi(api_client)
    blueprint_api_update_configuration_template_body = env0_client.BlueprintApiUpdateConfigurationTemplateBody() # BlueprintApiUpdateConfigurationTemplateBody |  (optional)

    try:
        # Update Existing Approval Policy
        api_response = api_instance.templates_update_approval_policy(blueprint_api_update_configuration_template_body=blueprint_api_update_configuration_template_body)
        print("The response of ApprovalPolicyApi->templates_update_approval_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalPolicyApi->templates_update_approval_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_api_update_configuration_template_body** | [**BlueprintApiUpdateConfigurationTemplateBody**](BlueprintApiUpdateConfigurationTemplateBody.md)|  | [optional] 

### Return type

[**BlueprintApiApprovalPolicyTemplate**](BlueprintApiApprovalPolicyTemplate.md)

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

