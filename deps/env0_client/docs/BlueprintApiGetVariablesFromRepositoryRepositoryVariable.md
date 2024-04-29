# BlueprintApiGetVariablesFromRepositoryRepositoryVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | [optional] 
**id** | **str** | The ID of the configuration property. If provided, will act as an update. Otherwise, a new configuration property will be created. | [optional] 
**is_sensitive** | **bool** |  | [optional] 
**is_readonly** | **bool** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**regex** | **str** |  | [optional] 
**scope** | [**ConfigurationScope**](ConfigurationScope.md) |  | 
**type** | [**ConfigurationType**](ConfigurationType.md) | Whether it is an Environment or Terraform variable 0 value maps to an Environment variable 1 value maps to an Terraform variable | 
**to_delete** | **bool** |  | [optional] 
**project_id** | **str** |  | [optional] 
**var_schema** | [**PartialJSONSchema7**](PartialJSONSchema7.md) | If none passed, JSON and HCL values will be considered to be of string type. Make sure you specify the correct variable type. ENVIRONMENT_OUTPUT is a special type that is used to indicate that the value is an output from the environment. Its is of format ${env0:&lt;environmentId&gt;:&lt;outputName&gt;} | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from env0_client.models.blueprint_api_get_variables_from_repository_repository_variable import BlueprintApiGetVariablesFromRepositoryRepositoryVariable

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiGetVariablesFromRepositoryRepositoryVariable from a JSON string
blueprint_api_get_variables_from_repository_repository_variable_instance = BlueprintApiGetVariablesFromRepositoryRepositoryVariable.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiGetVariablesFromRepositoryRepositoryVariable.to_json())

# convert the object into a dict
blueprint_api_get_variables_from_repository_repository_variable_dict = blueprint_api_get_variables_from_repository_repository_variable_instance.to_dict()
# create an instance of BlueprintApiGetVariablesFromRepositoryRepositoryVariable from a dict
blueprint_api_get_variables_from_repository_repository_variable_from_dict = BlueprintApiGetVariablesFromRepositoryRepositoryVariable.from_dict(blueprint_api_get_variables_from_repository_repository_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


