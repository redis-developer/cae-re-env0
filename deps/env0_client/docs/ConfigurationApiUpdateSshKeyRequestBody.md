# ConfigurationApiUpdateSshKeyRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**encryption_method** | **str** |  | [optional] 

## Example

```python
from env0_client.models.configuration_api_update_ssh_key_request_body import ConfigurationApiUpdateSshKeyRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationApiUpdateSshKeyRequestBody from a JSON string
configuration_api_update_ssh_key_request_body_instance = ConfigurationApiUpdateSshKeyRequestBody.from_json(json)
# print the JSON string representation of the object
print(ConfigurationApiUpdateSshKeyRequestBody.to_json())

# convert the object into a dict
configuration_api_update_ssh_key_request_body_dict = configuration_api_update_ssh_key_request_body_instance.to_dict()
# create an instance of ConfigurationApiUpdateSshKeyRequestBody from a dict
configuration_api_update_ssh_key_request_body_from_dict = ConfigurationApiUpdateSshKeyRequestBody.from_dict(configuration_api_update_ssh_key_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


