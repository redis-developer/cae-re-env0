# ConfigurationApiFindVariablesByScopeOverridingConfigurationPropertyOverwritesAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**ConfigurationScope**](ConfigurationScope.md) |  | 
**scope_id** | **object** | The ID of the entity of the provided &#x60;scope&#x60;. e.g. a project&#39;s ID when the provided &#x60;scope&#x60; is &#x60;PROJECT&#x60;. Inapplicable for &#x60;GLOBAL&#x60; scope, as it has no specific entity. | [optional] 
**value** | **str** |  | [optional] 
**var_schema** | [**PartialJSONSchema7**](PartialJSONSchema7.md) | If none passed, JSON and HCL values will be considered to be of string type. Make sure you specify the correct variable type. ENVIRONMENT_OUTPUT is a special type that is used to indicate that the value is an output from the environment. Its is of format ${env0:&lt;environmentId&gt;:&lt;outputName&gt;} | [optional] 
**is_readonly** | **bool** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**is_sensitive** | **bool** |  | [optional] 
**regex** | **str** |  | [optional] 

## Example

```python
from env0_client.models.configuration_api_find_variables_by_scope_overriding_configuration_property_overwrites_any_of import ConfigurationApiFindVariablesByScopeOverridingConfigurationPropertyOverwritesAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationApiFindVariablesByScopeOverridingConfigurationPropertyOverwritesAnyOf from a JSON string
configuration_api_find_variables_by_scope_overriding_configuration_property_overwrites_any_of_instance = ConfigurationApiFindVariablesByScopeOverridingConfigurationPropertyOverwritesAnyOf.from_json(json)
# print the JSON string representation of the object
print(ConfigurationApiFindVariablesByScopeOverridingConfigurationPropertyOverwritesAnyOf.to_json())

# convert the object into a dict
configuration_api_find_variables_by_scope_overriding_configuration_property_overwrites_any_of_dict = configuration_api_find_variables_by_scope_overriding_configuration_property_overwrites_any_of_instance.to_dict()
# create an instance of ConfigurationApiFindVariablesByScopeOverridingConfigurationPropertyOverwritesAnyOf from a dict
configuration_api_find_variables_by_scope_overriding_configuration_property_overwrites_any_of_from_dict = ConfigurationApiFindVariablesByScopeOverridingConfigurationPropertyOverwritesAnyOf.from_dict(configuration_api_find_variables_by_scope_overriding_configuration_property_overwrites_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


