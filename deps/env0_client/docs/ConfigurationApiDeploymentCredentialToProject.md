# ConfigurationApiDeploymentCredentialToProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**project_id** | **str** |  | 
**credential_id** | **str** |  | 
**created_by_user_id** | **str** |  | 

## Example

```python
from env0_client.models.configuration_api_deployment_credential_to_project import ConfigurationApiDeploymentCredentialToProject

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationApiDeploymentCredentialToProject from a JSON string
configuration_api_deployment_credential_to_project_instance = ConfigurationApiDeploymentCredentialToProject.from_json(json)
# print the JSON string representation of the object
print(ConfigurationApiDeploymentCredentialToProject.to_json())

# convert the object into a dict
configuration_api_deployment_credential_to_project_dict = configuration_api_deployment_credential_to_project_instance.to_dict()
# create an instance of ConfigurationApiDeploymentCredentialToProject from a dict
configuration_api_deployment_credential_to_project_from_dict = ConfigurationApiDeploymentCredentialToProject.from_dict(configuration_api_deployment_credential_to_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


