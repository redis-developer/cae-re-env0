# BlueprintApiRetryDeployOrDestroyConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**times** | **float** |  | 
**error_regex** | **str** |  | [optional] 

## Example

```python
from env0_client.models.blueprint_api_retry_deploy_or_destroy_config import BlueprintApiRetryDeployOrDestroyConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiRetryDeployOrDestroyConfig from a JSON string
blueprint_api_retry_deploy_or_destroy_config_instance = BlueprintApiRetryDeployOrDestroyConfig.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiRetryDeployOrDestroyConfig.to_json())

# convert the object into a dict
blueprint_api_retry_deploy_or_destroy_config_dict = blueprint_api_retry_deploy_or_destroy_config_instance.to_dict()
# create an instance of BlueprintApiRetryDeployOrDestroyConfig from a dict
blueprint_api_retry_deploy_or_destroy_config_from_dict = BlueprintApiRetryDeployOrDestroyConfig.from_dict(blueprint_api_retry_deploy_or_destroy_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


