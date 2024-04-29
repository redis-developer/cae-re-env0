# BlueprintApiEnvironmentDiscoveryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**glob_pattern** | **str** |  | 
**environment_placement** | [**BlueprintApiEnvironmentPlacement**](BlueprintApiEnvironmentPlacement.md) |  | 
**workspace_naming** | [**BlueprintApiWorkspaceNaming**](BlueprintApiWorkspaceNaming.md) |  | 
**auto_deploy_by_custom_glob** | **str** |  | [optional] 
**root_path** | **str** |  | [optional] 
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
**gitlab_project_id** | **float** |  | [optional] 
**token_name** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**ssh_keys** | [**List[BlueprintApiSshKey]**](BlueprintApiSshKey.md) |  | [optional] 
**github_installation_id** | **float** |  | [optional] 
**bitbucket_client_key** | **str** |  | [optional] 
**is_bitbucket_server** | **bool** |  | [optional] 
**is_git_lab_enterprise** | **bool** |  | [optional] 
**is_git_hub_enterprise** | **bool** |  | [optional] 
**is_git_lab** | **bool** |  | [optional] 
**is_azure_dev_ops** | **bool** |  | [optional] 
**is_helm_repository** | **bool** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**retry** | [**BlueprintApiRetry**](BlueprintApiRetry.md) |  | [optional] 
**run_tests_on_pull_request** | **bool** |  | [optional] 
**is_terragrunt_run_all** | **bool** |  | [optional] 
**project_ids** | **List[str]** |  | [optional] 
**tag_prefix** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**author** | [**User**](User.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**author_id** | **str** |  | [optional] 
**organization_id** | **str** |  | 
**project_id** | **str** |  | [optional] 
**is_single_use** | **bool** |  | [optional] 

## Example

```python
from env0_client.models.blueprint_api_environment_discovery_response import BlueprintApiEnvironmentDiscoveryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiEnvironmentDiscoveryResponse from a JSON string
blueprint_api_environment_discovery_response_instance = BlueprintApiEnvironmentDiscoveryResponse.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiEnvironmentDiscoveryResponse.to_json())

# convert the object into a dict
blueprint_api_environment_discovery_response_dict = blueprint_api_environment_discovery_response_instance.to_dict()
# create an instance of BlueprintApiEnvironmentDiscoveryResponse from a dict
blueprint_api_environment_discovery_response_from_dict = BlueprintApiEnvironmentDiscoveryResponse.from_dict(blueprint_api_environment_discovery_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


