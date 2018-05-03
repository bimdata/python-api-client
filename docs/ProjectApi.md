# bimdata_api_client.ProjectApi

All URIs are relative to *http://api-staging.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_classification**](ProjectApi.md#create_classification) | **POST** /cloud/{cloud_pk}/project/{project_pk}/classification | 
[**create_document**](ProjectApi.md#create_document) | **POST** /cloud/{cloud_pk}/project/{project_pk}/document | 
[**create_folder**](ProjectApi.md#create_folder) | **POST** /cloud/{cloud_pk}/project/{project_pk}/folder | 
[**create_project**](ProjectApi.md#create_project) | **POST** /cloud/{cloud_pk}/project | 
[**create_project_user**](ProjectApi.md#create_project_user) | **POST** /cloud/{cloud_pk}/project/{project_pk}/user | 
[**delete_classification**](ProjectApi.md#delete_classification) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | 
[**delete_document**](ProjectApi.md#delete_document) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | 
[**delete_folder**](ProjectApi.md#delete_folder) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | 
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /cloud/{cloud_pk}/project/{id} | 
[**delete_project_user**](ProjectApi.md#delete_project_user) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | 
[**full_update_classification**](ProjectApi.md#full_update_classification) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | 
[**full_update_document**](ProjectApi.md#full_update_document) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | 
[**full_update_folder**](ProjectApi.md#full_update_folder) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | 
[**full_update_project**](ProjectApi.md#full_update_project) | **PUT** /cloud/{cloud_pk}/project/{id} | 
[**full_update_project_user**](ProjectApi.md#full_update_project_user) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | 
[**get_classification**](ProjectApi.md#get_classification) | **GET** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | 
[**get_classifications**](ProjectApi.md#get_classifications) | **GET** /cloud/{cloud_pk}/project/{project_pk}/classification | 
[**get_document**](ProjectApi.md#get_document) | **GET** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | 
[**get_documents**](ProjectApi.md#get_documents) | **GET** /cloud/{cloud_pk}/project/{project_pk}/document | 
[**get_folder**](ProjectApi.md#get_folder) | **GET** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | 
[**get_folders**](ProjectApi.md#get_folders) | **GET** /cloud/{cloud_pk}/project/{project_pk}/folder | 
[**get_project**](ProjectApi.md#get_project) | **GET** /cloud/{cloud_pk}/project/{id} | 
[**get_project_tree**](ProjectApi.md#get_project_tree) | **GET** /cloud/{cloud_pk}/project/{id}/tree | 
[**get_project_user**](ProjectApi.md#get_project_user) | **GET** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | 
[**get_project_users**](ProjectApi.md#get_project_users) | **GET** /cloud/{cloud_pk}/project/{project_pk}/user | 
[**get_projects**](ProjectApi.md#get_projects) | **GET** /cloud/{cloud_pk}/project | 
[**update_classification**](ProjectApi.md#update_classification) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | 
[**update_document**](ProjectApi.md#update_document) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | 
[**update_folder**](ProjectApi.md#update_folder) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | 
[**update_project**](ProjectApi.md#update_project) | **PATCH** /cloud/{cloud_pk}/project/{id} | 
[**update_project_user**](ProjectApi.md#update_project_user) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | 


# **create_classification**
> list[Classification] create_classification(project_pk, cloud_pk, data)



         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors          If created classification already exists, it will not be duplicated and the previous one will be returned.     You also can add a 'classification' filter on this endpoint. By ex: /classification?name='untec'. The name is case sensitive     

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
data = [bimdata_api_client.Classification()] # list[Classification] | 

try:
    api_response = api_instance.create_classification(project_pk, cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **data** | [**list[Classification]**](Classification.md)|  | 

### Return type

[**list[Classification]**](Classification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document**
> Document create_document(project_pk, cloud_pk, data)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.Document() # Document | 

try:
    api_response = api_instance.create_document(project_pk, cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **data** | [**Document**](Document.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> Folder create_folder(project_pk, cloud_pk, data)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    api_response = api_instance.create_folder(project_pk, cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **data** | [**Folder**](Folder.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> Project create_project(cloud_pk, data)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.Project() # Project | 

try:
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_user**
> FosUserWrite create_project_user(project_pk, cloud_pk, data)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.FosUserWrite() # FosUserWrite | 

try:
    api_response = api_instance.create_project_user(project_pk, cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **data** | [**FosUserWrite**](FosUserWrite.md)|  | 

### Return type

[**FosUserWrite**](FosUserWrite.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_classification**
> delete_classification(project_pk, cloud_pk, id)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.delete_classification(project_pk, cloud_pk, id)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> delete_document(project_pk, cloud_pk, id)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.delete_document(project_pk, cloud_pk, id)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> delete_folder(project_pk, cloud_pk, id)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.delete_folder(project_pk, cloud_pk, id)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(id, cloud_pk)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 

try:
    api_instance.delete_project(id, cloud_pk)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cloud_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_user**
> delete_project_user(project_pk, cloud_pk, id)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.delete_project_user(project_pk, cloud_pk, id)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_classification**
> Classification full_update_classification(project_pk, cloud_pk, id, data)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.Classification() # Classification | 

try:
    api_response = api_instance.full_update_classification(project_pk, cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**Classification**](Classification.md)|  | 

### Return type

[**Classification**](Classification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_document**
> Document full_update_document(project_pk, cloud_pk, id, data)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.Document() # Document | 

try:
    api_response = api_instance.full_update_document(project_pk, cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**Document**](Document.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_folder**
> Folder full_update_folder(project_pk, cloud_pk, id, data)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    api_response = api_instance.full_update_folder(project_pk, cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**Folder**](Folder.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_project**
> Project full_update_project(id, cloud_pk, data)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.Project() # Project | 

try:
    api_response = api_instance.full_update_project(id, cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **data** | [**Project**](Project.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_project_user**
> FosUserWrite full_update_project_user(project_pk, cloud_pk, id, data)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.FosUserWrite() # FosUserWrite | 

try:
    api_response = api_instance.full_update_project_user(project_pk, cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->full_update_project_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**FosUserWrite**](FosUserWrite.md)|  | 

### Return type

[**FosUserWrite**](FosUserWrite.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classification**
> Classification get_classification(project_pk, cloud_pk, id)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_classification(project_pk, cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**Classification**](Classification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classifications**
> list[Classification] get_classifications(project_pk, cloud_pk)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 

try:
    api_response = api_instance.get_classifications(project_pk, cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 

### Return type

[**list[Classification]**](Classification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> Document get_document(project_pk, cloud_pk, id)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_document(project_pk, cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents**
> list[Document] get_documents(project_pk, cloud_pk)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 

try:
    api_response = api_instance.get_documents(project_pk, cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 

### Return type

[**list[Document]**](Document.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder**
> Folder get_folder(project_pk, cloud_pk, id)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_folder(project_pk, cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folders**
> list[Folder] get_folders(project_pk, cloud_pk)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 

try:
    api_response = api_instance.get_folders(project_pk, cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 

### Return type

[**list[Folder]**](Folder.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(id, cloud_pk)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 

try:
    api_response = api_instance.get_project(id, cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cloud_pk** | **str**|  | 

### Return type

[**Project**](Project.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tree**
> Folder get_project_tree(id, cloud_pk)



Returns the document tree from root folder

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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 

try:
    api_response = api_instance.get_project_tree(id, cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cloud_pk** | **str**|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_user**
> FosUser get_project_user(project_pk, cloud_pk, id)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_project_user(project_pk, cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**FosUser**](FosUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_users**
> list[FosUser] get_project_users(project_pk, cloud_pk)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 

try:
    api_response = api_instance.get_project_users(project_pk, cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 

### Return type

[**list[FosUser]**](FosUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> list[Project] get_projects(cloud_pk)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 

try:
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_classification**
> Classification update_classification(project_pk, cloud_pk, id, data)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.Classification() # Classification | 

try:
    api_response = api_instance.update_classification(project_pk, cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**Classification**](Classification.md)|  | 

### Return type

[**Classification**](Classification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> Document update_document(project_pk, cloud_pk, id, data)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.Document() # Document | 

try:
    api_response = api_instance.update_document(project_pk, cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**Document**](Document.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folder**
> Folder update_folder(project_pk, cloud_pk, id, data)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.Folder() # Folder | 

try:
    api_response = api_instance.update_folder(project_pk, cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**Folder**](Folder.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(id, cloud_pk, data)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.Project() # Project | 

try:
    api_response = api_instance.update_project(id, cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **data** | [**Project**](Project.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_user**
> FosUserWrite update_project_user(project_pk, cloud_pk, id, data)





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
api_instance = bimdata_api_client.ProjectApi(bimdata_api_client.ApiClient(configuration))
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.FosUserWrite() # FosUserWrite | 

try:
    api_response = api_instance.update_project_user(project_pk, cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**FosUserWrite**](FosUserWrite.md)|  | 

### Return type

[**FosUserWrite**](FosUserWrite.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

