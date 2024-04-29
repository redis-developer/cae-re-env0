# ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 
**organization_id** | **str** |  | 
**type** | [**TokenTypes**](TokenTypes.md) |  | 
**id** | **str** |  | 

## Example

```python
from env0_client.models.configuration_api_abstract_secret_response_configuration_api_persistent_token import ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken from a JSON string
configuration_api_abstract_secret_response_configuration_api_persistent_token_instance = ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken.from_json(json)
# print the JSON string representation of the object
print(ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken.to_json())

# convert the object into a dict
configuration_api_abstract_secret_response_configuration_api_persistent_token_dict = configuration_api_abstract_secret_response_configuration_api_persistent_token_instance.to_dict()
# create an instance of ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken from a dict
configuration_api_abstract_secret_response_configuration_api_persistent_token_from_dict = ConfigurationApiAbstractSecretResponseConfigurationApiPersistentToken.from_dict(configuration_api_abstract_secret_response_configuration_api_persistent_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


