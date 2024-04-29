# AccountApiUpdateVcsProviderUserMappingsRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vcs_provider_user_id** | **str** |  | 
**organization_id** | **str** |  | 

## Example

```python
from env0_client.models.account_api_update_vcs_provider_user_mappings_request_body import AccountApiUpdateVcsProviderUserMappingsRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of AccountApiUpdateVcsProviderUserMappingsRequestBody from a JSON string
account_api_update_vcs_provider_user_mappings_request_body_instance = AccountApiUpdateVcsProviderUserMappingsRequestBody.from_json(json)
# print the JSON string representation of the object
print(AccountApiUpdateVcsProviderUserMappingsRequestBody.to_json())

# convert the object into a dict
account_api_update_vcs_provider_user_mappings_request_body_dict = account_api_update_vcs_provider_user_mappings_request_body_instance.to_dict()
# create an instance of AccountApiUpdateVcsProviderUserMappingsRequestBody from a dict
account_api_update_vcs_provider_user_mappings_request_body_from_dict = AccountApiUpdateVcsProviderUserMappingsRequestBody.from_dict(account_api_update_vcs_provider_user_mappings_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


