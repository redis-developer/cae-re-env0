# EnvironmentApiFindDeploymentLogsByEnvironmentIdRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **str** |  | [optional] 
**offset** | **str** |  | [optional] 
**from_date** | **str** |  | [optional] 
**to_date** | **str** |  | [optional] 
**deployment_types** | [**EnvironmentApiDeploymentType**](EnvironmentApiDeploymentType.md) |  | [optional] 
**statuses** | [**EnvironmentApiDeploymentLogStatus**](EnvironmentApiDeploymentLogStatus.md) |  | [optional] 

## Example

```python
from env0_client.models.environment_api_find_deployment_logs_by_environment_id_request_query_params import EnvironmentApiFindDeploymentLogsByEnvironmentIdRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiFindDeploymentLogsByEnvironmentIdRequestQueryParams from a JSON string
environment_api_find_deployment_logs_by_environment_id_request_query_params_instance = EnvironmentApiFindDeploymentLogsByEnvironmentIdRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiFindDeploymentLogsByEnvironmentIdRequestQueryParams.to_json())

# convert the object into a dict
environment_api_find_deployment_logs_by_environment_id_request_query_params_dict = environment_api_find_deployment_logs_by_environment_id_request_query_params_instance.to_dict()
# create an instance of EnvironmentApiFindDeploymentLogsByEnvironmentIdRequestQueryParams from a dict
environment_api_find_deployment_logs_by_environment_id_request_query_params_from_dict = EnvironmentApiFindDeploymentLogsByEnvironmentIdRequestQueryParams.from_dict(environment_api_find_deployment_logs_by_environment_id_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


