# ConfigurationApiAbstractSecretResponseConfigurationApiSshKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**user** | [**User**](User.md) |  | [optional] 
**value** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**organization_id** | **str** |  | 

## Example

```python
from env0_client.models.configuration_api_abstract_secret_response_configuration_api_ssh_key import ConfigurationApiAbstractSecretResponseConfigurationApiSshKey

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationApiAbstractSecretResponseConfigurationApiSshKey from a JSON string
configuration_api_abstract_secret_response_configuration_api_ssh_key_instance = ConfigurationApiAbstractSecretResponseConfigurationApiSshKey.from_json(json)
# print the JSON string representation of the object
print(ConfigurationApiAbstractSecretResponseConfigurationApiSshKey.to_json())

# convert the object into a dict
configuration_api_abstract_secret_response_configuration_api_ssh_key_dict = configuration_api_abstract_secret_response_configuration_api_ssh_key_instance.to_dict()
# create an instance of ConfigurationApiAbstractSecretResponseConfigurationApiSshKey from a dict
configuration_api_abstract_secret_response_configuration_api_ssh_key_from_dict = ConfigurationApiAbstractSecretResponseConfigurationApiSshKey.from_dict(configuration_api_abstract_secret_response_configuration_api_ssh_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


