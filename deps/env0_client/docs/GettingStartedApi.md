# env0_client.GettingStartedApi

All URIs are relative to *https://api.env0.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication**](GettingStartedApi.md#authentication) | **HEAD** / | Authentication


# **authentication**
> authentication()

Authentication

Authentication against the env0 API is done via API Keys.  An API Key is created by an organization administrator, but is not connected to any specific user when it's being used.  ### Creating an API Key With a Specific Role - Once you've created your own organization, you can create and manage API Keys. - Navigate to the Organization Settings page and click the API Keys tab. - Click Add API Key, and enter a name for your key in the Name field. This name is for your reference and isn't used directly in authentication.    > ❗️Save Your API Key ID & Secret   > The secret will not be available after you close this modal  ### Creating a Personal API Key - Click on your avatar (located on the top right of the screen) - Click on Personal Settings - Select the API Keys tab - Click Add API Key, and enter a name for your key in the Name field. This name is for your reference and isn't used directly in authentication.    > ❗️Save Your API Key ID & Secret   > The secret will not be available after you close this modal  ### Using an API Key to Authenticate Authentication to the env0 API is done using the Basic Authentication method. Each request made should include the API Key ID as the username, and the API Key Secret as the password. For example - when Using curl, we can include these parameters using the flag --user {API Key ID}:{API Key Secret}.  ### API Key Permissions API Keys are given the role of an Organization Admin, meaning they can be used to perform any action, in any project, under the scope of the organization.

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
    api_instance = env0_client.GettingStartedApi(api_client)

    try:
        # Authentication
        api_instance.authentication()
    except Exception as e:
        print("Exception when calling GettingStartedApi->authentication: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[env0_API_Key](../README.md#env0_API_Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

