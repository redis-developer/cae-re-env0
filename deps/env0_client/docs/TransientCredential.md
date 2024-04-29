# TransientCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CredentialType**](CredentialType.md) |  | 
**created_by_user** | [**User**](User.md) |  | [optional] 
**value** | **object** | A JSON string representation of the provider credentials. - For AWS_ASSUMED_ROLE_FOR_DEPLOYMENT and AWS_ASSUMED_ROLE types use: { roleArn: \&quot;your-role-arn\&quot;, duration?: \&quot;duration-in-seconds\&quot; }  - For GCP_CREDENTIALS type use: { tableId: \&quot;your-table-id\&quot;, secret: \&quot;your-secret\&quot; }  - For AZURE_CREDENTIALS type use: { clientId: \&quot;your-clientId\&quot;, clientSecret: \&quot;your-clientSecret\&quot;, tenantId: \&quot;your-tenantId\&quot;, subscriptionId: \&quot;your-subscriptionId\&quot; } | 
**encryption_method** | **str** |  | [optional] 
**name** | **str** |  | 
**organization_id** | **str** |  | 

## Example

```python
from env0_client.models.transient_credential import TransientCredential

# TODO update the JSON string below
json = "{}"
# create an instance of TransientCredential from a JSON string
transient_credential_instance = TransientCredential.from_json(json)
# print the JSON string representation of the object
print(TransientCredential.to_json())

# convert the object into a dict
transient_credential_dict = transient_credential_instance.to_dict()
# create an instance of TransientCredential from a dict
transient_credential_from_dict = TransientCredential.from_dict(transient_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


