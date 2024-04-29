# EnvironmentApiSubscribeDownstreamEnvironmentsRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downstream_environment_ids** | **List[str]** |  | 

## Example

```python
from env0_client.models.environment_api_subscribe_downstream_environments_request_body import EnvironmentApiSubscribeDownstreamEnvironmentsRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiSubscribeDownstreamEnvironmentsRequestBody from a JSON string
environment_api_subscribe_downstream_environments_request_body_instance = EnvironmentApiSubscribeDownstreamEnvironmentsRequestBody.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiSubscribeDownstreamEnvironmentsRequestBody.to_json())

# convert the object into a dict
environment_api_subscribe_downstream_environments_request_body_dict = environment_api_subscribe_downstream_environments_request_body_instance.to_dict()
# create an instance of EnvironmentApiSubscribeDownstreamEnvironmentsRequestBody from a dict
environment_api_subscribe_downstream_environments_request_body_from_dict = EnvironmentApiSubscribeDownstreamEnvironmentsRequestBody.from_dict(environment_api_subscribe_downstream_environments_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


