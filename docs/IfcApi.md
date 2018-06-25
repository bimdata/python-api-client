# bimdata_api_client.IfcApi

All URIs are relative to *https://api-beta.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_ifc_classifications**](IfcApi.md#bulk_delete_ifc_classifications) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/list_destroy | 
[**bulk_delete_ifc_properties**](IfcApi.md#bulk_delete_ifc_properties) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/bulk_destroy | 
[**bulk_delete_ifc_property_definitions**](IfcApi.md#bulk_delete_ifc_property_definitions) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/bulk_destroy | 
[**bulk_delete_ifc_units**](IfcApi.md#bulk_delete_ifc_units) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/bulk_destroy | 
[**bulk_delete_property_set**](IfcApi.md#bulk_delete_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/bulk_destroy | 
[**bulk_full_update_elements**](IfcApi.md#bulk_full_update_elements) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/bulk_update | 
[**bulk_full_update_ifc_property**](IfcApi.md#bulk_full_update_ifc_property) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/bulk_update | 
[**bulk_remove_classifications_of_element**](IfcApi.md#bulk_remove_classifications_of_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification/bulk_destroy | 
[**bulk_remove_elements_from_classification**](IfcApi.md#bulk_remove_elements_from_classification) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/{ifc_classification_pk}/element/bulk_destroy | 
[**bulk_update_elements**](IfcApi.md#bulk_update_elements) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/bulk_update | 
[**bulk_update_ifc_property**](IfcApi.md#bulk_update_ifc_property) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/bulk_update | 
[**create_classification_element_relations**](IfcApi.md#create_classification_element_relations) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification-element | 
[**create_classifications_of_element**](IfcApi.md#create_classifications_of_element) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification | 
[**create_element**](IfcApi.md#create_element) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element | 
[**create_element_property_set**](IfcApi.md#create_element_property_set) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset | 
[**create_element_property_set_property**](IfcApi.md#create_element_property_set_property) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property | 
[**create_element_property_set_property_definition**](IfcApi.md#create_element_property_set_property_definition) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition | 
[**create_element_property_set_property_definition_unit**](IfcApi.md#create_element_property_set_property_definition_unit) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit | 
[**create_ifc_property_definition**](IfcApi.md#create_ifc_property_definition) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition | 
[**create_ifc_unit**](IfcApi.md#create_ifc_unit) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit | 
[**create_property_set**](IfcApi.md#create_property_set) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset | 
[**create_property_set_element_relations**](IfcApi.md#create_property_set_element_relations) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset-element | 
[**create_raw_elements**](IfcApi.md#create_raw_elements) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/raw | 
[**create_space**](IfcApi.md#create_space) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space | 
[**create_zone**](IfcApi.md#create_zone) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone | 
[**create_zone_space**](IfcApi.md#create_zone_space) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space | 
[**delete_element**](IfcApi.md#delete_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | 
[**delete_ifc**](IfcApi.md#delete_ifc) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | 
[**delete_ifc_property**](IfcApi.md#delete_ifc_property) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | 
[**delete_ifc_property_definition**](IfcApi.md#delete_ifc_property_definition) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | 
[**delete_ifc_unit**](IfcApi.md#delete_ifc_unit) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | 
[**delete_property_set**](IfcApi.md#delete_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | 
[**delete_space**](IfcApi.md#delete_space) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | 
[**delete_zone**](IfcApi.md#delete_zone) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | 
[**delete_zone_space**](IfcApi.md#delete_zone_space) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | 
[**full_update_element**](IfcApi.md#full_update_element) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | 
[**full_update_ifc**](IfcApi.md#full_update_ifc) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | 
[**full_update_ifc_property**](IfcApi.md#full_update_ifc_property) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | 
[**full_update_ifc_property_definition**](IfcApi.md#full_update_ifc_property_definition) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | 
[**full_update_ifc_unit**](IfcApi.md#full_update_ifc_unit) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | 
[**full_update_property_set**](IfcApi.md#full_update_property_set) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | 
[**full_update_space**](IfcApi.md#full_update_space) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | 
[**full_update_zone**](IfcApi.md#full_update_zone) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | 
[**full_update_zone_space**](IfcApi.md#full_update_zone_space) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | 
[**get_classifications_of_element**](IfcApi.md#get_classifications_of_element) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification | 
[**get_element**](IfcApi.md#get_element) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | 
[**get_element_property_set**](IfcApi.md#get_element_property_set) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{id} | 
[**get_element_property_set_properties**](IfcApi.md#get_element_property_set_properties) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property | 
[**get_element_property_set_property**](IfcApi.md#get_element_property_set_property) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{id} | 
[**get_element_property_set_property_definition**](IfcApi.md#get_element_property_set_property_definition) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{id} | 
[**get_element_property_set_property_definition_unit**](IfcApi.md#get_element_property_set_property_definition_unit) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit/{id} | 
[**get_element_property_set_property_definition_units**](IfcApi.md#get_element_property_set_property_definition_units) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit | 
[**get_element_property_set_property_definitions**](IfcApi.md#get_element_property_set_property_definitions) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition | 
[**get_element_property_sets**](IfcApi.md#get_element_property_sets) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset | 
[**get_elements**](IfcApi.md#get_elements) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element | 
[**get_elements_from_classification**](IfcApi.md#get_elements_from_classification) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/{ifc_classification_pk}/element | 
[**get_ifc**](IfcApi.md#get_ifc) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | 
[**get_ifc_bvh**](IfcApi.md#get_ifc_bvh) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/bvh | 
[**get_ifc_classifications**](IfcApi.md#get_ifc_classifications) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification | 
[**get_ifc_gltf**](IfcApi.md#get_ifc_gltf) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/gltf | 
[**get_ifc_map**](IfcApi.md#get_ifc_map) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/map | 
[**get_ifc_properties**](IfcApi.md#get_ifc_properties) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property | 
[**get_ifc_property**](IfcApi.md#get_ifc_property) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | 
[**get_ifc_property_definition**](IfcApi.md#get_ifc_property_definition) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | 
[**get_ifc_property_definitions**](IfcApi.md#get_ifc_property_definitions) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition | 
[**get_ifc_structure**](IfcApi.md#get_ifc_structure) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/structure | 
[**get_ifc_systems**](IfcApi.md#get_ifc_systems) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/systems | 
[**get_ifc_unit**](IfcApi.md#get_ifc_unit) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | 
[**get_ifc_units**](IfcApi.md#get_ifc_units) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit | 
[**get_ifcs**](IfcApi.md#get_ifcs) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc | 
[**get_property_set**](IfcApi.md#get_property_set) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | 
[**get_property_sets**](IfcApi.md#get_property_sets) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset | 
[**get_raw_elements**](IfcApi.md#get_raw_elements) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/raw | 
[**get_space**](IfcApi.md#get_space) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | 
[**get_spaces**](IfcApi.md#get_spaces) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space | 
[**get_zone**](IfcApi.md#get_zone) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | 
[**get_zone_space**](IfcApi.md#get_zone_space) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | 
[**get_zone_spaces**](IfcApi.md#get_zone_spaces) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space | 
[**get_zones**](IfcApi.md#get_zones) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone | 
[**list_classification_element_relations**](IfcApi.md#list_classification_element_relations) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification-element | 
[**remove_classification_of_element**](IfcApi.md#remove_classification_of_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification/{id} | 
[**remove_element_property_set**](IfcApi.md#remove_element_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{id} | 
[**remove_element_property_set_property**](IfcApi.md#remove_element_property_set_property) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{id} | 
[**remove_element_property_set_property_definition**](IfcApi.md#remove_element_property_set_property_definition) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{id} | 
[**remove_element_property_set_property_definition_unit**](IfcApi.md#remove_element_property_set_property_definition_unit) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit/{id} | 
[**remove_elements_from_classification**](IfcApi.md#remove_elements_from_classification) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/{ifc_classification_pk}/element/{uuid} | 
[**update_element**](IfcApi.md#update_element) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | 
[**update_ifc**](IfcApi.md#update_ifc) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | 
[**update_ifc_files**](IfcApi.md#update_ifc_files) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/files | 
[**update_ifc_property**](IfcApi.md#update_ifc_property) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | 
[**update_ifc_property_definition**](IfcApi.md#update_ifc_property_definition) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | 
[**update_ifc_unit**](IfcApi.md#update_ifc_unit) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | 
[**update_property_set**](IfcApi.md#update_property_set) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | 
[**update_space**](IfcApi.md#update_space) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | 
[**update_zone**](IfcApi.md#update_zone) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | 
[**update_zone_space**](IfcApi.md#update_zone_space) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | 


# **bulk_delete_ifc_classifications**
> bulk_delete_ifc_classifications(cloud_pk, ifc_pk, project_pk)



             Delete relation between filtered classifications (eg. /classifications?name=untec) and all ifc's elements.             No classification will be deleted on this endpoint, only the relation between ifc's elements and their classification.         

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.bulk_delete_ifc_classifications(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_ifc_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_ifc_properties**
> bulk_delete_ifc_properties(cloud_pk, ifc_pk, project_pk)



         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.bulk_delete_ifc_properties(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_ifc_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_ifc_property_definitions**
> bulk_delete_ifc_property_definitions(cloud_pk, ifc_pk, project_pk)



         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.bulk_delete_ifc_property_definitions(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_ifc_property_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_ifc_units**
> bulk_delete_ifc_units(cloud_pk, ifc_pk, project_pk)



         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.bulk_delete_ifc_units(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_ifc_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_property_set**
> bulk_delete_property_set(cloud_pk, ifc_pk, project_pk)



         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.bulk_delete_property_set(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_property_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_full_update_elements**
> list[Element] bulk_full_update_elements(cloud_pk, ifc_pk, project_pk, data)



         Bulk update.         Similar to update, but the body should be a list of objects to patch or put         The response will be a list (in the same order) of updated objects or of errors if any         If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Element()] # list[Element] | 

try:
    api_response = api_instance.bulk_full_update_elements(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_full_update_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**list[Element]**](Element.md)|  | 

### Return type

[**list[Element]**](Element.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_full_update_ifc_property**
> list[ModelProperty] bulk_full_update_ifc_property(cloud_pk, ifc_pk, project_pk, data)



         Bulk update.         Similar to update, but the body should be a list of objects to patch or put         The response will be a list (in the same order) of updated objects or of errors if any         If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ModelProperty()] # list[ModelProperty] | 

try:
    api_response = api_instance.bulk_full_update_ifc_property(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_full_update_ifc_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**list[ModelProperty]**](ModelProperty.md)|  | 

### Return type

[**list[ModelProperty]**](ModelProperty.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_remove_classifications_of_element**
> bulk_remove_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk)



         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.bulk_remove_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_remove_classifications_of_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_remove_elements_from_classification**
> bulk_remove_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk)



         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_classification_pk = 'ifc_classification_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.bulk_remove_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_remove_elements_from_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_classification_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_elements**
> list[Element] bulk_update_elements(cloud_pk, ifc_pk, project_pk, data)



         Bulk update.         Similar to update, but the body should be a list of objects to patch or put         The response will be a list (in the same order) of updated objects or of errors if any         If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Element()] # list[Element] | 

try:
    api_response = api_instance.bulk_update_elements(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_update_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**list[Element]**](Element.md)|  | 

### Return type

[**list[Element]**](Element.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_ifc_property**
> list[ModelProperty] bulk_update_ifc_property(cloud_pk, ifc_pk, project_pk, data)



         Bulk update.         Similar to update, but the body should be a list of objects to patch or put         The response will be a list (in the same order) of updated objects or of errors if any         If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ModelProperty()] # list[ModelProperty] | 

try:
    api_response = api_instance.bulk_update_ifc_property(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_update_ifc_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**list[ModelProperty]**](ModelProperty.md)|  | 

### Return type

[**list[ModelProperty]**](ModelProperty.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_classification_element_relations**
> create_classification_element_relations(cloud_pk, ifc_pk, project_pk, data)



             create association between existing classification and existing element         

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ElementClassificationRelation()] # list[ElementClassificationRelation] | 

try:
    api_instance.create_classification_element_relations(cloud_pk, ifc_pk, project_pk, data)
except ApiException as e:
    print("Exception when calling IfcApi->create_classification_element_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**list[ElementClassificationRelation]**](ElementClassificationRelation.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_classifications_of_element**
> list[Classification] create_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk, data)



         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors          If classification created already exists, it will just be added to item's classifications and will not be duplicated     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Classification()] # list[Classification] | 

try:
    api_response = api_instance.create_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_classifications_of_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**list[Classification]**](Classification.md)|  | 

### Return type

[**list[Classification]**](Classification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_element**
> list[Element] create_element(cloud_pk, ifc_pk, project_pk, data)



         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Element()] # list[Element] | 

try:
    api_response = api_instance.create_element(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**list[Element]**](Element.md)|  | 

### Return type

[**list[Element]**](Element.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_element_property_set**
> create_element_property_set(cloud_pk, element_uuid, ifc_pk, project_pk, data)



         Create an property_set that will be automatically linked to the element     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.PropertySet() # PropertySet | 

try:
    api_instance.create_element_property_set(cloud_pk, element_uuid, ifc_pk, project_pk, data)
except ApiException as e:
    print("Exception when calling IfcApi->create_element_property_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**PropertySet**](PropertySet.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_element_property_set_property**
> ModelProperty create_element_property_set_property(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.ModelProperty() # ModelProperty | 

try:
    api_response = api_instance.create_element_property_set_property(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_element_property_set_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **propertyset_pk** | **str**|  | 
 **data** | [**ModelProperty**](ModelProperty.md)|  | 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_element_property_set_property_definition**
> PropertyDefinition create_element_property_set_property_definition(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.PropertyDefinition() # PropertyDefinition | 

try:
    api_response = api_instance.create_element_property_set_property_definition(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_element_property_set_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **property_pk** | **str**|  | 
 **propertyset_pk** | **str**|  | 
 **data** | [**PropertyDefinition**](PropertyDefinition.md)|  | 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_element_property_set_property_definition_unit**
> Unit create_element_property_set_property_definition_unit(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.Unit() # Unit | 

try:
    api_response = api_instance.create_element_property_set_property_definition_unit(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_element_property_set_property_definition_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **property_pk** | **str**|  | 
 **propertydefinition_pk** | **str**|  | 
 **propertyset_pk** | **str**|  | 
 **data** | [**Unit**](Unit.md)|  | 

### Return type

[**Unit**](Unit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ifc_property_definition**
> list[PropertyDefinition] create_ifc_property_definition(cloud_pk, ifc_pk, project_pk, data)



         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors          If classification created already exists, it will just be added to item's classifications and will not be duplicated     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.PropertyDefinition()] # list[PropertyDefinition] | 

try:
    api_response = api_instance.create_ifc_property_definition(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_ifc_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**list[PropertyDefinition]**](PropertyDefinition.md)|  | 

### Return type

[**list[PropertyDefinition]**](PropertyDefinition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ifc_unit**
> list[Unit] create_ifc_unit(cloud_pk, ifc_pk, project_pk, data)



         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors          If classification created already exists, it will just be added to item's classifications and will not be duplicated     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Unit()] # list[Unit] | 

try:
    api_response = api_instance.create_ifc_unit(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_ifc_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**list[Unit]**](Unit.md)|  | 

### Return type

[**list[Unit]**](Unit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_property_set**
> list[PropertySet] create_property_set(cloud_pk, ifc_pk, project_pk, data)



         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors          If classification created already exists, it will just be added to item's classifications and will not be duplicated     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.PropertySet()] # list[PropertySet] | 

try:
    api_response = api_instance.create_property_set(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_property_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**list[PropertySet]**](PropertySet.md)|  | 

### Return type

[**list[PropertySet]**](PropertySet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_property_set_element_relations**
> create_property_set_element_relations(cloud_pk, ifc_pk, project_pk, data)



             create association between existing classification and existing element         

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ElementPropertySetRelation()] # list[ElementPropertySetRelation] | 

try:
    api_instance.create_property_set_element_relations(cloud_pk, ifc_pk, project_pk, data)
except ApiException as e:
    print("Exception when calling IfcApi->create_property_set_element_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**list[ElementPropertySetRelation]**](ElementPropertySetRelation.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_raw_elements**
> create_raw_elements(cloud_pk, ifc_pk, project_pk, data)



         You can use the same optimized structure to post multiple elements ,property_sets, properties, definitions and units at once.         If the structure is malformed, an error 500 without more explaination will be returned         

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Element() # Element | 

try:
    api_instance.create_raw_elements(cloud_pk, ifc_pk, project_pk, data)
except ApiException as e:
    print("Exception when calling IfcApi->create_raw_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**Element**](Element.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_space**
> list[Space] create_space(cloud_pk, ifc_pk, project_pk, data)



         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Space()] # list[Space] | 

try:
    api_response = api_instance.create_space(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**list[Space]**](Space.md)|  | 

### Return type

[**list[Space]**](Space.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_zone**
> list[Zone] create_zone(cloud_pk, ifc_pk, project_pk, data)



         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Zone()] # list[Zone] | 

try:
    api_response = api_instance.create_zone(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**list[Zone]**](Zone.md)|  | 

### Return type

[**list[Zone]**](Zone.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_zone_space**
> ZoneSpace create_zone_space(cloud_pk, ifc_pk, project_pk, zone_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = bimdata_api_client.ZoneSpace() # ZoneSpace | 

try:
    api_response = api_instance.create_zone_space(cloud_pk, ifc_pk, project_pk, zone_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_zone_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **zone_pk** | **str**|  | 
 **data** | [**ZoneSpace**](ZoneSpace.md)|  | 

### Return type

[**ZoneSpace**](ZoneSpace.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_element**
> delete_element(cloud_pk, ifc_pk, project_pk, uuid)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

try:
    api_instance.delete_element(cloud_pk, ifc_pk, project_pk, uuid)
except ApiException as e:
    print("Exception when calling IfcApi->delete_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **uuid** | **str**| IFC element or element type UUID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ifc**
> delete_ifc(cloud_pk, id, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    api_instance.delete_ifc(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc. | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ifc_property**
> delete_ifc_property(cloud_pk, id, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.delete_ifc_property(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ifc_property_definition**
> delete_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.delete_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ifc_unit**
> delete_ifc_unit(cloud_pk, id, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.delete_ifc_unit(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property_set**
> delete_property_set(cloud_pk, id, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.delete_property_set(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_property_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_space**
> delete_space(cloud_pk, id, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.delete_space(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this space. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone**
> delete_zone(cloud_pk, id, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.delete_zone(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this zone. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone_space**
> delete_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 

try:
    api_instance.delete_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_zone_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this space. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **zone_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_element**
> Element full_update_element(cloud_pk, ifc_pk, project_pk, uuid, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID
data = bimdata_api_client.Element() # Element | 

try:
    api_response = api_instance.full_update_element(cloud_pk, ifc_pk, project_pk, uuid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **uuid** | **str**| IFC element or element type UUID | 
 **data** | [**Element**](Element.md)|  | 

### Return type

[**Element**](Element.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_ifc**
> Ifc full_update_ifc(cloud_pk, id, project_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Ifc() # Ifc | 

try:
    api_response = api_instance.full_update_ifc(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc. | 
 **project_pk** | **str**|  | 
 **data** | [**Ifc**](Ifc.md)|  | 

### Return type

[**Ifc**](Ifc.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_ifc_property**
> ModelProperty full_update_ifc_property(cloud_pk, id, ifc_pk, project_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.ModelProperty() # ModelProperty | 

try:
    api_response = api_instance.full_update_ifc_property(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**ModelProperty**](ModelProperty.md)|  | 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_ifc_property_definition**
> PropertyDefinition full_update_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.PropertyDefinition() # PropertyDefinition | 

try:
    api_response = api_instance.full_update_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**PropertyDefinition**](PropertyDefinition.md)|  | 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_ifc_unit**
> Unit full_update_ifc_unit(cloud_pk, id, ifc_pk, project_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Unit() # Unit | 

try:
    api_response = api_instance.full_update_ifc_unit(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**Unit**](Unit.md)|  | 

### Return type

[**Unit**](Unit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_property_set**
> PropertySet full_update_property_set(cloud_pk, id, ifc_pk, project_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.PropertySet() # PropertySet | 

try:
    api_response = api_instance.full_update_property_set(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_property_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**PropertySet**](PropertySet.md)|  | 

### Return type

[**PropertySet**](PropertySet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_space**
> Space full_update_space(cloud_pk, id, ifc_pk, project_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Space() # Space | 

try:
    api_response = api_instance.full_update_space(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this space. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**Space**](Space.md)|  | 

### Return type

[**Space**](Space.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_zone**
> Zone full_update_zone(cloud_pk, id, ifc_pk, project_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Zone() # Zone | 

try:
    api_response = api_instance.full_update_zone(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this zone. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**Zone**](Zone.md)|  | 

### Return type

[**Zone**](Zone.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_zone_space**
> ZoneSpace full_update_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = bimdata_api_client.ZoneSpace() # ZoneSpace | 

try:
    api_response = api_instance.full_update_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_zone_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this space. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **zone_pk** | **str**|  | 
 **data** | [**ZoneSpace**](ZoneSpace.md)|  | 

### Return type

[**ZoneSpace**](ZoneSpace.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classifications_of_element**
> list[Classification] get_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_classifications_of_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Classification]**](Classification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element**
> Element get_element(cloud_pk, ifc_pk, project_pk, uuid)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

try:
    api_response = api_instance.get_element(cloud_pk, ifc_pk, project_pk, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **uuid** | **str**| IFC element or element type UUID | 

### Return type

[**Element**](Element.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_set**
> PropertySet get_element_property_set(cloud_pk, element_uuid, id, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_element_property_set(cloud_pk, element_uuid, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property set. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**PropertySet**](PropertySet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_set_properties**
> list[ModelProperty] get_element_property_set_properties(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    api_response = api_instance.get_element_property_set_properties(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **propertyset_pk** | **str**|  | 

### Return type

[**list[ModelProperty]**](ModelProperty.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_set_property**
> ModelProperty get_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    api_response = api_instance.get_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **propertyset_pk** | **str**|  | 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_set_property_definition**
> PropertyDefinition get_element_property_set_property_definition(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    api_response = api_instance.get_element_property_set_property_definition(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property definition. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **property_pk** | **str**|  | 
 **propertyset_pk** | **str**|  | 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_set_property_definition_unit**
> Unit get_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    api_response = api_instance.get_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property_definition_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **id** | **int**| A unique integer value identifying this unit. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **property_pk** | **str**|  | 
 **propertydefinition_pk** | **str**|  | 
 **propertyset_pk** | **str**|  | 

### Return type

[**Unit**](Unit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_set_property_definition_units**
> list[Unit] get_element_property_set_property_definition_units(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    api_response = api_instance.get_element_property_set_property_definition_units(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property_definition_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **property_pk** | **str**|  | 
 **propertydefinition_pk** | **str**|  | 
 **propertyset_pk** | **str**|  | 

### Return type

[**list[Unit]**](Unit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_set_property_definitions**
> list[PropertyDefinition] get_element_property_set_property_definitions(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    api_response = api_instance.get_element_property_set_property_definitions(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **property_pk** | **str**|  | 
 **propertyset_pk** | **str**|  | 

### Return type

[**list[PropertyDefinition]**](PropertyDefinition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_sets**
> list[PropertySet] get_element_property_sets(cloud_pk, element_uuid, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_element_property_sets(cloud_pk, element_uuid, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[PropertySet]**](PropertySet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_elements**
> list[Element] get_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
type = 'type_example' # str | Filter the returned list by type (optional)
classification = 'classification_example' # str | Filter the returned list by classification (optional)
classification__notation = 'classification__notation_example' # str | Filter the returned list by classification__notation (optional)

try:
    api_response = api_instance.get_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **type** | **str**| Filter the returned list by type | [optional] 
 **classification** | **str**| Filter the returned list by classification | [optional] 
 **classification__notation** | **str**| Filter the returned list by classification__notation | [optional] 

### Return type

[**list[Element]**](Element.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_elements_from_classification**
> list[Element] get_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_classification_pk = 'ifc_classification_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_elements_from_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_classification_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Element]**](Element.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc**
> Ifc get_ifc(cloud_pk, id, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_ifc(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc. | 
 **project_pk** | **str**|  | 

### Return type

[**Ifc**](Ifc.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_bvh**
> get_ifc_bvh(cloud_pk, id, project_pk)



         DEPRECATED: Now, retrieve the file url in the ifc object itself         Returns the bvh file         

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    api_instance.get_ifc_bvh(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_bvh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc. | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_classifications**
> list[Classification] get_ifc_classifications(cloud_pk, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_ifc_classifications(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Classification]**](Classification.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_gltf**
> get_ifc_gltf(cloud_pk, id, project_pk)



         DEPRECATED: Now, retrieve the file url in the ifc object itself         Returns the gltf file         

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    api_instance.get_ifc_gltf(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_gltf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc. | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_map**
> get_ifc_map(cloud_pk, id, project_pk)



         DEPRECATED: Now, retrieve the file url in the ifc object itself         Returns the map file         

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    api_instance.get_ifc_map(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc. | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_properties**
> list[ModelProperty] get_ifc_properties(cloud_pk, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_ifc_properties(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[ModelProperty]**](ModelProperty.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_property**
> ModelProperty get_ifc_property(cloud_pk, id, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_ifc_property(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_property_definition**
> PropertyDefinition get_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_property_definitions**
> list[PropertyDefinition] get_ifc_property_definitions(cloud_pk, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_ifc_property_definitions(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_property_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[PropertyDefinition]**](PropertyDefinition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_structure**
> get_ifc_structure(cloud_pk, id, project_pk)



         DEPRECATED: Now, retrieve the file url in the ifc object itself         Returns the structure file         

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    api_instance.get_ifc_structure(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_structure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc. | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_systems**
> get_ifc_systems(cloud_pk, id, project_pk)



         DEPRECATED: Now, retrieve the file url in the ifc object itself         Returns the system file         

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    api_instance.get_ifc_systems(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc. | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_unit**
> Unit get_ifc_unit(cloud_pk, id, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_ifc_unit(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**Unit**](Unit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_units**
> list[Unit] get_ifc_units(cloud_pk, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_ifc_units(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Unit]**](Unit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifcs**
> list[Ifc] get_ifcs(cloud_pk, project_pk, status=status)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
status = 'status_example' # str | Filter the returned list by status (optional)

try:
    api_response = api_instance.get_ifcs(cloud_pk, project_pk, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifcs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **status** | **str**| Filter the returned list by status | [optional] 

### Return type

[**list[Ifc]**](Ifc.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property_set**
> PropertySet get_property_set(cloud_pk, id, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_property_set(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_property_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**PropertySet**](PropertySet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property_sets**
> list[PropertySet] get_property_sets(cloud_pk, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_property_sets(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_property_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[PropertySet]**](PropertySet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_elements**
> get_raw_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)



         Returns elements ,property_sets, properties, definitions and units in a optimized structure         

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
type = 'type_example' # str | Filter the returned list by type (optional)
classification = 'classification_example' # str | Filter the returned list by classification (optional)
classification__notation = 'classification__notation_example' # str | Filter the returned list by classification__notation (optional)

try:
    api_instance.get_raw_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)
except ApiException as e:
    print("Exception when calling IfcApi->get_raw_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **type** | **str**| Filter the returned list by type | [optional] 
 **classification** | **str**| Filter the returned list by classification | [optional] 
 **classification__notation** | **str**| Filter the returned list by classification__notation | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space**
> Space get_space(cloud_pk, id, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_space(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this space. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**Space**](Space.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spaces**
> list[Space] get_spaces(cloud_pk, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_spaces(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Space]**](Space.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone**
> Zone get_zone(cloud_pk, id, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_zone(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this zone. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**Zone**](Zone.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_space**
> ZoneSpace get_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 

try:
    api_response = api_instance.get_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_zone_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this space. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **zone_pk** | **str**|  | 

### Return type

[**ZoneSpace**](ZoneSpace.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_spaces**
> list[ZoneSpace] get_zone_spaces(cloud_pk, ifc_pk, project_pk, zone_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 

try:
    api_response = api_instance.get_zone_spaces(cloud_pk, ifc_pk, project_pk, zone_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_zone_spaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **zone_pk** | **str**|  | 

### Return type

[**list[ZoneSpace]**](ZoneSpace.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zones**
> list[Zone] get_zones(cloud_pk, ifc_pk, project_pk, color=color)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
color = 'color_example' # str | Filter the returned list by color (optional)

try:
    api_response = api_instance.get_zones(cloud_pk, ifc_pk, project_pk, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_zones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **color** | **str**| Filter the returned list by color | [optional] 

### Return type

[**list[Zone]**](Zone.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_classification_element_relations**
> list[ElementClassificationRelation] list_classification_element_relations(cloud_pk, ifc_pk, project_pk)



             list association between classifications and elements         

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.list_classification_element_relations(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->list_classification_element_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[ElementClassificationRelation]**](ElementClassificationRelation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_classification_of_element**
> remove_classification_of_element(cloud_pk, element_uuid, id, ifc_pk, project_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.remove_classification_of_element(cloud_pk, element_uuid, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_classification_of_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **id** | **int**| A unique integer value identifying this classification. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_element_property_set**
> remove_element_property_set(cloud_pk, element_uuid, id, ifc_pk, project_pk)



         Delete the relation between the element and the property set. Does not delete any object     

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.remove_element_property_set(cloud_pk, element_uuid, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_element_property_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property set. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_element_property_set_property**
> remove_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    api_instance.remove_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_element_property_set_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **propertyset_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_element_property_set_property_definition**
> remove_element_property_set_property_definition(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    api_instance.remove_element_property_set_property_definition(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_element_property_set_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property definition. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **property_pk** | **str**|  | 
 **propertyset_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_element_property_set_property_definition_unit**
> remove_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    api_instance.remove_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_element_property_set_property_definition_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **id** | **int**| A unique integer value identifying this unit. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **property_pk** | **str**|  | 
 **propertydefinition_pk** | **str**|  | 
 **propertyset_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_elements_from_classification**
> remove_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk, uuid)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_classification_pk = 'ifc_classification_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | 

try:
    api_instance.remove_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk, uuid)
except ApiException as e:
    print("Exception when calling IfcApi->remove_elements_from_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_classification_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_element**
> Element update_element(cloud_pk, ifc_pk, project_pk, uuid, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID
data = bimdata_api_client.Element() # Element | 

try:
    api_response = api_instance.update_element(cloud_pk, ifc_pk, project_pk, uuid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **uuid** | **str**| IFC element or element type UUID | 
 **data** | [**Element**](Element.md)|  | 

### Return type

[**Element**](Element.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ifc**
> Ifc update_ifc(cloud_pk, id, project_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Ifc() # Ifc | 

try:
    api_response = api_instance.update_ifc(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc. | 
 **project_pk** | **str**|  | 
 **data** | [**Ifc**](Ifc.md)|  | 

### Return type

[**Ifc**](Ifc.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ifc_files**
> IfcFiles update_ifc_files(cloud_pk, id, project_pk, structure_file=structure_file, systems_file=systems_file, map_file=map_file, gltf_file=gltf_file, bvh_tree_file=bvh_tree_file)



         Patch ifc files (gltf, structure, svg, etc)         

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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
structure_file = '/path/to/file.txt' # file |  (optional)
systems_file = '/path/to/file.txt' # file |  (optional)
map_file = '/path/to/file.txt' # file |  (optional)
gltf_file = '/path/to/file.txt' # file |  (optional)
bvh_tree_file = '/path/to/file.txt' # file |  (optional)

try:
    api_response = api_instance.update_ifc_files(cloud_pk, id, project_pk, structure_file=structure_file, systems_file=systems_file, map_file=map_file, gltf_file=gltf_file, bvh_tree_file=bvh_tree_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc. | 
 **project_pk** | **str**|  | 
 **structure_file** | **file**|  | [optional] 
 **systems_file** | **file**|  | [optional] 
 **map_file** | **file**|  | [optional] 
 **gltf_file** | **file**|  | [optional] 
 **bvh_tree_file** | **file**|  | [optional] 

### Return type

[**IfcFiles**](IfcFiles.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ifc_property**
> ModelProperty update_ifc_property(cloud_pk, id, ifc_pk, project_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.ModelProperty() # ModelProperty | 

try:
    api_response = api_instance.update_ifc_property(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**ModelProperty**](ModelProperty.md)|  | 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ifc_property_definition**
> PropertyDefinition update_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.PropertyDefinition() # PropertyDefinition | 

try:
    api_response = api_instance.update_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**PropertyDefinition**](PropertyDefinition.md)|  | 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ifc_unit**
> Unit update_ifc_unit(cloud_pk, id, ifc_pk, project_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Unit() # Unit | 

try:
    api_response = api_instance.update_ifc_unit(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**Unit**](Unit.md)|  | 

### Return type

[**Unit**](Unit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_property_set**
> PropertySet update_property_set(cloud_pk, id, ifc_pk, project_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.PropertySet() # PropertySet | 

try:
    api_response = api_instance.update_property_set(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_property_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**PropertySet**](PropertySet.md)|  | 

### Return type

[**PropertySet**](PropertySet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_space**
> Space update_space(cloud_pk, id, ifc_pk, project_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Space() # Space | 

try:
    api_response = api_instance.update_space(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this space. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**Space**](Space.md)|  | 

### Return type

[**Space**](Space.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zone**
> Zone update_zone(cloud_pk, id, ifc_pk, project_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Zone() # Zone | 

try:
    api_response = api_instance.update_zone(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this zone. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**Zone**](Zone.md)|  | 

### Return type

[**Zone**](Zone.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zone_space**
> ZoneSpace update_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk, data)





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
api_instance = bimdata_api_client.IfcApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = bimdata_api_client.ZoneSpace() # ZoneSpace | 

try:
    api_response = api_instance.update_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_zone_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this space. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **zone_pk** | **str**|  | 
 **data** | [**ZoneSpace**](ZoneSpace.md)|  | 

### Return type

[**ZoneSpace**](ZoneSpace.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

