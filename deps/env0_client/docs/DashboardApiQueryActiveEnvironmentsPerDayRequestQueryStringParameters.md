# DashboardApiQueryActiveEnvironmentsPerDayRequestQueryStringParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** |  | 
**end_time** | **str** |  | 
**query_name** | **object** |  | 
**organization_id** | **str** |  | 

## Example

```python
from env0_client.models.dashboard_api_query_active_environments_per_day_request_query_string_parameters import DashboardApiQueryActiveEnvironmentsPerDayRequestQueryStringParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardApiQueryActiveEnvironmentsPerDayRequestQueryStringParameters from a JSON string
dashboard_api_query_active_environments_per_day_request_query_string_parameters_instance = DashboardApiQueryActiveEnvironmentsPerDayRequestQueryStringParameters.from_json(json)
# print the JSON string representation of the object
print(DashboardApiQueryActiveEnvironmentsPerDayRequestQueryStringParameters.to_json())

# convert the object into a dict
dashboard_api_query_active_environments_per_day_request_query_string_parameters_dict = dashboard_api_query_active_environments_per_day_request_query_string_parameters_instance.to_dict()
# create an instance of DashboardApiQueryActiveEnvironmentsPerDayRequestQueryStringParameters from a dict
dashboard_api_query_active_environments_per_day_request_query_string_parameters_from_dict = DashboardApiQueryActiveEnvironmentsPerDayRequestQueryStringParameters.from_dict(dashboard_api_query_active_environments_per_day_request_query_string_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


