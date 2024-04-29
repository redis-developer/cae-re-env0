# DashboardApiQueryRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** |  | 
**end_time** | **str** |  | 
**query_name** | **object** |  | 
**organization_id** | **str** |  | 

## Example

```python
from env0_client.models.dashboard_api_query_request_query_params import DashboardApiQueryRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardApiQueryRequestQueryParams from a JSON string
dashboard_api_query_request_query_params_instance = DashboardApiQueryRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(DashboardApiQueryRequestQueryParams.to_json())

# convert the object into a dict
dashboard_api_query_request_query_params_dict = dashboard_api_query_request_query_params_instance.to_dict()
# create an instance of DashboardApiQueryRequestQueryParams from a dict
dashboard_api_query_request_query_params_from_dict = DashboardApiQueryRequestQueryParams.from_dict(dashboard_api_query_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


