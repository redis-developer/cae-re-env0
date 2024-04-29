# EnvironmentApiReviewerUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) |  | 
**action** | **str** |  | 

## Example

```python
from env0_client.models.environment_api_reviewer_user import EnvironmentApiReviewerUser

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentApiReviewerUser from a JSON string
environment_api_reviewer_user_instance = EnvironmentApiReviewerUser.from_json(json)
# print the JSON string representation of the object
print(EnvironmentApiReviewerUser.to_json())

# convert the object into a dict
environment_api_reviewer_user_dict = environment_api_reviewer_user_instance.to_dict()
# create an instance of EnvironmentApiReviewerUser from a dict
environment_api_reviewer_user_from_dict = EnvironmentApiReviewerUser.from_dict(environment_api_reviewer_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


