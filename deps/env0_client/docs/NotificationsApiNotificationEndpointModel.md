# NotificationsApiNotificationEndpointModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**created_by_user** | [**User**](User.md) |  | [optional] 
**organization_id** | **str** |  | 
**name** | **str** |  | 
**type** | [**NotificationEndpointType**](NotificationEndpointType.md) |  | 
**value** | **str** |  | 

## Example

```python
from env0_client.models.notifications_api_notification_endpoint_model import NotificationsApiNotificationEndpointModel

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsApiNotificationEndpointModel from a JSON string
notifications_api_notification_endpoint_model_instance = NotificationsApiNotificationEndpointModel.from_json(json)
# print the JSON string representation of the object
print(NotificationsApiNotificationEndpointModel.to_json())

# convert the object into a dict
notifications_api_notification_endpoint_model_dict = notifications_api_notification_endpoint_model_instance.to_dict()
# create an instance of NotificationsApiNotificationEndpointModel from a dict
notifications_api_notification_endpoint_model_from_dict = NotificationsApiNotificationEndpointModel.from_dict(notifications_api_notification_endpoint_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


