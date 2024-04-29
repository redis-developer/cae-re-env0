# ModuleTestingApiTestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**status** | [**ModuleTestingApiTestStatus**](ModuleTestingApiTestStatus.md) |  | 

## Example

```python
from env0_client.models.module_testing_api_test_result import ModuleTestingApiTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleTestingApiTestResult from a JSON string
module_testing_api_test_result_instance = ModuleTestingApiTestResult.from_json(json)
# print the JSON string representation of the object
print(ModuleTestingApiTestResult.to_json())

# convert the object into a dict
module_testing_api_test_result_dict = module_testing_api_test_result_instance.to_dict()
# create an instance of ModuleTestingApiTestResult from a dict
module_testing_api_test_result_from_dict = ModuleTestingApiTestResult.from_dict(module_testing_api_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


