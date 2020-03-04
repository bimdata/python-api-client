# bimdata_api_client.CollaborationApi

All URIs are relative to *https://api.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_cloud_user_invitation**](CollaborationApi.md#cancel_cloud_user_invitation) | **DELETE** /cloud/{cloud_pk}/invitation/{id} | Cancel a pending invitation
[**cancel_project_user_invitation**](CollaborationApi.md#cancel_project_user_invitation) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/invitation/{id} | Cancel a pending invitation
[**create_classification**](CollaborationApi.md#create_classification) | **POST** /cloud/{cloud_pk}/project/{project_pk}/classification | Create a classification
[**create_cloud**](CollaborationApi.md#create_cloud) | **POST** /cloud | Create a cloud
[**create_demo**](CollaborationApi.md#create_demo) | **POST** /cloud/{id}/create-demo | Create a Demo project in a cloud
[**create_document**](CollaborationApi.md#create_document) | **POST** /cloud/{cloud_pk}/project/{project_pk}/document | Create a document
[**create_folder**](CollaborationApi.md#create_folder) | **POST** /cloud/{cloud_pk}/project/{project_pk}/folder | Create a folder
[**create_project**](CollaborationApi.md#create_project) | **POST** /cloud/{cloud_pk}/project | Create a project
[**delete_classification**](CollaborationApi.md#delete_classification) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | Delete a classification
[**delete_cloud**](CollaborationApi.md#delete_cloud) | **DELETE** /cloud/{id} | Delete a cloud
[**delete_cloud_user**](CollaborationApi.md#delete_cloud_user) | **DELETE** /cloud/{cloud_pk}/user/{id} | Remove a user from a cloud
[**delete_document**](CollaborationApi.md#delete_document) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | Delete the document
[**delete_folder**](CollaborationApi.md#delete_folder) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | Delete a folder
[**delete_project**](CollaborationApi.md#delete_project) | **DELETE** /cloud/{cloud_pk}/project/{id} | Delete a project
[**delete_project_user**](CollaborationApi.md#delete_project_user) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | Remove a user from a project
[**full_update_classification**](CollaborationApi.md#full_update_classification) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | Update all fields of a classification
[**full_update_cloud**](CollaborationApi.md#full_update_cloud) | **PUT** /cloud/{id} | Update all fields of a cloud
[**full_update_cloud_user**](CollaborationApi.md#full_update_cloud_user) | **PUT** /cloud/{cloud_pk}/user/{id} | Update all fields of a cloud user
[**full_update_document**](CollaborationApi.md#full_update_document) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | Update all fields of the document
[**full_update_folder**](CollaborationApi.md#full_update_folder) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | Update all fields of a folder
[**full_update_project**](CollaborationApi.md#full_update_project) | **PUT** /cloud/{cloud_pk}/project/{id} | Update all fields of a project
[**full_update_project_user**](CollaborationApi.md#full_update_project_user) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | Update all fields of a project user
[**get_classification**](CollaborationApi.md#get_classification) | **GET** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | Retrieve a classification
[**get_classifications**](CollaborationApi.md#get_classifications) | **GET** /cloud/{cloud_pk}/project/{project_pk}/classification | Retrieve all classifications
[**get_cloud**](CollaborationApi.md#get_cloud) | **GET** /cloud/{id} | Retrieve one cloud
[**get_cloud_invitations**](CollaborationApi.md#get_cloud_invitations) | **GET** /cloud/{cloud_pk}/invitation | Retrieve all pending invitations in the cloud
[**get_cloud_size**](CollaborationApi.md#get_cloud_size) | **GET** /cloud/{id}/size | Get size of all files in the cloud
[**get_cloud_user**](CollaborationApi.md#get_cloud_user) | **GET** /cloud/{cloud_pk}/user/{id} | Retrieve a user in a cloud
[**get_cloud_users**](CollaborationApi.md#get_cloud_users) | **GET** /cloud/{cloud_pk}/user | Retrieve all users in a cloud, or a list with a filter by email
[**get_clouds**](CollaborationApi.md#get_clouds) | **GET** /cloud | Retrieve all clouds
[**get_document**](CollaborationApi.md#get_document) | **GET** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | Retrieve a document
[**get_documents**](CollaborationApi.md#get_documents) | **GET** /cloud/{cloud_pk}/project/{project_pk}/document | Retrieve all documents
[**get_folder**](CollaborationApi.md#get_folder) | **GET** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | Retrieve a folder
[**get_folders**](CollaborationApi.md#get_folders) | **GET** /cloud/{cloud_pk}/project/{project_pk}/folder | Retrieve all folders
[**get_project**](CollaborationApi.md#get_project) | **GET** /cloud/{cloud_pk}/project/{id} | Retrieve a project
[**get_project_dms_tree**](CollaborationApi.md#get_project_dms_tree) | **GET** /cloud/{cloud_pk}/project/{id}/dms-tree | Retrieve the complete DMS tree
[**get_project_invitations**](CollaborationApi.md#get_project_invitations) | **GET** /cloud/{cloud_pk}/project/{project_pk}/invitation | Retrieve all pending invitations in the project
[**get_project_sub_tree**](CollaborationApi.md#get_project_sub_tree) | **GET** /cloud/{cloud_pk}/project/subtree | Retrieve the complete projects tree of the cloud
[**get_project_tree**](CollaborationApi.md#get_project_tree) | **GET** /cloud/{cloud_pk}/project/{id}/tree | Retrieve the complete DMS tree
[**get_project_user**](CollaborationApi.md#get_project_user) | **GET** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | Retrieve a user in a project
[**get_project_users**](CollaborationApi.md#get_project_users) | **GET** /cloud/{cloud_pk}/project/{project_pk}/user | Retrieve all users in a project, or a list with a filter by email
[**get_projects**](CollaborationApi.md#get_projects) | **GET** /cloud/{cloud_pk}/project | Retrieve all projects
[**get_self_projects**](CollaborationApi.md#get_self_projects) | **GET** /user/projects | List current user&#39;s projects
[**get_self_user**](CollaborationApi.md#get_self_user) | **GET** /user | Get info about the current user
[**invite_cloud_user**](CollaborationApi.md#invite_cloud_user) | **POST** /cloud/{cloud_pk}/invitation | Invite a cloud administrator
[**invite_project_user**](CollaborationApi.md#invite_project_user) | **POST** /cloud/{cloud_pk}/project/{project_pk}/invitation | Invite a project member
[**update_classification**](CollaborationApi.md#update_classification) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | Update some fields of a classification
[**update_cloud**](CollaborationApi.md#update_cloud) | **PATCH** /cloud/{id} | Update some fields of a cloud
[**update_cloud_user**](CollaborationApi.md#update_cloud_user) | **PATCH** /cloud/{cloud_pk}/user/{id} | Update some fields of a cloud user
[**update_document**](CollaborationApi.md#update_document) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | Update some fields of the document
[**update_folder**](CollaborationApi.md#update_folder) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | Update some fields of a folder
[**update_project**](CollaborationApi.md#update_project) | **PATCH** /cloud/{cloud_pk}/project/{id} | Update some fields of a project
[**update_project_user**](CollaborationApi.md#update_project_user) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | Update some fields of a project user
[**update_self_user**](CollaborationApi.md#update_self_user) | **PATCH** /user | Update info of the current user


# **cancel_cloud_user_invitation**
> cancel_cloud_user_invitation(cloud_pk, id)

Cancel a pending invitation

Cancel a pending invitation Required scopes: org:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this invitation.

try:
    # Cancel a pending invitation
    api_instance.cancel_cloud_user_invitation(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CollaborationApi->cancel_cloud_user_invitation: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this invitation.

try:
    # Cancel a pending invitation
    api_instance.cancel_cloud_user_invitation(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CollaborationApi->cancel_cloud_user_invitation: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this invitation.

try:
    # Cancel a pending invitation
    api_instance.cancel_cloud_user_invitation(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CollaborationApi->cancel_cloud_user_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this invitation. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_project_user_invitation**
> cancel_project_user_invitation(cloud_pk, id, project_pk)

Cancel a pending invitation

 Required scopes: org:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this invitation.
project_pk = 'project_pk_example' # str | 

try:
    # Cancel a pending invitation
    api_instance.cancel_project_user_invitation(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->cancel_project_user_invitation: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this invitation.
project_pk = 'project_pk_example' # str | 

try:
    # Cancel a pending invitation
    api_instance.cancel_project_user_invitation(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->cancel_project_user_invitation: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this invitation.
project_pk = 'project_pk_example' # str | 

try:
    # Cancel a pending invitation
    api_instance.cancel_project_user_invitation(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->cancel_project_user_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this invitation. | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_classification**
> list[Classification] create_classification(cloud_pk, project_pk, data)

Create a classification

         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors      If created classification already exists, it will not be duplicated and the previous one will be returned.     You also can add a 'classification' filter on this endpoint. By ex: /classification?name='untec'. The name is case sensitive  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Classification()] # list[Classification] | 

try:
    # Create a classification
    api_response = api_instance.create_classification(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_classification: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Classification()] # list[Classification] | 

try:
    # Create a classification
    api_response = api_instance.create_classification(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_classification: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Classification()] # list[Classification] | 

try:
    # Create a classification
    api_response = api_instance.create_classification(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**list[Classification]**](Classification.md)|  | 

### Return type

[**list[Classification]**](Classification.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud**
> Cloud create_cloud(data)

Create a cloud

 Required scopes: cloud:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Create a cloud
    api_response = api_instance.create_cloud(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_cloud: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Create a cloud
    api_response = api_instance.create_cloud(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_cloud: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Create a cloud
    api_response = api_instance.create_cloud(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Cloud**](Cloud.md)|  | 

### Return type

[**Cloud**](Cloud.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_demo**
> Project create_demo(id)

Create a Demo project in a cloud

Create a demo project with a pre-populated IFC and its data Required scopes: cloud:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Create a Demo project in a cloud
    api_response = api_instance.create_demo(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_demo: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Create a Demo project in a cloud
    api_response = api_instance.create_demo(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_demo: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Create a Demo project in a cloud
    api_response = api_instance.create_demo(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_demo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud. | 

### Return type

[**Project**](Project.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document**
> Document create_document(cloud_pk, project_pk, name, file, parent=parent, parent_id=parent_id, creator=creator, file_name=file_name, description=description, size=size, ifc_source=ifc_source)

Create a document

RCreate a document. If the document is an IFC, an IFC model will be created and attached to this document Required scopes: document:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
name = 'name_example' # str | Shown name of the file
file = '/path/to/file' # file | 
parent = 56 # int |  (optional)
parent_id = 56 # int |  (optional)
creator = 56 # int |  (optional)
file_name = 'file_name_example' # str | Full name of the file (optional)
description = 'description_example' # str | Description of the file (optional)
size = 56 # int | Size of the file. (optional)
ifc_source = 'ifc_source_example' # str | Define the ifc.source field if the upload is an IFC (optional)

try:
    # Create a document
    api_response = api_instance.create_document(cloud_pk, project_pk, name, file, parent=parent, parent_id=parent_id, creator=creator, file_name=file_name, description=description, size=size, ifc_source=ifc_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_document: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
name = 'name_example' # str | Shown name of the file
file = '/path/to/file' # file | 
parent = 56 # int |  (optional)
parent_id = 56 # int |  (optional)
creator = 56 # int |  (optional)
file_name = 'file_name_example' # str | Full name of the file (optional)
description = 'description_example' # str | Description of the file (optional)
size = 56 # int | Size of the file. (optional)
ifc_source = 'ifc_source_example' # str | Define the ifc.source field if the upload is an IFC (optional)

try:
    # Create a document
    api_response = api_instance.create_document(cloud_pk, project_pk, name, file, parent=parent, parent_id=parent_id, creator=creator, file_name=file_name, description=description, size=size, ifc_source=ifc_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_document: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
name = 'name_example' # str | Shown name of the file
file = '/path/to/file' # file | 
parent = 56 # int |  (optional)
parent_id = 56 # int |  (optional)
creator = 56 # int |  (optional)
file_name = 'file_name_example' # str | Full name of the file (optional)
description = 'description_example' # str | Description of the file (optional)
size = 56 # int | Size of the file. (optional)
ifc_source = 'ifc_source_example' # str | Define the ifc.source field if the upload is an IFC (optional)

try:
    # Create a document
    api_response = api_instance.create_document(cloud_pk, project_pk, name, file, parent=parent, parent_id=parent_id, creator=creator, file_name=file_name, description=description, size=size, ifc_source=ifc_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **name** | **str**| Shown name of the file | 
 **file** | **file**|  | 
 **parent** | **int**|  | [optional] 
 **parent_id** | **int**|  | [optional] 
 **creator** | **int**|  | [optional] 
 **file_name** | **str**| Full name of the file | [optional] 
 **description** | **str**| Description of the file | [optional] 
 **size** | **int**| Size of the file. | [optional] 
 **ifc_source** | **str**| Define the ifc.source field if the upload is an IFC | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> Folder create_folder(cloud_pk, project_pk, data)

Create a folder

If the created folder have no parent, it will be put as a child of the default root folder of the project Required scopes: document:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Create a folder
    api_response = api_instance.create_folder(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_folder: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Create a folder
    api_response = api_instance.create_folder(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_folder: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Create a folder
    api_response = api_instance.create_folder(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**Folder**](Folder.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> Project create_project(cloud_pk, data)

Create a project

Create a project Required scopes: org:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.Project() # Project | 

try:
    # Create a project
    api_response = api_instance.create_project(cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_project: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.Project() # Project | 

try:
    # Create a project
    api_response = api_instance.create_project(cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_project: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.Project() # Project | 

try:
    # Create a project
    api_response = api_instance.create_project(cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **data** | [**Project**](Project.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_classification**
> delete_classification(cloud_pk, id, project_pk)

Delete a classification

All elements having this classification will lose it Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a classification
    api_instance.delete_classification(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_classification: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a classification
    api_instance.delete_classification(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_classification: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a classification
    api_instance.delete_classification(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this classification. | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud**
> delete_cloud(id)

Delete a cloud

 Required scopes: cloud:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Delete a cloud
    api_instance.delete_cloud(id)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_cloud: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Delete a cloud
    api_instance.delete_cloud(id)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_cloud: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Delete a cloud
    api_instance.delete_cloud(id)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_user**
> delete_cloud_user(cloud_pk, id)

Remove a user from a cloud

The user will also be removed from all the projects of the cloud Required scopes: cloud:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.

try:
    # Remove a user from a cloud
    api_instance.delete_cloud_user(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_cloud_user: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.

try:
    # Remove a user from a cloud
    api_instance.delete_cloud_user(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_cloud_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.

try:
    # Remove a user from a cloud
    api_instance.delete_cloud_user(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_cloud_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this fos user. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> delete_document(cloud_pk, id, project_pk)

Delete the document

Delete the document Required scopes: document:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 

try:
    # Delete the document
    api_instance.delete_document(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_document: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 

try:
    # Delete the document
    api_instance.delete_document(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_document: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 

try:
    # Delete the document
    api_instance.delete_document(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this document. | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> delete_folder(cloud_pk, id, project_pk)

Delete a folder

All files and subfolders will be deleted too. If folder is a project's root folder, only children are deleted Required scopes: document:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a folder
    api_instance.delete_folder(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_folder: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a folder
    api_instance.delete_folder(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_folder: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a folder
    api_instance.delete_folder(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this folder. | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(cloud_pk, id)

Delete a project

It can take a long time to respond because we may need to delete all properties of all elements of all models in the project Required scopes: org:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Delete a project
    api_instance.delete_project(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_project: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Delete a project
    api_instance.delete_project(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_project: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Delete a project
    api_instance.delete_project(cloud_pk, id)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this project. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_user**
> delete_project_user(cloud_pk, id, project_pk)

Remove a user from a project

Remove a user from a project Required scopes: cloud:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 

try:
    # Remove a user from a project
    api_instance.delete_project_user(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_project_user: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 

try:
    # Remove a user from a project
    api_instance.delete_project_user(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_project_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 

try:
    # Remove a user from a project
    api_instance.delete_project_user(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CollaborationApi->delete_project_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this fos user. | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_classification**
> Classification full_update_classification(cloud_pk, id, project_pk, data)

Update all fields of a classification

Update all fields of a classification Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Classification() # Classification | 

try:
    # Update all fields of a classification
    api_response = api_instance.full_update_classification(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_classification: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Classification() # Classification | 

try:
    # Update all fields of a classification
    api_response = api_instance.full_update_classification(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_classification: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Classification() # Classification | 

try:
    # Update all fields of a classification
    api_response = api_instance.full_update_classification(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this classification. | 
 **project_pk** | **str**|  | 
 **data** | [**Classification**](Classification.md)|  | 

### Return type

[**Classification**](Classification.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_cloud**
> Cloud full_update_cloud(id, data)

Update all fields of a cloud

 Required scopes: cloud:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Update all fields of a cloud
    api_response = api_instance.full_update_cloud(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_cloud: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Update all fields of a cloud
    api_response = api_instance.full_update_cloud(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_cloud: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Update all fields of a cloud
    api_response = api_instance.full_update_cloud(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud. | 
 **data** | [**Cloud**](Cloud.md)|  | 

### Return type

[**Cloud**](Cloud.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_cloud_user**
> User full_update_cloud_user(cloud_pk, id, data)

Update all fields of a cloud user

Change the user role in the cloud Required scopes: cloud:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
data = bimdata_api_client.UserCloudUpdate() # UserCloudUpdate | 

try:
    # Update all fields of a cloud user
    api_response = api_instance.full_update_cloud_user(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_cloud_user: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
data = bimdata_api_client.UserCloudUpdate() # UserCloudUpdate | 

try:
    # Update all fields of a cloud user
    api_response = api_instance.full_update_cloud_user(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_cloud_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
data = bimdata_api_client.UserCloudUpdate() # UserCloudUpdate | 

try:
    # Update all fields of a cloud user
    api_response = api_instance.full_update_cloud_user(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_cloud_user: %s\n" % e)
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

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_document**
> Document full_update_document(cloud_pk, id, project_pk, name, file, parent=parent, parent_id=parent_id, creator=creator, file_name=file_name, description=description, size=size, ifc_source=ifc_source)

Update all fields of the document

Update all fields of the document Required scopes: document:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 
name = 'name_example' # str | Shown name of the file
file = '/path/to/file' # file | 
parent = 56 # int |  (optional)
parent_id = 56 # int |  (optional)
creator = 56 # int |  (optional)
file_name = 'file_name_example' # str | Full name of the file (optional)
description = 'description_example' # str | Description of the file (optional)
size = 56 # int | Size of the file. (optional)
ifc_source = 'ifc_source_example' # str | Define the ifc.source field if the upload is an IFC (optional)

try:
    # Update all fields of the document
    api_response = api_instance.full_update_document(cloud_pk, id, project_pk, name, file, parent=parent, parent_id=parent_id, creator=creator, file_name=file_name, description=description, size=size, ifc_source=ifc_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_document: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 
name = 'name_example' # str | Shown name of the file
file = '/path/to/file' # file | 
parent = 56 # int |  (optional)
parent_id = 56 # int |  (optional)
creator = 56 # int |  (optional)
file_name = 'file_name_example' # str | Full name of the file (optional)
description = 'description_example' # str | Description of the file (optional)
size = 56 # int | Size of the file. (optional)
ifc_source = 'ifc_source_example' # str | Define the ifc.source field if the upload is an IFC (optional)

try:
    # Update all fields of the document
    api_response = api_instance.full_update_document(cloud_pk, id, project_pk, name, file, parent=parent, parent_id=parent_id, creator=creator, file_name=file_name, description=description, size=size, ifc_source=ifc_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_document: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 
name = 'name_example' # str | Shown name of the file
file = '/path/to/file' # file | 
parent = 56 # int |  (optional)
parent_id = 56 # int |  (optional)
creator = 56 # int |  (optional)
file_name = 'file_name_example' # str | Full name of the file (optional)
description = 'description_example' # str | Description of the file (optional)
size = 56 # int | Size of the file. (optional)
ifc_source = 'ifc_source_example' # str | Define the ifc.source field if the upload is an IFC (optional)

try:
    # Update all fields of the document
    api_response = api_instance.full_update_document(cloud_pk, id, project_pk, name, file, parent=parent, parent_id=parent_id, creator=creator, file_name=file_name, description=description, size=size, ifc_source=ifc_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this document. | 
 **project_pk** | **str**|  | 
 **name** | **str**| Shown name of the file | 
 **file** | **file**|  | 
 **parent** | **int**|  | [optional] 
 **parent_id** | **int**|  | [optional] 
 **creator** | **int**|  | [optional] 
 **file_name** | **str**| Full name of the file | [optional] 
 **description** | **str**| Description of the file | [optional] 
 **size** | **int**| Size of the file. | [optional] 
 **ifc_source** | **str**| Define the ifc.source field if the upload is an IFC | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_folder**
> Folder full_update_folder(cloud_pk, id, project_pk, data)

Update all fields of a folder

Update all fields of a folder Required scopes: document:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Update all fields of a folder
    api_response = api_instance.full_update_folder(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_folder: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Update all fields of a folder
    api_response = api_instance.full_update_folder(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_folder: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Update all fields of a folder
    api_response = api_instance.full_update_folder(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this folder. | 
 **project_pk** | **str**|  | 
 **data** | [**Folder**](Folder.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_project**
> Project full_update_project(cloud_pk, id, data)

Update all fields of a project

Update all fields of a project Required scopes: org:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.Project() # Project | 

try:
    # Update all fields of a project
    api_response = api_instance.full_update_project(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_project: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.Project() # Project | 

try:
    # Update all fields of a project
    api_response = api_instance.full_update_project(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_project: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.Project() # Project | 

try:
    # Update all fields of a project
    api_response = api_instance.full_update_project(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this project. | 
 **data** | [**Project**](Project.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_project_user**
> User full_update_project_user(cloud_pk, id, project_pk, data)

Update all fields of a project user

Change the user role in the cloud Required scopes: cloud:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.UserProjectUpdate() # UserProjectUpdate | 

try:
    # Update all fields of a project user
    api_response = api_instance.full_update_project_user(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_project_user: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.UserProjectUpdate() # UserProjectUpdate | 

try:
    # Update all fields of a project user
    api_response = api_instance.full_update_project_user(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_project_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.UserProjectUpdate() # UserProjectUpdate | 

try:
    # Update all fields of a project user
    api_response = api_instance.full_update_project_user(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->full_update_project_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this fos user. | 
 **project_pk** | **str**|  | 
 **data** | [**UserProjectUpdate**](UserProjectUpdate.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classification**
> Classification get_classification(cloud_pk, id, project_pk)

Retrieve a classification

Retrieve a classification Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a classification
    api_response = api_instance.get_classification(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_classification: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a classification
    api_response = api_instance.get_classification(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_classification: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a classification
    api_response = api_instance.get_classification(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this classification. | 
 **project_pk** | **str**|  | 

### Return type

[**Classification**](Classification.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classifications**
> list[Classification] get_classifications(cloud_pk, project_pk)

Retrieve all classifications

Retrieve all classifications of all models in the project Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all classifications
    api_response = api_instance.get_classifications(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_classifications: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all classifications
    api_response = api_instance.get_classifications(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_classifications: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all classifications
    api_response = api_instance.get_classifications(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Classification]**](Classification.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud**
> Cloud get_cloud(id)

Retrieve one cloud

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Retrieve one cloud
    api_response = api_instance.get_cloud(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Retrieve one cloud
    api_response = api_instance.get_cloud(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Retrieve one cloud
    api_response = api_instance.get_cloud(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud. | 

### Return type

[**Cloud**](Cloud.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_invitations**
> list[CloudInvitation] get_cloud_invitations(cloud_pk)

Retrieve all pending invitations in the cloud

Returns app's invitations only Required scopes: org:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all pending invitations in the cloud
    api_response = api_instance.get_cloud_invitations(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud_invitations: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all pending invitations in the cloud
    api_response = api_instance.get_cloud_invitations(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud_invitations: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all pending invitations in the cloud
    api_response = api_instance.get_cloud_invitations(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 

### Return type

[**list[CloudInvitation]**](CloudInvitation.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_size**
> int get_cloud_size(id)

Get size of all files in the cloud

Returns the size of the cloud in Bytes

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Get size of all files in the cloud
    api_response = api_instance.get_cloud_size(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud_size: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Get size of all files in the cloud
    api_response = api_instance.get_cloud_size(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud_size: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.

try:
    # Get size of all files in the cloud
    api_response = api_instance.get_cloud_size(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud_size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud. | 

### Return type

**int**

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Size of the cloud in Bytes |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_user**
> User get_cloud_user(cloud_pk, id)

Retrieve a user in a cloud

Only administrators can see a cloud member Required scopes: cloud:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.

try:
    # Retrieve a user in a cloud
    api_response = api_instance.get_cloud_user(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud_user: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.

try:
    # Retrieve a user in a cloud
    api_response = api_instance.get_cloud_user(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.

try:
    # Retrieve a user in a cloud
    api_response = api_instance.get_cloud_user(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this fos user. | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_users**
> list[User] get_cloud_users(cloud_pk, email=email, email__contains=email__contains, email__startswith=email__startswith, email__endswith=email__endswith)

Retrieve all users in a cloud, or a list with a filter by email

Only administrators can see cloud members. Required scopes: cloud:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
email = 'email_example' # str | Filter the returned list by email (optional)
email__contains = 'email__contains_example' # str | Filter the returned list by email__contains (optional)
email__startswith = 'email__startswith_example' # str | Filter the returned list by email__startswith (optional)
email__endswith = 'email__endswith_example' # str | Filter the returned list by email__endswith (optional)

try:
    # Retrieve all users in a cloud, or a list with a filter by email
    api_response = api_instance.get_cloud_users(cloud_pk, email=email, email__contains=email__contains, email__startswith=email__startswith, email__endswith=email__endswith)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud_users: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
email = 'email_example' # str | Filter the returned list by email (optional)
email__contains = 'email__contains_example' # str | Filter the returned list by email__contains (optional)
email__startswith = 'email__startswith_example' # str | Filter the returned list by email__startswith (optional)
email__endswith = 'email__endswith_example' # str | Filter the returned list by email__endswith (optional)

try:
    # Retrieve all users in a cloud, or a list with a filter by email
    api_response = api_instance.get_cloud_users(cloud_pk, email=email, email__contains=email__contains, email__startswith=email__startswith, email__endswith=email__endswith)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud_users: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
email = 'email_example' # str | Filter the returned list by email (optional)
email__contains = 'email__contains_example' # str | Filter the returned list by email__contains (optional)
email__startswith = 'email__startswith_example' # str | Filter the returned list by email__startswith (optional)
email__endswith = 'email__endswith_example' # str | Filter the returned list by email__endswith (optional)

try:
    # Retrieve all users in a cloud, or a list with a filter by email
    api_response = api_instance.get_cloud_users(cloud_pk, email=email, email__contains=email__contains, email__startswith=email__startswith, email__endswith=email__endswith)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_cloud_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **email** | **str**| Filter the returned list by email | [optional] 
 **email__contains** | **str**| Filter the returned list by email__contains | [optional] 
 **email__startswith** | **str**| Filter the returned list by email__startswith | [optional] 
 **email__endswith** | **str**| Filter the returned list by email__endswith | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clouds**
> list[Cloud] get_clouds()

Retrieve all clouds

Returns user's (or app's) clouds only

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))

try:
    # Retrieve all clouds
    api_response = api_instance.get_clouds()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_clouds: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))

try:
    # Retrieve all clouds
    api_response = api_instance.get_clouds()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_clouds: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))

try:
    # Retrieve all clouds
    api_response = api_instance.get_clouds()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_clouds: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Cloud]**](Cloud.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> Document get_document(cloud_pk, id, project_pk)

Retrieve a document

Retrieve a document in the project Required scopes: document:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a document
    api_response = api_instance.get_document(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_document: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a document
    api_response = api_instance.get_document(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_document: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a document
    api_response = api_instance.get_document(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this document. | 
 **project_pk** | **str**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents**
> list[Document] get_documents(cloud_pk, project_pk)

Retrieve all documents

Retrieve all documents in the project Required scopes: document:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all documents
    api_response = api_instance.get_documents(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_documents: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all documents
    api_response = api_instance.get_documents(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_documents: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all documents
    api_response = api_instance.get_documents(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Document]**](Document.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder**
> Folder get_folder(cloud_pk, id, project_pk)

Retrieve a folder

Retrieve a folder Required scopes: document:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a folder
    api_response = api_instance.get_folder(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_folder: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a folder
    api_response = api_instance.get_folder(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_folder: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a folder
    api_response = api_instance.get_folder(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this folder. | 
 **project_pk** | **str**|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folders**
> list[Folder] get_folders(cloud_pk, project_pk)

Retrieve all folders

Retrieve all folders in the project. This is an array of folder. If you want to get the tree of all folders, see getProjectTree Required scopes: document:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all folders
    api_response = api_instance.get_folders(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_folders: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all folders
    api_response = api_instance.get_folders(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_folders: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all folders
    api_response = api_instance.get_folders(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Folder]**](Folder.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ProjectWithChildren get_project(cloud_pk, id)

Retrieve a project

Retrieve a project

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve a project
    api_response = api_instance.get_project(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve a project
    api_response = api_instance.get_project(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve a project
    api_response = api_instance.get_project(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this project. | 

### Return type

[**ProjectWithChildren**](ProjectWithChildren.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_dms_tree**
> Folder get_project_dms_tree(cloud_pk, id)

Retrieve the complete DMS tree

Retrieve the complete DMS tree (all folders and all documents in the project)

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve the complete DMS tree
    api_response = api_instance.get_project_dms_tree(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_dms_tree: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve the complete DMS tree
    api_response = api_instance.get_project_dms_tree(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_dms_tree: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve the complete DMS tree
    api_response = api_instance.get_project_dms_tree(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_dms_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this project. | 

### Return type

[**Folder**](Folder.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_invitations**
> list[ProjectInvitation] get_project_invitations(cloud_pk, project_pk)

Retrieve all pending invitations in the project

Returns app's invitations only Required scopes: org:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all pending invitations in the project
    api_response = api_instance.get_project_invitations(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_invitations: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all pending invitations in the project
    api_response = api_instance.get_project_invitations(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_invitations: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all pending invitations in the project
    api_response = api_instance.get_project_invitations(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[ProjectInvitation]**](ProjectInvitation.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_sub_tree**
> list[ProjectWithChildren] get_project_sub_tree(cloud_pk)

Retrieve the complete projects tree of the cloud

Retrieve the complete projects tree of the cloud

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve the complete projects tree of the cloud
    api_response = api_instance.get_project_sub_tree(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_sub_tree: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve the complete projects tree of the cloud
    api_response = api_instance.get_project_sub_tree(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_sub_tree: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve the complete projects tree of the cloud
    api_response = api_instance.get_project_sub_tree(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_sub_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 

### Return type

[**list[ProjectWithChildren]**](ProjectWithChildren.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tree**
> Folder get_project_tree(cloud_pk, id)

Retrieve the complete DMS tree

Retrieve the complete DMS tree (all folders and all documents in the project). DEPRECATED: renamed to getProjectDMSTree

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve the complete DMS tree
    api_response = api_instance.get_project_tree(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_tree: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve the complete DMS tree
    api_response = api_instance.get_project_tree(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_tree: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve the complete DMS tree
    api_response = api_instance.get_project_tree(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this project. | 

### Return type

[**Folder**](Folder.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_user**
> User get_project_user(cloud_pk, id, project_pk)

Retrieve a user in a project

Each member of a project can see other members of the project Required scopes: cloud:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a user in a project
    api_response = api_instance.get_project_user(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_user: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a user in a project
    api_response = api_instance.get_project_user(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a user in a project
    api_response = api_instance.get_project_user(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this fos user. | 
 **project_pk** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_users**
> list[User] get_project_users(cloud_pk, project_pk, email=email, email__contains=email__contains, email__startswith=email__startswith, email__endswith=email__endswith)

Retrieve all users in a project, or a list with a filter by email

Each member of a project can see other members of the project Required scopes: cloud:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
email = 'email_example' # str | Filter the returned list by email (optional)
email__contains = 'email__contains_example' # str | Filter the returned list by email__contains (optional)
email__startswith = 'email__startswith_example' # str | Filter the returned list by email__startswith (optional)
email__endswith = 'email__endswith_example' # str | Filter the returned list by email__endswith (optional)

try:
    # Retrieve all users in a project, or a list with a filter by email
    api_response = api_instance.get_project_users(cloud_pk, project_pk, email=email, email__contains=email__contains, email__startswith=email__startswith, email__endswith=email__endswith)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_users: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
email = 'email_example' # str | Filter the returned list by email (optional)
email__contains = 'email__contains_example' # str | Filter the returned list by email__contains (optional)
email__startswith = 'email__startswith_example' # str | Filter the returned list by email__startswith (optional)
email__endswith = 'email__endswith_example' # str | Filter the returned list by email__endswith (optional)

try:
    # Retrieve all users in a project, or a list with a filter by email
    api_response = api_instance.get_project_users(cloud_pk, project_pk, email=email, email__contains=email__contains, email__startswith=email__startswith, email__endswith=email__endswith)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_users: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
email = 'email_example' # str | Filter the returned list by email (optional)
email__contains = 'email__contains_example' # str | Filter the returned list by email__contains (optional)
email__startswith = 'email__startswith_example' # str | Filter the returned list by email__startswith (optional)
email__endswith = 'email__endswith_example' # str | Filter the returned list by email__endswith (optional)

try:
    # Retrieve all users in a project, or a list with a filter by email
    api_response = api_instance.get_project_users(cloud_pk, project_pk, email=email, email__contains=email__contains, email__startswith=email__startswith, email__endswith=email__endswith)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_project_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **email** | **str**| Filter the returned list by email | [optional] 
 **email__contains** | **str**| Filter the returned list by email__contains | [optional] 
 **email__startswith** | **str**| Filter the returned list by email__startswith | [optional] 
 **email__endswith** | **str**| Filter the returned list by email__endswith | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> list[Project] get_projects(cloud_pk)

Retrieve all projects

Retrieve all projects of the cloud. All project are shown at the same level. see #getProjectSubTree

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all projects
    api_response = api_instance.get_projects(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_projects: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all projects
    api_response = api_instance.get_projects(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_projects: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all projects
    api_response = api_instance.get_projects(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 

### Return type

[**list[Project]**](Project.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_projects**
> list[Project] get_self_projects()

List current user's projects

List user's projects of all clouds Required scopes: user:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))

try:
    # List current user's projects
    api_response = api_instance.get_self_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_self_projects: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))

try:
    # List current user's projects
    api_response = api_instance.get_self_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_self_projects: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))

try:
    # List current user's projects
    api_response = api_instance.get_self_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_self_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Project]**](Project.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_user**
> SelfUser get_self_user()

Get info about the current user

Get info about the current user

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))

try:
    # Get info about the current user
    api_response = api_instance.get_self_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_self_user: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))

try:
    # Get info about the current user
    api_response = api_instance.get_self_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_self_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))

try:
    # Get info about the current user
    api_response = api_instance.get_self_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->get_self_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SelfUser**](SelfUser.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_cloud_user**
> CloudInvitation invite_cloud_user(cloud_pk, data)

Invite a cloud administrator

Invite cloud administrators only. To invite in a project, see inviteProjectUser. You can't invite a user already in the cloud. Create multiple invitations of the same email in the same cloud will generate multiple invitation emails but not multiple invitation object Required scopes: org:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.CloudInvitation() # CloudInvitation | 

try:
    # Invite a cloud administrator
    api_response = api_instance.invite_cloud_user(cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->invite_cloud_user: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.CloudInvitation() # CloudInvitation | 

try:
    # Invite a cloud administrator
    api_response = api_instance.invite_cloud_user(cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->invite_cloud_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.CloudInvitation() # CloudInvitation | 

try:
    # Invite a cloud administrator
    api_response = api_instance.invite_cloud_user(cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->invite_cloud_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **data** | [**CloudInvitation**](CloudInvitation.md)|  | 

### Return type

[**CloudInvitation**](CloudInvitation.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_project_user**
> ProjectInvitation invite_project_user(cloud_pk, project_pk, data)

Invite a project member

Invite a project member. If the user is not already a cloud member, they will also be invited in the cloud with USER role. Required scopes: org:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.ProjectInvitation() # ProjectInvitation | 

try:
    # Invite a project member
    api_response = api_instance.invite_project_user(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->invite_project_user: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.ProjectInvitation() # ProjectInvitation | 

try:
    # Invite a project member
    api_response = api_instance.invite_project_user(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->invite_project_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.ProjectInvitation() # ProjectInvitation | 

try:
    # Invite a project member
    api_response = api_instance.invite_project_user(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->invite_project_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**ProjectInvitation**](ProjectInvitation.md)|  | 

### Return type

[**ProjectInvitation**](ProjectInvitation.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_classification**
> Classification update_classification(cloud_pk, id, project_pk, data)

Update some fields of a classification

Update some fields of a classification Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Classification() # Classification | 

try:
    # Update some fields of a classification
    api_response = api_instance.update_classification(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_classification: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Classification() # Classification | 

try:
    # Update some fields of a classification
    api_response = api_instance.update_classification(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_classification: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Classification() # Classification | 

try:
    # Update some fields of a classification
    api_response = api_instance.update_classification(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this classification. | 
 **project_pk** | **str**|  | 
 **data** | [**Classification**](Classification.md)|  | 

### Return type

[**Classification**](Classification.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud**
> Cloud update_cloud(id, data)

Update some fields of a cloud

Update some fields of a cloud Required scopes: cloud:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Update some fields of a cloud
    api_response = api_instance.update_cloud(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_cloud: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Update some fields of a cloud
    api_response = api_instance.update_cloud(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_cloud: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cloud.
data = bimdata_api_client.Cloud() # Cloud | 

try:
    # Update some fields of a cloud
    api_response = api_instance.update_cloud(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cloud. | 
 **data** | [**Cloud**](Cloud.md)|  | 

### Return type

[**Cloud**](Cloud.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_user**
> User update_cloud_user(cloud_pk, id, data)

Update some fields of a cloud user

Change the user role in the cloud Required scopes: cloud:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
data = bimdata_api_client.UserCloudUpdate() # UserCloudUpdate | 

try:
    # Update some fields of a cloud user
    api_response = api_instance.update_cloud_user(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_cloud_user: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
data = bimdata_api_client.UserCloudUpdate() # UserCloudUpdate | 

try:
    # Update some fields of a cloud user
    api_response = api_instance.update_cloud_user(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_cloud_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
data = bimdata_api_client.UserCloudUpdate() # UserCloudUpdate | 

try:
    # Update some fields of a cloud user
    api_response = api_instance.update_cloud_user(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_cloud_user: %s\n" % e)
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

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> Document update_document(cloud_pk, id, project_pk, data)

Update some fields of the document

Update some fields of the document Required scopes: document:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Document() # Document | 

try:
    # Update some fields of the document
    api_response = api_instance.update_document(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_document: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Document() # Document | 

try:
    # Update some fields of the document
    api_response = api_instance.update_document(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_document: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Document() # Document | 

try:
    # Update some fields of the document
    api_response = api_instance.update_document(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this document. | 
 **project_pk** | **str**|  | 
 **data** | [**Document**](Document.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folder**
> Folder update_folder(cloud_pk, id, project_pk, data)

Update some fields of a folder

Update some fields of a folder Required scopes: document:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Update some fields of a folder
    api_response = api_instance.update_folder(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_folder: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Update some fields of a folder
    api_response = api_instance.update_folder(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_folder: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Update some fields of a folder
    api_response = api_instance.update_folder(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this folder. | 
 **project_pk** | **str**|  | 
 **data** | [**Folder**](Folder.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(cloud_pk, id, data)

Update some fields of a project

Update some fields of a project Required scopes: org:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.Project() # Project | 

try:
    # Update some fields of a project
    api_response = api_instance.update_project(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_project: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.Project() # Project | 

try:
    # Update some fields of a project
    api_response = api_instance.update_project(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_project: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.Project() # Project | 

try:
    # Update some fields of a project
    api_response = api_instance.update_project(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this project. | 
 **data** | [**Project**](Project.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_user**
> User update_project_user(cloud_pk, id, project_pk, data)

Update some fields of a project user

Change the user role in the cloud Required scopes: cloud:manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.UserProjectUpdate() # UserProjectUpdate | 

try:
    # Update some fields of a project user
    api_response = api_instance.update_project_user(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_project_user: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.UserProjectUpdate() # UserProjectUpdate | 

try:
    # Update some fields of a project user
    api_response = api_instance.update_project_user(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_project_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.UserProjectUpdate() # UserProjectUpdate | 

try:
    # Update some fields of a project user
    api_response = api_instance.update_project_user(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_project_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this fos user. | 
 **project_pk** | **str**|  | 
 **data** | [**UserProjectUpdate**](UserProjectUpdate.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_self_user**
> SelfUser update_self_user(data)

Update info of the current user

DEPRECATED. The user must be updated on its identity provider

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
data = bimdata_api_client.SelfUser() # SelfUser | 

try:
    # Update info of the current user
    api_response = api_instance.update_self_user(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_self_user: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
data = bimdata_api_client.SelfUser() # SelfUser | 

try:
    # Update info of the current user
    api_response = api_instance.update_self_user(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_self_user: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
configuration = bimdata_api_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: bimdata_connect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = bimdata_api_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.bimdata.io
configuration.host = "https://api.bimdata.io"
# Create an instance of the API class
api_instance = bimdata_api_client.CollaborationApi(bimdata_api_client.ApiClient(configuration))
data = bimdata_api_client.SelfUser() # SelfUser | 

try:
    # Update info of the current user
    api_response = api_instance.update_self_user(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollaborationApi->update_self_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SelfUser**](SelfUser.md)|  | 

### Return type

[**SelfUser**](SelfUser.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

