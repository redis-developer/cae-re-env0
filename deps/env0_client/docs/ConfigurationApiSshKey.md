# ConfigurationApiSshKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**organization_id** | **str** |  | 
**value** | **str** |  | 
**encryption_method** | **str** |  | [optional] 
**user_id** | **str** |  | 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from env0_client.models.configuration_api_ssh_key import ConfigurationApiSshKey

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationApiSshKey from a JSON string
configuration_api_ssh_key_instance = ConfigurationApiSshKey.from_json(json)
# print the JSON string representation of the object
print(ConfigurationApiSshKey.to_json())

# convert the object into a dict
configuration_api_ssh_key_dict = configuration_api_ssh_key_instance.to_dict()
# create an instance of ConfigurationApiSshKey from a dict
configuration_api_ssh_key_from_dict = ConfigurationApiSshKey.from_dict(configuration_api_ssh_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


