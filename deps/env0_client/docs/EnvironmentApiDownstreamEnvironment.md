# EnvironmentApiDownstreamEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**workspace_name** | **str** |  | 
**project_id** | **str** |  | 
**latest_deployment_log** | [**EnvironmentApiDownstreamEnvironmentLatestDeploymentLog**](EnvironmentApiDownstreamEnvironmentLatestDeploymentLog.md) |  | 

## Example

```python
from env0_client.models.environment_api_downstream_environment import EnvironmentApiDownstreamEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiDownstreamEnvironment from a JSON string
environment_api_downstream_environment_instance = EnvironmentApiDownstreamEnvironment.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiDownstreamEnvironment.to_json())

# convert the object into a dict
environment_api_downstream_environment_dict = environment_api_downstream_environment_instance.to_dict()
# create an instance of EnvironmentApiDownstreamEnvironment from a dict
environment_api_downstream_environment_from_dict = EnvironmentApiDownstreamEnvironment.from_dict(environment_api_downstream_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


