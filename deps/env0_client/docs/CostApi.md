# env0_client.CostApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cost_add_project_costs_credentials**](CostApi.md#cost_add_project_costs_credentials) | **PUT** /costs/project/{projectId}/credentials | Associate Cost Credentials with Project
[**cost_get_accumulated_project_costs**](CostApi.md#cost_get_accumulated_project_costs) | **GET** /costs/budget/accumulated | Get a project&#39;s accumulated costs
[**cost_get_budget_summary**](CostApi.md#cost_get_budget_summary) | **GET** /costs/budget/summary | Get projects&#39; budget summary of the current period
[**cost_get_environment_costs**](CostApi.md#cost_get_environment_costs) | **GET** /costs/environments/{environmentId} | Get costs for an Environment
[**cost_get_organization_costs**](CostApi.md#cost_get_organization_costs) | **GET** /costs | Get costs for an Organization
[**cost_get_project_budget**](CostApi.md#cost_get_project_budget) | **GET** /costs/project/{projectId}/budget | Get a project&#39;s budget
[**cost_get_project_costs**](CostApi.md#cost_get_project_costs) | **GET** /costs/projects/{projectId} | Get costs for a Project
[**cost_get_project_costs_credentials**](CostApi.md#cost_get_project_costs_credentials) | **GET** /costs/project/{projectId}/credentials | List Cost Credentials associated to Project
[**cost_get_projects_with_cost_credentials**](CostApi.md#cost_get_projects_with_cost_credentials) | **GET** /costs/projects/enabled | List projects with cost credentials associated to organization
[**cost_get_weekly_costs**](CostApi.md#cost_get_weekly_costs) | **GET** /costs/weekly | Get weekly costs for projects or environments
[**cost_is_cost_enabled**](CostApi.md#cost_is_cost_enabled) | **GET** /costs/project/{projectId}/enabled | Return wether or not cost is enabled for a project
[**cost_remove_project_budget**](CostApi.md#cost_remove_project_budget) | **DELETE** /costs/project/{projectId}/budget | Remove a project&#39;s budget
[**cost_remove_project_costs_credentials**](CostApi.md#cost_remove_project_costs_credentials) | **DELETE** /costs/project/{projectId}/credentials/{credentialsId} | Dissociate Cost Credentials from Project
[**cost_upsert_project_budget**](CostApi.md#cost_upsert_project_budget) | **PUT** /costs/project/{projectId}/budget | Upsert a project&#39;s budget


# **cost_add_project_costs_credentials**
> CostApiProjectCostsCredentials cost_add_project_costs_credentials(project_id, cost_api_add_project_costs_credentials_request_body=cost_api_add_project_costs_credentials_request_body)

Associate Cost Credentials with Project

Associate Cloud provider Cost Credentials to a Project. This will enable cost tagging in deployments in the project.

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.cost_api_add_project_costs_credentials_request_body import CostApiAddProjectCostsCredentialsRequestBody
from env0_client.models.cost_api_project_costs_credentials import CostApiProjectCostsCredentials
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
    api_instance = env0_client.CostApi(api_client)
    project_id = 'project_id_example' # str | 
    cost_api_add_project_costs_credentials_request_body = env0_client.CostApiAddProjectCostsCredentialsRequestBody() # CostApiAddProjectCostsCredentialsRequestBody |  (optional)

    try:
        # Associate Cost Credentials with Project
        api_response = api_instance.cost_add_project_costs_credentials(project_id, cost_api_add_project_costs_credentials_request_body=cost_api_add_project_costs_credentials_request_body)
        print("The response of CostApi->cost_add_project_costs_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostApi->cost_add_project_costs_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **cost_api_add_project_costs_credentials_request_body** | [**CostApiAddProjectCostsCredentialsRequestBody**](CostApiAddProjectCostsCredentialsRequestBody.md)|  | [optional] 

### Return type

[**CostApiProjectCostsCredentials**](CostApiProjectCostsCredentials.md)

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

# **cost_get_accumulated_project_costs**
> List[CostApiGetAccumulatedProjectCostsResponseInner] cost_get_accumulated_project_costs(project_id)

Get a project's accumulated costs

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.cost_api_get_accumulated_project_costs_response_inner import CostApiGetAccumulatedProjectCostsResponseInner
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
    api_instance = env0_client.CostApi(api_client)
    project_id = 'project_id_example' # str | The project to get accumulated costs for

    try:
        # Get a project's accumulated costs
        api_response = api_instance.cost_get_accumulated_project_costs(project_id)
        print("The response of CostApi->cost_get_accumulated_project_costs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostApi->cost_get_accumulated_project_costs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project to get accumulated costs for | 

### Return type

[**List[CostApiGetAccumulatedProjectCostsResponseInner]**](CostApiGetAccumulatedProjectCostsResponseInner.md)

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

# **cost_get_budget_summary**
> List[CostApiProjectBudgetSummary] cost_get_budget_summary(project_ids)

Get projects' budget summary of the current period

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.cost_api_project_budget_summary import CostApiProjectBudgetSummary
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
    api_instance = env0_client.CostApi(api_client)
    project_ids = 'project_ids_example' # str | The projects to get summary for

    try:
        # Get projects' budget summary of the current period
        api_response = api_instance.cost_get_budget_summary(project_ids)
        print("The response of CostApi->cost_get_budget_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostApi->cost_get_budget_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_ids** | **str**| The projects to get summary for | 

### Return type

[**List[CostApiProjectBudgetSummary]**](CostApiProjectBudgetSummary.md)

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

# **cost_get_environment_costs**
> List[CostApiCostQueryResponseInner] cost_get_environment_costs(environment_id, timespan=timespan, granularity=granularity)

Get costs for an Environment

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.cost_api_cost_query_response_inner import CostApiCostQueryResponseInner
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
    api_instance = env0_client.CostApi(api_client)
    environment_id = 'environment_id_example' # str | 
    timespan = 'timespan_example' # str | A timespan to query cost for (optional)
    granularity = 'granularity_example' # str | Granularity of each cost record (optional)

    try:
        # Get costs for an Environment
        api_response = api_instance.cost_get_environment_costs(environment_id, timespan=timespan, granularity=granularity)
        print("The response of CostApi->cost_get_environment_costs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostApi->cost_get_environment_costs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**|  | 
 **timespan** | **str**| A timespan to query cost for | [optional] 
 **granularity** | **str**| Granularity of each cost record | [optional] 

### Return type

[**List[CostApiCostQueryResponseInner]**](CostApiCostQueryResponseInner.md)

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

# **cost_get_organization_costs**
> CostApiCostQueryResponseV2 cost_get_organization_costs(organization_id, timespan=timespan, granularity=granularity, project_ids=project_ids, accumulated=accumulated)

Get costs for an Organization

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.cost_api_cost_query_response_v2 import CostApiCostQueryResponseV2
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
    api_instance = env0_client.CostApi(api_client)
    organization_id = 'organization_id_example' # str | Organization Id to get all projects costs
    timespan = 'timespan_example' # str | A timespan to query cost for (optional)
    granularity = 'granularity_example' # str | Granularity of each cost record (optional)
    project_ids = 'project_ids_example' # str | Project ids to get costs for (optional)
    accumulated = 'accumulated_example' # str | Should the response be a sum of all costs or each cost individually (optional)

    try:
        # Get costs for an Organization
        api_response = api_instance.cost_get_organization_costs(organization_id, timespan=timespan, granularity=granularity, project_ids=project_ids, accumulated=accumulated)
        print("The response of CostApi->cost_get_organization_costs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostApi->cost_get_organization_costs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization Id to get all projects costs | 
 **timespan** | **str**| A timespan to query cost for | [optional] 
 **granularity** | **str**| Granularity of each cost record | [optional] 
 **project_ids** | **str**| Project ids to get costs for | [optional] 
 **accumulated** | **str**| Should the response be a sum of all costs or each cost individually | [optional] 

### Return type

[**CostApiCostQueryResponseV2**](CostApiCostQueryResponseV2.md)

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

# **cost_get_project_budget**
> CostApiBudget cost_get_project_budget(project_id)

Get a project's budget

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.cost_api_budget import CostApiBudget
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
    api_instance = env0_client.CostApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Get a project's budget
        api_response = api_instance.cost_get_project_budget(project_id)
        print("The response of CostApi->cost_get_project_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostApi->cost_get_project_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**CostApiBudget**](CostApiBudget.md)

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

# **cost_get_project_costs**
> List[CostApiCostQueryResponseInner] cost_get_project_costs(project_id, timespan=timespan, granularity=granularity)

Get costs for a Project

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.cost_api_cost_query_response_inner import CostApiCostQueryResponseInner
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
    api_instance = env0_client.CostApi(api_client)
    project_id = 'project_id_example' # str | 
    timespan = 'timespan_example' # str | A timespan to query cost for (optional)
    granularity = 'granularity_example' # str | Granularity of each cost record (optional)

    try:
        # Get costs for a Project
        api_response = api_instance.cost_get_project_costs(project_id, timespan=timespan, granularity=granularity)
        print("The response of CostApi->cost_get_project_costs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostApi->cost_get_project_costs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **timespan** | **str**| A timespan to query cost for | [optional] 
 **granularity** | **str**| Granularity of each cost record | [optional] 

### Return type

[**List[CostApiCostQueryResponseInner]**](CostApiCostQueryResponseInner.md)

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

# **cost_get_project_costs_credentials**
> List[CostApiProjectCostsCredentials] cost_get_project_costs_credentials(project_id)

List Cost Credentials associated to Project

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.cost_api_project_costs_credentials import CostApiProjectCostsCredentials
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
    api_instance = env0_client.CostApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # List Cost Credentials associated to Project
        api_response = api_instance.cost_get_project_costs_credentials(project_id)
        print("The response of CostApi->cost_get_project_costs_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostApi->cost_get_project_costs_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**List[CostApiProjectCostsCredentials]**](CostApiProjectCostsCredentials.md)

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

# **cost_get_projects_with_cost_credentials**
> List[str] cost_get_projects_with_cost_credentials(organization_id)

List projects with cost credentials associated to organization

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
    api_instance = env0_client.CostApi(api_client)
    organization_id = 'organization_id_example' # str | The organization to get projects for

    try:
        # List projects with cost credentials associated to organization
        api_response = api_instance.cost_get_projects_with_cost_credentials(organization_id)
        print("The response of CostApi->cost_get_projects_with_cost_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostApi->cost_get_projects_with_cost_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The organization to get projects for | 

### Return type

**List[str]**

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

# **cost_get_weekly_costs**
> Dict[str, CostApiWeeklyCostEntry] cost_get_weekly_costs(project_ids=project_ids, environment_ids=environment_ids)

Get weekly costs for projects or environments

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.cost_api_weekly_cost_entry import CostApiWeeklyCostEntry
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
    api_instance = env0_client.CostApi(api_client)
    project_ids = 'project_ids_example' # str |  (optional)
    environment_ids = 'environment_ids_example' # str |  (optional)

    try:
        # Get weekly costs for projects or environments
        api_response = api_instance.cost_get_weekly_costs(project_ids=project_ids, environment_ids=environment_ids)
        print("The response of CostApi->cost_get_weekly_costs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostApi->cost_get_weekly_costs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_ids** | **str**|  | [optional] 
 **environment_ids** | **str**|  | [optional] 

### Return type

[**Dict[str, CostApiWeeklyCostEntry]**](CostApiWeeklyCostEntry.md)

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

# **cost_is_cost_enabled**
> CostApiIsCostEnabledResponse cost_is_cost_enabled(project_id)

Return wether or not cost is enabled for a project

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.cost_api_is_cost_enabled_response import CostApiIsCostEnabledResponse
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
    api_instance = env0_client.CostApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Return wether or not cost is enabled for a project
        api_response = api_instance.cost_is_cost_enabled(project_id)
        print("The response of CostApi->cost_is_cost_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostApi->cost_is_cost_enabled: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**CostApiIsCostEnabledResponse**](CostApiIsCostEnabledResponse.md)

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

# **cost_remove_project_budget**
> cost_remove_project_budget(project_id)

Remove a project's budget

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
    api_instance = env0_client.CostApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Remove a project's budget
        api_instance.cost_remove_project_budget(project_id)
    except Exception as e:
        print("Exception when calling CostApi->cost_remove_project_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

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

# **cost_remove_project_costs_credentials**
> cost_remove_project_costs_credentials(project_id, credentials_id)

Dissociate Cost Credentials from Project

Dissociate Cloud provider Cost Credentials to a Project. This will disable cost tagging in deployments in the project.

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
    api_instance = env0_client.CostApi(api_client)
    project_id = 'project_id_example' # str | 
    credentials_id = 'credentials_id_example' # str | 

    try:
        # Dissociate Cost Credentials from Project
        api_instance.cost_remove_project_costs_credentials(project_id, credentials_id)
    except Exception as e:
        print("Exception when calling CostApi->cost_remove_project_costs_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **credentials_id** | **str**|  | 

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

# **cost_upsert_project_budget**
> CostApiBudget cost_upsert_project_budget(project_id, cost_api_upsert_project_budget_request_body=cost_api_upsert_project_budget_request_body)

Upsert a project's budget

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.cost_api_budget import CostApiBudget
from env0_client.models.cost_api_upsert_project_budget_request_body import CostApiUpsertProjectBudgetRequestBody
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
    api_instance = env0_client.CostApi(api_client)
    project_id = 'project_id_example' # str | 
    cost_api_upsert_project_budget_request_body = env0_client.CostApiUpsertProjectBudgetRequestBody() # CostApiUpsertProjectBudgetRequestBody |  (optional)

    try:
        # Upsert a project's budget
        api_response = api_instance.cost_upsert_project_budget(project_id, cost_api_upsert_project_budget_request_body=cost_api_upsert_project_budget_request_body)
        print("The response of CostApi->cost_upsert_project_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostApi->cost_upsert_project_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **cost_api_upsert_project_budget_request_body** | [**CostApiUpsertProjectBudgetRequestBody**](CostApiUpsertProjectBudgetRequestBody.md)|  | [optional] 

### Return type

[**CostApiBudget**](CostApiBudget.md)

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

