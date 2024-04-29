# NotificationsApiUpdateNotificationEndpointRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 
**type** | [**NotificationEndpointType**](NotificationEndpointType.md) |  | 

## Example

```python
from env0_client.models.notifications_api_update_notification_endpoint_request_body import NotificationsApiUpdateNotificationEndpointRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsApiUpdateNotificationEndpointRequestBody from a JSON string
notifications_api_update_notification_endpoint_request_body_instance = NotificationsApiUpdateNotificationEndpointRequestBody.from_json(json)
# print the JSON string representation of the object
print(NotificationsApiUpdateNotificationEndpointRequestBody.to_json())

# convert the object into a dict
notifications_api_update_notification_endpoint_request_body_dict = notifications_api_update_notification_endpoint_request_body_instance.to_dict()
# create an instance of NotificationsApiUpdateNotificationEndpointRequestBody from a dict
notifications_api_update_notification_endpoint_request_body_from_dict = NotificationsApiUpdateNotificationEndpointRequestBody.from_dict(notifications_api_update_notification_endpoint_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


