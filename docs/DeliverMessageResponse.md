# DeliverMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivered_count** | **int** |  | 

## Example

```python
from delivery_engine_client.models.deliver_message_response import DeliverMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverMessageResponse from a JSON string
deliver_message_response_instance = DeliverMessageResponse.from_json(json)
# print the JSON string representation of the object
print(DeliverMessageResponse.to_json())

# convert the object into a dict
deliver_message_response_dict = deliver_message_response_instance.to_dict()
# create an instance of DeliverMessageResponse from a dict
deliver_message_response_from_dict = DeliverMessageResponse.from_dict(deliver_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


