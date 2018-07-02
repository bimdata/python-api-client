# bimdata_api_client.UserApi

All URIs are relative to *https://api-staging.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ask_reset_password_token**](UserApi.md#ask_reset_password_token) | **POST** /user/forgot-password | 
[**full_update_notification**](UserApi.md#full_update_notification) | **PUT** /user/notification/{id} | 
[**get_notification**](UserApi.md#get_notification) | **GET** /user/notification/{id} | 
[**get_self_notifications**](UserApi.md#get_self_notifications) | **GET** /user/notification | 
[**get_self_projects**](UserApi.md#get_self_projects) | **GET** /user/projects | 
[**get_self_user**](UserApi.md#get_self_user) | **GET** /user | 
[**reset_password**](UserApi.md#reset_password) | **POST** /user/reset-password | 
[**sign_up**](UserApi.md#sign_up) | **POST** /user/signup | 
[**sign_up_with_invitation_token**](UserApi.md#sign_up_with_invitation_token) | **POST** /user/invited-signup | 
[**update_notification**](UserApi.md#update_notification) | **PATCH** /user/notification/{id} | 
[**update_self_user**](UserApi.md#update_self_user) | **PATCH** /user | 


# **ask_reset_password_token**
> ask_reset_password_token(data)





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
api_instance = bimdata_api_client.UserApi(bimdata_api_client.ApiClient(configuration))
data = bimdata_api_client.ForgotPassword() # ForgotPassword | 

try:
    api_instance.ask_reset_password_token(data)
except ApiException as e:
    print("Exception when calling UserApi->ask_reset_password_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ForgotPassword**](ForgotPassword.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_notification**
> Notification full_update_notification(id, data)





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
api_instance = bimdata_api_client.UserApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
data = bimdata_api_client.Notification() # Notification | 

try:
    api_response = api_instance.full_update_notification(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->full_update_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Notification**](Notification.md)|  | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification**
> Notification get_notification(id)





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
api_instance = bimdata_api_client.UserApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_notification(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_notifications**
> list[Notification] get_self_notifications()





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
api_instance = bimdata_api_client.UserApi(bimdata_api_client.ApiClient(configuration))

try:
    api_response = api_instance.get_self_notifications()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_self_notifications: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Notification]**](Notification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_projects**
> list[Project] get_self_projects()





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
api_instance = bimdata_api_client.UserApi(bimdata_api_client.ApiClient(configuration))

try:
    api_response = api_instance.get_self_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_self_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Project]**](Project.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_user**
> FosUser get_self_user()





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

[**FosUser**](FosUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password(data)





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
api_instance = bimdata_api_client.UserApi(bimdata_api_client.ApiClient(configuration))
data = bimdata_api_client.ResetPassword() # ResetPassword | 

try:
    api_instance.reset_password(data)
except ApiException as e:
    print("Exception when calling UserApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ResetPassword**](ResetPassword.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_up**
> SignupFosUser sign_up(data)





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
api_instance = bimdata_api_client.UserApi(bimdata_api_client.ApiClient(configuration))
data = bimdata_api_client.SignupFosUser() # SignupFosUser | 

try:
    api_response = api_instance.sign_up(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->sign_up: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SignupFosUser**](SignupFosUser.md)|  | 

### Return type

[**SignupFosUser**](SignupFosUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_up_with_invitation_token**
> SignupFosUser sign_up_with_invitation_token(data)





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
api_instance = bimdata_api_client.UserApi(bimdata_api_client.ApiClient(configuration))
data = bimdata_api_client.InvitedSignUp() # InvitedSignUp | 

try:
    api_response = api_instance.sign_up_with_invitation_token(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->sign_up_with_invitation_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InvitedSignUp**](InvitedSignUp.md)|  | 

### Return type

[**SignupFosUser**](SignupFosUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification**
> Notification update_notification(id, data)





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
api_instance = bimdata_api_client.UserApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
data = bimdata_api_client.Notification() # Notification | 

try:
    api_response = api_instance.update_notification(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Notification**](Notification.md)|  | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_self_user**
> FosUser update_self_user(data)





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
api_instance = bimdata_api_client.UserApi(bimdata_api_client.ApiClient(configuration))
data = bimdata_api_client.SelfFosUser() # SelfFosUser | 

try:
    api_response = api_instance.update_self_user(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_self_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SelfFosUser**](SelfFosUser.md)|  | 

### Return type

[**FosUser**](FosUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

