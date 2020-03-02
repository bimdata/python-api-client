# bimdata_api_client.BcfApi

All URIs are relative to *https://api.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_comment**](BcfApi.md#create_comment) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/comments | Create a comment
[**create_full_topic**](BcfApi.md#create_full_topic) | **POST** /bcf/2.1/projects/{projects_pk}/full-topic | Create a Topic with viewpoints and comments
[**create_topic**](BcfApi.md#create_topic) | **POST** /bcf/2.1/projects/{projects_pk}/topics | Create a topic
[**create_viewpoint**](BcfApi.md#create_viewpoint) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints | Create a Viewpoint
[**delete_comment**](BcfApi.md#delete_comment) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/comments/{guid} | Delete a comment
[**delete_topic**](BcfApi.md#delete_topic) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{guid} | Delete a topic
[**delete_viewpoint**](BcfApi.md#delete_viewpoint) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid} | Delete a Viewpoint
[**download_bcf_export**](BcfApi.md#download_bcf_export) | **GET** /bcf/2.1/projects/{id}/export | Export project&#39;s topics in bcf-xml format
[**full_update_bcf_project**](BcfApi.md#full_update_bcf_project) | **PUT** /bcf/2.1/projects/{id} | Update all fields of a BCF project
[**full_update_comment**](BcfApi.md#full_update_comment) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/comments/{guid} | Update all fields of a comment
[**full_update_full_topic**](BcfApi.md#full_update_full_topic) | **PUT** /bcf/2.1/projects/{projects_pk}/full-topic/{guid} | Update all fields of a topic
[**full_update_topic**](BcfApi.md#full_update_topic) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{guid} | Update all fields of a topic
[**full_update_viewpoint**](BcfApi.md#full_update_viewpoint) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid} | Update all fields of a Viewpoint
[**get_bcf_project**](BcfApi.md#get_bcf_project) | **GET** /bcf/2.1/projects/{id} | Retrieve a BCF project
[**get_bcf_projects**](BcfApi.md#get_bcf_projects) | **GET** /bcf/2.1/projects | Retrieve all BCF projects
[**get_colorings**](BcfApi.md#get_colorings) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid}/coloring | Retrieve all colorings of a viewpoint
[**get_comment**](BcfApi.md#get_comment) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/comments/{guid} | Retrieve a comment
[**get_comments**](BcfApi.md#get_comments) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/comments | Retrieve all comments
[**get_extensions**](BcfApi.md#get_extensions) | **GET** /bcf/2.1/projects/{projects_pk}/extensions | Retrieve project extensions
[**get_full_topic**](BcfApi.md#get_full_topic) | **GET** /bcf/2.1/projects/{projects_pk}/full-topic/{guid} | Retrieve a full topic
[**get_full_topics**](BcfApi.md#get_full_topics) | **GET** /bcf/2.1/projects/{projects_pk}/full-topic | Retrieve all full topics
[**get_selections**](BcfApi.md#get_selections) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid}/selection | Retrieve all selections of a viewpoint
[**get_snapshot**](BcfApi.md#get_snapshot) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid}/snapshot | Retrieve the viewpoint&#39; snapshot
[**get_topic**](BcfApi.md#get_topic) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{guid} | Retrieve a topic
[**get_topic_viewpoints**](BcfApi.md#get_topic_viewpoints) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/topic-viewpoints | Retrieve all viewpoints attached to the topic
[**get_topics**](BcfApi.md#get_topics) | **GET** /bcf/2.1/projects/{projects_pk}/topics | Retrieve all topics
[**get_user**](BcfApi.md#get_user) | **GET** /bcf/2.1/current-user | Get current user info
[**get_viewpoint**](BcfApi.md#get_viewpoint) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid} | Retrieve a Viewpoint
[**get_viewpoints**](BcfApi.md#get_viewpoints) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints | Retrieve all Viewpoints of a topic
[**get_visibilities**](BcfApi.md#get_visibilities) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid}/visibility | Retrieve all visibilities of a viewpoint
[**import_bcf**](BcfApi.md#import_bcf) | **POST** /bcf/2.1/projects/{id}/import | Import bcf-xml format into this project
[**update_bcf_project**](BcfApi.md#update_bcf_project) | **PATCH** /bcf/2.1/projects/{id} | Update some fields of a BCF project
[**update_comment**](BcfApi.md#update_comment) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/comments/{guid} | Update some fields of a comment
[**update_extensions**](BcfApi.md#update_extensions) | **PATCH** /bcf/2.1/projects/{projects_pk}/extensions | Update project extensions
[**update_full_topic**](BcfApi.md#update_full_topic) | **PATCH** /bcf/2.1/projects/{projects_pk}/full-topic/{guid} | Update some fields of a topic
[**update_topic**](BcfApi.md#update_topic) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{guid} | Update some fields of a topic
[**update_viewpoint**](BcfApi.md#update_viewpoint) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid} | Update some fields of a Viewpoint


# **create_comment**
> Comment create_comment(projects_pk, topics_guid, data)

Create a comment

Create a comment Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Comment() # Comment | 

try:
    # Create a comment
    api_response = api_instance.create_comment(projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_comment: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Comment() # Comment | 

try:
    # Create a comment
    api_response = api_instance.create_comment(projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_comment: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Comment() # Comment | 

try:
    # Create a comment
    api_response = api_instance.create_comment(projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 
 **data** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

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

# **create_full_topic**
> FullTopic create_full_topic(projects_pk, data)

Create a Topic with viewpoints and comments

This is not a standard route. You can send a topic, viewpoints and comments in a single call Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.FullTopic() # FullTopic | 

try:
    # Create a Topic with viewpoints and comments
    api_response = api_instance.create_full_topic(projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_full_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.FullTopic() # FullTopic | 

try:
    # Create a Topic with viewpoints and comments
    api_response = api_instance.create_full_topic(projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_full_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.FullTopic() # FullTopic | 

try:
    # Create a Topic with viewpoints and comments
    api_response = api_instance.create_full_topic(projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_full_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **data** | [**FullTopic**](FullTopic.md)|  | 

### Return type

[**FullTopic**](FullTopic.md)

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

# **create_topic**
> Topic create_topic(projects_pk, data)

Create a topic

Create a topic Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.Topic() # Topic | 

try:
    # Create a topic
    api_response = api_instance.create_topic(projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.Topic() # Topic | 

try:
    # Create a topic
    api_response = api_instance.create_topic(projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.Topic() # Topic | 

try:
    # Create a topic
    api_response = api_instance.create_topic(projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **data** | [**Topic**](Topic.md)|  | 

### Return type

[**Topic**](Topic.md)

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

# **create_viewpoint**
> Viewpoint create_viewpoint(projects_pk, topics_guid, data)

Create a Viewpoint

Create a Viewpoint Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    # Create a Viewpoint
    api_response = api_instance.create_viewpoint(projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_viewpoint: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    # Create a Viewpoint
    api_response = api_instance.create_viewpoint(projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_viewpoint: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    # Create a Viewpoint
    api_response = api_instance.create_viewpoint(projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_viewpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 
 **data** | [**Viewpoint**](Viewpoint.md)|  | 

### Return type

[**Viewpoint**](Viewpoint.md)

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

# **delete_comment**
> delete_comment(guid, projects_pk, topics_guid)

Delete a comment

Delete a comment Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Delete a comment
    api_instance.delete_comment(guid, projects_pk, topics_guid)
except ApiException as e:
    print("Exception when calling BcfApi->delete_comment: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Delete a comment
    api_instance.delete_comment(guid, projects_pk, topics_guid)
except ApiException as e:
    print("Exception when calling BcfApi->delete_comment: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Delete a comment
    api_instance.delete_comment(guid, projects_pk, topics_guid)
except ApiException as e:
    print("Exception when calling BcfApi->delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 

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

# **delete_topic**
> delete_topic(guid, projects_pk)

Delete a topic

Delete a topic Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 

try:
    # Delete a topic
    api_instance.delete_topic(guid, projects_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 

try:
    # Delete a topic
    api_instance.delete_topic(guid, projects_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 

try:
    # Delete a topic
    api_instance.delete_topic(guid, projects_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 

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

# **delete_viewpoint**
> delete_viewpoint(guid, projects_pk, topics_guid)

Delete a Viewpoint

This is not a standard route. Delete a Viewpoint Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Delete a Viewpoint
    api_instance.delete_viewpoint(guid, projects_pk, topics_guid)
except ApiException as e:
    print("Exception when calling BcfApi->delete_viewpoint: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Delete a Viewpoint
    api_instance.delete_viewpoint(guid, projects_pk, topics_guid)
except ApiException as e:
    print("Exception when calling BcfApi->delete_viewpoint: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Delete a Viewpoint
    api_instance.delete_viewpoint(guid, projects_pk, topics_guid)
except ApiException as e:
    print("Exception when calling BcfApi->delete_viewpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 

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

# **download_bcf_export**
> download_bcf_export(id, topics=topics, format=format)

Export project's topics in bcf-xml format

Export project's topics in bcf-xml format Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.
topics = 'topics_example' # str | topic guids to export, comma separated. Default = all (optional)
format = 'format_example' # str | topic format to export, comma separated. Default = all (optional)

try:
    # Export project's topics in bcf-xml format
    api_instance.download_bcf_export(id, topics=topics, format=format)
except ApiException as e:
    print("Exception when calling BcfApi->download_bcf_export: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.
topics = 'topics_example' # str | topic guids to export, comma separated. Default = all (optional)
format = 'format_example' # str | topic format to export, comma separated. Default = all (optional)

try:
    # Export project's topics in bcf-xml format
    api_instance.download_bcf_export(id, topics=topics, format=format)
except ApiException as e:
    print("Exception when calling BcfApi->download_bcf_export: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.
topics = 'topics_example' # str | topic guids to export, comma separated. Default = all (optional)
format = 'format_example' # str | topic format to export, comma separated. Default = all (optional)

try:
    # Export project's topics in bcf-xml format
    api_instance.download_bcf_export(id, topics=topics, format=format)
except ApiException as e:
    print("Exception when calling BcfApi->download_bcf_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this project. | 
 **topics** | **str**| topic guids to export, comma separated. Default &#x3D; all | [optional] 
 **format** | **str**| topic format to export, comma separated. Default &#x3D; all | [optional] 

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
**200** | The file |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_bcf_project**
> BcfProject full_update_bcf_project(id, data)

Update all fields of a BCF project

Update all fields of a BCF project Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.BcfProject() # BcfProject | 

try:
    # Update all fields of a BCF project
    api_response = api_instance.full_update_bcf_project(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_bcf_project: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.BcfProject() # BcfProject | 

try:
    # Update all fields of a BCF project
    api_response = api_instance.full_update_bcf_project(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_bcf_project: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.BcfProject() # BcfProject | 

try:
    # Update all fields of a BCF project
    api_response = api_instance.full_update_bcf_project(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_bcf_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this project. | 
 **data** | [**BcfProject**](BcfProject.md)|  | 

### Return type

[**BcfProject**](BcfProject.md)

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

# **full_update_comment**
> Comment full_update_comment(guid, projects_pk, topics_guid, data)

Update all fields of a comment

Update all fields of a comment Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Comment() # Comment | 

try:
    # Update all fields of a comment
    api_response = api_instance.full_update_comment(guid, projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_comment: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Comment() # Comment | 

try:
    # Update all fields of a comment
    api_response = api_instance.full_update_comment(guid, projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_comment: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Comment() # Comment | 

try:
    # Update all fields of a comment
    api_response = api_instance.full_update_comment(guid, projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 
 **data** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

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

# **full_update_full_topic**
> FullTopic full_update_full_topic(guid, projects_pk, data)

Update all fields of a topic

This is not a standard route. You can update topic, viewpoints and comment is a signle call Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.FullTopic() # FullTopic | 

try:
    # Update all fields of a topic
    api_response = api_instance.full_update_full_topic(guid, projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_full_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.FullTopic() # FullTopic | 

try:
    # Update all fields of a topic
    api_response = api_instance.full_update_full_topic(guid, projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_full_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.FullTopic() # FullTopic | 

try:
    # Update all fields of a topic
    api_response = api_instance.full_update_full_topic(guid, projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_full_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **data** | [**FullTopic**](FullTopic.md)|  | 

### Return type

[**FullTopic**](FullTopic.md)

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

# **full_update_topic**
> Topic full_update_topic(guid, projects_pk, data)

Update all fields of a topic

Update all fields of a topic Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.Topic() # Topic | 

try:
    # Update all fields of a topic
    api_response = api_instance.full_update_topic(guid, projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.Topic() # Topic | 

try:
    # Update all fields of a topic
    api_response = api_instance.full_update_topic(guid, projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.Topic() # Topic | 

try:
    # Update all fields of a topic
    api_response = api_instance.full_update_topic(guid, projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **data** | [**Topic**](Topic.md)|  | 

### Return type

[**Topic**](Topic.md)

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

# **full_update_viewpoint**
> Viewpoint full_update_viewpoint(guid, projects_pk, topics_guid, data)

Update all fields of a Viewpoint

This is not a standard route. Update all fields of a Viewpoint Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    # Update all fields of a Viewpoint
    api_response = api_instance.full_update_viewpoint(guid, projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_viewpoint: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    # Update all fields of a Viewpoint
    api_response = api_instance.full_update_viewpoint(guid, projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_viewpoint: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    # Update all fields of a Viewpoint
    api_response = api_instance.full_update_viewpoint(guid, projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_viewpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 
 **data** | [**Viewpoint**](Viewpoint.md)|  | 

### Return type

[**Viewpoint**](Viewpoint.md)

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

# **get_bcf_project**
> BcfProject get_bcf_project(id)

Retrieve a BCF project

Retrieve a BCF project Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve a BCF project
    api_response = api_instance.get_bcf_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_bcf_project: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve a BCF project
    api_response = api_instance.get_bcf_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_bcf_project: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.

try:
    # Retrieve a BCF project
    api_response = api_instance.get_bcf_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_bcf_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this project. | 

### Return type

[**BcfProject**](BcfProject.md)

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

# **get_bcf_projects**
> list[BcfProject] get_bcf_projects()

Retrieve all BCF projects

Retrieve all BCF projects Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))

try:
    # Retrieve all BCF projects
    api_response = api_instance.get_bcf_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_bcf_projects: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))

try:
    # Retrieve all BCF projects
    api_response = api_instance.get_bcf_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_bcf_projects: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))

try:
    # Retrieve all BCF projects
    api_response = api_instance.get_bcf_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_bcf_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BcfProject]**](BcfProject.md)

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

# **get_colorings**
> list[Coloring] get_colorings(guid, projects_pk, topics_guid)

Retrieve all colorings of a viewpoint

Retrieve all colorings of a viewpoint Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all colorings of a viewpoint
    api_response = api_instance.get_colorings(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_colorings: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all colorings of a viewpoint
    api_response = api_instance.get_colorings(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_colorings: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all colorings of a viewpoint
    api_response = api_instance.get_colorings(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_colorings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 

### Return type

[**list[Coloring]**](Coloring.md)

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

# **get_comment**
> Comment get_comment(guid, projects_pk, topics_guid)

Retrieve a comment

Retrieve a comment Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve a comment
    api_response = api_instance.get_comment(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_comment: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve a comment
    api_response = api_instance.get_comment(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_comment: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve a comment
    api_response = api_instance.get_comment(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 

### Return type

[**Comment**](Comment.md)

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

# **get_comments**
> list[Comment] get_comments(projects_pk, topics_guid)

Retrieve all comments

Retrieve all comments Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all comments
    api_response = api_instance.get_comments(projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_comments: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all comments
    api_response = api_instance.get_comments(projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_comments: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all comments
    api_response = api_instance.get_comments(projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 

### Return type

[**list[Comment]**](Comment.md)

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

# **get_extensions**
> Extensions get_extensions(projects_pk)

Retrieve project extensions

Retrieve project extensions

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 

try:
    # Retrieve project extensions
    api_response = api_instance.get_extensions(projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_extensions: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 

try:
    # Retrieve project extensions
    api_response = api_instance.get_extensions(projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_extensions: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 

try:
    # Retrieve project extensions
    api_response = api_instance.get_extensions(projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_extensions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 

### Return type

[**Extensions**](Extensions.md)

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

# **get_full_topic**
> FullTopic get_full_topic(guid, projects_pk)

Retrieve a full topic

This is not a standard route. It responds with a topic, its viewpoints and its comments Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 

try:
    # Retrieve a full topic
    api_response = api_instance.get_full_topic(guid, projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_full_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 

try:
    # Retrieve a full topic
    api_response = api_instance.get_full_topic(guid, projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_full_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 

try:
    # Retrieve a full topic
    api_response = api_instance.get_full_topic(guid, projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_full_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 

### Return type

[**FullTopic**](FullTopic.md)

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

# **get_full_topics**
> list[FullTopic] get_full_topics(projects_pk, ifcs=ifcs, format=format)

Retrieve all full topics

This is not a standard route. It responds with all topics, their viewpoints and their comments Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
ifcs = 'ifcs_example' # str | Filter the returned list by ifcs (optional)
format = 'format_example' # str | Filter the returned list by format (optional)

try:
    # Retrieve all full topics
    api_response = api_instance.get_full_topics(projects_pk, ifcs=ifcs, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_full_topics: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
ifcs = 'ifcs_example' # str | Filter the returned list by ifcs (optional)
format = 'format_example' # str | Filter the returned list by format (optional)

try:
    # Retrieve all full topics
    api_response = api_instance.get_full_topics(projects_pk, ifcs=ifcs, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_full_topics: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
ifcs = 'ifcs_example' # str | Filter the returned list by ifcs (optional)
format = 'format_example' # str | Filter the returned list by format (optional)

try:
    # Retrieve all full topics
    api_response = api_instance.get_full_topics(projects_pk, ifcs=ifcs, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_full_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **ifcs** | **str**| Filter the returned list by ifcs | [optional] 
 **format** | **str**| Filter the returned list by format | [optional] 

### Return type

[**list[FullTopic]**](FullTopic.md)

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

# **get_selections**
> list[Component] get_selections(guid, projects_pk, topics_guid)

Retrieve all selections of a viewpoint

Retrieve all selections of a viewpoint Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all selections of a viewpoint
    api_response = api_instance.get_selections(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_selections: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all selections of a viewpoint
    api_response = api_instance.get_selections(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_selections: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all selections of a viewpoint
    api_response = api_instance.get_selections(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_selections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 

### Return type

[**list[Component]**](Component.md)

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

# **get_snapshot**
> file get_snapshot(guid, projects_pk, topics_guid)

Retrieve the viewpoint' snapshot

Retrieve the viewpoint' snapshot Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve the viewpoint' snapshot
    api_response = api_instance.get_snapshot(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_snapshot: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve the viewpoint' snapshot
    api_response = api_instance.get_snapshot(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_snapshot: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve the viewpoint' snapshot
    api_response = api_instance.get_snapshot(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 

### Return type

**file**

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Snapshot file |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic**
> Topic get_topic(guid, projects_pk)

Retrieve a topic

Retrieve a topic Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 

try:
    # Retrieve a topic
    api_response = api_instance.get_topic(guid, projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 

try:
    # Retrieve a topic
    api_response = api_instance.get_topic(guid, projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 

try:
    # Retrieve a topic
    api_response = api_instance.get_topic(guid, projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 

### Return type

[**Topic**](Topic.md)

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

# **get_topic_viewpoints**
> list[Viewpoint] get_topic_viewpoints(projects_pk, topics_guid)

Retrieve all viewpoints attached to the topic

This is not a standard route. It returns all viewpoints of the topic that are not attached to a comment. Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all viewpoints attached to the topic
    api_response = api_instance.get_topic_viewpoints(projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topic_viewpoints: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all viewpoints attached to the topic
    api_response = api_instance.get_topic_viewpoints(projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topic_viewpoints: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all viewpoints attached to the topic
    api_response = api_instance.get_topic_viewpoints(projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topic_viewpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 

### Return type

[**list[Viewpoint]**](Viewpoint.md)

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

# **get_topics**
> list[Topic] get_topics(projects_pk, ifcs=ifcs, format=format)

Retrieve all topics

Retrieve all topics Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
ifcs = 'ifcs_example' # str | Filter the returned list by ifcs (optional)
format = 'format_example' # str | Filter the returned list by format (optional)

try:
    # Retrieve all topics
    api_response = api_instance.get_topics(projects_pk, ifcs=ifcs, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topics: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
ifcs = 'ifcs_example' # str | Filter the returned list by ifcs (optional)
format = 'format_example' # str | Filter the returned list by format (optional)

try:
    # Retrieve all topics
    api_response = api_instance.get_topics(projects_pk, ifcs=ifcs, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topics: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
ifcs = 'ifcs_example' # str | Filter the returned list by ifcs (optional)
format = 'format_example' # str | Filter the returned list by format (optional)

try:
    # Retrieve all topics
    api_response = api_instance.get_topics(projects_pk, ifcs=ifcs, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **ifcs** | **str**| Filter the returned list by ifcs | [optional] 
 **format** | **str**| Filter the returned list by format | [optional] 

### Return type

[**list[Topic]**](Topic.md)

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

# **get_user**
> SelfBcfUser get_user()

Get current user info

Get current user info Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))

try:
    # Get current user info
    api_response = api_instance.get_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_user: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))

try:
    # Get current user info
    api_response = api_instance.get_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_user: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))

try:
    # Get current user info
    api_response = api_instance.get_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SelfBcfUser**](SelfBcfUser.md)

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

# **get_viewpoint**
> Viewpoint get_viewpoint(guid, projects_pk, topics_guid)

Retrieve a Viewpoint

Retrieve a Viewpoint Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve a Viewpoint
    api_response = api_instance.get_viewpoint(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_viewpoint: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve a Viewpoint
    api_response = api_instance.get_viewpoint(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_viewpoint: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve a Viewpoint
    api_response = api_instance.get_viewpoint(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_viewpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 

### Return type

[**Viewpoint**](Viewpoint.md)

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

# **get_viewpoints**
> list[Viewpoint] get_viewpoints(projects_pk, topics_guid)

Retrieve all Viewpoints of a topic

Retrieve all Viewpoints of a topic Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all Viewpoints of a topic
    api_response = api_instance.get_viewpoints(projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_viewpoints: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all Viewpoints of a topic
    api_response = api_instance.get_viewpoints(projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_viewpoints: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all Viewpoints of a topic
    api_response = api_instance.get_viewpoints(projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_viewpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 

### Return type

[**list[Viewpoint]**](Viewpoint.md)

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

# **get_visibilities**
> Visibility get_visibilities(guid, projects_pk, topics_guid)

Retrieve all visibilities of a viewpoint

Retrieve all visibilities of a viewpoint Required scopes: bcf:read

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all visibilities of a viewpoint
    api_response = api_instance.get_visibilities(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_visibilities: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all visibilities of a viewpoint
    api_response = api_instance.get_visibilities(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_visibilities: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 

try:
    # Retrieve all visibilities of a viewpoint
    api_response = api_instance.get_visibilities(guid, projects_pk, topics_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_visibilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 

### Return type

[**Visibility**](Visibility.md)

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

# **import_bcf**
> import_bcf(id, name)

Import bcf-xml format into this project

Import bcf-xml format into this project. If there are guid conflict, an error will be raised. If there are index conflicts, indexes of the imported file will be overriden with a new index. Author and assigned_to fields will be linked to existing users in the project. If no matching user are found, fields will be emptied. Only BCF 2.1 is supported Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.
name = 'name_example' # str | Name of the project

try:
    # Import bcf-xml format into this project
    api_instance.import_bcf(id, name)
except ApiException as e:
    print("Exception when calling BcfApi->import_bcf: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.
name = 'name_example' # str | Name of the project

try:
    # Import bcf-xml format into this project
    api_instance.import_bcf(id, name)
except ApiException as e:
    print("Exception when calling BcfApi->import_bcf: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.
name = 'name_example' # str | Name of the project

try:
    # Import bcf-xml format into this project
    api_instance.import_bcf(id, name)
except ApiException as e:
    print("Exception when calling BcfApi->import_bcf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this project. | 
 **name** | **str**| Name of the project | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
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

# **update_bcf_project**
> BcfProject update_bcf_project(id, data)

Update some fields of a BCF project

Update some fields of a BCF project Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.BcfProject() # BcfProject | 

try:
    # Update some fields of a BCF project
    api_response = api_instance.update_bcf_project(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_bcf_project: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.BcfProject() # BcfProject | 

try:
    # Update some fields of a BCF project
    api_response = api_instance.update_bcf_project(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_bcf_project: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.
data = bimdata_api_client.BcfProject() # BcfProject | 

try:
    # Update some fields of a BCF project
    api_response = api_instance.update_bcf_project(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_bcf_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this project. | 
 **data** | [**BcfProject**](BcfProject.md)|  | 

### Return type

[**BcfProject**](BcfProject.md)

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

# **update_comment**
> Comment update_comment(guid, projects_pk, topics_guid, data)

Update some fields of a comment

Update some fields of a comment Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Comment() # Comment | 

try:
    # Update some fields of a comment
    api_response = api_instance.update_comment(guid, projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_comment: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Comment() # Comment | 

try:
    # Update some fields of a comment
    api_response = api_instance.update_comment(guid, projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_comment: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Comment() # Comment | 

try:
    # Update some fields of a comment
    api_response = api_instance.update_comment(guid, projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 
 **data** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

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

# **update_extensions**
> Extensions update_extensions(projects_pk, data)

Update project extensions

Update project extensions

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.Extensions() # Extensions | 

try:
    # Update project extensions
    api_response = api_instance.update_extensions(projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_extensions: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.Extensions() # Extensions | 

try:
    # Update project extensions
    api_response = api_instance.update_extensions(projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_extensions: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.Extensions() # Extensions | 

try:
    # Update project extensions
    api_response = api_instance.update_extensions(projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_extensions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **data** | [**Extensions**](Extensions.md)|  | 

### Return type

[**Extensions**](Extensions.md)

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

# **update_full_topic**
> FullTopic update_full_topic(guid, projects_pk, data)

Update some fields of a topic

This is not a standard route. You can update topic, viewpoints and comment is a signle call Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.FullTopic() # FullTopic | 

try:
    # Update some fields of a topic
    api_response = api_instance.update_full_topic(guid, projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_full_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.FullTopic() # FullTopic | 

try:
    # Update some fields of a topic
    api_response = api_instance.update_full_topic(guid, projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_full_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.FullTopic() # FullTopic | 

try:
    # Update some fields of a topic
    api_response = api_instance.update_full_topic(guid, projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_full_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **data** | [**FullTopic**](FullTopic.md)|  | 

### Return type

[**FullTopic**](FullTopic.md)

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

# **update_topic**
> Topic update_topic(guid, projects_pk, data)

Update some fields of a topic

Update some fields of a topic Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.Topic() # Topic | 

try:
    # Update some fields of a topic
    api_response = api_instance.update_topic(guid, projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.Topic() # Topic | 

try:
    # Update some fields of a topic
    api_response = api_instance.update_topic(guid, projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_topic: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
data = bimdata_api_client.Topic() # Topic | 

try:
    # Update some fields of a topic
    api_response = api_instance.update_topic(guid, projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **data** | [**Topic**](Topic.md)|  | 

### Return type

[**Topic**](Topic.md)

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

# **update_viewpoint**
> Viewpoint update_viewpoint(guid, projects_pk, topics_guid, data)

Update some fields of a Viewpoint

This is not a standard route. Update some fields of a Viewpoint Required scopes: bcf:write

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    # Update some fields of a Viewpoint
    api_response = api_instance.update_viewpoint(guid, projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_viewpoint: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    # Update some fields of a Viewpoint
    api_response = api_instance.update_viewpoint(guid, projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_viewpoint: %s\n" % e)
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_guid = 'topics_guid_example' # str | 
data = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    # Update some fields of a Viewpoint
    api_response = api_instance.update_viewpoint(guid, projects_pk, topics_guid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_viewpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)|  | 
 **projects_pk** | **str**|  | 
 **topics_guid** | **str**|  | 
 **data** | [**Viewpoint**](Viewpoint.md)|  | 

### Return type

[**Viewpoint**](Viewpoint.md)

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

