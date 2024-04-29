# ConfigurationApiCreateConfigurationSetRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**SetCreationScope**](SetCreationScope.md) |  | 
**scope_id** | **str** |  | 
**configuration_properties** | [**List[ConfigurationPropertyRequest]**](ConfigurationPropertyRequest.md) |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from env0_client.models.configuration_api_create_configuration_set_request_body import ConfigurationApiCreateConfigurationSetRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationApiCreateConfigurationSetRequestBody from a JSON string
configuration_api_create_configuration_set_request_body_instance = ConfigurationApiCreateConfigurationSetRequestBody.from_json(json)
# print the JSON string representation of the object
print(ConfigurationApiCreateConfigurationSetRequestBody.to_json())

# convert the object into a dict
configuration_api_create_configuration_set_request_body_dict = configuration_api_create_configuration_set_request_body_instance.to_dict()
# create an instance of ConfigurationApiCreateConfigurationSetRequestBody from a dict
configuration_api_create_configuration_set_request_body_from_dict = ConfigurationApiCreateConfigurationSetRequestBody.from_dict(configuration_api_create_configuration_set_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


