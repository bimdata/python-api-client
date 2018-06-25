# bimdata_api_client.CloudApi

All URIs are relative to *https://api-beta.bimdata.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud**](CloudApi.md#create_cloud) | **POST** /cloud | 
[**create_cloud_user**](CloudApi.md#create_cloud_user) | **POST** /cloud/{cloud_pk}/user | 
[**delete_cloud_user**](CloudApi.md#delete_cloud_user) | **DELETE** /cloud/{cloud_pk}/user/{id} | 
[**full_update_cloud**](CloudApi.md#full_update_cloud) | **PUT** /cloud/{id} | 
[**full_update_cloud_user**](CloudApi.md#full_update_cloud_user) | **PUT** /cloud/{cloud_pk}/user/{id} | 
[**get_cloud**](CloudApi.md#get_cloud) | **GET** /cloud/{id} | 
[**get_cloud_size**](CloudApi.md#get_cloud_size) | **GET** /cloud/{id}/size | 
[**get_cloud_user**](CloudApi.md#get_cloud_user) | **GET** /cloud/{cloud_pk}/user/{id} | 
[**get_cloud_users**](CloudApi.md#get_cloud_users) | **GET** /cloud/{cloud_pk}/user | 
[**get_clouds**](CloudApi.md#get_clouds) | **GET** /cloud | 
[**update_cloud**](CloudApi.md#update_cloud) | **PATCH** /cloud/{id} | 
[**update_cloud_user**](CloudApi.md#update_cloud_user) | **PATCH** /cloud/{cloud_pk}/user/{id} | 


# **create_cloud**
> Cloud create_cloud(cloud)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud = bimdata_api_client.Cloud() # Cloud | 

try:
    api_response = api_instance.create_cloud(cloud)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud** | [**Cloud**](Cloud.md)|  | 

### Return type

[**Cloud**](Cloud.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud_user**
> FosUserWrite create_cloud_user(cloud_pk, fos_user_write)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
fos_user_write = bimdata_api_client.FosUserWrite() # FosUserWrite | 

try:
    api_response = api_instance.create_cloud_user(cloud_pk, fos_user_write)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_cloud_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **fos_user_write** | [**FosUserWrite**](FosUserWrite.md)|  | 

### Return type

[**FosUserWrite**](FosUserWrite.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_user**
> delete_cloud_user(cloud_pk, id)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.delete_cloud_user(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CloudApi->delete_cloud_user: %s\n" % e)
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

# **full_update_cloud**
> Cloud full_update_cloud(id, cloud)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
cloud = bimdata_api_client.Cloud() # Cloud | 

try:
    api_response = api_instance.full_update_cloud(id, cloud)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->full_update_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cloud** | [**Cloud**](Cloud.md)|  | 

### Return type

[**Cloud**](Cloud.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_cloud_user**
> FosUserWrite full_update_cloud_user(cloud_pk, id, fos_user_write)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
fos_user_write = bimdata_api_client.FosUserWrite() # FosUserWrite | 

try:
    api_response = api_instance.full_update_cloud_user(cloud_pk, id, fos_user_write)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->full_update_cloud_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **fos_user_write** | [**FosUserWrite**](FosUserWrite.md)|  | 

### Return type

[**FosUserWrite**](FosUserWrite.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud**
> Cloud get_cloud(id)



Returns user and his cloud role

### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_cloud(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Cloud**](Cloud.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_size**
> int get_cloud_size(id)



Returns the size of the cloud in Bytes

### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_cloud_size(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**int**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_user**
> FosUser get_cloud_user(cloud_pk, id)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_cloud_user(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**FosUser**](FosUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_users**
> list[FosUser] get_cloud_users(cloud_pk)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    api_response = api_instance.get_cloud_users(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 

### Return type

[**list[FosUser]**](FosUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clouds**
> list[Cloud] get_clouds()



Returns user's cloud only

### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))

try:
    api_response = api_instance.get_clouds()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_clouds: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Cloud]**](Cloud.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud**
> Cloud update_cloud(id, cloud)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
cloud = bimdata_api_client.Cloud() # Cloud | 

try:
    api_response = api_instance.update_cloud(id, cloud)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cloud** | [**Cloud**](Cloud.md)|  | 

### Return type

[**Cloud**](Cloud.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_user**
> FosUserWrite update_cloud_user(cloud_pk, id, fos_user_write)



### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
fos_user_write = bimdata_api_client.FosUserWrite() # FosUserWrite | 

try:
    api_response = api_instance.update_cloud_user(cloud_pk, id, fos_user_write)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **fos_user_write** | [**FosUserWrite**](FosUserWrite.md)|  | 

### Return type

[**FosUserWrite**](FosUserWrite.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

