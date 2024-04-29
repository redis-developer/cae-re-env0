# EnvironmentApiDriftDetectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**cron** | **str** |  | [optional] 

## Example

```python
from env0_client.models.environment_api_drift_detection_request import EnvironmentApiDriftDetectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiDriftDetectionRequest from a JSON string
environment_api_drift_detection_request_instance = EnvironmentApiDriftDetectionRequest.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiDriftDetectionRequest.to_json())

# convert the object into a dict
environment_api_drift_detection_request_dict = environment_api_drift_detection_request_instance.to_dict()
# create an instance of EnvironmentApiDriftDetectionRequest from a dict
environment_api_drift_detection_request_from_dict = EnvironmentApiDriftDetectionRequest.from_dict(environment_api_drift_detection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


