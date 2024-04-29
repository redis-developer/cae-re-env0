# BlueprintApiRetryOnDestroy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**times** | **float** |  | 
**error_regex** | **str** |  | [optional] 

## Example

```python
from env0_client.models.blueprint_api_retry_on_destroy import BlueprintApiRetryOnDestroy

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiRetryOnDestroy from a JSON string
blueprint_api_retry_on_destroy_instance = BlueprintApiRetryOnDestroy.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiRetryOnDestroy.to_json())

# convert the object into a dict
blueprint_api_retry_on_destroy_dict = blueprint_api_retry_on_destroy_instance.to_dict()
# create an instance of BlueprintApiRetryOnDestroy from a dict
blueprint_api_retry_on_destroy_from_dict = BlueprintApiRetryOnDestroy.from_dict(blueprint_api_retry_on_destroy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


