# EnvironmentApiEnvironmentNextScheduledDates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy** | **datetime** |  | [optional] 
**destroy** | **datetime** |  | [optional] 

## Example

```python
from env0_client.models.environment_api_environment_next_scheduled_dates import EnvironmentApiEnvironmentNextScheduledDates

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiEnvironmentNextScheduledDates from a JSON string
environment_api_environment_next_scheduled_dates_instance = EnvironmentApiEnvironmentNextScheduledDates.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiEnvironmentNextScheduledDates.to_json())

# convert the object into a dict
environment_api_environment_next_scheduled_dates_dict = environment_api_environment_next_scheduled_dates_instance.to_dict()
# create an instance of EnvironmentApiEnvironmentNextScheduledDates from a dict
environment_api_environment_next_scheduled_dates_from_dict = EnvironmentApiEnvironmentNextScheduledDates.from_dict(environment_api_environment_next_scheduled_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


