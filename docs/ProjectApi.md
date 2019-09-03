# bimdata_api_client.ProjectApi

All URIs are relative to *https://api-beta.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_project_user_invitation**](ProjectApi.md#cancel_project_user_invitation) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/invitation/{id} | Cancel a pending invitation
[**create_classification**](ProjectApi.md#create_classification) | **POST** /cloud/{cloud_pk}/project/{project_pk}/classification | Create a classification
[**create_document**](ProjectApi.md#create_document) | **POST** /cloud/{cloud_pk}/project/{project_pk}/document | Create a document
[**create_folder**](ProjectApi.md#create_folder) | **POST** /cloud/{cloud_pk}/project/{project_pk}/folder | Create a folder
[**create_project**](ProjectApi.md#create_project) | **POST** /cloud/{cloud_pk}/project | Create a project
[**delete_classification**](ProjectApi.md#delete_classification) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | Delete a classification
[**delete_document**](ProjectApi.md#delete_document) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | Delete the document
[**delete_folder**](ProjectApi.md#delete_folder) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | Delete a folder
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /cloud/{cloud_pk}/project/{id} | Delete a project
[**delete_project_user**](ProjectApi.md#delete_project_user) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | Remove a user from a project
[**full_update_classification**](ProjectApi.md#full_update_classification) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | Update all fields of a classification
[**full_update_document**](ProjectApi.md#full_update_document) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | Update all fields of the document
[**full_update_folder**](ProjectApi.md#full_update_folder) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | Update all fields of a folder
[**full_update_project**](ProjectApi.md#full_update_project) | **PUT** /cloud/{cloud_pk}/project/{id} | Update all fields of a project
[**full_update_project_user**](ProjectApi.md#full_update_project_user) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | Update all fields of a project user
[**get_classification**](ProjectApi.md#get_classification) | **GET** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | Retrieve a classification
[**get_classifications**](ProjectApi.md#get_classifications) | **GET** /cloud/{cloud_pk}/project/{project_pk}/classification | Retrieve all classifications
[**get_document**](ProjectApi.md#get_document) | **GET** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | Retrieve a document
[**get_documents**](ProjectApi.md#get_documents) | **GET** /cloud/{cloud_pk}/project/{project_pk}/document | Retrieve all documents
[**get_folder**](ProjectApi.md#get_folder) | **GET** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | Retrieve a folder
[**get_folders**](ProjectApi.md#get_folders) | **GET** /cloud/{cloud_pk}/project/{project_pk}/folder | Retrieve all folders
[**get_project**](ProjectApi.md#get_project) | **GET** /cloud/{cloud_pk}/project/{id} | Retrieve a project
[**get_project_dms_tree**](ProjectApi.md#get_project_dms_tree) | **GET** /cloud/{cloud_pk}/project/{id}/dms-tree | Retrieve the complete DMS tree
[**get_project_invitations**](ProjectApi.md#get_project_invitations) | **GET** /cloud/{cloud_pk}/project/{project_pk}/invitation | Retrieve all pending invitations in the project
[**get_project_sub_tree**](ProjectApi.md#get_project_sub_tree) | **GET** /cloud/{cloud_pk}/project/subtree | Retrieve the complete projects tree of the cloud
[**get_project_tree**](ProjectApi.md#get_project_tree) | **GET** /cloud/{cloud_pk}/project/{id}/tree | Retrieve the complete DMS tree
[**get_project_user**](ProjectApi.md#get_project_user) | **GET** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | Retrieve a user in a project
[**get_project_users**](ProjectApi.md#get_project_users) | **GET** /cloud/{cloud_pk}/project/{project_pk}/user | Retrieve all users in a project
[**get_projects**](ProjectApi.md#get_projects) | **GET** /cloud/{cloud_pk}/project | Retrieve all projects
[**invite_project_user**](ProjectApi.md#invite_project_user) | **POST** /cloud/{cloud_pk}/project/{project_pk}/invitation | Invite a project member
[**update_classification**](ProjectApi.md#update_classification) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | Update some fields of a classification
[**update_document**](ProjectApi.md#update_document) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | Update some fields of the document
[**update_folder**](ProjectApi.md#update_folder) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | Update some fields of a folder
[**update_project**](ProjectApi.md#update_project) | **PATCH** /cloud/{cloud_pk}/project/{id} | Update some fields of a project
[**update_project_user**](ProjectApi.md#update_project_user) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | Update some fields of a project user


# **cancel_project_user_invitation**
> cancel_project_user_invitation(cloud_pk, id, project_pk)

Cancel a pending invitation

 Required scopes: org:manage

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this invitation.
project_pk = 'project_pk_example' # str | 

try:
    # Cancel a pending invitation
    api_instance.cancel_project_user_invitation(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->cancel_project_user_invitation: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this invitation.
project_pk = 'project_pk_example' # str | 

try:
    # Cancel a pending invitation
    api_instance.cancel_project_user_invitation(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->cancel_project_user_invitation: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this invitation.
project_pk = 'project_pk_example' # str | 

try:
    # Cancel a pending invitation
    api_instance.cancel_project_user_invitation(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->cancel_project_user_invitation: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_classification**
> list[Classification] create_classification(cloud_pk, project_pk, data)

Create a classification

         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors          If created classification already exists, it will not be duplicated and the previous one will be returned.     You also can add a 'classification' filter on this endpoint. By ex: /classification?name='untec'. The name is case sensitive      Required scopes: ifc:write

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Classification()] # list[Classification] | 

try:
    # Create a classification
    api_response = api_instance.create_classification(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_classification: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Classification()] # list[Classification] | 

try:
    # Create a classification
    api_response = api_instance.create_classification(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_classification: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Classification()] # list[Classification] | 

try:
    # Create a classification
    api_response = api_instance.create_classification(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_classification: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | All creates failed: list of errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document**
> Document create_document(cloud_pk, project_pk, name, parent=parent, parent_id=parent_id, creator=creator, project=project, file_name=file_name, description=description, file=file, size=size)

Create a document

RCreate a document. If the document is an IFC, an IFC model will be created and attached to this document Required scopes: document:write

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
name = 'name_example' # str | Shown name of the file
parent = 56 # int |  (optional)
parent_id = 56 # int |  (optional)
creator = 56 # int |  (optional)
project = 56 # int |  (optional)
file_name = 'file_name_example' # str | Full name of the file (optional)
description = 'description_example' # str | Description of the file (optional)
file = '/path/to/file' # file |  (optional)
size = 56 # int | Size of the file. The file may be compressed and show a smaller size (optional)

try:
    # Create a document
    api_response = api_instance.create_document(cloud_pk, project_pk, name, parent=parent, parent_id=parent_id, creator=creator, project=project, file_name=file_name, description=description, file=file, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_document: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
name = 'name_example' # str | Shown name of the file
parent = 56 # int |  (optional)
parent_id = 56 # int |  (optional)
creator = 56 # int |  (optional)
project = 56 # int |  (optional)
file_name = 'file_name_example' # str | Full name of the file (optional)
description = 'description_example' # str | Description of the file (optional)
file = '/path/to/file' # file |  (optional)
size = 56 # int | Size of the file. The file may be compressed and show a smaller size (optional)

try:
    # Create a document
    api_response = api_instance.create_document(cloud_pk, project_pk, name, parent=parent, parent_id=parent_id, creator=creator, project=project, file_name=file_name, description=description, file=file, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_document: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
name = 'name_example' # str | Shown name of the file
parent = 56 # int |  (optional)
parent_id = 56 # int |  (optional)
creator = 56 # int |  (optional)
project = 56 # int |  (optional)
file_name = 'file_name_example' # str | Full name of the file (optional)
description = 'description_example' # str | Description of the file (optional)
file = '/path/to/file' # file |  (optional)
size = 56 # int | Size of the file. The file may be compressed and show a smaller size (optional)

try:
    # Create a document
    api_response = api_instance.create_document(cloud_pk, project_pk, name, parent=parent, parent_id=parent_id, creator=creator, project=project, file_name=file_name, description=description, file=file, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **name** | **str**| Shown name of the file | 
 **parent** | **int**|  | [optional] 
 **parent_id** | **int**|  | [optional] 
 **creator** | **int**|  | [optional] 
 **project** | **int**|  | [optional] 
 **file_name** | **str**| Full name of the file | [optional] 
 **description** | **str**| Description of the file | [optional] 
 **file** | **file**|  | [optional] 
 **size** | **int**| Size of the file. The file may be compressed and show a smaller size | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> Folder create_folder(cloud_pk, project_pk, data)

Create a folder

If the created folder have no parent, it will be put as a child of the default root folder of the project Required scopes: document:write

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Create a folder
    api_response = api_instance.create_folder(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_folder: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Create a folder
    api_response = api_instance.create_folder(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_folder: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Create a folder
    api_response = api_instance.create_folder(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_folder: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> Project create_project(cloud_pk, data)

Create a project

Create a project Required scopes: org:manage

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.Project() # Project | 

try:
    # Create a project
    api_response = api_instance.create_project(cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.Project() # Project | 

try:
    # Create a project
    api_response = api_instance.create_project(cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.Project() # Project | 

try:
    # Create a project
    api_response = api_instance.create_project(cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **data** | [**Project**](Project.md)|  | 

### Return type

[**Project**](Project.md)

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

# **delete_classification**
> delete_classification(cloud_pk, id, project_pk)

Delete a classification

All elements having this classification will lose it Required scopes: ifc:write

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a classification
    api_instance.delete_classification(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_classification: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a classification
    api_instance.delete_classification(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_classification: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a classification
    api_instance.delete_classification(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_classification: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> delete_document(cloud_pk, id, project_pk)

Delete the document

Delete the document Required scopes: document:write

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 

try:
    # Delete the document
    api_instance.delete_document(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_document: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 

try:
    # Delete the document
    api_instance.delete_document(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_document: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 

try:
    # Delete the document
    api_instance.delete_document(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_document: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> delete_folder(cloud_pk, id, project_pk)

Delete a folder

All files and subfolders will be deleted too Required scopes: document:write

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a folder
    api_instance.delete_folder(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_folder: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a folder
    api_instance.delete_folder(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_folder: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a folder
    api_instance.delete_folder(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_folder: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(cloud_pk, id)

Delete a project

It can take a long time to respond because we may need to delete all properties of all elements of all models in the project Required scopes: org:manage

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Delete a project
    api_instance.delete_project(cloud_pk, id)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Delete a project
    api_instance.delete_project(cloud_pk, id)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Delete a project
    api_instance.delete_project(cloud_pk, id)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this project. | 

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

# **delete_project_user**
> delete_project_user(cloud_pk, id, project_pk)

Remove a user from a project

Remove a user from a project Required scopes: cloud:manage

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 

try:
    # Remove a user from a project
    api_instance.delete_project_user(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project_user: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 

try:
    # Remove a user from a project
    api_instance.delete_project_user(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project_user: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 

try:
    # Remove a user from a project
    api_instance.delete_project_user(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project_user: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_classification**
> Classification full_update_classification(cloud_pk, id, project_pk, data)

Update all fields of a classification

Update all fields of a classification Required scopes: ifc:write

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Classification() # Classification | 

try:
    # Update all fields of a classification
    api_response = api_instance.full_update_classification(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_classification: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Classification() # Classification | 

try:
    # Update all fields of a classification
    api_response = api_instance.full_update_classification(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_classification: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Classification() # Classification | 

try:
    # Update all fields of a classification
    api_response = api_instance.full_update_classification(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_classification: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_document**
> Document full_update_document(cloud_pk, id, project_pk, name, parent=parent, parent_id=parent_id, creator=creator, project=project, file_name=file_name, description=description, file=file, size=size)

Update all fields of the document

Update all fields of the document Required scopes: document:write

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 
name = 'name_example' # str | Shown name of the file
parent = 56 # int |  (optional)
parent_id = 56 # int |  (optional)
creator = 56 # int |  (optional)
project = 56 # int |  (optional)
file_name = 'file_name_example' # str | Full name of the file (optional)
description = 'description_example' # str | Description of the file (optional)
file = '/path/to/file' # file |  (optional)
size = 56 # int | Size of the file. The file may be compressed and show a smaller size (optional)

try:
    # Update all fields of the document
    api_response = api_instance.full_update_document(cloud_pk, id, project_pk, name, parent=parent, parent_id=parent_id, creator=creator, project=project, file_name=file_name, description=description, file=file, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_document: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 
name = 'name_example' # str | Shown name of the file
parent = 56 # int |  (optional)
parent_id = 56 # int |  (optional)
creator = 56 # int |  (optional)
project = 56 # int |  (optional)
file_name = 'file_name_example' # str | Full name of the file (optional)
description = 'description_example' # str | Description of the file (optional)
file = '/path/to/file' # file |  (optional)
size = 56 # int | Size of the file. The file may be compressed and show a smaller size (optional)

try:
    # Update all fields of the document
    api_response = api_instance.full_update_document(cloud_pk, id, project_pk, name, parent=parent, parent_id=parent_id, creator=creator, project=project, file_name=file_name, description=description, file=file, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_document: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 
name = 'name_example' # str | Shown name of the file
parent = 56 # int |  (optional)
parent_id = 56 # int |  (optional)
creator = 56 # int |  (optional)
project = 56 # int |  (optional)
file_name = 'file_name_example' # str | Full name of the file (optional)
description = 'description_example' # str | Description of the file (optional)
file = '/path/to/file' # file |  (optional)
size = 56 # int | Size of the file. The file may be compressed and show a smaller size (optional)

try:
    # Update all fields of the document
    api_response = api_instance.full_update_document(cloud_pk, id, project_pk, name, parent=parent, parent_id=parent_id, creator=creator, project=project, file_name=file_name, description=description, file=file, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this document. | 
 **project_pk** | **str**|  | 
 **name** | **str**| Shown name of the file | 
 **parent** | **int**|  | [optional] 
 **parent_id** | **int**|  | [optional] 
 **creator** | **int**|  | [optional] 
 **project** | **int**|  | [optional] 
 **file_name** | **str**| Full name of the file | [optional] 
 **description** | **str**| Description of the file | [optional] 
 **file** | **file**|  | [optional] 
 **size** | **int**| Size of the file. The file may be compressed and show a smaller size | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_folder**
> Folder full_update_folder(cloud_pk, id, project_pk, data)

Update all fields of a folder

Update all fields of a folder Required scopes: document:write

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Update all fields of a folder
    api_response = api_instance.full_update_folder(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_folder: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Update all fields of a folder
    api_response = api_instance.full_update_folder(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_folder: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Update all fields of a folder
    api_response = api_instance.full_update_folder(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_folder: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_project**
> Project full_update_project(cloud_pk, id, data)

Update all fields of a project

Update all fields of a project Required scopes: org:manage

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.Project() # Project | 

try:
    # Update all fields of a project
    api_response = api_instance.full_update_project(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_project: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.Project() # Project | 

try:
    # Update all fields of a project
    api_response = api_instance.full_update_project(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_project: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.Project() # Project | 

try:
    # Update all fields of a project
    api_response = api_instance.full_update_project(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_project: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_project_user**
> User full_update_project_user(cloud_pk, id, project_pk, data)

Update all fields of a project user

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.UserProjectUpdate() # UserProjectUpdate | 

try:
    # Update all fields of a project user
    api_response = api_instance.full_update_project_user(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_project_user: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.UserProjectUpdate() # UserProjectUpdate | 

try:
    # Update all fields of a project user
    api_response = api_instance.full_update_project_user(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_project_user: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.UserProjectUpdate() # UserProjectUpdate | 

try:
    # Update all fields of a project user
    api_response = api_instance.full_update_project_user(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_project_user: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classification**
> Classification get_classification(cloud_pk, id, project_pk)

Retrieve a classification

Retrieve a classification Required scopes: ifc:read

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a classification
    api_response = api_instance.get_classification(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_classification: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a classification
    api_response = api_instance.get_classification(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_classification: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a classification
    api_response = api_instance.get_classification(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_classification: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classifications**
> list[Classification] get_classifications(cloud_pk, project_pk)

Retrieve all classifications

Retrieve all classifications of all models in the project Required scopes: ifc:read

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all classifications
    api_response = api_instance.get_classifications(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_classifications: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all classifications
    api_response = api_instance.get_classifications(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_classifications: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all classifications
    api_response = api_instance.get_classifications(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Classification]**](Classification.md)

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

# **get_document**
> Document get_document(cloud_pk, id, project_pk)

Retrieve a document

Retrieve a document in the project Required scopes: document:read

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a document
    api_response = api_instance.get_document(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_document: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a document
    api_response = api_instance.get_document(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_document: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a document
    api_response = api_instance.get_document(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_document: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents**
> list[Document] get_documents(cloud_pk, project_pk)

Retrieve all documents

Retrieve all documents in the project Required scopes: document:read

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all documents
    api_response = api_instance.get_documents(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_documents: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all documents
    api_response = api_instance.get_documents(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_documents: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all documents
    api_response = api_instance.get_documents(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Document]**](Document.md)

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

# **get_folder**
> Folder get_folder(cloud_pk, id, project_pk)

Retrieve a folder

Retrieve a folder Required scopes: document:read

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a folder
    api_response = api_instance.get_folder(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_folder: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a folder
    api_response = api_instance.get_folder(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_folder: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a folder
    api_response = api_instance.get_folder(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_folder: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folders**
> list[Folder] get_folders(cloud_pk, project_pk)

Retrieve all folders

Retrieve all folders in the project. This is an array of folder. If you want to get the tree of all folders, see getProjectTree Required scopes: document:read

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all folders
    api_response = api_instance.get_folders(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_folders: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all folders
    api_response = api_instance.get_folders(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_folders: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all folders
    api_response = api_instance.get_folders(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Folder]**](Folder.md)

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

# **get_project**
> ProjectWithChildren get_project(cloud_pk, id)

Retrieve a project

Retrieve a project

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve a project
    api_response = api_instance.get_project(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve a project
    api_response = api_instance.get_project(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve a project
    api_response = api_instance.get_project(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this project. | 

### Return type

[**ProjectWithChildren**](ProjectWithChildren.md)

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

# **get_project_dms_tree**
> Folder get_project_dms_tree(cloud_pk, id)

Retrieve the complete DMS tree

Retrieve the complete DMS tree (all folders and all documents in the project)

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve the complete DMS tree
    api_response = api_instance.get_project_dms_tree(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_dms_tree: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve the complete DMS tree
    api_response = api_instance.get_project_dms_tree(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_dms_tree: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve the complete DMS tree
    api_response = api_instance.get_project_dms_tree(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_dms_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this project. | 

### Return type

[**Folder**](Folder.md)

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

# **get_project_invitations**
> list[ProjectInvitation] get_project_invitations(cloud_pk, project_pk)

Retrieve all pending invitations in the project

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all pending invitations in the project
    api_response = api_instance.get_project_invitations(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_invitations: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all pending invitations in the project
    api_response = api_instance.get_project_invitations(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_invitations: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all pending invitations in the project
    api_response = api_instance.get_project_invitations(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[ProjectInvitation]**](ProjectInvitation.md)

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

# **get_project_sub_tree**
> list[ProjectWithChildren] get_project_sub_tree(cloud_pk)

Retrieve the complete projects tree of the cloud

Retrieve the complete projects tree of the cloud

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve the complete projects tree of the cloud
    api_response = api_instance.get_project_sub_tree(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_sub_tree: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve the complete projects tree of the cloud
    api_response = api_instance.get_project_sub_tree(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_sub_tree: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve the complete projects tree of the cloud
    api_response = api_instance.get_project_sub_tree(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_sub_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 

### Return type

[**list[ProjectWithChildren]**](ProjectWithChildren.md)

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

# **get_project_tree**
> Folder get_project_tree(cloud_pk, id)

Retrieve the complete DMS tree

Retrieve the complete DMS tree (all folders and all documents in the project). DEPRECATED: renamed to getProjectDMSTree

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve the complete DMS tree
    api_response = api_instance.get_project_tree(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_tree: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve the complete DMS tree
    api_response = api_instance.get_project_tree(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_tree: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve the complete DMS tree
    api_response = api_instance.get_project_tree(cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this project. | 

### Return type

[**Folder**](Folder.md)

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

# **get_project_user**
> User get_project_user(cloud_pk, id, project_pk)

Retrieve a user in a project

Each member of a project can see other members of the project Required scopes: cloud:read

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a user in a project
    api_response = api_instance.get_project_user(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_user: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a user in a project
    api_response = api_instance.get_project_user(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_user: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a user in a project
    api_response = api_instance.get_project_user(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_user: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_users**
> list[User] get_project_users(cloud_pk, project_pk)

Retrieve all users in a project

Each member of a project can see other members of the project Required scopes: cloud:read

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all users in a project
    api_response = api_instance.get_project_users(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_users: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all users in a project
    api_response = api_instance.get_project_users(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_users: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all users in a project
    api_response = api_instance.get_project_users(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 

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

# **get_projects**
> list[Project] get_projects(cloud_pk)

Retrieve all projects

Retrieve all projects of the cloud. All project are shown at the same level. see #getProjectSubTree

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all projects
    api_response = api_instance.get_projects(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_projects: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all projects
    api_response = api_instance.get_projects(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_projects: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
    # Retrieve all projects
    api_response = api_instance.get_projects(cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 

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

# **invite_project_user**
> ProjectInvitation invite_project_user(cloud_pk, project_pk, data)

Invite a project member

Invite a project member. If the user is not already a cloud member, they will also be invited in the cloud with USER role. Required scopes: org:manage

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.ProjectInvitation() # ProjectInvitation | 

try:
    # Invite a project member
    api_response = api_instance.invite_project_user(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->invite_project_user: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.ProjectInvitation() # ProjectInvitation | 

try:
    # Invite a project member
    api_response = api_instance.invite_project_user(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->invite_project_user: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.ProjectInvitation() # ProjectInvitation | 

try:
    # Invite a project member
    api_response = api_instance.invite_project_user(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->invite_project_user: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_classification**
> Classification update_classification(cloud_pk, id, project_pk, data)

Update some fields of a classification

Update some fields of a classification Required scopes: ifc:write

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Classification() # Classification | 

try:
    # Update some fields of a classification
    api_response = api_instance.update_classification(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_classification: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Classification() # Classification | 

try:
    # Update some fields of a classification
    api_response = api_instance.update_classification(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_classification: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Classification() # Classification | 

try:
    # Update some fields of a classification
    api_response = api_instance.update_classification(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_classification: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> Document update_document(cloud_pk, id, project_pk, data)

Update some fields of the document

Update some fields of the document Required scopes: document:write

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Document() # Document | 

try:
    # Update some fields of the document
    api_response = api_instance.update_document(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_document: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Document() # Document | 

try:
    # Update some fields of the document
    api_response = api_instance.update_document(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_document: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this document.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Document() # Document | 

try:
    # Update some fields of the document
    api_response = api_instance.update_document(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_document: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folder**
> Folder update_folder(cloud_pk, id, project_pk, data)

Update some fields of a folder

Update some fields of a folder Required scopes: document:write

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Update some fields of a folder
    api_response = api_instance.update_folder(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_folder: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Update some fields of a folder
    api_response = api_instance.update_folder(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_folder: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this folder.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    # Update some fields of a folder
    api_response = api_instance.update_folder(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_folder: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(cloud_pk, id, data)

Update some fields of a project

Update some fields of a project Required scopes: org:manage

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.Project() # Project | 

try:
    # Update some fields of a project
    api_response = api_instance.update_project(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.Project() # Project | 

try:
    # Update some fields of a project
    api_response = api_instance.update_project(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.Project() # Project | 

try:
    # Update some fields of a project
    api_response = api_instance.update_project(cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_user**
> User update_project_user(cloud_pk, id, project_pk, data)

Update some fields of a project user

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.UserProjectUpdate() # UserProjectUpdate | 

try:
    # Update some fields of a project user
    api_response = api_instance.update_project_user(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project_user: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.UserProjectUpdate() # UserProjectUpdate | 

try:
    # Update some fields of a project user
    api_response = api_instance.update_project_user(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project_user: %s\n" % e)
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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this fos user.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.UserProjectUpdate() # UserProjectUpdate | 

try:
    # Update some fields of a project user
    api_response = api_instance.update_project_user(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project_user: %s\n" % e)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

