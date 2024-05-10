# delivery_engine_client.DeliveriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deliver_message_deliveries_deliver_message_post**](DeliveriesApi.md#deliver_message_deliveries_deliver_message_post) | **POST** /deliveries/deliver_message | Deliver Message
[**process_queue_deliveries_process_queue_post**](DeliveriesApi.md#process_queue_deliveries_process_queue_post) | **POST** /deliveries/process_queue | Process Queue


# **deliver_message_deliveries_deliver_message_post**
> DeliverMessageResponse deliver_message_deliveries_deliver_message_post(subscriber_id, message)

Deliver Message

Deliver a message to a subscriber.

### Example


```python
import delivery_engine_client
from delivery_engine_client.models.deliver_message_response import DeliverMessageResponse
from delivery_engine_client.models.message import Message
from delivery_engine_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = delivery_engine_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with delivery_engine_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = delivery_engine_client.DeliveriesApi(api_client)
    subscriber_id = 56 # int | 
    message = delivery_engine_client.Message() # Message | 

    try:
        # Deliver Message
        api_response = await api_instance.deliver_message_deliveries_deliver_message_post(subscriber_id, message)
        print("The response of DeliveriesApi->deliver_message_deliveries_deliver_message_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesApi->deliver_message_deliveries_deliver_message_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriber_id** | **int**|  | 
 **message** | [**Message**](Message.md)|  | 

### Return type

[**DeliverMessageResponse**](DeliverMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_queue_deliveries_process_queue_post**
> bool process_queue_deliveries_process_queue_post(subscriber_id)

Process Queue

Process the message queue for a subscriber.

### Example


```python
import delivery_engine_client
from delivery_engine_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = delivery_engine_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with delivery_engine_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = delivery_engine_client.DeliveriesApi(api_client)
    subscriber_id = 56 # int | 

    try:
        # Process Queue
        api_response = await api_instance.process_queue_deliveries_process_queue_post(subscriber_id)
        print("The response of DeliveriesApi->process_queue_deliveries_process_queue_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesApi->process_queue_deliveries_process_queue_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriber_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

