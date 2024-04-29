# env0_client.ConfigurationApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configuration_add_deploy_creds_to_project**](ConfigurationApi.md#configuration_add_deploy_creds_to_project) | **PUT** /credentials/deployment/{credentialId}/project/{projectId} | Associate credentials with project
[**configuration_assign_configuration_set_to_scope**](ConfigurationApi.md#configuration_assign_configuration_set_to_scope) | **POST** /configuration-sets/{id}/assignments/{scope}/{scopeId} | Assign set to entity
[**configuration_create_configuration_set**](ConfigurationApi.md#configuration_create_configuration_set) | **POST** /configuration-sets | Create a configuration set
[**configuration_create_credential**](ConfigurationApi.md#configuration_create_credential) | **POST** /credentials | Create Credentials
[**configuration_create_or_update_variable**](ConfigurationApi.md#configuration_create_or_update_variable) | **POST** /configuration | Create or update variable
[**configuration_create_ssh_key**](ConfigurationApi.md#configuration_create_ssh_key) | **POST** /ssh-keys | Create a new SSH key
[**configuration_create_token**](ConfigurationApi.md#configuration_create_token) | **POST** /tokens | Create a git token
[**configuration_delete_configuration_set**](ConfigurationApi.md#configuration_delete_configuration_set) | **DELETE** /configuration-sets/{id} | Delete a configuration set
[**configuration_delete_credential**](ConfigurationApi.md#configuration_delete_credential) | **DELETE** /credentials/{id} | Delete Credentials
[**configuration_delete_ssh_key**](ConfigurationApi.md#configuration_delete_ssh_key) | **DELETE** /ssh-keys/{id} | Delete SSH key
[**configuration_delete_token**](ConfigurationApi.md#configuration_delete_token) | **DELETE** /tokens/{id} | Delete a git token
[**configuration_delete_variable**](ConfigurationApi.md#configuration_delete_variable) | **DELETE** /configuration/{id} | Delete a variable
[**configuration_find_configuration_set_by_id**](ConfigurationApi.md#configuration_find_configuration_set_by_id) | **GET** /configuration-sets/{id} | Get configuration set by its ID
[**configuration_find_credentials**](ConfigurationApi.md#configuration_find_credentials) | **GET** /credentials | List Organization credentials
[**configuration_find_set_assignments_by_scope**](ConfigurationApi.md#configuration_find_set_assignments_by_scope) | **GET** /configuration-sets/assignments/{scope}/{scopeId} | Find sets assigned to scope
[**configuration_find_sets_by_creation_scope**](ConfigurationApi.md#configuration_find_sets_by_creation_scope) | **GET** /configuration-sets | List Sets created by Scope
[**configuration_find_ssh_keys_by_organization**](ConfigurationApi.md#configuration_find_ssh_keys_by_organization) | **GET** /ssh-keys | List all available SSH keys
[**configuration_find_token_by_id**](ConfigurationApi.md#configuration_find_token_by_id) | **GET** /tokens/{id} | Get git token by id
[**configuration_find_token_by_type**](ConfigurationApi.md#configuration_find_token_by_type) | **GET** /tokens | List git tokens
[**configuration_find_variable_by_id**](ConfigurationApi.md#configuration_find_variable_by_id) | **GET** /configuration/{id} | Query configuration variable by id
[**configuration_find_variables_by_scope**](ConfigurationApi.md#configuration_find_variables_by_scope) | **GET** /configuration | List Variables by Scope
[**configuration_get_deploy_creds_for_project**](ConfigurationApi.md#configuration_get_deploy_creds_for_project) | **GET** /credentials/deployment/project/{projectId} | List deployment a Project&#39;s deployment credentials
[**configuration_remove_deploy_creds_from_project**](ConfigurationApi.md#configuration_remove_deploy_creds_from_project) | **DELETE** /credentials/deployment/{credentialId}/project/{projectId} | Dissociate credentials with project
[**configuration_update_configuration_set**](ConfigurationApi.md#configuration_update_configuration_set) | **PUT** /configuration-sets/{id} | Update a configuration set
[**configuration_update_credential**](ConfigurationApi.md#configuration_update_credential) | **PATCH** /credentials/{id} | Update Credentials
[**configuration_update_ssh_key**](ConfigurationApi.md#configuration_update_ssh_key) | **PUT** /ssh-keys/{id} | Update an existing SSH key


# **configuration_add_deploy_creds_to_project**
> ConfigurationApiDeploymentCredentialToProject configuration_add_deploy_creds_to_project(credential_id, project_id, body=body)

Associate credentials with project

Associate cloud provider, kubernetes or vault deployment credentials to Project

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_api_deployment_credential_to_project import ConfigurationApiDeploymentCredentialToProject
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
    api_instance = env0_client.ConfigurationApi(api_client)
    credential_id = 'credential_id_example' # str | 
    project_id = 'project_id_example' # str | 
    body = None # object |  (optional)

    try:
        # Associate credentials with project
        api_response = api_instance.configuration_add_deploy_creds_to_project(credential_id, project_id, body=body)
        print("The response of ConfigurationApi->configuration_add_deploy_creds_to_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_add_deploy_creds_to_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 
 **project_id** | **str**|  | 
 **body** | **object**|  | [optional] 

### Return type

[**ConfigurationApiDeploymentCredentialToProject**](ConfigurationApiDeploymentCredentialToProject.md)

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

# **configuration_assign_configuration_set_to_scope**
> object configuration_assign_configuration_set_to_scope(id, scope, scope_id, body=body)

Assign set to entity

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
    api_instance = env0_client.ConfigurationApi(api_client)
    id = 'id_example' # str | 
    scope = 'scope_example' # str | 
    scope_id = 'scope_id_example' # str | 
    body = None # object |  (optional)

    try:
        # Assign set to entity
        api_response = api_instance.configuration_assign_configuration_set_to_scope(id, scope, scope_id, body=body)
        print("The response of ConfigurationApi->configuration_assign_configuration_set_to_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_assign_configuration_set_to_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **scope** | **str**|  | 
 **scope_id** | **str**|  | 
 **body** | **object**|  | [optional] 

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

# **configuration_create_configuration_set**
> ConfigurationSet configuration_create_configuration_set(configuration_api_create_configuration_set_request_body=configuration_api_create_configuration_set_request_body)

Create a configuration set

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_api_create_configuration_set_request_body import ConfigurationApiCreateConfigurationSetRequestBody
from env0_client.models.configuration_set import ConfigurationSet
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
    api_instance = env0_client.ConfigurationApi(api_client)
    configuration_api_create_configuration_set_request_body = env0_client.ConfigurationApiCreateConfigurationSetRequestBody() # ConfigurationApiCreateConfigurationSetRequestBody |  (optional)

    try:
        # Create a configuration set
        api_response = api_instance.configuration_create_configuration_set(configuration_api_create_configuration_set_request_body=configuration_api_create_configuration_set_request_body)
        print("The response of ConfigurationApi->configuration_create_configuration_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_create_configuration_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_api_create_configuration_set_request_body** | [**ConfigurationApiCreateConfigurationSetRequestBody**](ConfigurationApiCreateConfigurationSetRequestBody.md)|  | [optional] 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

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

# **configuration_create_credential**
> CredentialWithoutValue configuration_create_credential(transient_credential=transient_credential)

Create Credentials

Create a set of new cloud provider, kubernetes, vault or cost credentials for an Organization which may then be associated with a Project

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.credential_without_value import CredentialWithoutValue
from env0_client.models.transient_credential import TransientCredential
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
    api_instance = env0_client.ConfigurationApi(api_client)
    transient_credential = env0_client.TransientCredential() # TransientCredential |  (optional)

    try:
        # Create Credentials
        api_response = api_instance.configuration_create_credential(transient_credential=transient_credential)
        print("The response of ConfigurationApi->configuration_create_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_create_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transient_credential** | [**TransientCredential**](TransientCredential.md)|  | [optional] 

### Return type

[**CredentialWithoutValue**](CredentialWithoutValue.md)

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

# **configuration_create_or_update_variable**
> List[ConfigurationPropertyResponse] configuration_create_or_update_variable(configuration_property_request=configuration_property_request)

Create or update variable

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_property_request import ConfigurationPropertyRequest
from env0_client.models.configuration_property_response import ConfigurationPropertyResponse
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
    api_instance = env0_client.ConfigurationApi(api_client)
    configuration_property_request = [env0_client.ConfigurationPropertyRequest()] # List[ConfigurationPropertyRequest] |  (optional)

    try:
        # Create or update variable
        api_response = api_instance.configuration_create_or_update_variable(configuration_property_request=configuration_property_request)
        print("The response of ConfigurationApi->configuration_create_or_update_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_create_or_update_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_property_request** | [**List[ConfigurationPropertyRequest]**](ConfigurationPropertyRequest.md)|  | [optional] 

### Return type

[**List[ConfigurationPropertyResponse]**](ConfigurationPropertyResponse.md)

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

# **configuration_create_ssh_key**
> ConfigurationApiAbstractSecretResponseConfigurationApiSshKey configuration_create_ssh_key(configuration_api_create_ssh_key_request_body=configuration_api_create_ssh_key_request_body)

Create a new SSH key

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_api_abstract_secret_response_configuration_api_ssh_key import ConfigurationApiAbstractSecretResponseConfigurationApiSshKey
from env0_client.models.configuration_api_create_ssh_key_request_body import ConfigurationApiCreateSshKeyRequestBody
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
    api_instance = env0_client.ConfigurationApi(api_client)
    configuration_api_create_ssh_key_request_body = env0_client.ConfigurationApiCreateSshKeyRequestBody() # ConfigurationApiCreateSshKeyRequestBody |  (optional)

    try:
        # Create a new SSH key
        api_response = api_instance.configuration_create_ssh_key(configuration_api_create_ssh_key_request_body=configuration_api_create_ssh_key_request_body)
        print("The response of ConfigurationApi->configuration_create_ssh_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_create_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_api_create_ssh_key_request_body** | [**ConfigurationApiCreateSshKeyRequestBody**](ConfigurationApiCreateSshKeyRequestBody.md)|  | [optional] 

### Return type

[**ConfigurationApiAbstractSecretResponseConfigurationApiSshKey**](ConfigurationApiAbstractSecretResponseConfigurationApiSshKey.md)

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

# **configuration_create_token**
> ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken configuration_create_token(configuration_api_token=configuration_api_token)

Create a git token

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_api_abstract_secret_response_configuration_api_persistent_token import ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken
from env0_client.models.configuration_api_token import ConfigurationApiToken
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
    api_instance = env0_client.ConfigurationApi(api_client)
    configuration_api_token = env0_client.ConfigurationApiToken() # ConfigurationApiToken |  (optional)

    try:
        # Create a git token
        api_response = api_instance.configuration_create_token(configuration_api_token=configuration_api_token)
        print("The response of ConfigurationApi->configuration_create_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_create_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_api_token** | [**ConfigurationApiToken**](ConfigurationApiToken.md)|  | [optional] 

### Return type

[**ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken**](ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken.md)

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

# **configuration_delete_configuration_set**
> configuration_delete_configuration_set(id)

Delete a configuration set

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
    api_instance = env0_client.ConfigurationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a configuration set
        api_instance.configuration_delete_configuration_set(id)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_delete_configuration_set: %s\n" % e)
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

# **configuration_delete_credential**
> configuration_delete_credential(id)

Delete Credentials

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
    api_instance = env0_client.ConfigurationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Credentials
        api_instance.configuration_delete_credential(id)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_delete_credential: %s\n" % e)
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

# **configuration_delete_ssh_key**
> configuration_delete_ssh_key(id)

Delete SSH key

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
    api_instance = env0_client.ConfigurationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete SSH key
        api_instance.configuration_delete_ssh_key(id)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_delete_ssh_key: %s\n" % e)
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

# **configuration_delete_token**
> configuration_delete_token(id)

Delete a git token

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
    api_instance = env0_client.ConfigurationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a git token
        api_instance.configuration_delete_token(id)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_delete_token: %s\n" % e)
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

# **configuration_delete_variable**
> configuration_delete_variable(id)

Delete a variable

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
    api_instance = env0_client.ConfigurationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a variable
        api_instance.configuration_delete_variable(id)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_delete_variable: %s\n" % e)
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

# **configuration_find_configuration_set_by_id**
> ConfigurationSet configuration_find_configuration_set_by_id(id)

Get configuration set by its ID

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_set import ConfigurationSet
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
    api_instance = env0_client.ConfigurationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get configuration set by its ID
        api_response = api_instance.configuration_find_configuration_set_by_id(id)
        print("The response of ConfigurationApi->configuration_find_configuration_set_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_find_configuration_set_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

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

# **configuration_find_credentials**
> List[CredentialWithoutValue] configuration_find_credentials(organization_id)

List Organization credentials

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.credential_without_value import CredentialWithoutValue
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
    api_instance = env0_client.ConfigurationApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # List Organization credentials
        api_response = api_instance.configuration_find_credentials(organization_id)
        print("The response of ConfigurationApi->configuration_find_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_find_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**List[CredentialWithoutValue]**](CredentialWithoutValue.md)

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

# **configuration_find_set_assignments_by_scope**
> List[ConfigurationSet] configuration_find_set_assignments_by_scope(scope, scope_id)

Find sets assigned to scope

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_set import ConfigurationSet
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
    api_instance = env0_client.ConfigurationApi(api_client)
    scope = 'scope_example' # str | 
    scope_id = 'scope_id_example' # str | 

    try:
        # Find sets assigned to scope
        api_response = api_instance.configuration_find_set_assignments_by_scope(scope, scope_id)
        print("The response of ConfigurationApi->configuration_find_set_assignments_by_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_find_set_assignments_by_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **scope_id** | **str**|  | 

### Return type

[**List[ConfigurationSet]**](ConfigurationSet.md)

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

# **configuration_find_sets_by_creation_scope**
> List[ConfigurationSet] configuration_find_sets_by_creation_scope(organization_id=organization_id, project_id=project_id)

List Sets created by Scope

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_set import ConfigurationSet
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
    api_instance = env0_client.ConfigurationApi(api_client)
    organization_id = 'organization_id_example' # str |  (optional)
    project_id = 'project_id_example' # str |  (optional)

    try:
        # List Sets created by Scope
        api_response = api_instance.configuration_find_sets_by_creation_scope(organization_id=organization_id, project_id=project_id)
        print("The response of ConfigurationApi->configuration_find_sets_by_creation_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_find_sets_by_creation_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | [optional] 
 **project_id** | **str**|  | [optional] 

### Return type

[**List[ConfigurationSet]**](ConfigurationSet.md)

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

# **configuration_find_ssh_keys_by_organization**
> List[ConfigurationApiSshKey] configuration_find_ssh_keys_by_organization(organization_id)

List all available SSH keys

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_api_ssh_key import ConfigurationApiSshKey
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
    api_instance = env0_client.ConfigurationApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        # List all available SSH keys
        api_response = api_instance.configuration_find_ssh_keys_by_organization(organization_id)
        print("The response of ConfigurationApi->configuration_find_ssh_keys_by_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_find_ssh_keys_by_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**List[ConfigurationApiSshKey]**](ConfigurationApiSshKey.md)

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

# **configuration_find_token_by_id**
> ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken configuration_find_token_by_id(id)

Get git token by id

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_api_abstract_secret_response_configuration_api_persistent_token import ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken
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
    api_instance = env0_client.ConfigurationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get git token by id
        api_response = api_instance.configuration_find_token_by_id(id)
        print("The response of ConfigurationApi->configuration_find_token_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_find_token_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken**](ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken.md)

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

# **configuration_find_token_by_type**
> ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken configuration_find_token_by_type(type, organization_id)

List git tokens

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_api_abstract_secret_response_configuration_api_persistent_token import ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken
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
    api_instance = env0_client.ConfigurationApi(api_client)
    type = 'type_example' # str | 
    organization_id = 'organization_id_example' # str | 

    try:
        # List git tokens
        api_response = api_instance.configuration_find_token_by_type(type, organization_id)
        print("The response of ConfigurationApi->configuration_find_token_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_find_token_by_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **organization_id** | **str**|  | 

### Return type

[**ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken**](ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken.md)

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

# **configuration_find_variable_by_id**
> ConfigurationPropertyResponse configuration_find_variable_by_id(id)

Query configuration variable by id

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_property_response import ConfigurationPropertyResponse
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
    api_instance = env0_client.ConfigurationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Query configuration variable by id
        api_response = api_instance.configuration_find_variable_by_id(id)
        print("The response of ConfigurationApi->configuration_find_variable_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_find_variable_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ConfigurationPropertyResponse**](ConfigurationPropertyResponse.md)

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

# **configuration_find_variables_by_scope**
> List[ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty] configuration_find_variables_by_scope(organization_id, project_id=project_id, blueprint_id=blueprint_id, environment_id=environment_id, deployment_log_id=deployment_log_id)

List Variables by Scope

Lists all variables for the provided scope(s). If more than one scope is given - variables will be overridden by lower level scopes - just like env0 does. For example - Provided both organizationId and projectId, if a variable exists on both scopes, a single instance of it will be returned, with its Project scope value 

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_api_find_variables_by_scope_overriding_configuration_property import ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty
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
    api_instance = env0_client.ConfigurationApi(api_client)
    organization_id = 'organization_id_example' # str | 
    project_id = 'project_id_example' # str |  (optional)
    blueprint_id = 'blueprint_id_example' # str |  (optional)
    environment_id = 'environment_id_example' # str |  (optional)
    deployment_log_id = 'deployment_log_id_example' # str |  (optional)

    try:
        # List Variables by Scope
        api_response = api_instance.configuration_find_variables_by_scope(organization_id, project_id=project_id, blueprint_id=blueprint_id, environment_id=environment_id, deployment_log_id=deployment_log_id)
        print("The response of ConfigurationApi->configuration_find_variables_by_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_find_variables_by_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **project_id** | **str**|  | [optional] 
 **blueprint_id** | **str**|  | [optional] 
 **environment_id** | **str**|  | [optional] 
 **deployment_log_id** | **str**|  | [optional] 

### Return type

[**List[ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty]**](ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty.md)

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

# **configuration_get_deploy_creds_for_project**
> ConfigurationApiDeploymentCredentialsToProject configuration_get_deploy_creds_for_project(project_id)

List deployment a Project's deployment credentials

List deployment credentials associated with Project

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_api_deployment_credentials_to_project import ConfigurationApiDeploymentCredentialsToProject
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
    api_instance = env0_client.ConfigurationApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # List deployment a Project's deployment credentials
        api_response = api_instance.configuration_get_deploy_creds_for_project(project_id)
        print("The response of ConfigurationApi->configuration_get_deploy_creds_for_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_get_deploy_creds_for_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**ConfigurationApiDeploymentCredentialsToProject**](ConfigurationApiDeploymentCredentialsToProject.md)

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

# **configuration_remove_deploy_creds_from_project**
> configuration_remove_deploy_creds_from_project(credential_id, project_id)

Dissociate credentials with project

Dissociate cloud provider, kubernetes or vault deployment credentials with Project

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
    api_instance = env0_client.ConfigurationApi(api_client)
    credential_id = 'credential_id_example' # str | 
    project_id = 'project_id_example' # str | 

    try:
        # Dissociate credentials with project
        api_instance.configuration_remove_deploy_creds_from_project(credential_id, project_id)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_remove_deploy_creds_from_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 
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

# **configuration_update_configuration_set**
> ConfigurationSet configuration_update_configuration_set(id, configuration_api_update_configuration_set_request_body=configuration_api_update_configuration_set_request_body)

Update a configuration set

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_api_update_configuration_set_request_body import ConfigurationApiUpdateConfigurationSetRequestBody
from env0_client.models.configuration_set import ConfigurationSet
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
    api_instance = env0_client.ConfigurationApi(api_client)
    id = 'id_example' # str | 
    configuration_api_update_configuration_set_request_body = env0_client.ConfigurationApiUpdateConfigurationSetRequestBody() # ConfigurationApiUpdateConfigurationSetRequestBody |  (optional)

    try:
        # Update a configuration set
        api_response = api_instance.configuration_update_configuration_set(id, configuration_api_update_configuration_set_request_body=configuration_api_update_configuration_set_request_body)
        print("The response of ConfigurationApi->configuration_update_configuration_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_update_configuration_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **configuration_api_update_configuration_set_request_body** | [**ConfigurationApiUpdateConfigurationSetRequestBody**](ConfigurationApiUpdateConfigurationSetRequestBody.md)|  | [optional] 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

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

# **configuration_update_credential**
> CredentialWithoutValue configuration_update_credential(id, configuration_api_update_credential_request_body=configuration_api_update_credential_request_body)

Update Credentials

Update deployment credentials or cost credentials for an organization

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_api_update_credential_request_body import ConfigurationApiUpdateCredentialRequestBody
from env0_client.models.credential_without_value import CredentialWithoutValue
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
    api_instance = env0_client.ConfigurationApi(api_client)
    id = 'id_example' # str | 
    configuration_api_update_credential_request_body = env0_client.ConfigurationApiUpdateCredentialRequestBody() # ConfigurationApiUpdateCredentialRequestBody |  (optional)

    try:
        # Update Credentials
        api_response = api_instance.configuration_update_credential(id, configuration_api_update_credential_request_body=configuration_api_update_credential_request_body)
        print("The response of ConfigurationApi->configuration_update_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_update_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **configuration_api_update_credential_request_body** | [**ConfigurationApiUpdateCredentialRequestBody**](ConfigurationApiUpdateCredentialRequestBody.md)|  | [optional] 

### Return type

[**CredentialWithoutValue**](CredentialWithoutValue.md)

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

# **configuration_update_ssh_key**
> ConfigurationApiAbstractSecretResponseConfigurationApiSshKey configuration_update_ssh_key(id, configuration_api_update_ssh_key_request_body=configuration_api_update_ssh_key_request_body)

Update an existing SSH key

### Example

* Basic Authentication (env0_API_Key):

```python
import env0_client
from env0_client.models.configuration_api_abstract_secret_response_configuration_api_ssh_key import ConfigurationApiAbstractSecretResponseConfigurationApiSshKey
from env0_client.models.configuration_api_update_ssh_key_request_body import ConfigurationApiUpdateSshKeyRequestBody
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
    api_instance = env0_client.ConfigurationApi(api_client)
    id = 'id_example' # str | 
    configuration_api_update_ssh_key_request_body = env0_client.ConfigurationApiUpdateSshKeyRequestBody() # ConfigurationApiUpdateSshKeyRequestBody |  (optional)

    try:
        # Update an existing SSH key
        api_response = api_instance.configuration_update_ssh_key(id, configuration_api_update_ssh_key_request_body=configuration_api_update_ssh_key_request_body)
        print("The response of ConfigurationApi->configuration_update_ssh_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->configuration_update_ssh_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **configuration_api_update_ssh_key_request_body** | [**ConfigurationApiUpdateSshKeyRequestBody**](ConfigurationApiUpdateSshKeyRequestBody.md)|  | [optional] 

### Return type

[**ConfigurationApiAbstractSecretResponseConfigurationApiSshKey**](ConfigurationApiAbstractSecretResponseConfigurationApiSshKey.md)

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

