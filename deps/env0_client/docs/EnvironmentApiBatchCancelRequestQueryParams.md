# EnvironmentApiBatchCancelRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**EnvironmentApiDeploymentLogStatus**](EnvironmentApiDeploymentLogStatus.md) |  | 

## Example

```python
from env0_client.models.environment_api_batch_cancel_request_query_params import EnvironmentApiBatchCancelRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiBatchCancelRequestQueryParams from a JSON string
environment_api_batch_cancel_request_query_params_instance = EnvironmentApiBatchCancelRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiBatchCancelRequestQueryParams.to_json())

# convert the object into a dict
environment_api_batch_cancel_request_query_params_dict = environment_api_batch_cancel_request_query_params_instance.to_dict()
# create an instance of EnvironmentApiBatchCancelRequestQueryParams from a dict
environment_api_batch_cancel_request_query_params_from_dict = EnvironmentApiBatchCancelRequestQueryParams.from_dict(environment_api_batch_cancel_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


