# ModuleTestingApiTestFileSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passed** | **float** |  | [optional] 
**failed** | **float** |  | [optional] 
**skipped** | **float** |  | [optional] 
**errored** | **float** |  | [optional] 

## Example

```python
from env0_client.models.module_testing_api_test_file_summary import ModuleTestingApiTestFileSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleTestingApiTestFileSummary from a JSON string
module_testing_api_test_file_summary_instance = ModuleTestingApiTestFileSummary.from_json(json)
# print the JSON string representation of the object
print(ModuleTestingApiTestFileSummary.to_json())

# convert the object into a dict
module_testing_api_test_file_summary_dict = module_testing_api_test_file_summary_instance.to_dict()
# create an instance of ModuleTestingApiTestFileSummary from a dict
module_testing_api_test_file_summary_from_dict = ModuleTestingApiTestFileSummary.from_dict(module_testing_api_test_file_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


