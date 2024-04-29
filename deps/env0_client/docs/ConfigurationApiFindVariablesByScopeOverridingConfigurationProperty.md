# ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overwrites** | [**ConfigurationApiFindVariablesByScopeOverridingConfigurationPropertyOverwrites**](ConfigurationApiFindVariablesByScopeOverridingConfigurationPropertyOverwrites.md) |  | 
**created_at** | **datetime** |  | [optional] 
**name** | **str** |  | 
**value** | **str** |  | [optional] 
**id** | **object** | The ID of the configuration property. If provided, will act as an update. Otherwise, a new configuration property will be created. | [optional] 
**user_id** | **str** |  | [optional] 
**is_sensitive** | **bool** |  | [optional] 
**is_readonly** | **bool** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**regex** | **str** |  | [optional] 
**scope_id** | **object** | The ID of the entity of the provided &#x60;scope&#x60;. e.g. a project&#39;s ID when the provided &#x60;scope&#x60; is &#x60;PROJECT&#x60;. Inapplicable for &#x60;GLOBAL&#x60; scope, as it has no specific entity. | [optional] 
**scope** | [**ConfigurationScope**](ConfigurationScope.md) |  | 
**type** | [**ConfigurationType**](ConfigurationType.md) | Whether it is an Environment or Terraform variable 0 value maps to an Environment variable 1 value maps to an Terraform variable | 
**to_delete** | **bool** |  | [optional] 
**project_id** | **str** |  | [optional] 
**organization_id** | **str** |  | 
**var_schema** | [**PartialJSONSchema7**](PartialJSONSchema7.md) | If none passed, JSON and HCL values will be considered to be of string type. Make sure you specify the correct variable type. ENVIRONMENT_OUTPUT is a special type that is used to indicate that the value is an output from the environment. Its is of format ${env0:&lt;environmentId&gt;:&lt;outputName&gt;} | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from env0_client.models.configuration_api_find_variables_by_scope_overriding_configuration_property import ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty from a JSON string
configuration_api_find_variables_by_scope_overriding_configuration_property_instance = ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty.from_json(json)
# print the JSON string representation of the object
print(ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty.to_json())

# convert the object into a dict
configuration_api_find_variables_by_scope_overriding_configuration_property_dict = configuration_api_find_variables_by_scope_overriding_configuration_property_instance.to_dict()
# create an instance of ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty from a dict
configuration_api_find_variables_by_scope_overriding_configuration_property_from_dict = ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty.from_dict(configuration_api_find_variables_by_scope_overriding_configuration_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


