# OrganizationApiOrganizationPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_ttl** | **str** | The maximum allowed TTL. Must be 6-h, 12-h, 1-d, 3-d, 1-w, 2-w, 1-M, inherit or explicit null which means infinite | [optional] 
**default_ttl** | **str** | The default TTL set when creating environments. Must be 6-h, 12-h, 1-d, 3-d, 1-w, 2-w, 1-M, inherit or explicit null which means infinite | [optional] 
**do_not_report_skipped_status_checks** | **bool** |  | [optional] 
**do_not_consider_merge_commits_for_pr_plans** | **bool** |  | [optional] 
**enable_oidc** | **bool** |  | [optional] 
**enforce_pr_commenter_permissions** | **bool** |  | [optional] 
**project_custom_flows_policy** | [**OrganizationApiProjectCustomFlowsPolicy**](OrganizationApiProjectCustomFlowsPolicy.md) |  | [optional] 

## Example

```python
from env0_client.models.organization_api_organization_policy import OrganizationApiOrganizationPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationApiOrganizationPolicy from a JSON string
organization_api_organization_policy_instance = OrganizationApiOrganizationPolicy.from_json(json)
# print the JSON string representation of the object
print(OrganizationApiOrganizationPolicy.to_json())

# convert the object into a dict
organization_api_organization_policy_dict = organization_api_organization_policy_instance.to_dict()
# create an instance of OrganizationApiOrganizationPolicy from a dict
organization_api_organization_policy_from_dict = OrganizationApiOrganizationPolicy.from_dict(organization_api_organization_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


