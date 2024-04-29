# EnvironmentApiBatchCancelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 

## Example

```python
from env0_client.models.environment_api_batch_cancel_response import EnvironmentApiBatchCancelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiBatchCancelResponse from a JSON string
environment_api_batch_cancel_response_instance = EnvironmentApiBatchCancelResponse.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiBatchCancelResponse.to_json())

# convert the object into a dict
environment_api_batch_cancel_response_dict = environment_api_batch_cancel_response_instance.to_dict()
# create an instance of EnvironmentApiBatchCancelResponse from a dict
environment_api_batch_cancel_response_from_dict = EnvironmentApiBatchCancelResponse.from_dict(environment_api_batch_cancel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


