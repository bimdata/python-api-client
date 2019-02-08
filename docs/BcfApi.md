# bimdata_api_client.BcfApi

All URIs are relative to *https://api-beta.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coloring**](BcfApi.md#create_coloring) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring | 
[**create_comment**](BcfApi.md#create_comment) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments | 
[**create_full_topic**](BcfApi.md#create_full_topic) | **POST** /bcf/2.1/projects/{projects_pk}/full-topic | 
[**create_selection**](BcfApi.md#create_selection) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection | 
[**create_topic**](BcfApi.md#create_topic) | **POST** /bcf/2.1/projects/{projects_pk}/topics | 
[**create_viewpoint**](BcfApi.md#create_viewpoint) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints | 
[**create_visibility**](BcfApi.md#create_visibility) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility | 
[**delete_coloring**](BcfApi.md#delete_coloring) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring/{id} | 
[**delete_comment**](BcfApi.md#delete_comment) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{guid} | 
[**delete_selection**](BcfApi.md#delete_selection) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection/{id} | 
[**delete_topic**](BcfApi.md#delete_topic) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{guid} | 
[**delete_viewpoint**](BcfApi.md#delete_viewpoint) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{guid} | 
[**delete_visibility**](BcfApi.md#delete_visibility) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility/{id} | 
[**download_bcf_export**](BcfApi.md#download_bcf_export) | **GET** /bcf/2.1/projects/{id}/export | 
[**full_update_bcf_project**](BcfApi.md#full_update_bcf_project) | **PUT** /bcf/2.1/projects/{id} | 
[**full_update_coloring**](BcfApi.md#full_update_coloring) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring/{id} | 
[**full_update_comment**](BcfApi.md#full_update_comment) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{guid} | 
[**full_update_full_topic**](BcfApi.md#full_update_full_topic) | **PUT** /bcf/2.1/projects/{projects_pk}/full-topic/{guid} | 
[**full_update_selection**](BcfApi.md#full_update_selection) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection/{id} | 
[**full_update_topic**](BcfApi.md#full_update_topic) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{guid} | 
[**full_update_viewpoint**](BcfApi.md#full_update_viewpoint) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{guid} | 
[**full_update_visibility**](BcfApi.md#full_update_visibility) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility/{id} | 
[**get_bcf_project**](BcfApi.md#get_bcf_project) | **GET** /bcf/2.1/projects/{id} | 
[**get_bcf_projects**](BcfApi.md#get_bcf_projects) | **GET** /bcf/2.1/projects | 
[**get_coloring**](BcfApi.md#get_coloring) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring/{id} | 
[**get_colorings**](BcfApi.md#get_colorings) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring | 
[**get_comment**](BcfApi.md#get_comment) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{guid} | 
[**get_comments**](BcfApi.md#get_comments) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments | 
[**get_extensions**](BcfApi.md#get_extensions) | **GET** /bcf/2.1/projects/{projects_pk}/extensions | 
[**get_full_topic**](BcfApi.md#get_full_topic) | **GET** /bcf/2.1/projects/{projects_pk}/full-topic/{guid} | 
[**get_full_topics**](BcfApi.md#get_full_topics) | **GET** /bcf/2.1/projects/{projects_pk}/full-topic | 
[**get_selection**](BcfApi.md#get_selection) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection/{id} | 
[**get_selections**](BcfApi.md#get_selections) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection | 
[**get_snapshot**](BcfApi.md#get_snapshot) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/snapshot | 
[**get_topic**](BcfApi.md#get_topic) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{guid} | 
[**get_topic_viewpoints**](BcfApi.md#get_topic_viewpoints) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/topic-viewpoints | 
[**get_topics**](BcfApi.md#get_topics) | **GET** /bcf/2.1/projects/{projects_pk}/topics | 
[**get_user**](BcfApi.md#get_user) | **GET** /bcf/2.1/current-user | 
[**get_viewpoint**](BcfApi.md#get_viewpoint) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{guid} | 
[**get_viewpoints**](BcfApi.md#get_viewpoints) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints | 
[**get_visibilities**](BcfApi.md#get_visibilities) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility | 
[**get_visibility**](BcfApi.md#get_visibility) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility/{id} | 
[**update_bcf_project**](BcfApi.md#update_bcf_project) | **PATCH** /bcf/2.1/projects/{id} | 
[**update_coloring**](BcfApi.md#update_coloring) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring/{id} | 
[**update_comment**](BcfApi.md#update_comment) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{guid} | 
[**update_extensions**](BcfApi.md#update_extensions) | **PATCH** /bcf/2.1/projects/{projects_pk}/extensions | 
[**update_full_topic**](BcfApi.md#update_full_topic) | **PATCH** /bcf/2.1/projects/{projects_pk}/full-topic/{guid} | 
[**update_selection**](BcfApi.md#update_selection) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection/{id} | 
[**update_topic**](BcfApi.md#update_topic) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{guid} | 
[**update_viewpoint**](BcfApi.md#update_viewpoint) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{guid} | 
[**update_visibility**](BcfApi.md#update_visibility) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility/{id} | 


# **create_coloring**
> Coloring create_coloring(projects_pk, topics_pk, viewpoints_pk, coloring)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 
coloring = bimdata_api_client.Coloring() # Coloring | 

try:
    api_response = api_instance.create_coloring(projects_pk, topics_pk, viewpoints_pk, coloring)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_coloring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 
 **coloring** | [**Coloring**](Coloring.md)|  | 

### Return type

[**Coloring**](Coloring.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_comment**
> Comment create_comment(projects_pk, topics_pk, comment)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
comment = bimdata_api_client.Comment() # Comment | 

try:
    api_response = api_instance.create_comment(projects_pk, topics_pk, comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **comment** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_full_topic**
> SingleJsonTopic create_full_topic(projects_pk, single_json_topic)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
single_json_topic = bimdata_api_client.SingleJsonTopic() # SingleJsonTopic | 

try:
    api_response = api_instance.create_full_topic(projects_pk, single_json_topic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_full_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **single_json_topic** | [**SingleJsonTopic**](SingleJsonTopic.md)|  | 

### Return type

[**SingleJsonTopic**](SingleJsonTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_selection**
> Component create_selection(projects_pk, topics_pk, viewpoints_pk, component)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 
component = bimdata_api_client.Component() # Component | 

try:
    api_response = api_instance.create_selection(projects_pk, topics_pk, viewpoints_pk, component)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_selection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 
 **component** | [**Component**](Component.md)|  | 

### Return type

[**Component**](Component.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_topic**
> Topic create_topic(projects_pk, topic)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topic = bimdata_api_client.Topic() # Topic | 

try:
    api_response = api_instance.create_topic(projects_pk, topic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topic** | [**Topic**](Topic.md)|  | 

### Return type

[**Topic**](Topic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_viewpoint**
> Viewpoint create_viewpoint(projects_pk, topics_pk, viewpoint)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoint = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    api_response = api_instance.create_viewpoint(projects_pk, topics_pk, viewpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_viewpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoint** | [**Viewpoint**](Viewpoint.md)|  | 

### Return type

[**Viewpoint**](Viewpoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_visibility**
> Visibility create_visibility(projects_pk, topics_pk, viewpoints_pk, visibility)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 
visibility = bimdata_api_client.Visibility() # Visibility | 

try:
    api_response = api_instance.create_visibility(projects_pk, topics_pk, viewpoints_pk, visibility)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 
 **visibility** | [**Visibility**](Visibility.md)|  | 

### Return type

[**Visibility**](Visibility.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coloring**
> delete_coloring(id, projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this coloring.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_instance.delete_coloring(id, projects_pk, topics_pk, viewpoints_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_coloring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this coloring. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> delete_comment(guid, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this comment.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.delete_comment(guid, projects_pk, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this comment. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_selection**
> delete_selection(id, projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this component.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_instance.delete_selection(id, projects_pk, topics_pk, viewpoints_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_selection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this component. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topic**
> delete_topic(guid, projects_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this topic.
projects_pk = 'projects_pk_example' # str | 

try:
    api_instance.delete_topic(guid, projects_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this topic. | 
 **projects_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_viewpoint**
> delete_viewpoint(guid, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this viewpoint.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.delete_viewpoint(guid, projects_pk, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_viewpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this viewpoint. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_visibility**
> delete_visibility(id, projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this visibility.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_instance.delete_visibility(id, projects_pk, topics_pk, viewpoints_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this visibility. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_bcf_export**
> download_bcf_export(id)



         export project's topics in bcf-xml format         

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.

try:
    api_instance.download_bcf_export(id)
except ApiException as e:
    print("Exception when calling BcfApi->download_bcf_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this project. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_bcf_project**
> BcfProject full_update_bcf_project(id, bcf_project)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.
bcf_project = bimdata_api_client.BcfProject() # BcfProject | 

try:
    api_response = api_instance.full_update_bcf_project(id, bcf_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_bcf_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this project. | 
 **bcf_project** | [**BcfProject**](BcfProject.md)|  | 

### Return type

[**BcfProject**](BcfProject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_coloring**
> Coloring full_update_coloring(id, projects_pk, topics_pk, viewpoints_pk, coloring)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this coloring.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 
coloring = bimdata_api_client.Coloring() # Coloring | 

try:
    api_response = api_instance.full_update_coloring(id, projects_pk, topics_pk, viewpoints_pk, coloring)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_coloring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this coloring. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 
 **coloring** | [**Coloring**](Coloring.md)|  | 

### Return type

[**Coloring**](Coloring.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_comment**
> Comment full_update_comment(guid, projects_pk, topics_pk, comment)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this comment.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
comment = bimdata_api_client.Comment() # Comment | 

try:
    api_response = api_instance.full_update_comment(guid, projects_pk, topics_pk, comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this comment. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **comment** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_full_topic**
> SingleJsonTopic full_update_full_topic(guid, projects_pk, single_json_topic)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this topic.
projects_pk = 'projects_pk_example' # str | 
single_json_topic = bimdata_api_client.SingleJsonTopic() # SingleJsonTopic | 

try:
    api_response = api_instance.full_update_full_topic(guid, projects_pk, single_json_topic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_full_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this topic. | 
 **projects_pk** | **str**|  | 
 **single_json_topic** | [**SingleJsonTopic**](SingleJsonTopic.md)|  | 

### Return type

[**SingleJsonTopic**](SingleJsonTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_selection**
> Component full_update_selection(id, projects_pk, topics_pk, viewpoints_pk, component)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this component.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 
component = bimdata_api_client.Component() # Component | 

try:
    api_response = api_instance.full_update_selection(id, projects_pk, topics_pk, viewpoints_pk, component)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_selection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this component. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 
 **component** | [**Component**](Component.md)|  | 

### Return type

[**Component**](Component.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_topic**
> Topic full_update_topic(guid, projects_pk, topic)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this topic.
projects_pk = 'projects_pk_example' # str | 
topic = bimdata_api_client.Topic() # Topic | 

try:
    api_response = api_instance.full_update_topic(guid, projects_pk, topic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this topic. | 
 **projects_pk** | **str**|  | 
 **topic** | [**Topic**](Topic.md)|  | 

### Return type

[**Topic**](Topic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_viewpoint**
> Viewpoint full_update_viewpoint(guid, projects_pk, topics_pk, viewpoint)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this viewpoint.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoint = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    api_response = api_instance.full_update_viewpoint(guid, projects_pk, topics_pk, viewpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_viewpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this viewpoint. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoint** | [**Viewpoint**](Viewpoint.md)|  | 

### Return type

[**Viewpoint**](Viewpoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_visibility**
> Visibility full_update_visibility(id, projects_pk, topics_pk, viewpoints_pk, visibility)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this visibility.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 
visibility = bimdata_api_client.Visibility() # Visibility | 

try:
    api_response = api_instance.full_update_visibility(id, projects_pk, topics_pk, viewpoints_pk, visibility)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this visibility. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 
 **visibility** | [**Visibility**](Visibility.md)|  | 

### Return type

[**Visibility**](Visibility.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bcf_project**
> BcfProject get_bcf_project(id)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.

try:
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bcf_projects**
> list[BcfProject] get_bcf_projects()



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))

try:
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coloring**
> Coloring get_coloring(id, projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this coloring.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_response = api_instance.get_coloring(id, projects_pk, topics_pk, viewpoints_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_coloring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this coloring. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 

### Return type

[**Coloring**](Coloring.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_colorings**
> list[Coloring] get_colorings(projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_response = api_instance.get_colorings(projects_pk, topics_pk, viewpoints_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_colorings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 

### Return type

[**list[Coloring]**](Coloring.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> Comment get_comment(guid, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this comment.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_comment(guid, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this comment. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments**
> list[Comment] get_comments(projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_comments(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[Comment]**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extensions**
> Extensions get_extensions(projects_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 

try:
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_full_topic**
> SingleJsonTopic get_full_topic(guid, projects_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this topic.
projects_pk = 'projects_pk_example' # str | 

try:
    api_response = api_instance.get_full_topic(guid, projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_full_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this topic. | 
 **projects_pk** | **str**|  | 

### Return type

[**SingleJsonTopic**](SingleJsonTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_full_topics**
> list[SingleJsonTopic] get_full_topics(projects_pk, ifcs=ifcs, format=format)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
ifcs = 'ifcs_example' # str | Filter the returned list by ifcs (optional)
format = 'format_example' # str | Filter the returned list by format (optional)

try:
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

[**list[SingleJsonTopic]**](SingleJsonTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_selection**
> Component get_selection(id, projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this component.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_response = api_instance.get_selection(id, projects_pk, topics_pk, viewpoints_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_selection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this component. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 

### Return type

[**Component**](Component.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_selections**
> list[Component] get_selections(projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_response = api_instance.get_selections(projects_pk, topics_pk, viewpoints_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_selections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 

### Return type

[**list[Component]**](Component.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot**
> file get_snapshot(projects_pk, topics_pk, viewpoints_pk)



Retrieve the viewpoint' snapshot

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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_response = api_instance.get_snapshot(projects_pk, topics_pk, viewpoints_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 

### Return type

**file**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic**
> Topic get_topic(guid, projects_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this topic.
projects_pk = 'projects_pk_example' # str | 

try:
    api_response = api_instance.get_topic(guid, projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this topic. | 
 **projects_pk** | **str**|  | 

### Return type

[**Topic**](Topic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_viewpoints**
> list[Viewpoint] get_topic_viewpoints(projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_topic_viewpoints(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topic_viewpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[Viewpoint]**](Viewpoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topics**
> list[Topic] get_topics(projects_pk, ifcs=ifcs, format=format)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
ifcs = 'ifcs_example' # str | Filter the returned list by ifcs (optional)
format = 'format_example' # str | Filter the returned list by format (optional)

try:
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> SelfBcfUser get_user()



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))

try:
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_viewpoint**
> Viewpoint get_viewpoint(guid, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this viewpoint.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_viewpoint(guid, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_viewpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this viewpoint. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**Viewpoint**](Viewpoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_viewpoints**
> list[Viewpoint] get_viewpoints(projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_viewpoints(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_viewpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[Viewpoint]**](Viewpoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_visibilities**
> list[Visibility] get_visibilities(projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_response = api_instance.get_visibilities(projects_pk, topics_pk, viewpoints_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_visibilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 

### Return type

[**list[Visibility]**](Visibility.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_visibility**
> Visibility get_visibility(id, projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this visibility.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_response = api_instance.get_visibility(id, projects_pk, topics_pk, viewpoints_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this visibility. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 

### Return type

[**Visibility**](Visibility.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bcf_project**
> BcfProject update_bcf_project(id, bcf_project)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this project.
bcf_project = bimdata_api_client.BcfProject() # BcfProject | 

try:
    api_response = api_instance.update_bcf_project(id, bcf_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_bcf_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this project. | 
 **bcf_project** | [**BcfProject**](BcfProject.md)|  | 

### Return type

[**BcfProject**](BcfProject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coloring**
> Coloring update_coloring(id, projects_pk, topics_pk, viewpoints_pk, coloring)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this coloring.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 
coloring = bimdata_api_client.Coloring() # Coloring | 

try:
    api_response = api_instance.update_coloring(id, projects_pk, topics_pk, viewpoints_pk, coloring)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_coloring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this coloring. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 
 **coloring** | [**Coloring**](Coloring.md)|  | 

### Return type

[**Coloring**](Coloring.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment**
> Comment update_comment(guid, projects_pk, topics_pk, comment)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this comment.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
comment = bimdata_api_client.Comment() # Comment | 

try:
    api_response = api_instance.update_comment(guid, projects_pk, topics_pk, comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this comment. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **comment** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_extensions**
> Extensions update_extensions(projects_pk, extensions)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
extensions = bimdata_api_client.Extensions() # Extensions | 

try:
    api_response = api_instance.update_extensions(projects_pk, extensions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_extensions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **extensions** | [**Extensions**](Extensions.md)|  | 

### Return type

[**Extensions**](Extensions.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_full_topic**
> SingleJsonTopic update_full_topic(guid, projects_pk, single_json_topic)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this topic.
projects_pk = 'projects_pk_example' # str | 
single_json_topic = bimdata_api_client.SingleJsonTopic() # SingleJsonTopic | 

try:
    api_response = api_instance.update_full_topic(guid, projects_pk, single_json_topic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_full_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this topic. | 
 **projects_pk** | **str**|  | 
 **single_json_topic** | [**SingleJsonTopic**](SingleJsonTopic.md)|  | 

### Return type

[**SingleJsonTopic**](SingleJsonTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_selection**
> Component update_selection(id, projects_pk, topics_pk, viewpoints_pk, component)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this component.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 
component = bimdata_api_client.Component() # Component | 

try:
    api_response = api_instance.update_selection(id, projects_pk, topics_pk, viewpoints_pk, component)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_selection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this component. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 
 **component** | [**Component**](Component.md)|  | 

### Return type

[**Component**](Component.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_topic**
> Topic update_topic(guid, projects_pk, topic)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this topic.
projects_pk = 'projects_pk_example' # str | 
topic = bimdata_api_client.Topic() # Topic | 

try:
    api_response = api_instance.update_topic(guid, projects_pk, topic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this topic. | 
 **projects_pk** | **str**|  | 
 **topic** | [**Topic**](Topic.md)|  | 

### Return type

[**Topic**](Topic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_viewpoint**
> Viewpoint update_viewpoint(guid, projects_pk, topics_pk, viewpoint)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
guid = 'guid_example' # str | A UUID string identifying this viewpoint.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoint = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    api_response = api_instance.update_viewpoint(guid, projects_pk, topics_pk, viewpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_viewpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| A UUID string identifying this viewpoint. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoint** | [**Viewpoint**](Viewpoint.md)|  | 

### Return type

[**Viewpoint**](Viewpoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_visibility**
> Visibility update_visibility(id, projects_pk, topics_pk, viewpoints_pk, visibility)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this visibility.
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 
visibility = bimdata_api_client.Visibility() # Visibility | 

try:
    api_response = api_instance.update_visibility(id, projects_pk, topics_pk, viewpoints_pk, visibility)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this visibility. | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 
 **visibility** | [**Visibility**](Visibility.md)|  | 

### Return type

[**Visibility**](Visibility.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

