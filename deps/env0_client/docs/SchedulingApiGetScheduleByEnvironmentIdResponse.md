# SchedulingApiGetScheduleByEnvironmentIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy** | [**SchedulingApiScheduledAction**](SchedulingApiScheduledAction.md) |  | [optional] 
**destroy** | [**SchedulingApiScheduledAction**](SchedulingApiScheduledAction.md) |  | [optional] 

## Example

```python
from env0_client.models.scheduling_api_get_schedule_by_environment_id_response import SchedulingApiGetScheduleByEnvironmentIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingApiGetScheduleByEnvironmentIdResponse from a JSON string
scheduling_api_get_schedule_by_environment_id_response_instance = SchedulingApiGetScheduleByEnvironmentIdResponse.from_json(json)
# print the JSON string representation of the object
print(SchedulingApiGetScheduleByEnvironmentIdResponse.to_json())

# convert the object into a dict
scheduling_api_get_schedule_by_environment_id_response_dict = scheduling_api_get_schedule_by_environment_id_response_instance.to_dict()
# create an instance of SchedulingApiGetScheduleByEnvironmentIdResponse from a dict
scheduling_api_get_schedule_by_environment_id_response_from_dict = SchedulingApiGetScheduleByEnvironmentIdResponse.from_dict(scheduling_api_get_schedule_by_environment_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


