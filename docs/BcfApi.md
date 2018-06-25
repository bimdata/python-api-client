# bimdata_api_client.BcfApi

All URIs are relative to *https://api-beta.bimdata.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bcf2_1_current_user_list**](BcfApi.md#bcf2_1_current_user_list) | **GET** /bcf/2.1/current-user | 
[**bcf2_1_projects_topics_comments_events_delete**](BcfApi.md#bcf2_1_projects_topics_comments_events_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/events/{id} | 
[**bcf2_1_projects_topics_comments_events_delete_0**](BcfApi.md#bcf2_1_projects_topics_comments_events_delete_0) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{comments_pk}/events/{id} | 
[**bcf2_1_projects_topics_events_delete**](BcfApi.md#bcf2_1_projects_topics_events_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/events/{id} | 
[**bcf2_1_projects_topics_viewpoints_bitmap_delete**](BcfApi.md#bcf2_1_projects_topics_viewpoints_bitmap_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/bitmap/{id} | 
[**bcf2_1_projects_topics_viewpoints_coloring_delete**](BcfApi.md#bcf2_1_projects_topics_viewpoints_coloring_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring/{id} | 
[**bcf2_1_projects_topics_viewpoints_delete**](BcfApi.md#bcf2_1_projects_topics_viewpoints_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{id} | 
[**bcf2_1_projects_topics_viewpoints_selection_delete**](BcfApi.md#bcf2_1_projects_topics_viewpoints_selection_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection/{id} | 
[**bcf2_1_projects_topics_viewpoints_visibility_delete**](BcfApi.md#bcf2_1_projects_topics_viewpoints_visibility_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility/{id} | 
[**create_bcf_document**](BcfApi.md#create_bcf_document) | **POST** /bcf/2.1/projects/{projects_pk}/documents | 
[**create_bcf_project**](BcfApi.md#create_bcf_project) | **POST** /bcf/2.1/projects | 
[**create_bitmap**](BcfApi.md#create_bitmap) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/bitmap | 
[**create_coloring**](BcfApi.md#create_coloring) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring | 
[**create_comment**](BcfApi.md#create_comment) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments | 
[**create_comment_event**](BcfApi.md#create_comment_event) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/events | 
[**create_comment_event_0**](BcfApi.md#create_comment_event_0) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{comments_pk}/events | 
[**create_document_reference**](BcfApi.md#create_document_reference) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/document_references | 
[**create_file**](BcfApi.md#create_file) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/file | 
[**create_related_topic**](BcfApi.md#create_related_topic) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/related_topics | 
[**create_selection**](BcfApi.md#create_selection) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection | 
[**create_snippet**](BcfApi.md#create_snippet) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/snippet | 
[**create_topic**](BcfApi.md#create_topic) | **POST** /bcf/2.1/projects/{projects_pk}/topics | 
[**create_topic_event**](BcfApi.md#create_topic_event) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/events | 
[**create_viewpoint**](BcfApi.md#create_viewpoint) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints | 
[**create_visibility**](BcfApi.md#create_visibility) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility | 
[**delete_bcf_document**](BcfApi.md#delete_bcf_document) | **DELETE** /bcf/2.1/projects/{projects_pk}/documents/{id} | 
[**delete_bcf_project**](BcfApi.md#delete_bcf_project) | **DELETE** /bcf/2.1/projects/{id} | 
[**delete_comment**](BcfApi.md#delete_comment) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{id} | 
[**delete_document_reference**](BcfApi.md#delete_document_reference) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/document_references/{id} | 
[**delete_file**](BcfApi.md#delete_file) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/file/{id} | 
[**delete_related_topic**](BcfApi.md#delete_related_topic) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/related_topics/{id} | 
[**delete_snippet**](BcfApi.md#delete_snippet) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/snippet/{id} | 
[**delete_topic**](BcfApi.md#delete_topic) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{id} | 
[**full_update_bcf_document**](BcfApi.md#full_update_bcf_document) | **PUT** /bcf/2.1/projects/{projects_pk}/documents/{id} | 
[**full_update_bcf_project**](BcfApi.md#full_update_bcf_project) | **PUT** /bcf/2.1/projects/{id} | 
[**full_update_bitmap**](BcfApi.md#full_update_bitmap) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/bitmap/{id} | 
[**full_update_coloring**](BcfApi.md#full_update_coloring) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring/{id} | 
[**full_update_comment**](BcfApi.md#full_update_comment) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{id} | 
[**full_update_comment_event**](BcfApi.md#full_update_comment_event) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/events/{id} | 
[**full_update_comment_event_0**](BcfApi.md#full_update_comment_event_0) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{comments_pk}/events/{id} | 
[**full_update_document_reference**](BcfApi.md#full_update_document_reference) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/document_references/{id} | 
[**full_update_file**](BcfApi.md#full_update_file) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/file/{id} | 
[**full_update_related_topic**](BcfApi.md#full_update_related_topic) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/related_topics/{id} | 
[**full_update_selection**](BcfApi.md#full_update_selection) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection/{id} | 
[**full_update_snippet**](BcfApi.md#full_update_snippet) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/snippet/{id} | 
[**full_update_topic**](BcfApi.md#full_update_topic) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{id} | 
[**full_update_topic_event**](BcfApi.md#full_update_topic_event) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/events/{id} | 
[**full_update_viewpoint**](BcfApi.md#full_update_viewpoint) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{id} | 
[**full_update_visibility**](BcfApi.md#full_update_visibility) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility/{id} | 
[**get_all_comments_events**](BcfApi.md#get_all_comments_events) | **GET** /bcf/2.1/projects/{projects_pk}/topics/comments/events | 
[**get_all_topics_events**](BcfApi.md#get_all_topics_events) | **GET** /bcf/2.1/projects/{projects_pk}/topics/events | 
[**get_bcf_document**](BcfApi.md#get_bcf_document) | **GET** /bcf/2.1/projects/{projects_pk}/documents/{id} | 
[**get_bcf_documents**](BcfApi.md#get_bcf_documents) | **GET** /bcf/2.1/projects/{projects_pk}/documents | 
[**get_bcf_project**](BcfApi.md#get_bcf_project) | **GET** /bcf/2.1/projects/{id} | 
[**get_bcf_projects**](BcfApi.md#get_bcf_projects) | **GET** /bcf/2.1/projects | 
[**get_bitmap**](BcfApi.md#get_bitmap) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/bitmap/{id} | 
[**get_bitmaps**](BcfApi.md#get_bitmaps) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/bitmap | 
[**get_coloring**](BcfApi.md#get_coloring) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring/{id} | 
[**get_colorings**](BcfApi.md#get_colorings) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring | 
[**get_comment**](BcfApi.md#get_comment) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{id} | 
[**get_comment_event**](BcfApi.md#get_comment_event) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/events/{id} | 
[**get_comment_event_0**](BcfApi.md#get_comment_event_0) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{comments_pk}/events/{id} | 
[**get_comment_events**](BcfApi.md#get_comment_events) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/events | 
[**get_comment_events_0**](BcfApi.md#get_comment_events_0) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{comments_pk}/events | 
[**get_comments**](BcfApi.md#get_comments) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments | 
[**get_document_reference**](BcfApi.md#get_document_reference) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/document_references/{id} | 
[**get_document_references**](BcfApi.md#get_document_references) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/document_references | 
[**get_extensions**](BcfApi.md#get_extensions) | **GET** /bcf/2.1/projects/{projects_pk}/extensions | 
[**get_file**](BcfApi.md#get_file) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/file/{id} | 
[**get_files**](BcfApi.md#get_files) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/file | 
[**get_related_topic**](BcfApi.md#get_related_topic) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/related_topics/{id} | 
[**get_related_topics**](BcfApi.md#get_related_topics) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/related_topics | 
[**get_selection**](BcfApi.md#get_selection) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection/{id} | 
[**get_selections**](BcfApi.md#get_selections) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection | 
[**get_snapshots**](BcfApi.md#get_snapshots) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/snapshot | 
[**get_snippet**](BcfApi.md#get_snippet) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/snippet/{id} | 
[**get_snippets**](BcfApi.md#get_snippets) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/snippet | 
[**get_topic**](BcfApi.md#get_topic) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{id} | 
[**get_topic_event**](BcfApi.md#get_topic_event) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/events/{id} | 
[**get_topic_events**](BcfApi.md#get_topic_events) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/events | 
[**get_topics**](BcfApi.md#get_topics) | **GET** /bcf/2.1/projects/{projects_pk}/topics | 
[**get_viewpoint**](BcfApi.md#get_viewpoint) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{id} | 
[**get_viewpoints**](BcfApi.md#get_viewpoints) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints | 
[**get_visibilities**](BcfApi.md#get_visibilities) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility | 
[**get_visibility**](BcfApi.md#get_visibility) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility/{id} | 
[**update_bcf_document**](BcfApi.md#update_bcf_document) | **PATCH** /bcf/2.1/projects/{projects_pk}/documents/{id} | 
[**update_bcf_project**](BcfApi.md#update_bcf_project) | **PATCH** /bcf/2.1/projects/{id} | 
[**update_bitmap**](BcfApi.md#update_bitmap) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/bitmap/{id} | 
[**update_coloring**](BcfApi.md#update_coloring) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring/{id} | 
[**update_comment**](BcfApi.md#update_comment) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{id} | 
[**update_comment_event**](BcfApi.md#update_comment_event) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/events/{id} | 
[**update_comment_event_0**](BcfApi.md#update_comment_event_0) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{comments_pk}/events/{id} | 
[**update_document_reference**](BcfApi.md#update_document_reference) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/document_references/{id} | 
[**update_file**](BcfApi.md#update_file) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/file/{id} | 
[**update_related_topic**](BcfApi.md#update_related_topic) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/related_topics/{id} | 
[**update_selection**](BcfApi.md#update_selection) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection/{id} | 
[**update_snippet**](BcfApi.md#update_snippet) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/snippet/{id} | 
[**update_topic**](BcfApi.md#update_topic) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{id} | 
[**update_topic_event**](BcfApi.md#update_topic_event) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/events/{id} | 
[**update_viewpoint**](BcfApi.md#update_viewpoint) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{id} | 
[**update_visibility**](BcfApi.md#update_visibility) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility/{id} | 


# **bcf2_1_current_user_list**
> list[SelfUser] bcf2_1_current_user_list()



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))

try:
    api_response = api_instance.bcf2_1_current_user_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_current_user_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SelfUser]**](SelfUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_events_delete**
> bcf2_1_projects_topics_comments_events_delete(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_comments_events_delete(id, projects_pk, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **bcf2_1_projects_topics_comments_events_delete_0**
> bcf2_1_projects_topics_comments_events_delete_0(comments_pk, id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
comments_pk = 'comments_pk_example' # str | 
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_comments_events_delete_0(comments_pk, id, projects_pk, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments_pk** | **str**|  | 
 **id** | **str**|  | 
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

# **bcf2_1_projects_topics_events_delete**
> bcf2_1_projects_topics_events_delete(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_events_delete(id, projects_pk, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_events_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **bcf2_1_projects_topics_viewpoints_bitmap_delete**
> bcf2_1_projects_topics_viewpoints_bitmap_delete(id, projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_viewpoints_bitmap_delete(id, projects_pk, topics_pk, viewpoints_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_bitmap_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **bcf2_1_projects_topics_viewpoints_coloring_delete**
> bcf2_1_projects_topics_viewpoints_coloring_delete(id, projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_viewpoints_coloring_delete(id, projects_pk, topics_pk, viewpoints_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_coloring_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **bcf2_1_projects_topics_viewpoints_delete**
> bcf2_1_projects_topics_viewpoints_delete(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_viewpoints_delete(id, projects_pk, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **bcf2_1_projects_topics_viewpoints_selection_delete**
> bcf2_1_projects_topics_viewpoints_selection_delete(id, projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_viewpoints_selection_delete(id, projects_pk, topics_pk, viewpoints_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_selection_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **bcf2_1_projects_topics_viewpoints_visibility_delete**
> bcf2_1_projects_topics_viewpoints_visibility_delete(id, projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_viewpoints_visibility_delete(id, projects_pk, topics_pk, viewpoints_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_visibility_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **create_bcf_document**
> create_bcf_document(projects_pk, guid=guid, filename=filename)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
guid = 'guid_example' # str |  (optional)
filename = 'filename_example' # str |  (optional)

try:
    api_instance.create_bcf_document(projects_pk, guid=guid, filename=filename)
except ApiException as e:
    print("Exception when calling BcfApi->create_bcf_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **guid** | [**str**](str.md)|  | [optional] 
 **filename** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bcf_project**
> BcfProject create_bcf_project(bcf_project)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
bcf_project = bimdata_api_client.BcfProject() # BcfProject | 

try:
    api_response = api_instance.create_bcf_project(bcf_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_bcf_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bcf_project** | [**BcfProject**](BcfProject.md)|  | 

### Return type

[**BcfProject**](BcfProject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bitmap**
> Bitmap create_bitmap(projects_pk, topics_pk, viewpoints_pk, bitmap)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 
bitmap = bimdata_api_client.Bitmap() # Bitmap | 

try:
    api_response = api_instance.create_bitmap(projects_pk, topics_pk, viewpoints_pk, bitmap)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_bitmap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 
 **bitmap** | [**Bitmap**](Bitmap.md)|  | 

### Return type

[**Bitmap**](Bitmap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coloring**
> Coloring create_coloring(projects_pk, topics_pk, viewpoints_pk, coloring)



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

# **create_comment_event**
> CommentEvent create_comment_event(projects_pk, topics_pk, comment_event)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
comment_event = bimdata_api_client.CommentEvent() # CommentEvent | 

try:
    api_response = api_instance.create_comment_event(projects_pk, topics_pk, comment_event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_comment_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **comment_event** | [**CommentEvent**](CommentEvent.md)|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_comment_event_0**
> CommentEvent create_comment_event_0(comments_pk, projects_pk, topics_pk, comment_event)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
comments_pk = 'comments_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
comment_event = bimdata_api_client.CommentEvent() # CommentEvent | 

try:
    api_response = api_instance.create_comment_event_0(comments_pk, projects_pk, topics_pk, comment_event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_comment_event_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **comment_event** | [**CommentEvent**](CommentEvent.md)|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document_reference**
> DocumentReference create_document_reference(projects_pk, topics_pk, document_reference)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
document_reference = bimdata_api_client.DocumentReference() # DocumentReference | 

try:
    api_response = api_instance.create_document_reference(projects_pk, topics_pk, document_reference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_document_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **document_reference** | [**DocumentReference**](DocumentReference.md)|  | 

### Return type

[**DocumentReference**](DocumentReference.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file**
> BimSnippet create_file(projects_pk, topics_pk, bim_snippet)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
bim_snippet = bimdata_api_client.BimSnippet() # BimSnippet | 

try:
    api_response = api_instance.create_file(projects_pk, topics_pk, bim_snippet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **bim_snippet** | [**BimSnippet**](BimSnippet.md)|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_related_topic**
> RelatedTopic create_related_topic(projects_pk, topics_pk, related_topic)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
related_topic = bimdata_api_client.RelatedTopic() # RelatedTopic | 

try:
    api_response = api_instance.create_related_topic(projects_pk, topics_pk, related_topic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_related_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **related_topic** | [**RelatedTopic**](RelatedTopic.md)|  | 

### Return type

[**RelatedTopic**](RelatedTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_selection**
> Component create_selection(projects_pk, topics_pk, viewpoints_pk, component)



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

# **create_snippet**
> BimSnippet create_snippet(projects_pk, topics_pk, bim_snippet)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
bim_snippet = bimdata_api_client.BimSnippet() # BimSnippet | 

try:
    api_response = api_instance.create_snippet(projects_pk, topics_pk, bim_snippet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_snippet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **bim_snippet** | [**BimSnippet**](BimSnippet.md)|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_topic**
> Topic create_topic(projects_pk, topic)



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

# **create_topic_event**
> TopicEvents create_topic_event(projects_pk, topics_pk, topic_events)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
topic_events = bimdata_api_client.TopicEvents() # TopicEvents | 

try:
    api_response = api_instance.create_topic_event(projects_pk, topics_pk, topic_events)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->create_topic_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **topic_events** | [**TopicEvents**](TopicEvents.md)|  | 

### Return type

[**TopicEvents**](TopicEvents.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_viewpoint**
> Viewpoint create_viewpoint(projects_pk, topics_pk, viewpoint)



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

# **delete_bcf_document**
> delete_bcf_document(id, projects_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 

try:
    api_instance.delete_bcf_document(id, projects_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_bcf_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bcf_project**
> delete_bcf_project(id)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.delete_bcf_project(id)
except ApiException as e:
    print("Exception when calling BcfApi->delete_bcf_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> delete_comment(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.delete_comment(id, projects_pk, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **delete_document_reference**
> delete_document_reference(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.delete_document_reference(id, projects_pk, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_document_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **delete_file**
> delete_file(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.delete_file(id, projects_pk, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **delete_related_topic**
> delete_related_topic(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.delete_related_topic(id, projects_pk, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_related_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **delete_snippet**
> delete_snippet(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.delete_snippet(id, projects_pk, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_snippet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **delete_topic**
> delete_topic(id, projects_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 

try:
    api_instance.delete_topic(id, projects_pk)
except ApiException as e:
    print("Exception when calling BcfApi->delete_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_bcf_document**
> full_update_bcf_document(id, projects_pk, guid=guid, filename=filename)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
guid = 'guid_example' # str |  (optional)
filename = 'filename_example' # str |  (optional)

try:
    api_instance.full_update_bcf_document(id, projects_pk, guid=guid, filename=filename)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_bcf_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **guid** | [**str**](str.md)|  | [optional] 
 **filename** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_bcf_project**
> BcfProject full_update_bcf_project(id, bcf_project)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
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
 **id** | **str**|  | 
 **bcf_project** | [**BcfProject**](BcfProject.md)|  | 

### Return type

[**BcfProject**](BcfProject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_bitmap**
> Bitmap full_update_bitmap(id, projects_pk, topics_pk, viewpoints_pk, bitmap)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 
bitmap = bimdata_api_client.Bitmap() # Bitmap | 

try:
    api_response = api_instance.full_update_bitmap(id, projects_pk, topics_pk, viewpoints_pk, bitmap)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_bitmap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 
 **bitmap** | [**Bitmap**](Bitmap.md)|  | 

### Return type

[**Bitmap**](Bitmap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_coloring**
> Coloring full_update_coloring(id, projects_pk, topics_pk, viewpoints_pk, coloring)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
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
 **id** | **str**|  | 
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
> Comment full_update_comment(id, projects_pk, topics_pk, comment)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
comment = bimdata_api_client.Comment() # Comment | 

try:
    api_response = api_instance.full_update_comment(id, projects_pk, topics_pk, comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **full_update_comment_event**
> CommentEvent full_update_comment_event(id, projects_pk, topics_pk, comment_event)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
comment_event = bimdata_api_client.CommentEvent() # CommentEvent | 

try:
    api_response = api_instance.full_update_comment_event(id, projects_pk, topics_pk, comment_event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_comment_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **comment_event** | [**CommentEvent**](CommentEvent.md)|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_comment_event_0**
> CommentEvent full_update_comment_event_0(comments_pk, id, projects_pk, topics_pk, comment_event)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
comments_pk = 'comments_pk_example' # str | 
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
comment_event = bimdata_api_client.CommentEvent() # CommentEvent | 

try:
    api_response = api_instance.full_update_comment_event_0(comments_pk, id, projects_pk, topics_pk, comment_event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_comment_event_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments_pk** | **str**|  | 
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **comment_event** | [**CommentEvent**](CommentEvent.md)|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_document_reference**
> DocumentReference full_update_document_reference(id, projects_pk, topics_pk, document_reference)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
document_reference = bimdata_api_client.DocumentReference() # DocumentReference | 

try:
    api_response = api_instance.full_update_document_reference(id, projects_pk, topics_pk, document_reference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_document_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **document_reference** | [**DocumentReference**](DocumentReference.md)|  | 

### Return type

[**DocumentReference**](DocumentReference.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_file**
> BimSnippet full_update_file(id, projects_pk, topics_pk, bim_snippet)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
bim_snippet = bimdata_api_client.BimSnippet() # BimSnippet | 

try:
    api_response = api_instance.full_update_file(id, projects_pk, topics_pk, bim_snippet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **bim_snippet** | [**BimSnippet**](BimSnippet.md)|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_related_topic**
> RelatedTopic full_update_related_topic(id, projects_pk, topics_pk, related_topic)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
related_topic = bimdata_api_client.RelatedTopic() # RelatedTopic | 

try:
    api_response = api_instance.full_update_related_topic(id, projects_pk, topics_pk, related_topic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_related_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **related_topic** | [**RelatedTopic**](RelatedTopic.md)|  | 

### Return type

[**RelatedTopic**](RelatedTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_selection**
> Component full_update_selection(id, projects_pk, topics_pk, viewpoints_pk, component)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
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
 **id** | **str**|  | 
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

# **full_update_snippet**
> BimSnippet full_update_snippet(id, projects_pk, topics_pk, bim_snippet)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
bim_snippet = bimdata_api_client.BimSnippet() # BimSnippet | 

try:
    api_response = api_instance.full_update_snippet(id, projects_pk, topics_pk, bim_snippet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_snippet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **bim_snippet** | [**BimSnippet**](BimSnippet.md)|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_topic**
> Topic full_update_topic(id, projects_pk, topic)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topic = bimdata_api_client.Topic() # Topic | 

try:
    api_response = api_instance.full_update_topic(id, projects_pk, topic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **full_update_topic_event**
> TopicEvents full_update_topic_event(id, projects_pk, topics_pk, topic_events)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
topic_events = bimdata_api_client.TopicEvents() # TopicEvents | 

try:
    api_response = api_instance.full_update_topic_event(id, projects_pk, topics_pk, topic_events)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_topic_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **topic_events** | [**TopicEvents**](TopicEvents.md)|  | 

### Return type

[**TopicEvents**](TopicEvents.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_viewpoint**
> Viewpoint full_update_viewpoint(id, projects_pk, topics_pk, viewpoint)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoint = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    api_response = api_instance.full_update_viewpoint(id, projects_pk, topics_pk, viewpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->full_update_viewpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
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
 **id** | **str**|  | 
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

# **get_all_comments_events**
> list[CommentEvent] get_all_comments_events(projects_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 

try:
    api_response = api_instance.get_all_comments_events(projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_all_comments_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 

### Return type

[**list[CommentEvent]**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_topics_events**
> list[TopicEvents] get_all_topics_events(projects_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 

try:
    api_response = api_instance.get_all_topics_events(projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_all_topics_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 

### Return type

[**list[TopicEvents]**](TopicEvents.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bcf_document**
> get_bcf_document(id, projects_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 

try:
    api_instance.get_bcf_document(id, projects_pk)
except ApiException as e:
    print("Exception when calling BcfApi->get_bcf_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bcf_documents**
> get_bcf_documents(projects_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 

try:
    api_instance.get_bcf_documents(projects_pk)
except ApiException as e:
    print("Exception when calling BcfApi->get_bcf_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bcf_project**
> BcfProject get_bcf_project(id)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_bcf_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_bcf_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **get_bitmap**
> Bitmap get_bitmap(id, projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_response = api_instance.get_bitmap(id, projects_pk, topics_pk, viewpoints_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_bitmap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 

### Return type

[**Bitmap**](Bitmap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bitmaps**
> list[Bitmap] get_bitmaps(projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_response = api_instance.get_bitmaps(projects_pk, topics_pk, viewpoints_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_bitmaps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 

### Return type

[**list[Bitmap]**](Bitmap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coloring**
> Coloring get_coloring(id, projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
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
 **id** | **str**|  | 
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
> Comment get_comment(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_comment(id, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **get_comment_event**
> CommentEvent get_comment_event(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_comment_event(id, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_comment_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment_event_0**
> CommentEvent get_comment_event_0(comments_pk, id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
comments_pk = 'comments_pk_example' # str | 
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_comment_event_0(comments_pk, id, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_comment_event_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments_pk** | **str**|  | 
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment_events**
> list[CommentEvent] get_comment_events(projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_comment_events(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_comment_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[CommentEvent]**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment_events_0**
> list[CommentEvent] get_comment_events_0(comments_pk, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
comments_pk = 'comments_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_comment_events_0(comments_pk, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_comment_events_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[CommentEvent]**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments**
> list[Comment] get_comments(projects_pk, topics_pk)



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

# **get_document_reference**
> DocumentReference get_document_reference(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_document_reference(id, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_document_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**DocumentReference**](DocumentReference.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_references**
> list[DocumentReference] get_document_references(projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_document_references(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_document_references: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[DocumentReference]**](DocumentReference.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extensions**
> list[Extensions] get_extensions(projects_pk)



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

[**list[Extensions]**](Extensions.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> BimSnippet get_file(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_file(id, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files**
> list[BimSnippet] get_files(projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_files(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[BimSnippet]**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_related_topic**
> RelatedTopic get_related_topic(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_related_topic(id, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_related_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**RelatedTopic**](RelatedTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_related_topics**
> list[RelatedTopic] get_related_topics(projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_related_topics(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_related_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[RelatedTopic]**](RelatedTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_selection**
> Component get_selection(id, projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
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
 **id** | **str**|  | 
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

# **get_snapshots**
> list[Snapshot] get_snapshots(projects_pk, topics_pk, viewpoints_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 

try:
    api_response = api_instance.get_snapshots(projects_pk, topics_pk, viewpoints_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 

### Return type

[**list[Snapshot]**](Snapshot.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippet**
> BimSnippet get_snippet(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_snippet(id, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_snippet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snippets**
> list[BimSnippet] get_snippets(projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_snippets(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_snippets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[BimSnippet]**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic**
> Topic get_topic(id, projects_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 

try:
    api_response = api_instance.get_topic(id, projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 

### Return type

[**Topic**](Topic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_event**
> TopicEvents get_topic_event(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_topic_event(id, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topic_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**TopicEvents**](TopicEvents.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_events**
> list[TopicEvents] get_topic_events(projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_topic_events(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topic_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[TopicEvents]**](TopicEvents.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topics**
> list[Topic] get_topics(projects_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
projects_pk = 'projects_pk_example' # str | 

try:
    api_response = api_instance.get_topics(projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 

### Return type

[**list[Topic]**](Topic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_viewpoint**
> Viewpoint get_viewpoint(id, projects_pk, topics_pk)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.get_viewpoint(id, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->get_viewpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
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
 **id** | **str**|  | 
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

# **update_bcf_document**
> update_bcf_document(id, projects_pk, guid=guid, filename=filename)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
guid = 'guid_example' # str |  (optional)
filename = 'filename_example' # str |  (optional)

try:
    api_instance.update_bcf_document(id, projects_pk, guid=guid, filename=filename)
except ApiException as e:
    print("Exception when calling BcfApi->update_bcf_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **guid** | [**str**](str.md)|  | [optional] 
 **filename** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bcf_project**
> BcfProject update_bcf_project(id, bcf_project)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
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
 **id** | **str**|  | 
 **bcf_project** | [**BcfProject**](BcfProject.md)|  | 

### Return type

[**BcfProject**](BcfProject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bitmap**
> Bitmap update_bitmap(id, projects_pk, topics_pk, viewpoints_pk, bitmap)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoints_pk = 'viewpoints_pk_example' # str | 
bitmap = bimdata_api_client.Bitmap() # Bitmap | 

try:
    api_response = api_instance.update_bitmap(id, projects_pk, topics_pk, viewpoints_pk, bitmap)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_bitmap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **viewpoints_pk** | **str**|  | 
 **bitmap** | [**Bitmap**](Bitmap.md)|  | 

### Return type

[**Bitmap**](Bitmap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coloring**
> Coloring update_coloring(id, projects_pk, topics_pk, viewpoints_pk, coloring)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
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
 **id** | **str**|  | 
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
> Comment update_comment(id, projects_pk, topics_pk, comment)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
comment = bimdata_api_client.Comment() # Comment | 

try:
    api_response = api_instance.update_comment(id, projects_pk, topics_pk, comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **update_comment_event**
> CommentEvent update_comment_event(id, projects_pk, topics_pk, comment_event)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
comment_event = bimdata_api_client.CommentEvent() # CommentEvent | 

try:
    api_response = api_instance.update_comment_event(id, projects_pk, topics_pk, comment_event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_comment_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **comment_event** | [**CommentEvent**](CommentEvent.md)|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment_event_0**
> CommentEvent update_comment_event_0(comments_pk, id, projects_pk, topics_pk, comment_event)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
comments_pk = 'comments_pk_example' # str | 
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
comment_event = bimdata_api_client.CommentEvent() # CommentEvent | 

try:
    api_response = api_instance.update_comment_event_0(comments_pk, id, projects_pk, topics_pk, comment_event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_comment_event_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments_pk** | **str**|  | 
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **comment_event** | [**CommentEvent**](CommentEvent.md)|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document_reference**
> DocumentReference update_document_reference(id, projects_pk, topics_pk, document_reference)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
document_reference = bimdata_api_client.DocumentReference() # DocumentReference | 

try:
    api_response = api_instance.update_document_reference(id, projects_pk, topics_pk, document_reference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_document_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **document_reference** | [**DocumentReference**](DocumentReference.md)|  | 

### Return type

[**DocumentReference**](DocumentReference.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file**
> BimSnippet update_file(id, projects_pk, topics_pk, bim_snippet)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
bim_snippet = bimdata_api_client.BimSnippet() # BimSnippet | 

try:
    api_response = api_instance.update_file(id, projects_pk, topics_pk, bim_snippet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **bim_snippet** | [**BimSnippet**](BimSnippet.md)|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_related_topic**
> RelatedTopic update_related_topic(id, projects_pk, topics_pk, related_topic)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
related_topic = bimdata_api_client.RelatedTopic() # RelatedTopic | 

try:
    api_response = api_instance.update_related_topic(id, projects_pk, topics_pk, related_topic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_related_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **related_topic** | [**RelatedTopic**](RelatedTopic.md)|  | 

### Return type

[**RelatedTopic**](RelatedTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_selection**
> Component update_selection(id, projects_pk, topics_pk, viewpoints_pk, component)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
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
 **id** | **str**|  | 
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

# **update_snippet**
> BimSnippet update_snippet(id, projects_pk, topics_pk, bim_snippet)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
bim_snippet = bimdata_api_client.BimSnippet() # BimSnippet | 

try:
    api_response = api_instance.update_snippet(id, projects_pk, topics_pk, bim_snippet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_snippet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **bim_snippet** | [**BimSnippet**](BimSnippet.md)|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_topic**
> Topic update_topic(id, projects_pk, topic)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topic = bimdata_api_client.Topic() # Topic | 

try:
    api_response = api_instance.update_topic(id, projects_pk, topic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **update_topic_event**
> TopicEvents update_topic_event(id, projects_pk, topics_pk, topic_events)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
topic_events = bimdata_api_client.TopicEvents() # TopicEvents | 

try:
    api_response = api_instance.update_topic_event(id, projects_pk, topics_pk, topic_events)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_topic_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **topic_events** | [**TopicEvents**](TopicEvents.md)|  | 

### Return type

[**TopicEvents**](TopicEvents.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_viewpoint**
> Viewpoint update_viewpoint(id, projects_pk, topics_pk, viewpoint)



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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
viewpoint = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    api_response = api_instance.update_viewpoint(id, projects_pk, topics_pk, viewpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->update_viewpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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
api_instance = bimdata_api_client.BcfApi(bimdata_api_client.ApiClient(configuration))
id = 'id_example' # str | 
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
 **id** | **str**|  | 
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

