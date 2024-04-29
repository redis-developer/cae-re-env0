# EnvironmentApiTTLRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EnvironmentApiTTLType**](EnvironmentApiTTLType.md) |  | 
**value** | **str** | Format is yyyy-mm-ddThh:MM:ss.000Z (For example 2023-06-04T20:05:00.000Z) | [optional] 

## Example

```python
from env0_client.models.environment_api_ttl_request import EnvironmentApiTTLRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiTTLRequest from a JSON string
environment_api_ttl_request_instance = EnvironmentApiTTLRequest.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiTTLRequest.to_json())

# convert the object into a dict
environment_api_ttl_request_dict = environment_api_ttl_request_instance.to_dict()
# create an instance of EnvironmentApiTTLRequest from a dict
environment_api_ttl_request_from_dict = EnvironmentApiTTLRequest.from_dict(environment_api_ttl_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


