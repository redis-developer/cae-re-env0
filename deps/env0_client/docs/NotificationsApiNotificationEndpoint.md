# NotificationsApiNotificationEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**created_by_user** | [**User**](User.md) |  | [optional] 
**organization_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**NotificationEndpointType**](NotificationEndpointType.md) |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from env0_client.models.notifications_api_notification_endpoint import NotificationsApiNotificationEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsApiNotificationEndpoint from a JSON string
notifications_api_notification_endpoint_instance = NotificationsApiNotificationEndpoint.from_json(json)
# print the JSON string representation of the object
print(NotificationsApiNotificationEndpoint.to_json())

# convert the object into a dict
notifications_api_notification_endpoint_dict = notifications_api_notification_endpoint_instance.to_dict()
# create an instance of NotificationsApiNotificationEndpoint from a dict
notifications_api_notification_endpoint_from_dict = NotificationsApiNotificationEndpoint.from_dict(notifications_api_notification_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


