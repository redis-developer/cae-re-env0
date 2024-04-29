# BlueprintApiSshKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from env0_client.models.blueprint_api_ssh_key import BlueprintApiSshKey

# TODO update the JSON string below
json = "{}"
# create an instance of BlueprintApiSshKey from a JSON string
blueprint_api_ssh_key_instance = BlueprintApiSshKey.from_json(json)
# print the JSON string representation of the object
print(BlueprintApiSshKey.to_json())

# convert the object into a dict
blueprint_api_ssh_key_dict = blueprint_api_ssh_key_instance.to_dict()
# create an instance of BlueprintApiSshKey from a dict
blueprint_api_ssh_key_from_dict = BlueprintApiSshKey.from_dict(blueprint_api_ssh_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


