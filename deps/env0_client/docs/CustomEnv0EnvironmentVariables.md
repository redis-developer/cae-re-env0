# CustomEnv0EnvironmentVariables


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_id** | **str** | The deployed Environment ID | [optional] 
**project_id** | **str** | ENV0_PROJECT_ID | [optional] 
**project_name** | **str** | The Project Name of the deployed Environment | [optional] 
**deployment_log_id** | **str** | The deployment ID | [optional] 
**deployment_type** | **str** | The deployment type. | [optional] 
**deployment_revision** | **str** | Available only when deployment revision defined | [optional] 
**workspace_name** | **str** | The Terraform Workspace name used in the Environment | [optional] 
**root_dir** | **str** | The root repository path | [optional] 
**organization_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**template_dir** | **str** |  | [optional] 
**template_name** | **str** |  | [optional] 
**environment_name** | **str** |  | [optional] 
**environment_creator_name** | **str** |  | [optional] 
**environment_creator_email** | **str** |  | [optional] 
**deployer_name** | **str** |  | [optional] 
**deployer_email** | **str** |  | [optional] 
**reviewer_name** | **str** |  | [optional] 
**reviewer_email** | **str** |  | [optional] 
**pr_author** | **str** | pr author. available only in PR Plan | [optional] 
**pr_source_branch** | **str** | the source branch. available only in PR Plan | [optional] 
**pr_target_branch** | **str** | the target branch. available only in PR Plan | [optional] 
**commit_hash** | **str** | the commit hash | [optional] 
**commit_url** | **str** | the commit url | [optional] 
**oidc_token** | **str** | The OIDC Token - read more here(https://docs.env0.com/docs/oidc-integrations) on how to enable it and use it | [optional] 
**vcs_access_token** | **str** | When using a native VCS integration, this will represent the access token we use to clone the repository | [optional] 
**tf_plan_json** | **str** | The file path to a JSON representation of a Terraform Plan file | [optional] 
**cli_args_plan** | **str** | add additional cli arguments when running a plan | [optional] 
**cli_args_apply** | **str** | add additional cli arguments when running the &#x60;apply&#x60; command | [optional] 

## Example

```python
from env0_client.models.custom_env0_environment_variables import CustomEnv0EnvironmentVariables

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEnv0EnvironmentVariables from a JSON string
custom_env0_environment_variables_instance = CustomEnv0EnvironmentVariables.from_json(json)
# print the JSON string representation of the object
print(CustomEnv0EnvironmentVariables.to_json())

# convert the object into a dict
custom_env0_environment_variables_dict = custom_env0_environment_variables_instance.to_dict()
# create an instance of CustomEnv0EnvironmentVariables from a dict
custom_env0_environment_variables_from_dict = CustomEnv0EnvironmentVariables.from_dict(custom_env0_environment_variables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


