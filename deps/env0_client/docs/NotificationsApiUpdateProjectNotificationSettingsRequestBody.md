# NotificationsApiUpdateProjectNotificationSettingsRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_names** | [**List[EventNameType]**](EventNameType.md) |  | 

## Example

```python
from env0_client.models.notifications_api_update_project_notification_settings_request_body import NotificationsApiUpdateProjectNotificationSettingsRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsApiUpdateProjectNotificationSettingsRequestBody from a JSON string
notifications_api_update_project_notification_settings_request_body_instance = NotificationsApiUpdateProjectNotificationSettingsRequestBody.from_json(json)
# print the JSON string representation of the object
print(NotificationsApiUpdateProjectNotificationSettingsRequestBody.to_json())

# convert the object into a dict
notifications_api_update_project_notification_settings_request_body_dict = notifications_api_update_project_notification_settings_request_body_instance.to_dict()
# create an instance of NotificationsApiUpdateProjectNotificationSettingsRequestBody from a dict
notifications_api_update_project_notification_settings_request_body_from_dict = NotificationsApiUpdateProjectNotificationSettingsRequestBody.from_dict(notifications_api_update_project_notification_settings_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


