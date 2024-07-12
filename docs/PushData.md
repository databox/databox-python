# PushData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[PushDataAttribute]**](PushDataAttribute.md) |  | [optional] 
**var_date** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**period_from** | **str** |  | [optional] 
**period_to** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from databox.models.push_data import PushData

# TODO update the JSON string below
json = "{}"
# create an instance of PushData from a JSON string
push_data_instance = PushData.from_json(json)
# print the JSON string representation of the object
print(PushData.to_json())

# convert the object into a dict
push_data_dict = push_data_instance.to_dict()
# create an instance of PushData from a dict
push_data_from_dict = PushData.from_dict(push_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


