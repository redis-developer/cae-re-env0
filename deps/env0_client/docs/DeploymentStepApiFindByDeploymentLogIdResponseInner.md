# DeploymentStepApiFindByDeploymentLogIdResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deployment_log_id** | **str** |  | 
**name** | **str** |  | 
**order** | **float** |  | 
**environment_id** | **str** |  | [optional] 
**project_id** | **str** |  | 
**organization_id** | **str** |  | 
**status** | [**DeploymentStepApiDeploymentStepStatus**](DeploymentStepApiDeploymentStepStatus.md) |  | 
**started_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**display_name** | **str** |  | [optional] 
**retry_count** | **float** |  | [optional] 

## Example

```python
from env0_client.models.deployment_step_api_find_by_deployment_log_id_response_inner import DeploymentStepApiFindByDeploymentLogIdResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStepApiFindByDeploymentLogIdResponseInner from a JSON string
deployment_step_api_find_by_deployment_log_id_response_inner_instance = DeploymentStepApiFindByDeploymentLogIdResponseInner.from_json(json)
# print the JSON string representation of the object
print(DeploymentStepApiFindByDeploymentLogIdResponseInner.to_json())

# convert the object into a dict
deployment_step_api_find_by_deployment_log_id_response_inner_dict = deployment_step_api_find_by_deployment_log_id_response_inner_instance.to_dict()
# create an instance of DeploymentStepApiFindByDeploymentLogIdResponseInner from a dict
deployment_step_api_find_by_deployment_log_id_response_inner_from_dict = DeploymentStepApiFindByDeploymentLogIdResponseInner.from_dict(deployment_step_api_find_by_deployment_log_id_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


