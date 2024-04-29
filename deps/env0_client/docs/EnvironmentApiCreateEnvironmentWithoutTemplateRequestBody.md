# EnvironmentApiCreateEnvironmentWithoutTemplateRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy_request** | [**EnvironmentApiCreateEnvironmentWithoutTemplateRequestBodyDeployRequest**](EnvironmentApiCreateEnvironmentWithoutTemplateRequestBodyDeployRequest.md) |  | [optional] 
**name** | **str** |  | 
**project_id** | **object** |  | 
**workspace_name** | **str** |  | [optional] 
**requires_approval** | **bool** |  | [optional] 
**ttl** | [**EnvironmentApiTTLRequest**](EnvironmentApiTTLRequest.md) |  | [optional] 
**configuration_changes** | [**EnvironmentApiConfigurationChanges**](EnvironmentApiConfigurationChanges.md) |  | [optional] 
**vcs_commands_alias** | **str** |  | [optional] 
**continuous_deployment** | **bool** |  | [optional] 
**pull_request_plan_deployments** | **bool** |  | [optional] 
**drift_detection_request** | [**EnvironmentApiDriftDetectionRequest**](EnvironmentApiDriftDetectionRequest.md) |  | [optional] 
**auto_deploy_on_path_changes_only** | **bool** |  | [optional] 
**auto_deploy_by_custom_glob** | **str** |  | [optional] 
**terragrunt_working_directory** | **str** |  | [optional] 
**is_remote_backend** | **bool** |  | [optional] 
**k8s_namespace** | **str** |  | [optional] 
**prevent_auto_deploy** | **bool** |  | [optional] 
**organization_id** | **str** |  | 
**description** | **str** |  | [optional] 
**retry** | [**BlueprintApiRetry**](BlueprintApiRetry.md) |  | [optional] 
**run_tests_on_pull_request** | **bool** |  | [optional] 
**is_terragrunt_run_all** | **bool** |  | [optional] 
**project_ids** | **List[str]** |  | [optional] 
**tag_prefix** | **str** |  | [optional] 
**repository** | **str** |  | 
**revision** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**helm_chart_name** | **str** |  | [optional] 
**terraform_version** | [**BlueprintApiTerraformVersion**](BlueprintApiTerraformVersion.md) | A string representing semantic version of Terraform. If set to \&quot;RESOLVE_FROM_TERRAFORM_CODE\&quot;, the version will be determined by using tfenv&#39;s &#39;min-required&#39;. When set to \&quot;latest\&quot;, the version used will be the most recent one available for Terraform. | [optional] 
**opentofu_version** | **str** |  | [optional] 
**terragrunt_version** | **str** |  | [optional] 
**terragrunt_tf_binary** | [**BlueprintApiTerragruntTfBinary**](BlueprintApiTerragruntTfBinary.md) |  | [optional] 
**pulumi_version** | **str** |  | [optional] 
**type** | [**BlueprintType**](BlueprintType.md) |  | 
**gitlab_project_id** | **object** |  | [optional] 
**token_name** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**ssh_keys** | [**List[BlueprintApiSshKey]**](BlueprintApiSshKey.md) |  | [optional] 
**github_installation_id** | **object** |  | [optional] 
**bitbucket_client_key** | **str** |  | [optional] 
**is_bitbucket_server** | **bool** |  | [optional] 
**is_git_lab_enterprise** | **bool** |  | [optional] 
**is_git_hub_enterprise** | **bool** |  | [optional] 
**is_git_lab** | **bool** |  | [optional] 
**is_azure_dev_ops** | **bool** |  | [optional] 
**is_helm_repository** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.environment_api_create_environment_without_template_request_body import EnvironmentApiCreateEnvironmentWithoutTemplateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiCreateEnvironmentWithoutTemplateRequestBody from a JSON string
environment_api_create_environment_without_template_request_body_instance = EnvironmentApiCreateEnvironmentWithoutTemplateRequestBody.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiCreateEnvironmentWithoutTemplateRequestBody.to_json())

# convert the object into a dict
environment_api_create_environment_without_template_request_body_dict = environment_api_create_environment_without_template_request_body_instance.to_dict()
# create an instance of EnvironmentApiCreateEnvironmentWithoutTemplateRequestBody from a dict
environment_api_create_environment_without_template_request_body_from_dict = EnvironmentApiCreateEnvironmentWithoutTemplateRequestBody.from_dict(environment_api_create_environment_without_template_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


