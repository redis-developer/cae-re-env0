# AuditEventApiFetchAuditLogsRequestQueryParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **str** |  | [optional] 
**offset** | **str** |  | [optional] 
**organization_id** | **str** |  | 
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 

## Example

```python
from env0_client.models.audit_event_api_fetch_audit_logs_request_query_params import AuditEventApiFetchAuditLogsRequestQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEventApiFetchAuditLogsRequestQueryParams from a JSON string
audit_event_api_fetch_audit_logs_request_query_params_instance = AuditEventApiFetchAuditLogsRequestQueryParams.from_json(json)
# print the JSON string representation of the object
print(AuditEventApiFetchAuditLogsRequestQueryParams.to_json())

# convert the object into a dict
audit_event_api_fetch_audit_logs_request_query_params_dict = audit_event_api_fetch_audit_logs_request_query_params_instance.to_dict()
# create an instance of AuditEventApiFetchAuditLogsRequestQueryParams from a dict
audit_event_api_fetch_audit_logs_request_query_params_from_dict = AuditEventApiFetchAuditLogsRequestQueryParams.from_dict(audit_event_api_fetch_audit_logs_request_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


