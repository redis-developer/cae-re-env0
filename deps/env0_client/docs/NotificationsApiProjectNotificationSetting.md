# NotificationsApiProjectNotificationSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**notification_endpoint_id** | **str** |  | 
**event_names** | [**List[EventNameType]**](EventNameType.md) |  | 
**created_by** | **str** |  | [optional] 
**created_by_user** | [**User**](User.md) |  | [optional] 

## Example

```python
from env0_client.models.notifications_api_project_notification_setting import NotificationsApiProjectNotificationSetting

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsApiProjectNotificationSetting from a JSON string
notifications_api_project_notification_setting_instance = NotificationsApiProjectNotificationSetting.from_json(json)
# print the JSON string representation of the object
print(NotificationsApiProjectNotificationSetting.to_json())

# convert the object into a dict
notifications_api_project_notification_setting_dict = notifications_api_project_notification_setting_instance.to_dict()
# create an instance of NotificationsApiProjectNotificationSetting from a dict
notifications_api_project_notification_setting_from_dict = NotificationsApiProjectNotificationSetting.from_dict(notifications_api_project_notification_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


