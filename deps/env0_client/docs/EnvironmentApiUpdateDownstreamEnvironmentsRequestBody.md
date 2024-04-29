# EnvironmentApiUpdateDownstreamEnvironmentsRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downstream_environment_ids** | **List[str]** |  | 

## Example

```python
from env0_client.models.environment_api_update_downstream_environments_request_body import EnvironmentApiUpdateDownstreamEnvironmentsRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiUpdateDownstreamEnvironmentsRequestBody from a JSON string
environment_api_update_downstream_environments_request_body_instance = EnvironmentApiUpdateDownstreamEnvironmentsRequestBody.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiUpdateDownstreamEnvironmentsRequestBody.to_json())

# convert the object into a dict
environment_api_update_downstream_environments_request_body_dict = environment_api_update_downstream_environments_request_body_instance.to_dict()
# create an instance of EnvironmentApiUpdateDownstreamEnvironmentsRequestBody from a dict
environment_api_update_downstream_environments_request_body_from_dict = EnvironmentApiUpdateDownstreamEnvironmentsRequestBody.from_dict(environment_api_update_downstream_environments_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


