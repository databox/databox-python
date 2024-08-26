# PushDataAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from databox.models.push_data_attribute import PushDataAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of PushDataAttribute from a JSON string
push_data_attribute_instance = PushDataAttribute.from_json(json)
# print the JSON string representation of the object
print(PushDataAttribute.to_json())

# convert the object into a dict
push_data_attribute_dict = push_data_attribute_instance.to_dict()
# create an instance of PushDataAttribute from a dict
push_data_attribute_from_dict = PushDataAttribute.from_dict(push_data_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


