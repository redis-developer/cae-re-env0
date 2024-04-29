# AuditEventApiFetchAuditLogsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[AuditEventApiAuditLog]**](AuditEventApiAuditLog.md) |  | 
**next_page_key** | **str** |  | 

## Example

```python
from env0_client.models.audit_event_api_fetch_audit_logs_response import AuditEventApiFetchAuditLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEventApiFetchAuditLogsResponse from a JSON string
audit_event_api_fetch_audit_logs_response_instance = AuditEventApiFetchAuditLogsResponse.from_json(json)
# print the JSON string representation of the object
print(AuditEventApiFetchAuditLogsResponse.to_json())

# convert the object into a dict
audit_event_api_fetch_audit_logs_response_dict = audit_event_api_fetch_audit_logs_response_instance.to_dict()
# create an instance of AuditEventApiFetchAuditLogsResponse from a dict
audit_event_api_fetch_audit_logs_response_from_dict = AuditEventApiFetchAuditLogsResponse.from_dict(audit_event_api_fetch_audit_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


