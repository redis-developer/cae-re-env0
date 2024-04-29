# DeploymentStepApiFindStepLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[DeploymentStepApiLogEvent]**](DeploymentStepApiLogEvent.md) |  | 
**next_start_time** | [**DeploymentStepApiLogEventTimestamp**](DeploymentStepApiLogEventTimestamp.md) |  | [optional] 
**has_more_logs** | **bool** |  | 

## Example

```python
from env0_client.models.deployment_step_api_find_step_log_response import DeploymentStepApiFindStepLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStepApiFindStepLogResponse from a JSON string
deployment_step_api_find_step_log_response_instance = DeploymentStepApiFindStepLogResponse.from_json(json)
# print the JSON string representation of the object
print(DeploymentStepApiFindStepLogResponse.to_json())

# convert the object into a dict
deployment_step_api_find_step_log_response_dict = deployment_step_api_find_step_log_response_instance.to_dict()
# create an instance of DeploymentStepApiFindStepLogResponse from a dict
deployment_step_api_find_step_log_response_from_dict = DeploymentStepApiFindStepLogResponse.from_dict(deployment_step_api_find_step_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


