# EnvironmentApiCountByProjectRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **str** |  | [optional] 
**status** | [**EnvironmentApiEnvironmentStatus**](EnvironmentApiEnvironmentStatus.md) |  | [optional] 
**project_id** | **str** |  | 

## Example

```python
from env0_client.models.environment_api_count_by_project_request_query_params import EnvironmentApiCountByProjectRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiCountByProjectRequestQueryParams from a JSON string
environment_api_count_by_project_request_query_params_instance = EnvironmentApiCountByProjectRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiCountByProjectRequestQueryParams.to_json())

# convert the object into a dict
environment_api_count_by_project_request_query_params_dict = environment_api_count_by_project_request_query_params_instance.to_dict()
# create an instance of EnvironmentApiCountByProjectRequestQueryParams from a dict
environment_api_count_by_project_request_query_params_from_dict = EnvironmentApiCountByProjectRequestQueryParams.from_dict(environment_api_count_by_project_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


