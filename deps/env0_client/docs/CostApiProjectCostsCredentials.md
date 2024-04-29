# CostApiProjectCostsCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**credentials_id** | **str** |  | 
**credentials_type** | [**CredentialType**](CredentialType.md) |  | [optional] 

## Example

```python
from env0_client.models.cost_api_project_costs_credentials import CostApiProjectCostsCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of CostApiProjectCostsCredentials from a JSON string
cost_api_project_costs_credentials_instance = CostApiProjectCostsCredentials.from_json(json)
# print the JSON string representation of the object
print(CostApiProjectCostsCredentials.to_json())

# convert the object into a dict
cost_api_project_costs_credentials_dict = cost_api_project_costs_credentials_instance.to_dict()
# create an instance of CostApiProjectCostsCredentials from a dict
cost_api_project_costs_credentials_from_dict = CostApiProjectCostsCredentials.from_dict(cost_api_project_costs_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


