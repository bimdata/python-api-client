# bimdata_api_client.ApplicationApi

All URIs are relative to *https://api-beta.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloud_webhook_ping**](ApplicationApi.md#cloud_webhook_ping) | **POST** /cloud/{cloud_pk}/webhook/{id}/ping | 
[**create_web_hook**](ApplicationApi.md#create_web_hook) | **POST** /cloud/{cloud_pk}/webhook | 
[**delete_web_hook**](ApplicationApi.md#delete_web_hook) | **DELETE** /cloud/{cloud_pk}/webhook/{id} | 
[**full_update_web_hook**](ApplicationApi.md#full_update_web_hook) | **PUT** /cloud/{cloud_pk}/webhook/{id} | 
[**get_web_hook**](ApplicationApi.md#get_web_hook) | **GET** /cloud/{cloud_pk}/webhook/{id} | 
[**get_web_hooks**](ApplicationApi.md#get_web_hooks) | **GET** /cloud/{cloud_pk}/webhook | 
[**update_web_hook**](ApplicationApi.md#update_web_hook) | **PATCH** /cloud/{cloud_pk}/webhook/{id} | 


# **cloud_webhook_ping**
> WebHook cloud_webhook_ping(cloud_pk, id, web_hook)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.ApplicationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
web_hook = bimdata_api_client.WebHook() # WebHook | 

try:
    api_response = api_instance.cloud_webhook_ping(cloud_pk, id, web_hook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->cloud_webhook_ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **web_hook** | [**WebHook**](WebHook.md)|  | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_web_hook**
> WebHook create_web_hook(cloud_pk, web_hook)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.ApplicationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
web_hook = bimdata_api_client.WebHook() # WebHook | 

try:
    api_response = api_instance.create_web_hook(cloud_pk, web_hook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->create_web_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **web_hook** | [**WebHook**](WebHook.md)|  | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_web_hook**
> delete_web_hook(cloud_pk, id)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.ApplicationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.delete_web_hook(cloud_pk, id)
except ApiException as e:
    print("Exception when calling ApplicationApi->delete_web_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_web_hook**
> WebHook full_update_web_hook(cloud_pk, id, web_hook)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.ApplicationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
web_hook = bimdata_api_client.WebHook() # WebHook | 

try:
    api_response = api_instance.full_update_web_hook(cloud_pk, id, web_hook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->full_update_web_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **web_hook** | [**WebHook**](WebHook.md)|  | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_hook**
> WebHook get_web_hook(cloud_pk, id)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.ApplicationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_web_hook(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_web_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_hooks**
> list[WebHook] get_web_hooks(cloud_pk)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.ApplicationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    api_response = api_instance.get_web_hooks(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_web_hooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 

### Return type

[**list[WebHook]**](WebHook.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_web_hook**
> WebHook update_web_hook(cloud_pk, id, web_hook)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.ApplicationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
web_hook = bimdata_api_client.WebHook() # WebHook | 

try:
    api_response = api_instance.update_web_hook(cloud_pk, id, web_hook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->update_web_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **web_hook** | [**WebHook**](WebHook.md)|  | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

