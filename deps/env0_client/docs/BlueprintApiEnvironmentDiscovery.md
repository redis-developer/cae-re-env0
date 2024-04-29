# BlueprintApiEnvironmentDiscovery


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

## Example

```python
from env0_client.models.blueprint_api_environment_discovery import BlueprintApiEnvironmentDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiEnvironmentDiscovery from a JSON string
blueprint_api_environment_discovery_instance = BlueprintApiEnvironmentDiscovery.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiEnvironmentDiscovery.to_json())

# convert the object into a dict
blueprint_api_environment_discovery_dict = blueprint_api_environment_discovery_instance.to_dict()
# create an instance of BlueprintApiEnvironmentDiscovery from a dict
blueprint_api_environment_discovery_from_dict = BlueprintApiEnvironmentDiscovery.from_dict(blueprint_api_environment_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


