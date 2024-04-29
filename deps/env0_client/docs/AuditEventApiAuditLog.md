# AuditEventApiAuditLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**actor** | [**User**](User.md) |  | [optional] 
**actor_id** | **str** |  | 
**action_name** | **str** |  | 
**project_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | 
**ip_address** | **str** |  | [optional] 
**payload** | **object** |  | [optional] 

## Example

```python
from env0_client.models.audit_event_api_audit_log import AuditEventApiAuditLog

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEventApiAuditLog from a JSON string
audit_event_api_audit_log_instance = AuditEventApiAuditLog.from_json(json)
# print the JSON string representation of the object
print(AuditEventApiAuditLog.to_json())

# convert the object into a dict
audit_event_api_audit_log_dict = audit_event_api_audit_log_instance.to_dict()
# create an instance of AuditEventApiAuditLog from a dict
audit_event_api_audit_log_from_dict = AuditEventApiAuditLog.from_dict(audit_event_api_audit_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


