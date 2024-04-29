# ConfigurationPropertyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**id** | **str** | The ID of the configuration property. If provided, will act as an update. Otherwise, a new configuration property will be created. | [optional] 
**user_id** | **str** |  | [optional] 
**is_sensitive** | **bool** |  | [optional] 
**is_readonly** | **bool** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**regex** | **str** |  | [optional] 
**scope_id** | **str** | The ID of the entity of the provided &#x60;scope&#x60;. e.g. a project&#39;s ID when the provided &#x60;scope&#x60; is &#x60;PROJECT&#x60;. Inapplicable for &#x60;GLOBAL&#x60; scope, as it has no specific entity. | [optional] 
**scope** | [**ConfigurationScope**](ConfigurationScope.md) |  | [optional] 
**type** | [**ConfigurationType**](ConfigurationType.md) | Whether it is an Environment or Terraform variable 0 value maps to an Environment variable 1 value maps to an Terraform variable | [optional] 
**project_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**var_schema** | [**PartialJSONSchema7**](PartialJSONSchema7.md) | If none passed, JSON and HCL values will be considered to be of string type. Make sure you specify the correct variable type. ENVIRONMENT_OUTPUT is a special type that is used to indicate that the value is an output from the environment. Its is of format ${env0:&lt;environmentId&gt;:&lt;outputName&gt;} | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from env0_client.models.configuration_property_response import ConfigurationPropertyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationPropertyResponse from a JSON string
configuration_property_response_instance = ConfigurationPropertyResponse.from_json(json)
# print the JSON string representation of the object
print(ConfigurationPropertyResponse.to_json())

# convert the object into a dict
configuration_property_response_dict = configuration_property_response_instance.to_dict()
# create an instance of ConfigurationPropertyResponse from a dict
configuration_property_response_from_dict = ConfigurationPropertyResponse.from_dict(configuration_property_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


