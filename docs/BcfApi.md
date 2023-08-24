# bimdata_api_client.BcfApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_comment**](BcfApi.md#create_comment) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/comments | Create a comment
[**create_extension_label**](BcfApi.md#create_extension_label) | **POST** /bcf/2.1/projects/{projects_pk}/extension/label | Create a Label
[**create_extension_priority**](BcfApi.md#create_extension_priority) | **POST** /bcf/2.1/projects/{projects_pk}/extension/priority | Create a Priority
[**create_extension_stage**](BcfApi.md#create_extension_stage) | **POST** /bcf/2.1/projects/{projects_pk}/extension/stage | Create a Stage
[**create_extension_status**](BcfApi.md#create_extension_status) | **POST** /bcf/2.1/projects/{projects_pk}/extension/status | Create a TopicStatus
[**create_extension_type**](BcfApi.md#create_extension_type) | **POST** /bcf/2.1/projects/{projects_pk}/extension/type | Create a TopicType
[**create_full_topic**](BcfApi.md#create_full_topic) | **POST** /bcf/2.1/projects/{projects_pk}/full-topic | Create a Topic with viewpoints and comments
[**create_pin**](BcfApi.md#create_pin) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{viewpoints_guid}/pin | Create a Pin
[**create_topic**](BcfApi.md#create_topic) | **POST** /bcf/2.1/projects/{projects_pk}/topics | Create a topic
[**create_viewpoint**](BcfApi.md#create_viewpoint) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints | Create a Viewpoint
[**delete_comment**](BcfApi.md#delete_comment) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/comments/{guid} | Delete a comment
[**delete_extension_label**](BcfApi.md#delete_extension_label) | **DELETE** /bcf/2.1/projects/{projects_pk}/extension/label/{id} | Delete a Label
[**delete_extension_priority**](BcfApi.md#delete_extension_priority) | **DELETE** /bcf/2.1/projects/{projects_pk}/extension/priority/{id} | Delete a Priority
[**delete_extension_stage**](BcfApi.md#delete_extension_stage) | **DELETE** /bcf/2.1/projects/{projects_pk}/extension/stage/{id} | Delete a Stage
[**delete_extension_status**](BcfApi.md#delete_extension_status) | **DELETE** /bcf/2.1/projects/{projects_pk}/extension/status/{id} | Delete a TopicStatus
[**delete_extension_type**](BcfApi.md#delete_extension_type) | **DELETE** /bcf/2.1/projects/{projects_pk}/extension/type/{id} | Delete a TopicType
[**delete_pin**](BcfApi.md#delete_pin) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{viewpoints_guid}/pin/{guid} | Delete a Pin
[**delete_topic**](BcfApi.md#delete_topic) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{guid} | Delete a topic
[**delete_viewpoint**](BcfApi.md#delete_viewpoint) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid} | Delete a Viewpoint
[**download_bcf_export**](BcfApi.md#download_bcf_export) | **GET** /bcf/2.1/projects/{id}/export | Export project&#39;s topics in bcf-xml format
[**full_update_bcf_project**](BcfApi.md#full_update_bcf_project) | **PUT** /bcf/2.1/projects/{id} | Update all fields of a BCF project
[**full_update_comment**](BcfApi.md#full_update_comment) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/comments/{guid} | Update all fields of a comment
[**full_update_full_topic**](BcfApi.md#full_update_full_topic) | **PUT** /bcf/2.1/projects/{projects_pk}/full-topic/{guid} | Update all fields of a topic
[**full_update_pin**](BcfApi.md#full_update_pin) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{viewpoints_guid}/pin/{guid} | Update all fields of a Pin
[**full_update_topic**](BcfApi.md#full_update_topic) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{guid} | Update all fields of a topic
[**full_update_viewpoint**](BcfApi.md#full_update_viewpoint) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid} | Update all fields of a Viewpoint
[**get_auth**](BcfApi.md#get_auth) | **GET** /bcf/2.1/auth | Retrieve Authentication Information
[**get_bcf_project**](BcfApi.md#get_bcf_project) | **GET** /bcf/2.1/projects/{id} | Retrieve a BCF project
[**get_bcf_projects**](BcfApi.md#get_bcf_projects) | **GET** /bcf/2.1/projects | Retrieve all BCF projects
[**get_colorings**](BcfApi.md#get_colorings) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid}/coloring | Retrieve all colorings of a viewpoint
[**get_comment**](BcfApi.md#get_comment) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/comments/{guid} | Retrieve a comment
[**get_comments**](BcfApi.md#get_comments) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/comments | Retrieve all comments
[**get_detailed_extensions**](BcfApi.md#get_detailed_extensions) | **GET** /bcf/2.1/projects/{id}/detailed-extensions | Retrieve project detailed extensions
[**get_extensions**](BcfApi.md#get_extensions) | **GET** /bcf/2.1/projects/{id}/extensions | Retrieve project extensions
[**get_full_topic**](BcfApi.md#get_full_topic) | **GET** /bcf/2.1/projects/{projects_pk}/full-topic/{guid} | Retrieve a full topic
[**get_full_topics**](BcfApi.md#get_full_topics) | **GET** /bcf/2.1/projects/{projects_pk}/full-topic | Retrieve all full topics
[**get_pins**](BcfApi.md#get_pins) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{viewpoints_guid}/pin | Retrieve all Pins of a viewpoint
[**get_related_topics**](BcfApi.md#get_related_topics) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{guid}/related_topics | Get all related topics
[**get_selections**](BcfApi.md#get_selections) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid}/selection | Retrieve all selections of a viewpoint
[**get_snapshot**](BcfApi.md#get_snapshot) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid}/snapshot | Retrieve the viewpoint&#39; snapshot
[**get_topic**](BcfApi.md#get_topic) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{guid} | Retrieve a topic
[**get_topic_document_references**](BcfApi.md#get_topic_document_references) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{guid}/document_references | Get all related documents
[**get_topic_viewpoints**](BcfApi.md#get_topic_viewpoints) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/topic-viewpoints | Retrieve all viewpoints attached to the topic
[**get_topics**](BcfApi.md#get_topics) | **GET** /bcf/2.1/projects/{projects_pk}/topics | Retrieve all topics
[**get_user**](BcfApi.md#get_user) | **GET** /bcf/2.1/current-user | Get current user info
[**get_versions**](BcfApi.md#get_versions) | **GET** /bcf/versions | Retrieve all supported BCF versions by this API
[**get_viewpoin_pin**](BcfApi.md#get_viewpoin_pin) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{viewpoints_guid}/pin/{guid} | Retrieve a Pin
[**get_viewpoint**](BcfApi.md#get_viewpoint) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid} | Retrieve a Viewpoint
[**get_viewpoints**](BcfApi.md#get_viewpoints) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints | Retrieve all Viewpoints of a topic
[**get_visibilities**](BcfApi.md#get_visibilities) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid}/visibility | Retrieve all visibilities of a viewpoint
[**import_bcf**](BcfApi.md#import_bcf) | **POST** /bcf/2.1/projects/{id}/import | Import bcf-xml format into this project
[**update_bcf_project**](BcfApi.md#update_bcf_project) | **PATCH** /bcf/2.1/projects/{id} | Update some fields of a BCF project
[**update_comment**](BcfApi.md#update_comment) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/comments/{guid} | Update some fields of a comment
[**update_extension_label**](BcfApi.md#update_extension_label) | **PATCH** /bcf/2.1/projects/{projects_pk}/extension/label/{id} | Update a Label
[**update_extension_priority**](BcfApi.md#update_extension_priority) | **PATCH** /bcf/2.1/projects/{projects_pk}/extension/priority/{id} | Update a Priority
[**update_extension_stage**](BcfApi.md#update_extension_stage) | **PATCH** /bcf/2.1/projects/{projects_pk}/extension/stage/{id} | Update a Stage
[**update_extension_status**](BcfApi.md#update_extension_status) | **PATCH** /bcf/2.1/projects/{projects_pk}/extension/status/{id} | Update a TopicStatus
[**update_extension_type**](BcfApi.md#update_extension_type) | **PATCH** /bcf/2.1/projects/{projects_pk}/extension/type/{id} | Update a TopicType
[**update_full_topic**](BcfApi.md#update_full_topic) | **PATCH** /bcf/2.1/projects/{projects_pk}/full-topic/{guid} | Update some fields of a topic
[**update_pin**](BcfApi.md#update_pin) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{viewpoints_guid}/pin/{guid} | Update some fields of a Pin
[**update_topic**](BcfApi.md#update_topic) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{guid} | Update some fields of a topic
[**update_viewpoint**](BcfApi.md#update_viewpoint) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_guid}/viewpoints/{guid} | Update some fields of a Viewpoint


# **create_comment**
> Comment create_comment(projects_pk, topics_guid)

Create a comment

Create a comment  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.comment_request import CommentRequest
from bimdata_api_client.model.comment import Comment
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | A unique integer value identifying this project.
    topics_guid = "topics_guid_example" # str | 
    comment_request = CommentRequest(
        guid="guid_example",
        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        author="author_example",
        comment="comment_example",
        viewpoint_guid="viewpoint_guid_example",
        reply_to_comment_guid="reply_to_comment_guid_example",
        modified_author="modified_author_example",
        viewpoint_temp_id=1,
    ) # CommentRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a comment
        api_response = api_instance.create_comment(projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->create_comment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a comment
        api_response = api_instance.create_comment(projects_pk, topics_guid, comment_request=comment_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->create_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**| A unique integer value identifying this project. |
 **topics_guid** | **str**|  |
 **comment_request** | [**CommentRequest**](CommentRequest.md)|  | [optional]

### Return type

[**Comment**](Comment.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **create_extension_label**
> Label create_extension_label(projects_pk, label_request)

Create a Label

This is not a standard route. Create a Label available for the project  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.label_request import LabelRequest
from bimdata_api_client.model.label import Label
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | 
    label_request = LabelRequest(
        label="label_example",
        project=1,
    ) # LabelRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Label
        api_response = api_instance.create_extension_label(projects_pk, label_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->create_extension_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**|  |
 **label_request** | [**LabelRequest**](LabelRequest.md)|  |

### Return type

[**Label**](Label.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **create_extension_priority**
> Priority create_extension_priority(projects_pk, priority_request)

Create a Priority

This is not a standard route. Create a Priority available for the project  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.priority import Priority
from bimdata_api_client.model.priority_request import PriorityRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | 
    priority_request = PriorityRequest(
        priority="priority_example",
        color="color_example",
        project=1,
    ) # PriorityRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Priority
        api_response = api_instance.create_extension_priority(projects_pk, priority_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->create_extension_priority: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**|  |
 **priority_request** | [**PriorityRequest**](PriorityRequest.md)|  |

### Return type

[**Priority**](Priority.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **create_extension_stage**
> Stage create_extension_stage(projects_pk, stage_request)

Create a Stage

This is not a standard route. Create a Stage available for the project  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.stage_request import StageRequest
from bimdata_api_client.model.stage import Stage
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | 
    stage_request = StageRequest(
        stage="stage_example",
        project=1,
    ) # StageRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Stage
        api_response = api_instance.create_extension_stage(projects_pk, stage_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->create_extension_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**|  |
 **stage_request** | [**StageRequest**](StageRequest.md)|  |

### Return type

[**Stage**](Stage.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **create_extension_status**
> TopicStatus create_extension_status(projects_pk, topic_status_request)

Create a TopicStatus

This is not a standard route. Create a TopicStatus available for the project  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.topic_status_request import TopicStatusRequest
from bimdata_api_client.model.topic_status import TopicStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | 
    topic_status_request = TopicStatusRequest(
        topic_status="topic_status_example",
        color="color_example",
        project=1,
    ) # TopicStatusRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a TopicStatus
        api_response = api_instance.create_extension_status(projects_pk, topic_status_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->create_extension_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**|  |
 **topic_status_request** | [**TopicStatusRequest**](TopicStatusRequest.md)|  |

### Return type

[**TopicStatus**](TopicStatus.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **create_extension_type**
> TopicType create_extension_type(projects_pk, topic_type_request)

Create a TopicType

This is not a standard route. Create a TopicType available for the project  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.topic_type import TopicType
from bimdata_api_client.model.topic_type_request import TopicTypeRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | 
    topic_type_request = TopicTypeRequest(
        topic_type="topic_type_example",
        project=1,
    ) # TopicTypeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a TopicType
        api_response = api_instance.create_extension_type(projects_pk, topic_type_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->create_extension_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**|  |
 **topic_type_request** | [**TopicTypeRequest**](TopicTypeRequest.md)|  |

### Return type

[**TopicType**](TopicType.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
> FullTopic create_full_topic(projects_pk, full_topic_request)

Create a Topic with viewpoints and comments

This is not a standard route. You can send a topic, viewpoints and comments in a single call  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.full_topic_request import FullTopicRequest
from bimdata_api_client.model.full_topic import FullTopic
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | 
    full_topic_request = FullTopicRequest(
        guid="guid_example",
        creation_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        creation_author="creation_author_example",
        modified_author="modified_author_example",
        title="title_example",
        description="description_example",
        reference_links=[
            "reference_links_example",
        ],
        ifcs=[
            1,
        ],
        models=[
            1,
        ],
        labels=[
            "labels_example",
        ],
        topic_type="topic_type_example",
        topic_status="topic_status_example",
        stage="stage_example",
        priority="priority_example",
        index=0,
        assigned_to="assigned_to_example",
        format="format_example",
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        comments=[
            CommentRequest(
                guid="guid_example",
                date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                author="author_example",
                comment="comment_example",
                viewpoint_guid="viewpoint_guid_example",
                reply_to_comment_guid="reply_to_comment_guid_example",
                modified_author="modified_author_example",
                viewpoint_temp_id=1,
            ),
        ],
        viewpoints=[
            ViewpointRequest(
                index=0,
                guid="guid_example",
                originating_system="originating_system_example",
                authoring_tool_id="authoring_tool_id_example",
                orthogonal_camera=None,
                perspective_camera=None,
                lines=[
                    LineRequest(
                        end_point=PointRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                        start_point=PointRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                    ),
                ],
                clipping_planes=[
                    ClippingPlaneRequest(
                        location=PointRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                        direction=DirectionRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                    ),
                ],
                snapshot=None,
                components=None,
                pins=[
                    PinRequest(
                        guid="guid_example",
                        name="name_example",
                        color="color_example",
                        point=GeometryPointRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                        index=0,
                    ),
                ],
                temp_id=1,
            ),
        ],
        project=1,
    ) # FullTopicRequest | 
    img_format = "url" # str | All snapshot_data will be returned as url instead of base64 (optional) if omitted the server will use the default value of "url"

    # example passing only required values which don't have defaults set
    try:
        # Create a Topic with viewpoints and comments
        api_response = api_instance.create_full_topic(projects_pk, full_topic_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->create_full_topic: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Topic with viewpoints and comments
        api_response = api_instance.create_full_topic(projects_pk, full_topic_request, img_format=img_format)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->create_full_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**|  |
 **full_topic_request** | [**FullTopicRequest**](FullTopicRequest.md)|  |
 **img_format** | **str**| All snapshot_data will be returned as url instead of base64 | [optional] if omitted the server will use the default value of "url"

### Return type

[**FullTopic**](FullTopic.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **create_pin**
> Pin create_pin(projects_pk, topics_guid, viewpoints_guid, pin_request)

Create a Pin

This is not a standard route. Create a Pin  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.pin import Pin
from bimdata_api_client.model.pin_request import PinRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 
    viewpoints_guid = "viewpoints_guid_example" # str | 
    pin_request = PinRequest(
        guid="guid_example",
        name="name_example",
        color="color_example",
        point=GeometryPointRequest(
            x=3.14,
            y=3.14,
            z=3.14,
        ),
        index=0,
    ) # PinRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Pin
        api_response = api_instance.create_pin(projects_pk, topics_guid, viewpoints_guid, pin_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->create_pin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |
 **viewpoints_guid** | **str**|  |
 **pin_request** | [**PinRequest**](PinRequest.md)|  |

### Return type

[**Pin**](Pin.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
> Topic create_topic(projects_pk, topic_request)

Create a topic

Create a topic  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.topic_request import TopicRequest
from bimdata_api_client.model.topic import Topic
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | 
    topic_request = TopicRequest(
        guid="guid_example",
        topic_type="topic_type_example",
        topic_status="topic_status_example",
        title="title_example",
        priority="priority_example",
        labels=[
            "labels_example",
        ],
        creation_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        creation_author="creation_author_example",
        modified_author="modified_author_example",
        assigned_to="assigned_to_example",
        reference_links=[
            "reference_links_example",
        ],
        stage="stage_example",
        description="description_example",
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ifcs=[
            1,
        ],
        models=[
            1,
        ],
        format="format_example",
        index=0,
        project=1,
    ) # TopicRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a topic
        api_response = api_instance.create_topic(projects_pk, topic_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->create_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**|  |
 **topic_request** | [**TopicRequest**](TopicRequest.md)|  |

### Return type

[**Topic**](Topic.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
> Viewpoint create_viewpoint(projects_pk, topics_guid)

Create a Viewpoint

Create a Viewpoint  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.viewpoint_request import ViewpointRequest
from bimdata_api_client.model.viewpoint import Viewpoint
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 
    img_format = "url" # str | All snapshot_data will be returned as url instead of base64 (optional) if omitted the server will use the default value of "url"
    viewpoint_request = ViewpointRequest(
        index=0,
        guid="guid_example",
        originating_system="originating_system_example",
        authoring_tool_id="authoring_tool_id_example",
        orthogonal_camera=None,
        perspective_camera=None,
        lines=[
            LineRequest(
                end_point=PointRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
                start_point=PointRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
            ),
        ],
        clipping_planes=[
            ClippingPlaneRequest(
                location=PointRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
                direction=DirectionRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
            ),
        ],
        snapshot=None,
        components=None,
        pins=[
            PinRequest(
                guid="guid_example",
                name="name_example",
                color="color_example",
                point=GeometryPointRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
                index=0,
            ),
        ],
        temp_id=1,
    ) # ViewpointRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Viewpoint
        api_response = api_instance.create_viewpoint(projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->create_viewpoint: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Viewpoint
        api_response = api_instance.create_viewpoint(projects_pk, topics_guid, img_format=img_format, viewpoint_request=viewpoint_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->create_viewpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |
 **img_format** | **str**| All snapshot_data will be returned as url instead of base64 | [optional] if omitted the server will use the default value of "url"
 **viewpoint_request** | [**ViewpointRequest**](ViewpointRequest.md)|  | [optional]

### Return type

[**Viewpoint**](Viewpoint.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

Delete a comment  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | A unique integer value identifying this project.
    topics_guid = "topics_guid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a comment
        api_instance.delete_comment(guid, projects_pk, topics_guid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->delete_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**| A unique integer value identifying this project. |
 **topics_guid** | **str**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_extension_label**
> delete_extension_label(id, projects_pk)

Delete a Label

This is not a standard route. Delete a Label. Topics using this label won't be deleted   Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this label.
    projects_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a Label
        api_instance.delete_extension_label(id, projects_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->delete_extension_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this label. |
 **projects_pk** | **int**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_extension_priority**
> delete_extension_priority(id, projects_pk)

Delete a Priority

This is not a standard route. Delete a Priority. Topics using this priority won't be deleted   Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this priority.
    projects_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a Priority
        api_instance.delete_extension_priority(id, projects_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->delete_extension_priority: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this priority. |
 **projects_pk** | **int**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_extension_stage**
> delete_extension_stage(id, projects_pk)

Delete a Stage

This is not a standard route. Delete a Stage. Topics using this stage won't be deleted   Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this stage.
    projects_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a Stage
        api_instance.delete_extension_stage(id, projects_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->delete_extension_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this stage. |
 **projects_pk** | **int**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_extension_status**
> delete_extension_status(id, projects_pk)

Delete a TopicStatus

This is not a standard route. Delete a TopicStatus. Topics using this status won't be deleted   Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this topic status.
    projects_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a TopicStatus
        api_instance.delete_extension_status(id, projects_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->delete_extension_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this topic status. |
 **projects_pk** | **int**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_extension_type**
> delete_extension_type(id, projects_pk)

Delete a TopicType

This is not a standard route. Delete a TopicType. Topics using this type won't be deleted  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this topic type.
    projects_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a TopicType
        api_instance.delete_extension_type(id, projects_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->delete_extension_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this topic type. |
 **projects_pk** | **int**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pin**
> delete_pin(guid, projects_pk, topics_guid, viewpoints_guid)

Delete a Pin

This is not a standard route. Delete a Pin  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 
    viewpoints_guid = "viewpoints_guid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a Pin
        api_instance.delete_pin(guid, projects_pk, topics_guid, viewpoints_guid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->delete_pin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |
 **viewpoints_guid** | **str**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topic**
> delete_topic(guid, projects_pk)

Delete a topic

Delete a topic  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a topic
        api_instance.delete_topic(guid, projects_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->delete_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_viewpoint**
> delete_viewpoint(guid, projects_pk, topics_guid)

Delete a Viewpoint

This is not a standard route. Delete a Viewpoint  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 
    img_format = "url" # str | All snapshot_data will be returned as url instead of base64 (optional) if omitted the server will use the default value of "url"

    # example passing only required values which don't have defaults set
    try:
        # Delete a Viewpoint
        api_instance.delete_viewpoint(guid, projects_pk, topics_guid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->delete_viewpoint: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a Viewpoint
        api_instance.delete_viewpoint(guid, projects_pk, topics_guid, img_format=img_format)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->delete_viewpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |
 **img_format** | **str**| All snapshot_data will be returned as url instead of base64 | [optional] if omitted the server will use the default value of "url"

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_bcf_export**
> file_type download_bcf_export(id)

Export project's topics in bcf-xml format

This is not a standard route. Export project's topics in bcf-xml format  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this project.
    format = "format_example" # str | topic format to export, comma separated. Default = standard (optional)
    topics = "topics_example" # str | topic guids to export, comma separated. Default = all (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export project's topics in bcf-xml format
        api_response = api_instance.download_bcf_export(id)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->download_bcf_export: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export project's topics in bcf-xml format
        api_response = api_instance.download_bcf_export(id, format=format, topics=topics)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->download_bcf_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this project. |
 **format** | **str**| topic format to export, comma separated. Default &#x3D; standard | [optional]
 **topics** | **str**| topic guids to export, comma separated. Default &#x3D; all | [optional]

### Return type

**file_type**

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bcf-xml file |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_bcf_project**
> BcfProject full_update_bcf_project(id, bcf_project_request)

Update all fields of a BCF project

Update all fields of a BCF project  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.bcf_project_request import BcfProjectRequest
from bimdata_api_client.model.bcf_project import BcfProject
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this project.
    bcf_project_request = BcfProjectRequest(
        name="name_example",
    ) # BcfProjectRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update all fields of a BCF project
        api_response = api_instance.full_update_bcf_project(id, bcf_project_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->full_update_bcf_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this project. |
 **bcf_project_request** | [**BcfProjectRequest**](BcfProjectRequest.md)|  |

### Return type

[**BcfProject**](BcfProject.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
> Comment full_update_comment(guid, projects_pk, topics_guid)

Update all fields of a comment

Update all fields of a comment  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.comment_request import CommentRequest
from bimdata_api_client.model.comment import Comment
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | A unique integer value identifying this project.
    topics_guid = "topics_guid_example" # str | 
    comment_request = CommentRequest(
        guid="guid_example",
        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        author="author_example",
        comment="comment_example",
        viewpoint_guid="viewpoint_guid_example",
        reply_to_comment_guid="reply_to_comment_guid_example",
        modified_author="modified_author_example",
        viewpoint_temp_id=1,
    ) # CommentRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update all fields of a comment
        api_response = api_instance.full_update_comment(guid, projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->full_update_comment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update all fields of a comment
        api_response = api_instance.full_update_comment(guid, projects_pk, topics_guid, comment_request=comment_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->full_update_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**| A unique integer value identifying this project. |
 **topics_guid** | **str**|  |
 **comment_request** | [**CommentRequest**](CommentRequest.md)|  | [optional]

### Return type

[**Comment**](Comment.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
> FullTopic full_update_full_topic(guid, projects_pk, full_topic_request)

Update all fields of a topic

This is not a standard route. You can update topic, viewpoints and comment is a signle call  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.full_topic_request import FullTopicRequest
from bimdata_api_client.model.full_topic import FullTopic
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    full_topic_request = FullTopicRequest(
        guid="guid_example",
        creation_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        creation_author="creation_author_example",
        modified_author="modified_author_example",
        title="title_example",
        description="description_example",
        reference_links=[
            "reference_links_example",
        ],
        ifcs=[
            1,
        ],
        models=[
            1,
        ],
        labels=[
            "labels_example",
        ],
        topic_type="topic_type_example",
        topic_status="topic_status_example",
        stage="stage_example",
        priority="priority_example",
        index=0,
        assigned_to="assigned_to_example",
        format="format_example",
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        comments=[
            CommentRequest(
                guid="guid_example",
                date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                author="author_example",
                comment="comment_example",
                viewpoint_guid="viewpoint_guid_example",
                reply_to_comment_guid="reply_to_comment_guid_example",
                modified_author="modified_author_example",
                viewpoint_temp_id=1,
            ),
        ],
        viewpoints=[
            ViewpointRequest(
                index=0,
                guid="guid_example",
                originating_system="originating_system_example",
                authoring_tool_id="authoring_tool_id_example",
                orthogonal_camera=None,
                perspective_camera=None,
                lines=[
                    LineRequest(
                        end_point=PointRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                        start_point=PointRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                    ),
                ],
                clipping_planes=[
                    ClippingPlaneRequest(
                        location=PointRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                        direction=DirectionRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                    ),
                ],
                snapshot=None,
                components=None,
                pins=[
                    PinRequest(
                        guid="guid_example",
                        name="name_example",
                        color="color_example",
                        point=GeometryPointRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                        index=0,
                    ),
                ],
                temp_id=1,
            ),
        ],
        project=1,
    ) # FullTopicRequest | 
    img_format = "url" # str | All snapshot_data will be returned as url instead of base64 (optional) if omitted the server will use the default value of "url"

    # example passing only required values which don't have defaults set
    try:
        # Update all fields of a topic
        api_response = api_instance.full_update_full_topic(guid, projects_pk, full_topic_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->full_update_full_topic: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update all fields of a topic
        api_response = api_instance.full_update_full_topic(guid, projects_pk, full_topic_request, img_format=img_format)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->full_update_full_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **full_topic_request** | [**FullTopicRequest**](FullTopicRequest.md)|  |
 **img_format** | **str**| All snapshot_data will be returned as url instead of base64 | [optional] if omitted the server will use the default value of "url"

### Return type

[**FullTopic**](FullTopic.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **full_update_pin**
> Pin full_update_pin(guid, projects_pk, topics_guid, viewpoints_guid, pin_request)

Update all fields of a Pin

This is not a standard route. Update all fields of a Pin  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.pin import Pin
from bimdata_api_client.model.pin_request import PinRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 
    viewpoints_guid = "viewpoints_guid_example" # str | 
    pin_request = PinRequest(
        guid="guid_example",
        name="name_example",
        color="color_example",
        point=GeometryPointRequest(
            x=3.14,
            y=3.14,
            z=3.14,
        ),
        index=0,
    ) # PinRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update all fields of a Pin
        api_response = api_instance.full_update_pin(guid, projects_pk, topics_guid, viewpoints_guid, pin_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->full_update_pin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |
 **viewpoints_guid** | **str**|  |
 **pin_request** | [**PinRequest**](PinRequest.md)|  |

### Return type

[**Pin**](Pin.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
> Topic full_update_topic(guid, projects_pk, topic_request)

Update all fields of a topic

Update all fields of a topic  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.topic_request import TopicRequest
from bimdata_api_client.model.topic import Topic
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    topic_request = TopicRequest(
        guid="guid_example",
        topic_type="topic_type_example",
        topic_status="topic_status_example",
        title="title_example",
        priority="priority_example",
        labels=[
            "labels_example",
        ],
        creation_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        creation_author="creation_author_example",
        modified_author="modified_author_example",
        assigned_to="assigned_to_example",
        reference_links=[
            "reference_links_example",
        ],
        stage="stage_example",
        description="description_example",
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ifcs=[
            1,
        ],
        models=[
            1,
        ],
        format="format_example",
        index=0,
        project=1,
    ) # TopicRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update all fields of a topic
        api_response = api_instance.full_update_topic(guid, projects_pk, topic_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->full_update_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **topic_request** | [**TopicRequest**](TopicRequest.md)|  |

### Return type

[**Topic**](Topic.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
> Viewpoint full_update_viewpoint(guid, projects_pk, topics_guid)

Update all fields of a Viewpoint

This is not a standard route. Update all fields of a Viewpoint  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.viewpoint_request import ViewpointRequest
from bimdata_api_client.model.viewpoint import Viewpoint
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 
    img_format = "url" # str | All snapshot_data will be returned as url instead of base64 (optional) if omitted the server will use the default value of "url"
    viewpoint_request = ViewpointRequest(
        index=0,
        guid="guid_example",
        originating_system="originating_system_example",
        authoring_tool_id="authoring_tool_id_example",
        orthogonal_camera=None,
        perspective_camera=None,
        lines=[
            LineRequest(
                end_point=PointRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
                start_point=PointRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
            ),
        ],
        clipping_planes=[
            ClippingPlaneRequest(
                location=PointRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
                direction=DirectionRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
            ),
        ],
        snapshot=None,
        components=None,
        pins=[
            PinRequest(
                guid="guid_example",
                name="name_example",
                color="color_example",
                point=GeometryPointRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
                index=0,
            ),
        ],
        temp_id=1,
    ) # ViewpointRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update all fields of a Viewpoint
        api_response = api_instance.full_update_viewpoint(guid, projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->full_update_viewpoint: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update all fields of a Viewpoint
        api_response = api_instance.full_update_viewpoint(guid, projects_pk, topics_guid, img_format=img_format, viewpoint_request=viewpoint_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->full_update_viewpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |
 **img_format** | **str**| All snapshot_data will be returned as url instead of base64 | [optional] if omitted the server will use the default value of "url"
 **viewpoint_request** | [**ViewpointRequest**](ViewpointRequest.md)|  | [optional]

### Return type

[**Viewpoint**](Viewpoint.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **get_auth**
> [Auth] get_auth()

Retrieve Authentication Information

oauth2_dynamic_client_reg_url is not supported, http_basic_supported is always set to false, 

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.auth import Auth
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve Authentication Information
        api_response = api_instance.get_auth()
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_auth: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Auth]**](Auth.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bcf_project**
> BcfProject get_bcf_project(id)

Retrieve a BCF project

Retrieve a BCF project  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.bcf_project import BcfProject
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a BCF project
        api_response = api_instance.get_bcf_project(id)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_bcf_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this project. |

### Return type

[**BcfProject**](BcfProject.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bcf_projects**
> [BcfProject] get_bcf_projects()

Retrieve all BCF projects

Retrieve all BCF projects  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.bcf_project import BcfProject
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve all BCF projects
        api_response = api_instance.get_bcf_projects()
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_bcf_projects: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[BcfProject]**](BcfProject.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_colorings**
> [Coloring] get_colorings(guid, projects_pk, topics_guid)

Retrieve all colorings of a viewpoint

Retrieve all colorings of a viewpoint  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.coloring import Coloring
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all colorings of a viewpoint
        api_response = api_instance.get_colorings(guid, projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_colorings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |

### Return type

[**[Coloring]**](Coloring.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> Comment get_comment(guid, projects_pk, topics_guid)

Retrieve a comment

Retrieve a comment  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.comment import Comment
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | A unique integer value identifying this project.
    topics_guid = "topics_guid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a comment
        api_response = api_instance.get_comment(guid, projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**| A unique integer value identifying this project. |
 **topics_guid** | **str**|  |

### Return type

[**Comment**](Comment.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments**
> [Comment] get_comments(projects_pk, topics_guid)

Retrieve all comments

Retrieve all comments  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.comment import Comment
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | A unique integer value identifying this project.
    topics_guid = "topics_guid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all comments
        api_response = api_instance.get_comments(projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_comments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**| A unique integer value identifying this project. |
 **topics_guid** | **str**|  |

### Return type

[**[Comment]**](Comment.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_detailed_extensions**
> DetailedExtensions get_detailed_extensions(id)

Retrieve project detailed extensions

This is not a standard route. Retrieve project detailed extensions  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.detailed_extensions import DetailedExtensions
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve project detailed extensions
        api_response = api_instance.get_detailed_extensions(id)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_detailed_extensions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this project. |

### Return type

[**DetailedExtensions**](DetailedExtensions.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extensions**
> Extensions get_extensions(id)

Retrieve project extensions

Retrieve project extensions  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.extensions import Extensions
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve project extensions
        api_response = api_instance.get_extensions(id)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_extensions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this project. |

### Return type

[**Extensions**](Extensions.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_full_topic**
> FullTopic get_full_topic(guid, projects_pk)

Retrieve a full topic

This is not a standard route. It responds with a topic, its viewpoints and its comments  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.full_topic import FullTopic
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    img_format = "url" # str | All snapshot_data will be returned as url instead of base64 (optional) if omitted the server will use the default value of "url"

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a full topic
        api_response = api_instance.get_full_topic(guid, projects_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_full_topic: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a full topic
        api_response = api_instance.get_full_topic(guid, projects_pk, img_format=img_format)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_full_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **img_format** | **str**| All snapshot_data will be returned as url instead of base64 | [optional] if omitted the server will use the default value of "url"

### Return type

[**FullTopic**](FullTopic.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_full_topics**
> [FullTopic] get_full_topics(projects_pk)

Retrieve all full topics

This is not a standard route. It responds with all topics, their viewpoints and their comments  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.full_topic import FullTopic
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | 
    format = "format_example" # str | format (optional)
    ifcs = "ifcs_example" # str | ifcs (optional)
    img_format = "url" # str | All snapshot_data will be returned as url instead of base64 (optional) if omitted the server will use the default value of "url"
    models = "models_example" # str | models (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all full topics
        api_response = api_instance.get_full_topics(projects_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_full_topics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve all full topics
        api_response = api_instance.get_full_topics(projects_pk, format=format, ifcs=ifcs, img_format=img_format, models=models)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_full_topics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**|  |
 **format** | **str**| format | [optional]
 **ifcs** | **str**| ifcs | [optional]
 **img_format** | **str**| All snapshot_data will be returned as url instead of base64 | [optional] if omitted the server will use the default value of "url"
 **models** | **str**| models | [optional]

### Return type

[**[FullTopic]**](FullTopic.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pins**
> [Pin] get_pins(projects_pk, topics_guid, viewpoints_guid)

Retrieve all Pins of a viewpoint

This is not a standard route. Retrieve all Pins of a viewpoint  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.pin import Pin
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 
    viewpoints_guid = "viewpoints_guid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all Pins of a viewpoint
        api_response = api_instance.get_pins(projects_pk, topics_guid, viewpoints_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_pins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |
 **viewpoints_guid** | **str**|  |

### Return type

[**[Pin]**](Pin.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_related_topics**
> [str] get_related_topics(guid, projects_pk)

Get all related topics

This feature is not supported yet and will always respond with an empty array  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    format = "format_example" # str | format (optional)
    ifcs = "ifcs_example" # str | ifcs (optional)
    models = "models_example" # str | models (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all related topics
        api_response = api_instance.get_related_topics(guid, projects_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_related_topics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all related topics
        api_response = api_instance.get_related_topics(guid, projects_pk, format=format, ifcs=ifcs, models=models)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_related_topics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **format** | **str**| format | [optional]
 **ifcs** | **str**| ifcs | [optional]
 **models** | **str**| models | [optional]

### Return type

**[str]**

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_selections**
> [Component] get_selections(guid, projects_pk, topics_guid)

Retrieve all selections of a viewpoint

Retrieve all selections of a viewpoint  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.component import Component
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all selections of a viewpoint
        api_response = api_instance.get_selections(guid, projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_selections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |

### Return type

[**[Component]**](Component.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot**
> file_type get_snapshot(guid, projects_pk, topics_guid)

Retrieve the viewpoint' snapshot

Retrieve the viewpoint' snapshot  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the viewpoint' snapshot
        api_response = api_instance.get_snapshot(guid, projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_snapshot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |

### Return type

**file_type**

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Snapshot file |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic**
> Topic get_topic(guid, projects_pk)

Retrieve a topic

Retrieve a topic  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.topic import Topic
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a topic
        api_response = api_instance.get_topic(guid, projects_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |

### Return type

[**Topic**](Topic.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_document_references**
> [str] get_topic_document_references(guid, projects_pk)

Get all related documents

This feature is not supported yet and will always respond with an empty array  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    format = "format_example" # str | format (optional)
    ifcs = "ifcs_example" # str | ifcs (optional)
    models = "models_example" # str | models (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all related documents
        api_response = api_instance.get_topic_document_references(guid, projects_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_topic_document_references: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all related documents
        api_response = api_instance.get_topic_document_references(guid, projects_pk, format=format, ifcs=ifcs, models=models)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_topic_document_references: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **format** | **str**| format | [optional]
 **ifcs** | **str**| ifcs | [optional]
 **models** | **str**| models | [optional]

### Return type

**[str]**

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_viewpoints**
> [Viewpoint] get_topic_viewpoints(projects_pk, topics_guid)

Retrieve all viewpoints attached to the topic

This is not a standard route. It returns all viewpoints of the topic that are not attached to a comment.  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.viewpoint import Viewpoint
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 
    img_format = "url" # str | All snapshot_data will be returned as url instead of base64 (optional) if omitted the server will use the default value of "url"

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all viewpoints attached to the topic
        api_response = api_instance.get_topic_viewpoints(projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_topic_viewpoints: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve all viewpoints attached to the topic
        api_response = api_instance.get_topic_viewpoints(projects_pk, topics_guid, img_format=img_format)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_topic_viewpoints: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |
 **img_format** | **str**| All snapshot_data will be returned as url instead of base64 | [optional] if omitted the server will use the default value of "url"

### Return type

[**[Viewpoint]**](Viewpoint.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topics**
> [Topic] get_topics(projects_pk)

Retrieve all topics

Retrieve all topics  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.topic import Topic
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | 
    format = "format_example" # str | format (optional)
    ifcs = "ifcs_example" # str | ifcs (optional)
    models = "models_example" # str | models (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all topics
        api_response = api_instance.get_topics(projects_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_topics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve all topics
        api_response = api_instance.get_topics(projects_pk, format=format, ifcs=ifcs, models=models)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_topics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**|  |
 **format** | **str**| format | [optional]
 **ifcs** | **str**| ifcs | [optional]
 **models** | **str**| models | [optional]

### Return type

[**[Topic]**](Topic.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> SelfBcfUser get_user()

Get current user info

Get current user info. If request comes from an App, the response is always:{    \"id\": None,    \"name\": None,    \"is_client\": True,}  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.self_bcf_user import SelfBcfUser
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get current user info
        api_response = api_instance.get_user()
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SelfBcfUser**](SelfBcfUser.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions**
> [Version] get_versions()

Retrieve all supported BCF versions by this API

Spoiler: it's only v2.1

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.version import Version
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve all supported BCF versions by this API
        api_response = api_instance.get_versions()
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_versions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Version]**](Version.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_viewpoin_pin**
> Pin get_viewpoin_pin(guid, projects_pk, topics_guid, viewpoints_guid)

Retrieve a Pin

This is not a standard route. Retrieve a Pin  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.pin import Pin
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 
    viewpoints_guid = "viewpoints_guid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Pin
        api_response = api_instance.get_viewpoin_pin(guid, projects_pk, topics_guid, viewpoints_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_viewpoin_pin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |
 **viewpoints_guid** | **str**|  |

### Return type

[**Pin**](Pin.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_viewpoint**
> Viewpoint get_viewpoint(guid, projects_pk, topics_guid)

Retrieve a Viewpoint

Retrieve a Viewpoint  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.viewpoint import Viewpoint
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 
    img_format = "url" # str | All snapshot_data will be returned as url instead of base64 (optional) if omitted the server will use the default value of "url"

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Viewpoint
        api_response = api_instance.get_viewpoint(guid, projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_viewpoint: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a Viewpoint
        api_response = api_instance.get_viewpoint(guid, projects_pk, topics_guid, img_format=img_format)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_viewpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |
 **img_format** | **str**| All snapshot_data will be returned as url instead of base64 | [optional] if omitted the server will use the default value of "url"

### Return type

[**Viewpoint**](Viewpoint.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_viewpoints**
> [Viewpoint] get_viewpoints(projects_pk, topics_guid)

Retrieve all Viewpoints of a topic

Retrieve all Viewpoints of a topic  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.viewpoint import Viewpoint
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 
    img_format = "url" # str | All snapshot_data will be returned as url instead of base64 (optional) if omitted the server will use the default value of "url"

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all Viewpoints of a topic
        api_response = api_instance.get_viewpoints(projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_viewpoints: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve all Viewpoints of a topic
        api_response = api_instance.get_viewpoints(projects_pk, topics_guid, img_format=img_format)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_viewpoints: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |
 **img_format** | **str**| All snapshot_data will be returned as url instead of base64 | [optional] if omitted the server will use the default value of "url"

### Return type

[**[Viewpoint]**](Viewpoint.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_visibilities**
> Visibility get_visibilities(guid, projects_pk, topics_guid)

Retrieve all visibilities of a viewpoint

Retrieve all visibilities of a viewpoint  Required scopes: bcf:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.visibility import Visibility
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all visibilities of a viewpoint
        api_response = api_instance.get_visibilities(guid, projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->get_visibilities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |

### Return type

[**Visibility**](Visibility.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_bcf**
> import_bcf(id, name)

Import bcf-xml format into this project

This is not a standard route. Import bcf-xml format into this project. If there are guid conflict, an error will be raised. If there are index conflicts, indexes of the imported file will be overriden with a new index. Author and assigned_to fields will be linked to existing users in the project. If no matching user are found, fields will be emptied. Only BCF 2.1 is supported  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this project.
    name = "name_example" # str | Name of the project

    # example passing only required values which don't have defaults set
    try:
        # Import bcf-xml format into this project
        api_instance.import_bcf(id, name)
    except bimdata_api_client.ApiException as e:
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

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bcf_project**
> BcfProject update_bcf_project(id)

Update some fields of a BCF project

Update some fields of a BCF project  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.patched_bcf_project_request import PatchedBcfProjectRequest
from bimdata_api_client.model.bcf_project import BcfProject
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this project.
    patched_bcf_project_request = PatchedBcfProjectRequest(
        name="name_example",
    ) # PatchedBcfProjectRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a BCF project
        api_response = api_instance.update_bcf_project(id)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_bcf_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a BCF project
        api_response = api_instance.update_bcf_project(id, patched_bcf_project_request=patched_bcf_project_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_bcf_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this project. |
 **patched_bcf_project_request** | [**PatchedBcfProjectRequest**](PatchedBcfProjectRequest.md)|  | [optional]

### Return type

[**BcfProject**](BcfProject.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
> Comment update_comment(guid, projects_pk, topics_guid)

Update some fields of a comment

Update some fields of a comment  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.patched_comment_request import PatchedCommentRequest
from bimdata_api_client.model.comment import Comment
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | A unique integer value identifying this project.
    topics_guid = "topics_guid_example" # str | 
    patched_comment_request = PatchedCommentRequest(
        guid="guid_example",
        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        author="author_example",
        comment="comment_example",
        viewpoint_guid="viewpoint_guid_example",
        reply_to_comment_guid="reply_to_comment_guid_example",
        modified_author="modified_author_example",
        viewpoint_temp_id=1,
    ) # PatchedCommentRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a comment
        api_response = api_instance.update_comment(guid, projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_comment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a comment
        api_response = api_instance.update_comment(guid, projects_pk, topics_guid, patched_comment_request=patched_comment_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**| A unique integer value identifying this project. |
 **topics_guid** | **str**|  |
 **patched_comment_request** | [**PatchedCommentRequest**](PatchedCommentRequest.md)|  | [optional]

### Return type

[**Comment**](Comment.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **update_extension_label**
> Label update_extension_label(id, projects_pk)

Update a Label

This is not a standard route. Update a Label. All topics using this label will be updated  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.label import Label
from bimdata_api_client.model.patched_label_request import PatchedLabelRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this label.
    projects_pk = 1 # int | 
    patched_label_request = PatchedLabelRequest(
        label="label_example",
        project=1,
    ) # PatchedLabelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Label
        api_response = api_instance.update_extension_label(id, projects_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_extension_label: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Label
        api_response = api_instance.update_extension_label(id, projects_pk, patched_label_request=patched_label_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_extension_label: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this label. |
 **projects_pk** | **int**|  |
 **patched_label_request** | [**PatchedLabelRequest**](PatchedLabelRequest.md)|  | [optional]

### Return type

[**Label**](Label.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **update_extension_priority**
> Priority update_extension_priority(id, projects_pk)

Update a Priority

This is not a standard route. Update a Priority. All topics using this priority will be updated  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.priority import Priority
from bimdata_api_client.model.patched_priority_request import PatchedPriorityRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this priority.
    projects_pk = 1 # int | 
    patched_priority_request = PatchedPriorityRequest(
        priority="priority_example",
        color="color_example",
        project=1,
    ) # PatchedPriorityRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Priority
        api_response = api_instance.update_extension_priority(id, projects_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_extension_priority: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Priority
        api_response = api_instance.update_extension_priority(id, projects_pk, patched_priority_request=patched_priority_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_extension_priority: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this priority. |
 **projects_pk** | **int**|  |
 **patched_priority_request** | [**PatchedPriorityRequest**](PatchedPriorityRequest.md)|  | [optional]

### Return type

[**Priority**](Priority.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **update_extension_stage**
> Stage update_extension_stage(id, projects_pk)

Update a Stage

This is not a standard route. Update a Stage. All topics using this stage will be updated  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.stage import Stage
from bimdata_api_client.model.patched_stage_request import PatchedStageRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this stage.
    projects_pk = 1 # int | 
    patched_stage_request = PatchedStageRequest(
        stage="stage_example",
        project=1,
    ) # PatchedStageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Stage
        api_response = api_instance.update_extension_stage(id, projects_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_extension_stage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Stage
        api_response = api_instance.update_extension_stage(id, projects_pk, patched_stage_request=patched_stage_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_extension_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this stage. |
 **projects_pk** | **int**|  |
 **patched_stage_request** | [**PatchedStageRequest**](PatchedStageRequest.md)|  | [optional]

### Return type

[**Stage**](Stage.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **update_extension_status**
> TopicStatus update_extension_status(id, projects_pk)

Update a TopicStatus

This is not a standard route. Update a TopicStatus. All topics using this status will be updated  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.patched_topic_status_request import PatchedTopicStatusRequest
from bimdata_api_client.model.topic_status import TopicStatus
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this topic status.
    projects_pk = 1 # int | 
    patched_topic_status_request = PatchedTopicStatusRequest(
        topic_status="topic_status_example",
        color="color_example",
        project=1,
    ) # PatchedTopicStatusRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a TopicStatus
        api_response = api_instance.update_extension_status(id, projects_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_extension_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a TopicStatus
        api_response = api_instance.update_extension_status(id, projects_pk, patched_topic_status_request=patched_topic_status_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_extension_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this topic status. |
 **projects_pk** | **int**|  |
 **patched_topic_status_request** | [**PatchedTopicStatusRequest**](PatchedTopicStatusRequest.md)|  | [optional]

### Return type

[**TopicStatus**](TopicStatus.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **update_extension_type**
> TopicType update_extension_type(id, projects_pk)

Update a TopicType

This is not a standard route. Update a TopicType. All topics using this type will be updated  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.topic_type import TopicType
from bimdata_api_client.model.patched_topic_type_request import PatchedTopicTypeRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    id = 1 # int | A unique integer value identifying this topic type.
    projects_pk = 1 # int | 
    patched_topic_type_request = PatchedTopicTypeRequest(
        topic_type="topic_type_example",
        project=1,
    ) # PatchedTopicTypeRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a TopicType
        api_response = api_instance.update_extension_type(id, projects_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_extension_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a TopicType
        api_response = api_instance.update_extension_type(id, projects_pk, patched_topic_type_request=patched_topic_type_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_extension_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this topic type. |
 **projects_pk** | **int**|  |
 **patched_topic_type_request** | [**PatchedTopicTypeRequest**](PatchedTopicTypeRequest.md)|  | [optional]

### Return type

[**TopicType**](TopicType.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
> FullTopic update_full_topic(guid, projects_pk)

Update some fields of a topic

This is not a standard route. You can update topic, viewpoints and comment is a signle call  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.patched_full_topic_request import PatchedFullTopicRequest
from bimdata_api_client.model.full_topic import FullTopic
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    img_format = "url" # str | All snapshot_data will be returned as url instead of base64 (optional) if omitted the server will use the default value of "url"
    patched_full_topic_request = PatchedFullTopicRequest(
        guid="guid_example",
        creation_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        creation_author="creation_author_example",
        modified_author="modified_author_example",
        title="title_example",
        description="description_example",
        reference_links=[
            "reference_links_example",
        ],
        ifcs=[
            1,
        ],
        models=[
            1,
        ],
        labels=[
            "labels_example",
        ],
        topic_type="topic_type_example",
        topic_status="topic_status_example",
        stage="stage_example",
        priority="priority_example",
        index=0,
        assigned_to="assigned_to_example",
        format="format_example",
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        comments=[
            CommentRequest(
                guid="guid_example",
                date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                author="author_example",
                comment="comment_example",
                viewpoint_guid="viewpoint_guid_example",
                reply_to_comment_guid="reply_to_comment_guid_example",
                modified_author="modified_author_example",
                viewpoint_temp_id=1,
            ),
        ],
        viewpoints=[
            ViewpointRequest(
                index=0,
                guid="guid_example",
                originating_system="originating_system_example",
                authoring_tool_id="authoring_tool_id_example",
                orthogonal_camera=None,
                perspective_camera=None,
                lines=[
                    LineRequest(
                        end_point=PointRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                        start_point=PointRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                    ),
                ],
                clipping_planes=[
                    ClippingPlaneRequest(
                        location=PointRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                        direction=DirectionRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                    ),
                ],
                snapshot=None,
                components=None,
                pins=[
                    PinRequest(
                        guid="guid_example",
                        name="name_example",
                        color="color_example",
                        point=GeometryPointRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                        index=0,
                    ),
                ],
                temp_id=1,
            ),
        ],
        project=1,
    ) # PatchedFullTopicRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a topic
        api_response = api_instance.update_full_topic(guid, projects_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_full_topic: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a topic
        api_response = api_instance.update_full_topic(guid, projects_pk, img_format=img_format, patched_full_topic_request=patched_full_topic_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_full_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **img_format** | **str**| All snapshot_data will be returned as url instead of base64 | [optional] if omitted the server will use the default value of "url"
 **patched_full_topic_request** | [**PatchedFullTopicRequest**](PatchedFullTopicRequest.md)|  | [optional]

### Return type

[**FullTopic**](FullTopic.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **update_pin**
> Pin update_pin(guid, projects_pk, topics_guid, viewpoints_guid)

Update some fields of a Pin

This is not a standard route. Update some fields of a Pin  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.pin import Pin
from bimdata_api_client.model.patched_pin_request import PatchedPinRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 
    viewpoints_guid = "viewpoints_guid_example" # str | 
    patched_pin_request = PatchedPinRequest(
        guid="guid_example",
        name="name_example",
        color="color_example",
        point=GeometryPointRequest(
            x=3.14,
            y=3.14,
            z=3.14,
        ),
        index=0,
    ) # PatchedPinRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a Pin
        api_response = api_instance.update_pin(guid, projects_pk, topics_guid, viewpoints_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_pin: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a Pin
        api_response = api_instance.update_pin(guid, projects_pk, topics_guid, viewpoints_guid, patched_pin_request=patched_pin_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_pin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |
 **viewpoints_guid** | **str**|  |
 **patched_pin_request** | [**PatchedPinRequest**](PatchedPinRequest.md)|  | [optional]

### Return type

[**Pin**](Pin.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
> Topic update_topic(guid, projects_pk)

Update some fields of a topic

Update some fields of a topic  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.topic import Topic
from bimdata_api_client.model.patched_topic_request import PatchedTopicRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    patched_topic_request = PatchedTopicRequest(
        guid="guid_example",
        topic_type="topic_type_example",
        topic_status="topic_status_example",
        title="title_example",
        priority="priority_example",
        labels=[
            "labels_example",
        ],
        creation_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        creation_author="creation_author_example",
        modified_author="modified_author_example",
        assigned_to="assigned_to_example",
        reference_links=[
            "reference_links_example",
        ],
        stage="stage_example",
        description="description_example",
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ifcs=[
            1,
        ],
        models=[
            1,
        ],
        format="format_example",
        index=0,
        project=1,
    ) # PatchedTopicRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a topic
        api_response = api_instance.update_topic(guid, projects_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_topic: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a topic
        api_response = api_instance.update_topic(guid, projects_pk, patched_topic_request=patched_topic_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **patched_topic_request** | [**PatchedTopicRequest**](PatchedTopicRequest.md)|  | [optional]

### Return type

[**Topic**](Topic.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
> Viewpoint update_viewpoint(guid, projects_pk, topics_guid)

Update some fields of a Viewpoint

This is not a standard route. Update some fields of a Viewpoint  Required scopes: bcf:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import bcf_api
from bimdata_api_client.model.viewpoint import Viewpoint
from bimdata_api_client.model.patched_viewpoint_request import PatchedViewpointRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: BIMData_Connect
configuration = bimdata_api_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bcf_api.BcfApi(api_client)
    guid = "guid_example" # str | 
    projects_pk = 1 # int | 
    topics_guid = "topics_guid_example" # str | 
    img_format = "url" # str | All snapshot_data will be returned as url instead of base64 (optional) if omitted the server will use the default value of "url"
    patched_viewpoint_request = PatchedViewpointRequest(
        index=0,
        guid="guid_example",
        originating_system="originating_system_example",
        authoring_tool_id="authoring_tool_id_example",
        orthogonal_camera=None,
        perspective_camera=None,
        lines=[
            LineRequest(
                end_point=PointRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
                start_point=PointRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
            ),
        ],
        clipping_planes=[
            ClippingPlaneRequest(
                location=PointRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
                direction=DirectionRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
            ),
        ],
        snapshot=None,
        components=None,
        pins=[
            PinRequest(
                guid="guid_example",
                name="name_example",
                color="color_example",
                point=GeometryPointRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
                index=0,
            ),
        ],
        temp_id=1,
    ) # PatchedViewpointRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a Viewpoint
        api_response = api_instance.update_viewpoint(guid, projects_pk, topics_guid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_viewpoint: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a Viewpoint
        api_response = api_instance.update_viewpoint(guid, projects_pk, topics_guid, img_format=img_format, patched_viewpoint_request=patched_viewpoint_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling BcfApi->update_viewpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  |
 **projects_pk** | **int**|  |
 **topics_guid** | **str**|  |
 **img_format** | **str**| All snapshot_data will be returned as url instead of base64 | [optional] if omitted the server will use the default value of "url"
 **patched_viewpoint_request** | [**PatchedViewpointRequest**](PatchedViewpointRequest.md)|  | [optional]

### Return type

[**Viewpoint**](Viewpoint.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

