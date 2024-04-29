# OrganizationApiOrganizationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**max_ttl** | **str** |  | [optional] 
**default_ttl** | **str** |  | [optional] 
**do_not_report_skipped_status_checks** | **bool** |  | [optional] 
**do_not_consider_merge_commits_for_pr_plans** | **bool** |  | [optional] 
**enable_oidc** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**mode** | [**OrganizationApiOrganizationMode**](OrganizationApiOrganizationMode.md) |  | 
**trial_end** | **datetime** |  | [optional] 
**enforce_pr_commenter_permissions** | **bool** |  | [optional] 
**project_custom_flows_policy** | [**OrganizationApiProjectCustomFlowsPolicy**](OrganizationApiProjectCustomFlowsPolicy.md) |  | 

## Example

```python
from env0_client.models.organization_api_organization_model import OrganizationApiOrganizationModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationApiOrganizationModel from a JSON string
organization_api_organization_model_instance = OrganizationApiOrganizationModel.from_json(json)
# print the JSON string representation of the object
print(OrganizationApiOrganizationModel.to_json())

# convert the object into a dict
organization_api_organization_model_dict = organization_api_organization_model_instance.to_dict()
# create an instance of OrganizationApiOrganizationModel from a dict
organization_api_organization_model_from_dict = OrganizationApiOrganizationModel.from_dict(organization_api_organization_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


