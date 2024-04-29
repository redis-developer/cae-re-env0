# ConfigurationApiUpdateCredentialRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CredentialType**](CredentialType.md) |  | [optional] 
**created_by_user** | [**User**](User.md) |  | [optional] 
**value** | **object** | A JSON string representation of the provider credentials. - For AWS_ASSUMED_ROLE_FOR_DEPLOYMENT and AWS_ASSUMED_ROLE types use: { roleArn: \&quot;your-role-arn\&quot;, duration?: \&quot;duration-in-seconds\&quot; }  - For GCP_CREDENTIALS type use: { tableId: \&quot;your-table-id\&quot;, secret: \&quot;your-secret\&quot; }  - For AZURE_CREDENTIALS type use: { clientId: \&quot;your-clientId\&quot;, clientSecret: \&quot;your-clientSecret\&quot;, tenantId: \&quot;your-tenantId\&quot;, subscriptionId: \&quot;your-subscriptionId\&quot; } | [optional] 
**encryption_method** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 

## Example

```python
from env0_client.models.configuration_api_update_credential_request_body import ConfigurationApiUpdateCredentialRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationApiUpdateCredentialRequestBody from a JSON string
configuration_api_update_credential_request_body_instance = ConfigurationApiUpdateCredentialRequestBody.from_json(json)
# print the JSON string representation of the object
print(ConfigurationApiUpdateCredentialRequestBody.to_json())

# convert the object into a dict
configuration_api_update_credential_request_body_dict = configuration_api_update_credential_request_body_instance.to_dict()
# create an instance of ConfigurationApiUpdateCredentialRequestBody from a dict
configuration_api_update_credential_request_body_from_dict = ConfigurationApiUpdateCredentialRequestBody.from_dict(configuration_api_update_credential_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


