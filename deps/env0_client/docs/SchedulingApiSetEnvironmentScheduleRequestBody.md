# SchedulingApiSetEnvironmentScheduleRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy** | [**SchedulingApiSetEnvironmentScheduleRequestScheduledAction**](SchedulingApiSetEnvironmentScheduleRequestScheduledAction.md) |  | [optional] 
**destroy** | [**SchedulingApiSetEnvironmentScheduleRequestScheduledAction**](SchedulingApiSetEnvironmentScheduleRequestScheduledAction.md) |  | [optional] 

## Example

```python
from env0_client.models.scheduling_api_set_environment_schedule_request_body import SchedulingApiSetEnvironmentScheduleRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingApiSetEnvironmentScheduleRequestBody from a JSON string
scheduling_api_set_environment_schedule_request_body_instance = SchedulingApiSetEnvironmentScheduleRequestBody.from_json(json)
# print the JSON string representation of the object
print(SchedulingApiSetEnvironmentScheduleRequestBody.to_json())

# convert the object into a dict
scheduling_api_set_environment_schedule_request_body_dict = scheduling_api_set_environment_schedule_request_body_instance.to_dict()
# create an instance of SchedulingApiSetEnvironmentScheduleRequestBody from a dict
scheduling_api_set_environment_schedule_request_body_from_dict = SchedulingApiSetEnvironmentScheduleRequestBody.from_dict(scheduling_api_set_environment_schedule_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


