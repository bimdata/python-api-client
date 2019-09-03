# bimdata_api_client.CloudApi

All URIs are relative to *https://api-beta.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_cloud_user_invitation**](CloudApi.md#cancel_cloud_user_invitation) | **DELETE** /cloud/{cloud_pk}/invitation/{id} | Cancel a pending invitation
[**create_cloud**](CloudApi.md#create_cloud) | **POST** /cloud | Create a cloud
[**create_demo**](CloudApi.md#create_demo) | **POST** /cloud/{id}/create-demo | Create a Demo project in a cloud
[**delete_cloud**](CloudApi.md#delete_cloud) | **DELETE** /cloud/{id} | Delete a cloud
[**delete_cloud_user**](CloudApi.md#delete_cloud_user) | **DELETE** /cloud/{cloud_pk}/user/{id} | Remove a user from a cloud
[**full_update_cloud**](CloudApi.md#full_update_cloud) | **PUT** /cloud/{id} | Update all fields of a cloud
[**full_update_cloud_user**](CloudApi.md#full_update_cloud_user) | **PUT** /cloud/{cloud_pk}/user/{id} | Update all fields of a cloud user
[**get_cloud**](CloudApi.md#get_cloud) | **GET** /cloud/{id} | Retrieve one cloud
[**get_cloud_invitations**](CloudApi.md#get_cloud_invitations) | **GET** /cloud/{cloud_pk}/invitation | Retrieve all pending invitations in the cloud
[**get_cloud_size**](CloudApi.md#get_cloud_size) | **GET** /cloud/{id}/size | Get size of all files in the cloud
[**get_cloud_user**](CloudApi.md#get_cloud_user) | **GET** /cloud/{cloud_pk}/user/{id} | Retrieve a user in a cloud
[**get_cloud_users**](CloudApi.md#get_cloud_users) | **GET** /cloud/{cloud_pk}/user | Retrieve all users in a cloud
[**get_clouds**](CloudApi.md#get_clouds) | **GET** /cloud | Retrieve all clouds
[**invite_cloud_user**](CloudApi.md#invite_cloud_user) | **POST** /cloud/{cloud_pk}/invitation | Invite a cloud administrator
[**update_cloud**](CloudApi.md#update_cloud) | **PATCH** /cloud/{id} | Update some fields of a cloud
[**update_cloud_user**](CloudApi.md#update_cloud_user) | **PATCH** /cloud/{cloud_pk}/user/{id} | Update some fields of a cloud user


# **cancel_cloud_user_invitation**
> cancel_cloud_user_invitation(cloud_pk, id)

Cancel a pending invitation

Cancel a pending invitation Required scopes: org:manage

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this invitation.

try:
    # Cancel a pending invitation
    api_instance.cancel_cloud_user_invitation(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CloudApi->cancel_cloud_user_invitation: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this invitation.

try:
    # Cancel a pending invitation
    api_instance.cancel_cloud_user_invitation(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CloudApi->cancel_cloud_user_invitation: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this invitation.

try:
    # Cancel a pending invitation
    api_instance.cancel_cloud_user_invitation(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CloudApi->cancel_cloud_user_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this invitation. | 

### Return type

void (empty response body)

### Authorization

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud**
> Cloud create_cloud(data)

Create a cloud

 Required scopes: cloud:manage

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Create a cloud
    api_response = api_instance.create_cloud(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_cloud: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Create a cloud
    api_response = api_instance.create_cloud(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_cloud: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Create a cloud
    api_response = api_instance.create_cloud(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Cloud**](Cloud.md)|  | 

### Return type

[**Cloud**](Cloud.md)

### Authorization

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_demo**
> Project create_demo(id)

Create a Demo project in a cloud

Create a demo project with a pre-populated IFC and its data Required scopes: cloud:manage

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Create a Demo project in a cloud
    api_response = api_instance.create_demo(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_demo: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Create a Demo project in a cloud
    api_response = api_instance.create_demo(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_demo: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Create a Demo project in a cloud
    api_response = api_instance.create_demo(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_demo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud. | 

### Return type

[**Project**](Project.md)

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

# **delete_cloud**
> delete_cloud(id)

Delete a cloud

 Required scopes: cloud:manage

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Delete a cloud
    api_instance.delete_cloud(id)
except ApiException as e:
    print("Exception when calling CloudApi->delete_cloud: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Delete a cloud
    api_instance.delete_cloud(id)
except ApiException as e:
    print("Exception when calling CloudApi->delete_cloud: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Delete a cloud
    api_instance.delete_cloud(id)
except ApiException as e:
    print("Exception when calling CloudApi->delete_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud. | 

### Return type

void (empty response body)

### Authorization

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_user**
> delete_cloud_user(cloud_pk, id)

Remove a user from a cloud

The user will also be removed from all the projects of the cloud Required scopes: cloud:manage

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.

try:
    # Remove a user from a cloud
    api_instance.delete_cloud_user(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CloudApi->delete_cloud_user: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.

try:
    # Remove a user from a cloud
    api_instance.delete_cloud_user(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CloudApi->delete_cloud_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.

try:
    # Remove a user from a cloud
    api_instance.delete_cloud_user(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CloudApi->delete_cloud_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this fos user. | 

### Return type

void (empty response body)

### Authorization

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_cloud**
> Cloud full_update_cloud(id, data)

Update all fields of a cloud

 Required scopes: cloud:manage

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Update all fields of a cloud
    api_response = api_instance.full_update_cloud(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->full_update_cloud: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Update all fields of a cloud
    api_response = api_instance.full_update_cloud(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->full_update_cloud: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Update all fields of a cloud
    api_response = api_instance.full_update_cloud(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->full_update_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud. | 
 **data** | [**Cloud**](Cloud.md)|  | 

### Return type

[**Cloud**](Cloud.md)

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

# **full_update_cloud_user**
> User full_update_cloud_user(cloud_pk, id, data)

Update all fields of a cloud user

Change the user role in the cloud Required scopes: cloud:manage

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
data = bimdata_api_client.UserCloudUpdate() # UserCloudUpdate | 

try:
    # Update all fields of a cloud user
    api_response = api_instance.full_update_cloud_user(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->full_update_cloud_user: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
data = bimdata_api_client.UserCloudUpdate() # UserCloudUpdate | 

try:
    # Update all fields of a cloud user
    api_response = api_instance.full_update_cloud_user(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->full_update_cloud_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
data = bimdata_api_client.UserCloudUpdate() # UserCloudUpdate | 

try:
    # Update all fields of a cloud user
    api_response = api_instance.full_update_cloud_user(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->full_update_cloud_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this fos user. | 
 **data** | [**UserCloudUpdate**](UserCloudUpdate.md)|  | 

### Return type

[**User**](User.md)

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

# **get_cloud**
> Cloud get_cloud(id)

Retrieve one cloud

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Retrieve one cloud
    api_response = api_instance.get_cloud(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Retrieve one cloud
    api_response = api_instance.get_cloud(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Retrieve one cloud
    api_response = api_instance.get_cloud(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud. | 

### Return type

[**Cloud**](Cloud.md)

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

# **get_cloud_invitations**
> list[CloudInvitation] get_cloud_invitations(cloud_pk)

Retrieve all pending invitations in the cloud

Returns app's invitations only Required scopes: org:manage

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all pending invitations in the cloud
    api_response = api_instance.get_cloud_invitations(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_invitations: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all pending invitations in the cloud
    api_response = api_instance.get_cloud_invitations(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_invitations: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all pending invitations in the cloud
    api_response = api_instance.get_cloud_invitations(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 

### Return type

[**list[CloudInvitation]**](CloudInvitation.md)

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

# **get_cloud_size**
> int get_cloud_size(id)

Get size of all files in the cloud

Returns the size of the cloud in Bytes

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Get size of all files in the cloud
    api_response = api_instance.get_cloud_size(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_size: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Get size of all files in the cloud
    api_response = api_instance.get_cloud_size(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_size: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Get size of all files in the cloud
    api_response = api_instance.get_cloud_size(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud. | 

### Return type

**int**

### Authorization

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Size of the cloud in Bytes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_user**
> User get_cloud_user(cloud_pk, id)

Retrieve a user in a cloud

Only administrators can see a cloud member Required scopes: cloud:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.

try:
    # Retrieve a user in a cloud
    api_response = api_instance.get_cloud_user(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_user: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.

try:
    # Retrieve a user in a cloud
    api_response = api_instance.get_cloud_user(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.

try:
    # Retrieve a user in a cloud
    api_response = api_instance.get_cloud_user(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this fos user. | 

### Return type

[**User**](User.md)

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

# **get_cloud_users**
> list[User] get_cloud_users(cloud_pk)

Retrieve all users in a cloud

Only administrators can see all cloud members Required scopes: cloud:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all users in a cloud
    api_response = api_instance.get_cloud_users(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_users: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all users in a cloud
    api_response = api_instance.get_cloud_users(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_users: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all users in a cloud
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

[**list[User]**](User.md)

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

# **get_clouds**
> list[Cloud] get_clouds()

Retrieve all clouds

Returns user's (or app's) clouds only

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))

try:
    # Retrieve all clouds
    api_response = api_instance.get_clouds()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_clouds: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))

try:
    # Retrieve all clouds
    api_response = api_instance.get_clouds()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_clouds: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))

try:
    # Retrieve all clouds
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_cloud_user**
> CloudInvitation invite_cloud_user(cloud_pk, data)

Invite a cloud administrator

Invite cloud administrators only. To invite in a project, see inviteProjectUser. You can't invite a user already in the cloud. Create multiple invitations of the same email in the same cloud will generate multiple invitation emails but not multiple invitation object Required scopes: org:manage

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.CloudInvitation() # CloudInvitation | 

try:
    # Invite a cloud administrator
    api_response = api_instance.invite_cloud_user(cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->invite_cloud_user: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.CloudInvitation() # CloudInvitation | 

try:
    # Invite a cloud administrator
    api_response = api_instance.invite_cloud_user(cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->invite_cloud_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.CloudInvitation() # CloudInvitation | 

try:
    # Invite a cloud administrator
    api_response = api_instance.invite_cloud_user(cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->invite_cloud_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **data** | [**CloudInvitation**](CloudInvitation.md)|  | 

### Return type

[**CloudInvitation**](CloudInvitation.md)

### Authorization

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud**
> Cloud update_cloud(id, data)

Update some fields of a cloud

Update some fields of a cloud Required scopes: cloud:manage

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Update some fields of a cloud
    api_response = api_instance.update_cloud(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Update some fields of a cloud
    api_response = api_instance.update_cloud(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Update some fields of a cloud
    api_response = api_instance.update_cloud(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud. | 
 **data** | [**Cloud**](Cloud.md)|  | 

### Return type

[**Cloud**](Cloud.md)

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

# **update_cloud_user**
> User update_cloud_user(cloud_pk, id, data)

Update some fields of a cloud user

Change the user role in the cloud Required scopes: cloud:manage

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
data = bimdata_api_client.UserCloudUpdate() # UserCloudUpdate | 

try:
    # Update some fields of a cloud user
    api_response = api_instance.update_cloud_user(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud_user: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
data = bimdata_api_client.UserCloudUpdate() # UserCloudUpdate | 

try:
    # Update some fields of a cloud user
    api_response = api_instance.update_cloud_user(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CloudApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
data = bimdata_api_client.UserCloudUpdate() # UserCloudUpdate | 

try:
    # Update some fields of a cloud user
    api_response = api_instance.update_cloud_user(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this fos user. | 
 **data** | [**UserCloudUpdate**](UserCloudUpdate.md)|  | 

### Return type

[**User**](User.md)

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

