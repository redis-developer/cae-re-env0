# EnvironmentApiCheckLimitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | [**EnvironmentApiCheckLimitEnvironmentLimitsWarnings**](EnvironmentApiCheckLimitEnvironmentLimitsWarnings.md) |  | [optional] 
**total** | **float** |  | [optional] 
**user** | **float** |  | [optional] 

## Example

```python
from env0_client.models.environment_api_check_limit_response import EnvironmentApiCheckLimitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiCheckLimitResponse from a JSON string
environment_api_check_limit_response_instance = EnvironmentApiCheckLimitResponse.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiCheckLimitResponse.to_json())

# convert the object into a dict
environment_api_check_limit_response_dict = environment_api_check_limit_response_instance.to_dict()
# create an instance of EnvironmentApiCheckLimitResponse from a dict
environment_api_check_limit_response_from_dict = EnvironmentApiCheckLimitResponse.from_dict(environment_api_check_limit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


