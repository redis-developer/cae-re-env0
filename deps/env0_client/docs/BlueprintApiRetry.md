# BlueprintApiRetry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_destroy** | [**BlueprintApiRetryOnDestroy**](BlueprintApiRetryOnDestroy.md) |  | [optional] 
**on_deploy** | [**BlueprintApiRetryOnDestroy**](BlueprintApiRetryOnDestroy.md) |  | [optional] 

## Example

```python
from env0_client.models.blueprint_api_retry import BlueprintApiRetry

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiRetry from a JSON string
blueprint_api_retry_instance = BlueprintApiRetry.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiRetry.to_json())

# convert the object into a dict
blueprint_api_retry_dict = blueprint_api_retry_instance.to_dict()
# create an instance of BlueprintApiRetry from a dict
blueprint_api_retry_from_dict = BlueprintApiRetry.from_dict(blueprint_api_retry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


