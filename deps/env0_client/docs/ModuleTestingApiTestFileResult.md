# ModuleTestingApiTestFileResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_file** | **str** |  | 
**summary** | [**ModuleTestingApiTestFileSummary**](ModuleTestingApiTestFileSummary.md) |  | 
**tests** | [**List[ModuleTestingApiTestResult]**](ModuleTestingApiTestResult.md) |  | [optional] 

## Example

```python
from env0_client.models.module_testing_api_test_file_result import ModuleTestingApiTestFileResult

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleTestingApiTestFileResult from a JSON string
module_testing_api_test_file_result_instance = ModuleTestingApiTestFileResult.from_json(json)
# print the JSON string representation of the object
print(ModuleTestingApiTestFileResult.to_json())

# convert the object into a dict
module_testing_api_test_file_result_dict = module_testing_api_test_file_result_instance.to_dict()
# create an instance of ModuleTestingApiTestFileResult from a dict
module_testing_api_test_file_result_from_dict = ModuleTestingApiTestFileResult.from_dict(module_testing_api_test_file_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


