# ConfigurationApiUpdateConfigurationSetRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_properties_changes** | [**List[ConfigurationPropertyRequest]**](ConfigurationPropertyRequest.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from env0_client.models.configuration_api_update_configuration_set_request_body import ConfigurationApiUpdateConfigurationSetRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationApiUpdateConfigurationSetRequestBody from a JSON string
configuration_api_update_configuration_set_request_body_instance = ConfigurationApiUpdateConfigurationSetRequestBody.from_json(json)
# print the JSON string representation of the object
print(ConfigurationApiUpdateConfigurationSetRequestBody.to_json())

# convert the object into a dict
configuration_api_update_configuration_set_request_body_dict = configuration_api_update_configuration_set_request_body_instance.to_dict()
# create an instance of ConfigurationApiUpdateConfigurationSetRequestBody from a dict
configuration_api_update_configuration_set_request_body_from_dict = ConfigurationApiUpdateConfigurationSetRequestBody.from_dict(configuration_api_update_configuration_set_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


