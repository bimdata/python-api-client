# openapi_client.UserApi

All URIs are relative to *https://api-beta.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_self_user**](UserApi.md#get_self_user) | **GET** /user | 
[**update_self_user**](UserApi.md#update_self_user) | **PATCH** /user | 
[**user_projects_list**](UserApi.md#user_projects_list) | **GET** /user/projects | 


# **get_self_user**
> SelfUser get_self_user()



### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.UserApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_self_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_self_user: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.UserApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_self_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_self_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.UserApi(openapi_client.ApiClient(configuration))

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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_self_user**
> SelfUser update_self_user(data)



### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.UserApi(openapi_client.ApiClient(configuration))
data = openapi_client.SelfUser() # SelfUser | 

try:
    api_response = api_instance.update_self_user(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_self_user: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.UserApi(openapi_client.ApiClient(configuration))
data = openapi_client.SelfUser() # SelfUser | 

try:
    api_response = api_instance.update_self_user(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_self_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.UserApi(openapi_client.ApiClient(configuration))
data = openapi_client.SelfUser() # SelfUser | 

try:
    api_response = api_instance.update_self_user(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_self_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SelfUser**](SelfUser.md)|  | 

### Return type

[**SelfUser**](SelfUser.md)

### Authorization

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_projects_list**
> list[Project] user_projects_list()



### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.UserApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.user_projects_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_projects_list: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.UserApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.user_projects_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_projects_list: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.UserApi(openapi_client.ApiClient(configuration))

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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

