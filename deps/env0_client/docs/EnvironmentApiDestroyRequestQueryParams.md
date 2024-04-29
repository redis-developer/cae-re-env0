# EnvironmentApiDestroyRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_updated_code** | [**EnvironmentApiQueryBoolean**](EnvironmentApiQueryBoolean.md) |  | [optional] 
**is_scheduled_run** | [**EnvironmentApiQueryBoolean**](EnvironmentApiQueryBoolean.md) |  | [optional] 
**skip_state_refresh** | [**EnvironmentApiQueryBoolean**](EnvironmentApiQueryBoolean.md) |  | [optional] 
**revision** | **str** |  | [optional] 
**requires_approval** | [**EnvironmentApiQueryBoolean**](EnvironmentApiQueryBoolean.md) |  | [optional] 

## Example

```python
from env0_client.models.environment_api_destroy_request_query_params import EnvironmentApiDestroyRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiDestroyRequestQueryParams from a JSON string
environment_api_destroy_request_query_params_instance = EnvironmentApiDestroyRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiDestroyRequestQueryParams.to_json())

# convert the object into a dict
environment_api_destroy_request_query_params_dict = environment_api_destroy_request_query_params_instance.to_dict()
# create an instance of EnvironmentApiDestroyRequestQueryParams from a dict
environment_api_destroy_request_query_params_from_dict = EnvironmentApiDestroyRequestQueryParams.from_dict(environment_api_destroy_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


