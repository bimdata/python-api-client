# bimdata_api_client.BcfApi

All URIs are relative to *https://api-staging.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bcf2_1_current_user_list**](BcfApi.md#bcf2_1_current_user_list) | **GET** /bcf/2.1/current-user | 
[**bcf2_1_projects_create**](BcfApi.md#bcf2_1_projects_create) | **POST** /bcf/2.1/projects | 
[**bcf2_1_projects_delete**](BcfApi.md#bcf2_1_projects_delete) | **DELETE** /bcf/2.1/projects/{id} | 
[**bcf2_1_projects_documents_create**](BcfApi.md#bcf2_1_projects_documents_create) | **POST** /bcf/2.1/projects/{projects_pk}/documents | 
[**bcf2_1_projects_documents_delete**](BcfApi.md#bcf2_1_projects_documents_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/documents/{id} | 
[**bcf2_1_projects_documents_list**](BcfApi.md#bcf2_1_projects_documents_list) | **GET** /bcf/2.1/projects/{projects_pk}/documents | 
[**bcf2_1_projects_documents_partial_update**](BcfApi.md#bcf2_1_projects_documents_partial_update) | **PATCH** /bcf/2.1/projects/{projects_pk}/documents/{id} | 
[**bcf2_1_projects_documents_read**](BcfApi.md#bcf2_1_projects_documents_read) | **GET** /bcf/2.1/projects/{projects_pk}/documents/{id} | 
[**bcf2_1_projects_documents_update**](BcfApi.md#bcf2_1_projects_documents_update) | **PUT** /bcf/2.1/projects/{projects_pk}/documents/{id} | 
[**bcf2_1_projects_extensions_list**](BcfApi.md#bcf2_1_projects_extensions_list) | **GET** /bcf/2.1/projects/{projects_pk}/extensions | 
[**bcf2_1_projects_list**](BcfApi.md#bcf2_1_projects_list) | **GET** /bcf/2.1/projects | 
[**bcf2_1_projects_partial_update**](BcfApi.md#bcf2_1_projects_partial_update) | **PATCH** /bcf/2.1/projects/{id} | 
[**bcf2_1_projects_read**](BcfApi.md#bcf2_1_projects_read) | **GET** /bcf/2.1/projects/{id} | 
[**bcf2_1_projects_topics_comments_create**](BcfApi.md#bcf2_1_projects_topics_comments_create) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments | 
[**bcf2_1_projects_topics_comments_delete**](BcfApi.md#bcf2_1_projects_topics_comments_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{id} | 
[**bcf2_1_projects_topics_comments_events_create**](BcfApi.md#bcf2_1_projects_topics_comments_events_create) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/events | 
[**bcf2_1_projects_topics_comments_events_create_0**](BcfApi.md#bcf2_1_projects_topics_comments_events_create_0) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{comments_pk}/events | 
[**bcf2_1_projects_topics_comments_events_delete**](BcfApi.md#bcf2_1_projects_topics_comments_events_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/events/{id} | 
[**bcf2_1_projects_topics_comments_events_delete_0**](BcfApi.md#bcf2_1_projects_topics_comments_events_delete_0) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{comments_pk}/events/{id} | 
[**bcf2_1_projects_topics_comments_events_list**](BcfApi.md#bcf2_1_projects_topics_comments_events_list) | **GET** /bcf/2.1/projects/{projects_pk}/topics/comments/events | 
[**bcf2_1_projects_topics_comments_events_list_0**](BcfApi.md#bcf2_1_projects_topics_comments_events_list_0) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/events | 
[**bcf2_1_projects_topics_comments_events_list_1**](BcfApi.md#bcf2_1_projects_topics_comments_events_list_1) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{comments_pk}/events | 
[**bcf2_1_projects_topics_comments_events_partial_update**](BcfApi.md#bcf2_1_projects_topics_comments_events_partial_update) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/events/{id} | 
[**bcf2_1_projects_topics_comments_events_partial_update_0**](BcfApi.md#bcf2_1_projects_topics_comments_events_partial_update_0) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{comments_pk}/events/{id} | 
[**bcf2_1_projects_topics_comments_events_read**](BcfApi.md#bcf2_1_projects_topics_comments_events_read) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/events/{id} | 
[**bcf2_1_projects_topics_comments_events_read_0**](BcfApi.md#bcf2_1_projects_topics_comments_events_read_0) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{comments_pk}/events/{id} | 
[**bcf2_1_projects_topics_comments_events_update**](BcfApi.md#bcf2_1_projects_topics_comments_events_update) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/events/{id} | 
[**bcf2_1_projects_topics_comments_events_update_0**](BcfApi.md#bcf2_1_projects_topics_comments_events_update_0) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{comments_pk}/events/{id} | 
[**bcf2_1_projects_topics_comments_list**](BcfApi.md#bcf2_1_projects_topics_comments_list) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments | 
[**bcf2_1_projects_topics_comments_partial_update**](BcfApi.md#bcf2_1_projects_topics_comments_partial_update) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{id} | 
[**bcf2_1_projects_topics_comments_read**](BcfApi.md#bcf2_1_projects_topics_comments_read) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{id} | 
[**bcf2_1_projects_topics_comments_update**](BcfApi.md#bcf2_1_projects_topics_comments_update) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/comments/{id} | 
[**bcf2_1_projects_topics_create**](BcfApi.md#bcf2_1_projects_topics_create) | **POST** /bcf/2.1/projects/{projects_pk}/topics | 
[**bcf2_1_projects_topics_delete**](BcfApi.md#bcf2_1_projects_topics_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{id} | 
[**bcf2_1_projects_topics_document_references_create**](BcfApi.md#bcf2_1_projects_topics_document_references_create) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/document_references | 
[**bcf2_1_projects_topics_document_references_delete**](BcfApi.md#bcf2_1_projects_topics_document_references_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/document_references/{id} | 
[**bcf2_1_projects_topics_document_references_list**](BcfApi.md#bcf2_1_projects_topics_document_references_list) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/document_references | 
[**bcf2_1_projects_topics_document_references_partial_update**](BcfApi.md#bcf2_1_projects_topics_document_references_partial_update) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/document_references/{id} | 
[**bcf2_1_projects_topics_document_references_read**](BcfApi.md#bcf2_1_projects_topics_document_references_read) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/document_references/{id} | 
[**bcf2_1_projects_topics_document_references_update**](BcfApi.md#bcf2_1_projects_topics_document_references_update) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/document_references/{id} | 
[**bcf2_1_projects_topics_events_create**](BcfApi.md#bcf2_1_projects_topics_events_create) | **POST** /bcf/2.1/projects/{projects_pk}/topics/events | 
[**bcf2_1_projects_topics_events_create_0**](BcfApi.md#bcf2_1_projects_topics_events_create_0) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/events | 
[**bcf2_1_projects_topics_events_delete**](BcfApi.md#bcf2_1_projects_topics_events_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/events/{id} | 
[**bcf2_1_projects_topics_events_delete_0**](BcfApi.md#bcf2_1_projects_topics_events_delete_0) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/events/{id} | 
[**bcf2_1_projects_topics_events_list**](BcfApi.md#bcf2_1_projects_topics_events_list) | **GET** /bcf/2.1/projects/{projects_pk}/topics/events | 
[**bcf2_1_projects_topics_events_list_0**](BcfApi.md#bcf2_1_projects_topics_events_list_0) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/events | 
[**bcf2_1_projects_topics_events_partial_update**](BcfApi.md#bcf2_1_projects_topics_events_partial_update) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/events/{id} | 
[**bcf2_1_projects_topics_events_partial_update_0**](BcfApi.md#bcf2_1_projects_topics_events_partial_update_0) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/events/{id} | 
[**bcf2_1_projects_topics_events_read**](BcfApi.md#bcf2_1_projects_topics_events_read) | **GET** /bcf/2.1/projects/{projects_pk}/topics/events/{id} | 
[**bcf2_1_projects_topics_events_read_0**](BcfApi.md#bcf2_1_projects_topics_events_read_0) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/events/{id} | 
[**bcf2_1_projects_topics_events_update**](BcfApi.md#bcf2_1_projects_topics_events_update) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/events/{id} | 
[**bcf2_1_projects_topics_events_update_0**](BcfApi.md#bcf2_1_projects_topics_events_update_0) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/events/{id} | 
[**bcf2_1_projects_topics_file_create**](BcfApi.md#bcf2_1_projects_topics_file_create) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/file | 
[**bcf2_1_projects_topics_file_delete**](BcfApi.md#bcf2_1_projects_topics_file_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/file/{id} | 
[**bcf2_1_projects_topics_file_list**](BcfApi.md#bcf2_1_projects_topics_file_list) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/file | 
[**bcf2_1_projects_topics_file_partial_update**](BcfApi.md#bcf2_1_projects_topics_file_partial_update) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/file/{id} | 
[**bcf2_1_projects_topics_file_read**](BcfApi.md#bcf2_1_projects_topics_file_read) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/file/{id} | 
[**bcf2_1_projects_topics_file_update**](BcfApi.md#bcf2_1_projects_topics_file_update) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/file/{id} | 
[**bcf2_1_projects_topics_list**](BcfApi.md#bcf2_1_projects_topics_list) | **GET** /bcf/2.1/projects/{projects_pk}/topics | 
[**bcf2_1_projects_topics_partial_update**](BcfApi.md#bcf2_1_projects_topics_partial_update) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{id} | 
[**bcf2_1_projects_topics_read**](BcfApi.md#bcf2_1_projects_topics_read) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{id} | 
[**bcf2_1_projects_topics_related_topics_create**](BcfApi.md#bcf2_1_projects_topics_related_topics_create) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/related_topics | 
[**bcf2_1_projects_topics_related_topics_delete**](BcfApi.md#bcf2_1_projects_topics_related_topics_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/related_topics/{id} | 
[**bcf2_1_projects_topics_related_topics_list**](BcfApi.md#bcf2_1_projects_topics_related_topics_list) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/related_topics | 
[**bcf2_1_projects_topics_related_topics_partial_update**](BcfApi.md#bcf2_1_projects_topics_related_topics_partial_update) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/related_topics/{id} | 
[**bcf2_1_projects_topics_related_topics_read**](BcfApi.md#bcf2_1_projects_topics_related_topics_read) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/related_topics/{id} | 
[**bcf2_1_projects_topics_related_topics_update**](BcfApi.md#bcf2_1_projects_topics_related_topics_update) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/related_topics/{id} | 
[**bcf2_1_projects_topics_snippet_create**](BcfApi.md#bcf2_1_projects_topics_snippet_create) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/snippet | 
[**bcf2_1_projects_topics_snippet_delete**](BcfApi.md#bcf2_1_projects_topics_snippet_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/snippet/{id} | 
[**bcf2_1_projects_topics_snippet_list**](BcfApi.md#bcf2_1_projects_topics_snippet_list) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/snippet | 
[**bcf2_1_projects_topics_snippet_partial_update**](BcfApi.md#bcf2_1_projects_topics_snippet_partial_update) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/snippet/{id} | 
[**bcf2_1_projects_topics_snippet_read**](BcfApi.md#bcf2_1_projects_topics_snippet_read) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/snippet/{id} | 
[**bcf2_1_projects_topics_snippet_update**](BcfApi.md#bcf2_1_projects_topics_snippet_update) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/snippet/{id} | 
[**bcf2_1_projects_topics_update**](BcfApi.md#bcf2_1_projects_topics_update) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{id} | 
[**bcf2_1_projects_topics_viewpoints_bitmap_create**](BcfApi.md#bcf2_1_projects_topics_viewpoints_bitmap_create) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/bitmap | 
[**bcf2_1_projects_topics_viewpoints_bitmap_delete**](BcfApi.md#bcf2_1_projects_topics_viewpoints_bitmap_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/bitmap/{id} | 
[**bcf2_1_projects_topics_viewpoints_bitmap_list**](BcfApi.md#bcf2_1_projects_topics_viewpoints_bitmap_list) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/bitmap | 
[**bcf2_1_projects_topics_viewpoints_bitmap_partial_update**](BcfApi.md#bcf2_1_projects_topics_viewpoints_bitmap_partial_update) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/bitmap/{id} | 
[**bcf2_1_projects_topics_viewpoints_bitmap_read**](BcfApi.md#bcf2_1_projects_topics_viewpoints_bitmap_read) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/bitmap/{id} | 
[**bcf2_1_projects_topics_viewpoints_bitmap_update**](BcfApi.md#bcf2_1_projects_topics_viewpoints_bitmap_update) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/bitmap/{id} | 
[**bcf2_1_projects_topics_viewpoints_coloring_create**](BcfApi.md#bcf2_1_projects_topics_viewpoints_coloring_create) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring | 
[**bcf2_1_projects_topics_viewpoints_coloring_delete**](BcfApi.md#bcf2_1_projects_topics_viewpoints_coloring_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring/{id} | 
[**bcf2_1_projects_topics_viewpoints_coloring_list**](BcfApi.md#bcf2_1_projects_topics_viewpoints_coloring_list) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring | 
[**bcf2_1_projects_topics_viewpoints_coloring_partial_update**](BcfApi.md#bcf2_1_projects_topics_viewpoints_coloring_partial_update) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring/{id} | 
[**bcf2_1_projects_topics_viewpoints_coloring_read**](BcfApi.md#bcf2_1_projects_topics_viewpoints_coloring_read) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring/{id} | 
[**bcf2_1_projects_topics_viewpoints_coloring_update**](BcfApi.md#bcf2_1_projects_topics_viewpoints_coloring_update) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/coloring/{id} | 
[**bcf2_1_projects_topics_viewpoints_create**](BcfApi.md#bcf2_1_projects_topics_viewpoints_create) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints | 
[**bcf2_1_projects_topics_viewpoints_delete**](BcfApi.md#bcf2_1_projects_topics_viewpoints_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{id} | 
[**bcf2_1_projects_topics_viewpoints_list**](BcfApi.md#bcf2_1_projects_topics_viewpoints_list) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints | 
[**bcf2_1_projects_topics_viewpoints_partial_update**](BcfApi.md#bcf2_1_projects_topics_viewpoints_partial_update) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{id} | 
[**bcf2_1_projects_topics_viewpoints_read**](BcfApi.md#bcf2_1_projects_topics_viewpoints_read) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{id} | 
[**bcf2_1_projects_topics_viewpoints_selection_create**](BcfApi.md#bcf2_1_projects_topics_viewpoints_selection_create) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection | 
[**bcf2_1_projects_topics_viewpoints_selection_delete**](BcfApi.md#bcf2_1_projects_topics_viewpoints_selection_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection/{id} | 
[**bcf2_1_projects_topics_viewpoints_selection_list**](BcfApi.md#bcf2_1_projects_topics_viewpoints_selection_list) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection | 
[**bcf2_1_projects_topics_viewpoints_selection_partial_update**](BcfApi.md#bcf2_1_projects_topics_viewpoints_selection_partial_update) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection/{id} | 
[**bcf2_1_projects_topics_viewpoints_selection_read**](BcfApi.md#bcf2_1_projects_topics_viewpoints_selection_read) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection/{id} | 
[**bcf2_1_projects_topics_viewpoints_selection_update**](BcfApi.md#bcf2_1_projects_topics_viewpoints_selection_update) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/selection/{id} | 
[**bcf2_1_projects_topics_viewpoints_snapshot_list**](BcfApi.md#bcf2_1_projects_topics_viewpoints_snapshot_list) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/snapshot | 
[**bcf2_1_projects_topics_viewpoints_update**](BcfApi.md#bcf2_1_projects_topics_viewpoints_update) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{id} | 
[**bcf2_1_projects_topics_viewpoints_visibility_create**](BcfApi.md#bcf2_1_projects_topics_viewpoints_visibility_create) | **POST** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility | 
[**bcf2_1_projects_topics_viewpoints_visibility_delete**](BcfApi.md#bcf2_1_projects_topics_viewpoints_visibility_delete) | **DELETE** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility/{id} | 
[**bcf2_1_projects_topics_viewpoints_visibility_list**](BcfApi.md#bcf2_1_projects_topics_viewpoints_visibility_list) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility | 
[**bcf2_1_projects_topics_viewpoints_visibility_partial_update**](BcfApi.md#bcf2_1_projects_topics_viewpoints_visibility_partial_update) | **PATCH** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility/{id} | 
[**bcf2_1_projects_topics_viewpoints_visibility_read**](BcfApi.md#bcf2_1_projects_topics_viewpoints_visibility_read) | **GET** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility/{id} | 
[**bcf2_1_projects_topics_viewpoints_visibility_update**](BcfApi.md#bcf2_1_projects_topics_viewpoints_visibility_update) | **PUT** /bcf/2.1/projects/{projects_pk}/topics/{topics_pk}/viewpoints/{viewpoints_pk}/visibility/{id} | 
[**bcf2_1_projects_update**](BcfApi.md#bcf2_1_projects_update) | **PUT** /bcf/2.1/projects/{id} | 
[**bcf_versions_create**](BcfApi.md#bcf_versions_create) | **POST** /bcf/versions | 
[**bcf_versions_delete**](BcfApi.md#bcf_versions_delete) | **DELETE** /bcf/versions/{id} | 
[**bcf_versions_list**](BcfApi.md#bcf_versions_list) | **GET** /bcf/versions | 
[**bcf_versions_partial_update**](BcfApi.md#bcf_versions_partial_update) | **PATCH** /bcf/versions/{id} | 
[**bcf_versions_read**](BcfApi.md#bcf_versions_read) | **GET** /bcf/versions/{id} | 
[**bcf_versions_update**](BcfApi.md#bcf_versions_update) | **PUT** /bcf/versions/{id} | 


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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_create**
> BcfProject bcf2_1_projects_create(data)





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
data = bimdata_api_client.BcfProject() # BcfProject | 

try:
    api_response = api_instance.bcf2_1_projects_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**BcfProject**](BcfProject.md)|  | 

### Return type

[**BcfProject**](BcfProject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_delete**
> bcf2_1_projects_delete(id)





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
    api_instance.bcf2_1_projects_delete(id)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_delete: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_documents_create**
> bcf2_1_projects_documents_create(projects_pk, guid=guid, filename=filename)





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
    api_instance.bcf2_1_projects_documents_create(projects_pk, guid=guid, filename=filename)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_documents_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **guid** | [**str**](.md)|  | [optional] 
 **filename** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_documents_delete**
> bcf2_1_projects_documents_delete(projects_pk, id)





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
id = 'id_example' # str | 

try:
    api_instance.bcf2_1_projects_documents_delete(projects_pk, id)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_documents_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_documents_list**
> bcf2_1_projects_documents_list(projects_pk)





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
    api_instance.bcf2_1_projects_documents_list(projects_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_documents_list: %s\n" % e)
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

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_documents_partial_update**
> bcf2_1_projects_documents_partial_update(projects_pk, id, guid=guid, filename=filename)





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
id = 'id_example' # str | 
guid = 'guid_example' # str |  (optional)
filename = 'filename_example' # str |  (optional)

try:
    api_instance.bcf2_1_projects_documents_partial_update(projects_pk, id, guid=guid, filename=filename)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_documents_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **guid** | [**str**](.md)|  | [optional] 
 **filename** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_documents_read**
> bcf2_1_projects_documents_read(projects_pk, id)





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
id = 'id_example' # str | 

try:
    api_instance.bcf2_1_projects_documents_read(projects_pk, id)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_documents_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_documents_update**
> bcf2_1_projects_documents_update(projects_pk, id, guid=guid, filename=filename)





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
id = 'id_example' # str | 
guid = 'guid_example' # str |  (optional)
filename = 'filename_example' # str |  (optional)

try:
    api_instance.bcf2_1_projects_documents_update(projects_pk, id, guid=guid, filename=filename)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_documents_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **guid** | [**str**](.md)|  | [optional] 
 **filename** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_extensions_list**
> list[Extensions] bcf2_1_projects_extensions_list(projects_pk)





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
    api_response = api_instance.bcf2_1_projects_extensions_list(projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_extensions_list: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_list**
> list[BcfProject] bcf2_1_projects_list()





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
    api_response = api_instance.bcf2_1_projects_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BcfProject]**](BcfProject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_partial_update**
> BcfProject bcf2_1_projects_partial_update(id, data)





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
data = bimdata_api_client.BcfProject() # BcfProject | 

try:
    api_response = api_instance.bcf2_1_projects_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**BcfProject**](BcfProject.md)|  | 

### Return type

[**BcfProject**](BcfProject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_read**
> BcfProject bcf2_1_projects_read(id)





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
    api_response = api_instance.bcf2_1_projects_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_read: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_create**
> Comment bcf2_1_projects_topics_comments_create(projects_pk, topics_pk, data)





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
data = bimdata_api_client.Comment() # Comment | 

try:
    api_response = api_instance.bcf2_1_projects_topics_comments_create(projects_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_delete**
> bcf2_1_projects_topics_comments_delete(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_comments_delete(projects_pk, id, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_events_create**
> CommentEvent bcf2_1_projects_topics_comments_events_create(projects_pk, topics_pk, data)





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
data = bimdata_api_client.CommentEvent() # CommentEvent | 

try:
    api_response = api_instance.bcf2_1_projects_topics_comments_events_create(projects_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**CommentEvent**](CommentEvent.md)|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_events_create_0**
> CommentEvent bcf2_1_projects_topics_comments_events_create_0(projects_pk, comments_pk, topics_pk, data)





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
comments_pk = 'comments_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.CommentEvent() # CommentEvent | 

try:
    api_response = api_instance.bcf2_1_projects_topics_comments_events_create_0(projects_pk, comments_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_create_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **comments_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**CommentEvent**](CommentEvent.md)|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_events_delete**
> bcf2_1_projects_topics_comments_events_delete(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_comments_events_delete(projects_pk, id, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_events_delete_0**
> bcf2_1_projects_topics_comments_events_delete_0(projects_pk, id, comments_pk, topics_pk)





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
id = 'id_example' # str | 
comments_pk = 'comments_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_comments_events_delete_0(projects_pk, id, comments_pk, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **comments_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_events_list**
> list[CommentEvent] bcf2_1_projects_topics_comments_events_list(projects_pk)





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
    api_response = api_instance.bcf2_1_projects_topics_comments_events_list(projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_list: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_events_list_0**
> list[CommentEvent] bcf2_1_projects_topics_comments_events_list_0(projects_pk, topics_pk)





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
    api_response = api_instance.bcf2_1_projects_topics_comments_events_list_0(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_list_0: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_events_list_1**
> list[CommentEvent] bcf2_1_projects_topics_comments_events_list_1(projects_pk, comments_pk, topics_pk)





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
comments_pk = 'comments_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_comments_events_list_1(projects_pk, comments_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_list_1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **comments_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[CommentEvent]**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_events_partial_update**
> CommentEvent bcf2_1_projects_topics_comments_events_partial_update(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.CommentEvent() # CommentEvent | 

try:
    api_response = api_instance.bcf2_1_projects_topics_comments_events_partial_update(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**CommentEvent**](CommentEvent.md)|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_events_partial_update_0**
> CommentEvent bcf2_1_projects_topics_comments_events_partial_update_0(projects_pk, id, comments_pk, topics_pk, data)





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
id = 'id_example' # str | 
comments_pk = 'comments_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.CommentEvent() # CommentEvent | 

try:
    api_response = api_instance.bcf2_1_projects_topics_comments_events_partial_update_0(projects_pk, id, comments_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **comments_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**CommentEvent**](CommentEvent.md)|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_events_read**
> CommentEvent bcf2_1_projects_topics_comments_events_read(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_comments_events_read(projects_pk, id, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_events_read_0**
> CommentEvent bcf2_1_projects_topics_comments_events_read_0(projects_pk, id, comments_pk, topics_pk)





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
id = 'id_example' # str | 
comments_pk = 'comments_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_comments_events_read_0(projects_pk, id, comments_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_read_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **comments_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_events_update**
> CommentEvent bcf2_1_projects_topics_comments_events_update(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.CommentEvent() # CommentEvent | 

try:
    api_response = api_instance.bcf2_1_projects_topics_comments_events_update(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**CommentEvent**](CommentEvent.md)|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_events_update_0**
> CommentEvent bcf2_1_projects_topics_comments_events_update_0(projects_pk, id, comments_pk, topics_pk, data)





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
id = 'id_example' # str | 
comments_pk = 'comments_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.CommentEvent() # CommentEvent | 

try:
    api_response = api_instance.bcf2_1_projects_topics_comments_events_update_0(projects_pk, id, comments_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_events_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **comments_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**CommentEvent**](CommentEvent.md)|  | 

### Return type

[**CommentEvent**](CommentEvent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_list**
> list[Comment] bcf2_1_projects_topics_comments_list(projects_pk, topics_pk)





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
    api_response = api_instance.bcf2_1_projects_topics_comments_list(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_list: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_partial_update**
> Comment bcf2_1_projects_topics_comments_partial_update(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Comment() # Comment | 

try:
    api_response = api_instance.bcf2_1_projects_topics_comments_partial_update(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_read**
> Comment bcf2_1_projects_topics_comments_read(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_comments_read(projects_pk, id, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_comments_update**
> Comment bcf2_1_projects_topics_comments_update(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Comment() # Comment | 

try:
    api_response = api_instance.bcf2_1_projects_topics_comments_update(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_comments_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Comment**](Comment.md)|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_create**
> Topic bcf2_1_projects_topics_create(projects_pk, data)





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
data = bimdata_api_client.Topic() # Topic | 

try:
    api_response = api_instance.bcf2_1_projects_topics_create(projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **data** | [**Topic**](Topic.md)|  | 

### Return type

[**Topic**](Topic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_delete**
> bcf2_1_projects_topics_delete(projects_pk, id)





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
id = 'id_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_delete(projects_pk, id)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_document_references_create**
> DocumentReference bcf2_1_projects_topics_document_references_create(projects_pk, topics_pk, data)





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
data = bimdata_api_client.DocumentReference() # DocumentReference | 

try:
    api_response = api_instance.bcf2_1_projects_topics_document_references_create(projects_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_document_references_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**DocumentReference**](DocumentReference.md)|  | 

### Return type

[**DocumentReference**](DocumentReference.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_document_references_delete**
> bcf2_1_projects_topics_document_references_delete(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_document_references_delete(projects_pk, id, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_document_references_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_document_references_list**
> list[DocumentReference] bcf2_1_projects_topics_document_references_list(projects_pk, topics_pk)





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
    api_response = api_instance.bcf2_1_projects_topics_document_references_list(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_document_references_list: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_document_references_partial_update**
> DocumentReference bcf2_1_projects_topics_document_references_partial_update(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.DocumentReference() # DocumentReference | 

try:
    api_response = api_instance.bcf2_1_projects_topics_document_references_partial_update(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_document_references_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**DocumentReference**](DocumentReference.md)|  | 

### Return type

[**DocumentReference**](DocumentReference.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_document_references_read**
> DocumentReference bcf2_1_projects_topics_document_references_read(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_document_references_read(projects_pk, id, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_document_references_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**DocumentReference**](DocumentReference.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_document_references_update**
> DocumentReference bcf2_1_projects_topics_document_references_update(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.DocumentReference() # DocumentReference | 

try:
    api_response = api_instance.bcf2_1_projects_topics_document_references_update(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_document_references_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**DocumentReference**](DocumentReference.md)|  | 

### Return type

[**DocumentReference**](DocumentReference.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_events_create**
> TopicEvents bcf2_1_projects_topics_events_create(projects_pk, data)





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
data = bimdata_api_client.TopicEvents() # TopicEvents | 

try:
    api_response = api_instance.bcf2_1_projects_topics_events_create(projects_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_events_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **data** | [**TopicEvents**](TopicEvents.md)|  | 

### Return type

[**TopicEvents**](TopicEvents.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_events_create_0**
> TopicEvents bcf2_1_projects_topics_events_create_0(projects_pk, topics_pk, data)





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
data = bimdata_api_client.TopicEvents() # TopicEvents | 

try:
    api_response = api_instance.bcf2_1_projects_topics_events_create_0(projects_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_events_create_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**TopicEvents**](TopicEvents.md)|  | 

### Return type

[**TopicEvents**](TopicEvents.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_events_delete**
> bcf2_1_projects_topics_events_delete(projects_pk, id)





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
id = 'id_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_events_delete(projects_pk, id)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_events_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_events_delete_0**
> bcf2_1_projects_topics_events_delete_0(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_events_delete_0(projects_pk, id, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_events_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_events_list**
> list[TopicEvents] bcf2_1_projects_topics_events_list(projects_pk)





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
    api_response = api_instance.bcf2_1_projects_topics_events_list(projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_events_list: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_events_list_0**
> list[TopicEvents] bcf2_1_projects_topics_events_list_0(projects_pk, topics_pk)





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
    api_response = api_instance.bcf2_1_projects_topics_events_list_0(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_events_list_0: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_events_partial_update**
> TopicEvents bcf2_1_projects_topics_events_partial_update(projects_pk, id, data)





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
id = 'id_example' # str | 
data = bimdata_api_client.TopicEvents() # TopicEvents | 

try:
    api_response = api_instance.bcf2_1_projects_topics_events_partial_update(projects_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_events_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**TopicEvents**](TopicEvents.md)|  | 

### Return type

[**TopicEvents**](TopicEvents.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_events_partial_update_0**
> TopicEvents bcf2_1_projects_topics_events_partial_update_0(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.TopicEvents() # TopicEvents | 

try:
    api_response = api_instance.bcf2_1_projects_topics_events_partial_update_0(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_events_partial_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**TopicEvents**](TopicEvents.md)|  | 

### Return type

[**TopicEvents**](TopicEvents.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_events_read**
> TopicEvents bcf2_1_projects_topics_events_read(projects_pk, id)





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
id = 'id_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_events_read(projects_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_events_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**TopicEvents**](TopicEvents.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_events_read_0**
> TopicEvents bcf2_1_projects_topics_events_read_0(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_events_read_0(projects_pk, id, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_events_read_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**TopicEvents**](TopicEvents.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_events_update**
> TopicEvents bcf2_1_projects_topics_events_update(projects_pk, id, data)





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
id = 'id_example' # str | 
data = bimdata_api_client.TopicEvents() # TopicEvents | 

try:
    api_response = api_instance.bcf2_1_projects_topics_events_update(projects_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_events_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**TopicEvents**](TopicEvents.md)|  | 

### Return type

[**TopicEvents**](TopicEvents.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_events_update_0**
> TopicEvents bcf2_1_projects_topics_events_update_0(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.TopicEvents() # TopicEvents | 

try:
    api_response = api_instance.bcf2_1_projects_topics_events_update_0(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_events_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**TopicEvents**](TopicEvents.md)|  | 

### Return type

[**TopicEvents**](TopicEvents.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_file_create**
> BimSnippet bcf2_1_projects_topics_file_create(projects_pk, topics_pk, data)





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
data = bimdata_api_client.BimSnippet() # BimSnippet | 

try:
    api_response = api_instance.bcf2_1_projects_topics_file_create(projects_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_file_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**BimSnippet**](BimSnippet.md)|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_file_delete**
> bcf2_1_projects_topics_file_delete(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_file_delete(projects_pk, id, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_file_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_file_list**
> list[BimSnippet] bcf2_1_projects_topics_file_list(projects_pk, topics_pk)





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
    api_response = api_instance.bcf2_1_projects_topics_file_list(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_file_list: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_file_partial_update**
> BimSnippet bcf2_1_projects_topics_file_partial_update(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.BimSnippet() # BimSnippet | 

try:
    api_response = api_instance.bcf2_1_projects_topics_file_partial_update(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_file_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**BimSnippet**](BimSnippet.md)|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_file_read**
> BimSnippet bcf2_1_projects_topics_file_read(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_file_read(projects_pk, id, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_file_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_file_update**
> BimSnippet bcf2_1_projects_topics_file_update(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.BimSnippet() # BimSnippet | 

try:
    api_response = api_instance.bcf2_1_projects_topics_file_update(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_file_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**BimSnippet**](BimSnippet.md)|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_list**
> list[Topic] bcf2_1_projects_topics_list(projects_pk)





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
    api_response = api_instance.bcf2_1_projects_topics_list(projects_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_list: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_partial_update**
> Topic bcf2_1_projects_topics_partial_update(projects_pk, id, data)





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
id = 'id_example' # str | 
data = bimdata_api_client.Topic() # Topic | 

try:
    api_response = api_instance.bcf2_1_projects_topics_partial_update(projects_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**Topic**](Topic.md)|  | 

### Return type

[**Topic**](Topic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_read**
> Topic bcf2_1_projects_topics_read(projects_pk, id)





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
id = 'id_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_read(projects_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**Topic**](Topic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_related_topics_create**
> RelatedTopic bcf2_1_projects_topics_related_topics_create(projects_pk, topics_pk, data)





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
data = bimdata_api_client.RelatedTopic() # RelatedTopic | 

try:
    api_response = api_instance.bcf2_1_projects_topics_related_topics_create(projects_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_related_topics_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**RelatedTopic**](RelatedTopic.md)|  | 

### Return type

[**RelatedTopic**](RelatedTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_related_topics_delete**
> bcf2_1_projects_topics_related_topics_delete(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_related_topics_delete(projects_pk, id, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_related_topics_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_related_topics_list**
> list[RelatedTopic] bcf2_1_projects_topics_related_topics_list(projects_pk, topics_pk)





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
    api_response = api_instance.bcf2_1_projects_topics_related_topics_list(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_related_topics_list: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_related_topics_partial_update**
> RelatedTopic bcf2_1_projects_topics_related_topics_partial_update(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.RelatedTopic() # RelatedTopic | 

try:
    api_response = api_instance.bcf2_1_projects_topics_related_topics_partial_update(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_related_topics_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**RelatedTopic**](RelatedTopic.md)|  | 

### Return type

[**RelatedTopic**](RelatedTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_related_topics_read**
> RelatedTopic bcf2_1_projects_topics_related_topics_read(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_related_topics_read(projects_pk, id, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_related_topics_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**RelatedTopic**](RelatedTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_related_topics_update**
> RelatedTopic bcf2_1_projects_topics_related_topics_update(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.RelatedTopic() # RelatedTopic | 

try:
    api_response = api_instance.bcf2_1_projects_topics_related_topics_update(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_related_topics_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**RelatedTopic**](RelatedTopic.md)|  | 

### Return type

[**RelatedTopic**](RelatedTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_snippet_create**
> BimSnippet bcf2_1_projects_topics_snippet_create(projects_pk, topics_pk, data)





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
data = bimdata_api_client.BimSnippet() # BimSnippet | 

try:
    api_response = api_instance.bcf2_1_projects_topics_snippet_create(projects_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_snippet_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**BimSnippet**](BimSnippet.md)|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_snippet_delete**
> bcf2_1_projects_topics_snippet_delete(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_snippet_delete(projects_pk, id, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_snippet_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_snippet_list**
> list[BimSnippet] bcf2_1_projects_topics_snippet_list(projects_pk, topics_pk)





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
    api_response = api_instance.bcf2_1_projects_topics_snippet_list(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_snippet_list: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_snippet_partial_update**
> BimSnippet bcf2_1_projects_topics_snippet_partial_update(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.BimSnippet() # BimSnippet | 

try:
    api_response = api_instance.bcf2_1_projects_topics_snippet_partial_update(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_snippet_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**BimSnippet**](BimSnippet.md)|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_snippet_read**
> BimSnippet bcf2_1_projects_topics_snippet_read(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_snippet_read(projects_pk, id, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_snippet_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_snippet_update**
> BimSnippet bcf2_1_projects_topics_snippet_update(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.BimSnippet() # BimSnippet | 

try:
    api_response = api_instance.bcf2_1_projects_topics_snippet_update(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_snippet_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**BimSnippet**](BimSnippet.md)|  | 

### Return type

[**BimSnippet**](BimSnippet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_update**
> Topic bcf2_1_projects_topics_update(projects_pk, id, data)





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
id = 'id_example' # str | 
data = bimdata_api_client.Topic() # Topic | 

try:
    api_response = api_instance.bcf2_1_projects_topics_update(projects_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**Topic**](Topic.md)|  | 

### Return type

[**Topic**](Topic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_bitmap_create**
> Bitmap bcf2_1_projects_topics_viewpoints_bitmap_create(viewpoints_pk, projects_pk, topics_pk, data)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Bitmap() # Bitmap | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_bitmap_create(viewpoints_pk, projects_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_bitmap_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Bitmap**](Bitmap.md)|  | 

### Return type

[**Bitmap**](Bitmap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_bitmap_delete**
> bcf2_1_projects_topics_viewpoints_bitmap_delete(viewpoints_pk, projects_pk, id, topics_pk)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_viewpoints_bitmap_delete(viewpoints_pk, projects_pk, id, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_bitmap_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_bitmap_list**
> list[Bitmap] bcf2_1_projects_topics_viewpoints_bitmap_list(viewpoints_pk, projects_pk, topics_pk)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_bitmap_list(viewpoints_pk, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_bitmap_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[Bitmap]**](Bitmap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_bitmap_partial_update**
> Bitmap bcf2_1_projects_topics_viewpoints_bitmap_partial_update(viewpoints_pk, projects_pk, id, topics_pk, data)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Bitmap() # Bitmap | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_bitmap_partial_update(viewpoints_pk, projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_bitmap_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Bitmap**](Bitmap.md)|  | 

### Return type

[**Bitmap**](Bitmap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_bitmap_read**
> Bitmap bcf2_1_projects_topics_viewpoints_bitmap_read(viewpoints_pk, projects_pk, id, topics_pk)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_bitmap_read(viewpoints_pk, projects_pk, id, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_bitmap_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**Bitmap**](Bitmap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_bitmap_update**
> Bitmap bcf2_1_projects_topics_viewpoints_bitmap_update(viewpoints_pk, projects_pk, id, topics_pk, data)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Bitmap() # Bitmap | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_bitmap_update(viewpoints_pk, projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_bitmap_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Bitmap**](Bitmap.md)|  | 

### Return type

[**Bitmap**](Bitmap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_coloring_create**
> Coloring bcf2_1_projects_topics_viewpoints_coloring_create(viewpoints_pk, projects_pk, topics_pk, data)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Coloring() # Coloring | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_coloring_create(viewpoints_pk, projects_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_coloring_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Coloring**](Coloring.md)|  | 

### Return type

[**Coloring**](Coloring.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_coloring_delete**
> bcf2_1_projects_topics_viewpoints_coloring_delete(viewpoints_pk, projects_pk, id, topics_pk)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_viewpoints_coloring_delete(viewpoints_pk, projects_pk, id, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_coloring_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_coloring_list**
> list[Coloring] bcf2_1_projects_topics_viewpoints_coloring_list(viewpoints_pk, projects_pk, topics_pk)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_coloring_list(viewpoints_pk, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_coloring_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[Coloring]**](Coloring.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_coloring_partial_update**
> Coloring bcf2_1_projects_topics_viewpoints_coloring_partial_update(viewpoints_pk, projects_pk, id, topics_pk, data)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Coloring() # Coloring | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_coloring_partial_update(viewpoints_pk, projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_coloring_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Coloring**](Coloring.md)|  | 

### Return type

[**Coloring**](Coloring.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_coloring_read**
> Coloring bcf2_1_projects_topics_viewpoints_coloring_read(viewpoints_pk, projects_pk, id, topics_pk)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_coloring_read(viewpoints_pk, projects_pk, id, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_coloring_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**Coloring**](Coloring.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_coloring_update**
> Coloring bcf2_1_projects_topics_viewpoints_coloring_update(viewpoints_pk, projects_pk, id, topics_pk, data)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Coloring() # Coloring | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_coloring_update(viewpoints_pk, projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_coloring_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Coloring**](Coloring.md)|  | 

### Return type

[**Coloring**](Coloring.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_create**
> Viewpoint bcf2_1_projects_topics_viewpoints_create(projects_pk, topics_pk, data)





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
data = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_create(projects_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Viewpoint**](Viewpoint.md)|  | 

### Return type

[**Viewpoint**](Viewpoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_delete**
> bcf2_1_projects_topics_viewpoints_delete(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_viewpoints_delete(projects_pk, id, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_list**
> list[Viewpoint] bcf2_1_projects_topics_viewpoints_list(projects_pk, topics_pk)





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
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_list(projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_list: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_partial_update**
> Viewpoint bcf2_1_projects_topics_viewpoints_partial_update(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_partial_update(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Viewpoint**](Viewpoint.md)|  | 

### Return type

[**Viewpoint**](Viewpoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_read**
> Viewpoint bcf2_1_projects_topics_viewpoints_read(projects_pk, id, topics_pk)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_read(projects_pk, id, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**Viewpoint**](Viewpoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_selection_create**
> Component bcf2_1_projects_topics_viewpoints_selection_create(viewpoints_pk, projects_pk, topics_pk, data)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Component() # Component | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_selection_create(viewpoints_pk, projects_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_selection_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Component**](Component.md)|  | 

### Return type

[**Component**](Component.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_selection_delete**
> bcf2_1_projects_topics_viewpoints_selection_delete(viewpoints_pk, projects_pk, id, topics_pk)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_viewpoints_selection_delete(viewpoints_pk, projects_pk, id, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_selection_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_selection_list**
> list[Component] bcf2_1_projects_topics_viewpoints_selection_list(viewpoints_pk, projects_pk, topics_pk)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_selection_list(viewpoints_pk, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_selection_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[Component]**](Component.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_selection_partial_update**
> Component bcf2_1_projects_topics_viewpoints_selection_partial_update(viewpoints_pk, projects_pk, id, topics_pk, data)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Component() # Component | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_selection_partial_update(viewpoints_pk, projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_selection_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Component**](Component.md)|  | 

### Return type

[**Component**](Component.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_selection_read**
> Component bcf2_1_projects_topics_viewpoints_selection_read(viewpoints_pk, projects_pk, id, topics_pk)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_selection_read(viewpoints_pk, projects_pk, id, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_selection_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**Component**](Component.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_selection_update**
> Component bcf2_1_projects_topics_viewpoints_selection_update(viewpoints_pk, projects_pk, id, topics_pk, data)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Component() # Component | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_selection_update(viewpoints_pk, projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_selection_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Component**](Component.md)|  | 

### Return type

[**Component**](Component.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_snapshot_list**
> list[Snapshot] bcf2_1_projects_topics_viewpoints_snapshot_list(viewpoints_pk, projects_pk, topics_pk)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_snapshot_list(viewpoints_pk, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_snapshot_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[Snapshot]**](Snapshot.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_update**
> Viewpoint bcf2_1_projects_topics_viewpoints_update(projects_pk, id, topics_pk, data)





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
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Viewpoint() # Viewpoint | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_update(projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Viewpoint**](Viewpoint.md)|  | 

### Return type

[**Viewpoint**](Viewpoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_visibility_create**
> Visibility bcf2_1_projects_topics_viewpoints_visibility_create(viewpoints_pk, projects_pk, topics_pk, data)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Visibility() # Visibility | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_visibility_create(viewpoints_pk, projects_pk, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_visibility_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Visibility**](Visibility.md)|  | 

### Return type

[**Visibility**](Visibility.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_visibility_delete**
> bcf2_1_projects_topics_viewpoints_visibility_delete(viewpoints_pk, projects_pk, id, topics_pk)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_instance.bcf2_1_projects_topics_viewpoints_visibility_delete(viewpoints_pk, projects_pk, id, topics_pk)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_visibility_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_visibility_list**
> list[Visibility] bcf2_1_projects_topics_viewpoints_visibility_list(viewpoints_pk, projects_pk, topics_pk)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_visibility_list(viewpoints_pk, projects_pk, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_visibility_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**list[Visibility]**](Visibility.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_visibility_partial_update**
> Visibility bcf2_1_projects_topics_viewpoints_visibility_partial_update(viewpoints_pk, projects_pk, id, topics_pk, data)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Visibility() # Visibility | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_visibility_partial_update(viewpoints_pk, projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_visibility_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Visibility**](Visibility.md)|  | 

### Return type

[**Visibility**](Visibility.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_visibility_read**
> Visibility bcf2_1_projects_topics_viewpoints_visibility_read(viewpoints_pk, projects_pk, id, topics_pk)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_visibility_read(viewpoints_pk, projects_pk, id, topics_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_visibility_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 

### Return type

[**Visibility**](Visibility.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_topics_viewpoints_visibility_update**
> Visibility bcf2_1_projects_topics_viewpoints_visibility_update(viewpoints_pk, projects_pk, id, topics_pk, data)





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
viewpoints_pk = 'viewpoints_pk_example' # str | 
projects_pk = 'projects_pk_example' # str | 
id = 'id_example' # str | 
topics_pk = 'topics_pk_example' # str | 
data = bimdata_api_client.Visibility() # Visibility | 

try:
    api_response = api_instance.bcf2_1_projects_topics_viewpoints_visibility_update(viewpoints_pk, projects_pk, id, topics_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_topics_viewpoints_visibility_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **viewpoints_pk** | **str**|  | 
 **projects_pk** | **str**|  | 
 **id** | **str**|  | 
 **topics_pk** | **str**|  | 
 **data** | [**Visibility**](Visibility.md)|  | 

### Return type

[**Visibility**](Visibility.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf2_1_projects_update**
> BcfProject bcf2_1_projects_update(id, data)





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
data = bimdata_api_client.BcfProject() # BcfProject | 

try:
    api_response = api_instance.bcf2_1_projects_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf2_1_projects_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**BcfProject**](BcfProject.md)|  | 

### Return type

[**BcfProject**](BcfProject.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf_versions_create**
> Version bcf_versions_create(data)





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
data = bimdata_api_client.Version() # Version | 

try:
    api_response = api_instance.bcf_versions_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf_versions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Version**](Version.md)|  | 

### Return type

[**Version**](Version.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf_versions_delete**
> bcf_versions_delete(id)





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
    api_instance.bcf_versions_delete(id)
except ApiException as e:
    print("Exception when calling BcfApi->bcf_versions_delete: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf_versions_list**
> list[Version] bcf_versions_list()





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
    api_response = api_instance.bcf_versions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf_versions_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Version]**](Version.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf_versions_partial_update**
> Version bcf_versions_partial_update(id, data)





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
data = bimdata_api_client.Version() # Version | 

try:
    api_response = api_instance.bcf_versions_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf_versions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Version**](Version.md)|  | 

### Return type

[**Version**](Version.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf_versions_read**
> Version bcf_versions_read(id)





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
    api_response = api_instance.bcf_versions_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf_versions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Version**](Version.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcf_versions_update**
> Version bcf_versions_update(id, data)





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
data = bimdata_api_client.Version() # Version | 

try:
    api_response = api_instance.bcf_versions_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BcfApi->bcf_versions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Version**](Version.md)|  | 

### Return type

[**Version**](Version.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

