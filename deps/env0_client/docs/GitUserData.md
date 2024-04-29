# GitUserData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_user** | **str** |  | [optional] 
**git_avatar_url** | **str** |  | [optional] 
**pr_number** | **str** |  | [optional] 

## Example

```python
from env0_client.models.git_user_data import GitUserData

# TODO update the JSON string below
json = "{}"
# create an instance of GitUserData from a JSON string
git_user_data_instance = GitUserData.from_json(json)
# print the JSON string representation of the object
print(GitUserData.to_json())

# convert the object into a dict
git_user_data_dict = git_user_data_instance.to_dict()
# create an instance of GitUserData from a dict
git_user_data_from_dict = GitUserData.from_dict(git_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


