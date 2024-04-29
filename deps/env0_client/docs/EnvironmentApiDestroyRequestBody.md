# EnvironmentApiDestroyRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_name** | [**TriggerName**](TriggerName.md) |  | [optional] 
**workflow_deployment_id** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from env0_client.models.environment_api_destroy_request_body import EnvironmentApiDestroyRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiDestroyRequestBody from a JSON string
environment_api_destroy_request_body_instance = EnvironmentApiDestroyRequestBody.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiDestroyRequestBody.to_json())

# convert the object into a dict
environment_api_destroy_request_body_dict = environment_api_destroy_request_body_instance.to_dict()
# create an instance of EnvironmentApiDestroyRequestBody from a dict
environment_api_destroy_request_body_from_dict = EnvironmentApiDestroyRequestBody.from_dict(environment_api_destroy_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


