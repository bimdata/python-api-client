# bimdata_api_client.UserApi

All URIs are relative to *https://api-beta.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_self_user**](UserApi.md#get_self_user) | **GET** /user | 
[**update_self_user**](UserApi.md#update_self_user) | **PATCH** /user | 
[**user_projects_list**](UserApi.md#user_projects_list) | **GET** /user/projects | 


# **get_self_user**
> SelfUser get_self_user()



### Example

* Api Key Authentication (Bearer): 
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
api_instance = bimdata_api_client.UserApi(bimdata_api_client.ApiClient(configuration))

try:
    api_response = api_instance.get_self_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_self_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SelfUser**](SelfUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_self_user**
> SelfUser update_self_user(self_user)



### Example

* Api Key Authentication (Bearer): 
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
api_instance = bimdata_api_client.UserApi(bimdata_api_client.ApiClient(configuration))
self_user = bimdata_api_client.SelfUser() # SelfUser | 

try:
    api_response = api_instance.update_self_user(self_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_self_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **self_user** | [**SelfUser**](SelfUser.md)|  | 

### Return type

[**SelfUser**](SelfUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_projects_list**
> list[Project] user_projects_list()



### Example

* Api Key Authentication (Bearer): 
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
api_instance = bimdata_api_client.UserApi(bimdata_api_client.ApiClient(configuration))

try:
    api_response = api_instance.user_projects_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_projects_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Project]**](Project.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

