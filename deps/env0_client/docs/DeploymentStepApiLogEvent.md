# DeploymentStepApiLogEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** |  | 
**message** | **str** |  | 
**level** | **str** |  | 
**timestamp** | [**DeploymentStepApiLogEventTimestamp**](DeploymentStepApiLogEventTimestamp.md) |  | 

## Example

```python
from env0_client.models.deployment_step_api_log_event import DeploymentStepApiLogEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStepApiLogEvent from a JSON string
deployment_step_api_log_event_instance = DeploymentStepApiLogEvent.from_json(json)
# print the JSON string representation of the object
print(DeploymentStepApiLogEvent.to_json())

# convert the object into a dict
deployment_step_api_log_event_dict = deployment_step_api_log_event_instance.to_dict()
# create an instance of DeploymentStepApiLogEvent from a dict
deployment_step_api_log_event_from_dict = DeploymentStepApiLogEvent.from_dict(deployment_step_api_log_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


