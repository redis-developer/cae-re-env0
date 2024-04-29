# SchedulingApiScheduledAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**environment_id** | **str** |  | 
**project_id** | **str** |  | 
**organization_id** | **str** |  | 
**cron** | **str** |  | 
**next_schedule** | **datetime** |  | [optional] 
**enabled** | **bool** |  | 

## Example

```python
from env0_client.models.scheduling_api_scheduled_action import SchedulingApiScheduledAction

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingApiScheduledAction from a JSON string
scheduling_api_scheduled_action_instance = SchedulingApiScheduledAction.from_json(json)
# print the JSON string representation of the object
print(SchedulingApiScheduledAction.to_json())

# convert the object into a dict
scheduling_api_scheduled_action_dict = scheduling_api_scheduled_action_instance.to_dict()
# create an instance of SchedulingApiScheduledAction from a dict
scheduling_api_scheduled_action_from_dict = SchedulingApiScheduledAction.from_dict(scheduling_api_scheduled_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


