# ConfigurationApiToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 
**organization_id** | **str** |  | 
**type** | [**TokenTypes**](TokenTypes.md) |  | 

## Example

```python
from env0_client.models.configuration_api_token import ConfigurationApiToken

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationApiToken from a JSON string
configuration_api_token_instance = ConfigurationApiToken.from_json(json)
# print the JSON string representation of the object
print(ConfigurationApiToken.to_json())

# convert the object into a dict
configuration_api_token_dict = configuration_api_token_instance.to_dict()
# create an instance of ConfigurationApiToken from a dict
configuration_api_token_from_dict = ConfigurationApiToken.from_dict(configuration_api_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


