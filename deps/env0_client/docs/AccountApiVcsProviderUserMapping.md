# AccountApiVcsProviderUserMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**vcs_provider_user_id** | **str** |  | 
**organization_id** | **str** |  | 

## Example

```python
from env0_client.models.account_api_vcs_provider_user_mapping import AccountApiVcsProviderUserMapping

# TODO update the JSON string below
json = "{}"
# create an instance of AccountApiVcsProviderUserMapping from a JSON string
account_api_vcs_provider_user_mapping_instance = AccountApiVcsProviderUserMapping.from_json(json)
# print the JSON string representation of the object
print(AccountApiVcsProviderUserMapping.to_json())

# convert the object into a dict
account_api_vcs_provider_user_mapping_dict = account_api_vcs_provider_user_mapping_instance.to_dict()
# create an instance of AccountApiVcsProviderUserMapping from a dict
account_api_vcs_provider_user_mapping_from_dict = AccountApiVcsProviderUserMapping.from_dict(account_api_vcs_provider_user_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


