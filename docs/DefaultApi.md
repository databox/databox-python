# databox.DefaultApi

All URIs are relative to *https://push.databox.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_delete**](DefaultApi.md#data_delete) | **DELETE** /data | 
[**data_metric_key_delete**](DefaultApi.md#data_metric_key_delete) | **DELETE** /data/{metricKey} | 
[**data_post**](DefaultApi.md#data_post) | **POST** /data | 
[**metrickeys_get**](DefaultApi.md#metrickeys_get) | **GET** /metrickeys | 
[**metrickeys_post**](DefaultApi.md#metrickeys_post) | **POST** /metrickeys | 
[**ping_get**](DefaultApi.md#ping_get) | **GET** /ping | 


# **data_delete**
> data_delete()



### Example

* Basic Authentication (basicAuth):

```python
import databox
from databox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://push.databox.com
# See configuration.py for a list of all supported configuration parameters.
configuration = databox.Configuration(
    host = "https://push.databox.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = databox.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with databox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databox.DefaultApi(api_client)

    try:
        api_instance.data_delete()
    except Exception as e:
        print("Exception when calling DefaultApi->data_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_metric_key_delete**
> data_metric_key_delete(metric_key)



### Example

* Basic Authentication (basicAuth):

```python
import databox
from databox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://push.databox.com
# See configuration.py for a list of all supported configuration parameters.
configuration = databox.Configuration(
    host = "https://push.databox.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = databox.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with databox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databox.DefaultApi(api_client)
    metric_key = 'metric_key_example' # str | 

    try:
        api_instance.data_metric_key_delete(metric_key)
    except Exception as e:
        print("Exception when calling DefaultApi->data_metric_key_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_post**
> data_post(push_data=push_data)



### Example

* Basic Authentication (basicAuth):

```python
import databox
from databox.models.push_data import PushData
from databox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://push.databox.com
# See configuration.py for a list of all supported configuration parameters.
configuration = databox.Configuration(
    host = "https://push.databox.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = databox.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with databox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databox.DefaultApi(api_client)
    push_data = [databox.PushData()] # List[PushData] |  (optional)

    try:
        api_instance.data_post(push_data=push_data)
    except Exception as e:
        print("Exception when calling DefaultApi->data_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_data** | [**List[PushData]**](PushData.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.databox.v2+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrickeys_get**
> metrickeys_get()



### Example

* Basic Authentication (basicAuth):

```python
import databox
from databox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://push.databox.com
# See configuration.py for a list of all supported configuration parameters.
configuration = databox.Configuration(
    host = "https://push.databox.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = databox.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with databox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databox.DefaultApi(api_client)

    try:
        api_instance.metrickeys_get()
    except Exception as e:
        print("Exception when calling DefaultApi->metrickeys_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrickeys_post**
> metrickeys_post(body=body)



### Example

* Basic Authentication (basicAuth):

```python
import databox
from databox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://push.databox.com
# See configuration.py for a list of all supported configuration parameters.
configuration = databox.Configuration(
    host = "https://push.databox.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = databox.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with databox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databox.DefaultApi(api_client)
    body = None # object |  (optional)

    try:
        api_instance.metrickeys_post(body=body)
    except Exception as e:
        print("Exception when calling DefaultApi->metrickeys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.databox.v2+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_get**
> ping_get()



### Example

* Basic Authentication (basicAuth):

```python
import databox
from databox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://push.databox.com
# See configuration.py for a list of all supported configuration parameters.
configuration = databox.Configuration(
    host = "https://push.databox.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = databox.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with databox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databox.DefaultApi(api_client)

    try:
        api_instance.ping_get()
    except Exception as e:
        print("Exception when calling DefaultApi->ping_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

