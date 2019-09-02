# openapi_client.IfcApi

All URIs are relative to *https://api-beta.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_ifc_classifications**](IfcApi.md#bulk_delete_ifc_classifications) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/list_destroy | Remove all classifications from model&#39;s elements
[**bulk_delete_ifc_properties**](IfcApi.md#bulk_delete_ifc_properties) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/bulk_destroy | Delete many Property of a model
[**bulk_delete_ifc_property_definitions**](IfcApi.md#bulk_delete_ifc_property_definitions) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/bulk_destroy | Delete many PropertyDefinitions of a model
[**bulk_delete_ifc_units**](IfcApi.md#bulk_delete_ifc_units) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/bulk_destroy | Delete many Units of a model
[**bulk_delete_property_set**](IfcApi.md#bulk_delete_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/bulk_destroy | Delete many PropertySet of a model
[**bulk_full_update_elements**](IfcApi.md#bulk_full_update_elements) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/bulk_update | Update many elements at once (only changing fields may be defined)
[**bulk_full_update_ifc_property**](IfcApi.md#bulk_full_update_ifc_property) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/bulk_update | Update some fields of many properties of a model
[**bulk_remove_classifications_of_element**](IfcApi.md#bulk_remove_classifications_of_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification/bulk_destroy | Remove many classifications from an element
[**bulk_remove_elements_from_classification**](IfcApi.md#bulk_remove_elements_from_classification) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/{ifc_classification_pk}/element/bulk_destroy | Remove the classifications from all elements
[**bulk_update_elements**](IfcApi.md#bulk_update_elements) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/bulk_update | Update many elements at once (all field must be defined)
[**bulk_update_ifc_property**](IfcApi.md#bulk_update_ifc_property) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/bulk_update | Update all fields of many properties of a model
[**cloud_project_ifc_processorhandler_partial_update**](IfcApi.md#cloud_project_ifc_processorhandler_partial_update) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/processorhandler/{id} | 
[**create_classification_element_relations**](IfcApi.md#create_classification_element_relations) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification-element | Create association between existing classification and existing element
[**create_classifications_of_element**](IfcApi.md#create_classifications_of_element) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification | Create one or many classifications to an element
[**create_element**](IfcApi.md#create_element) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element | Create an element in the model
[**create_element_property_set**](IfcApi.md#create_element_property_set) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset | Create a PropertySets to an element
[**create_element_property_set_property**](IfcApi.md#create_element_property_set_property) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property | Create a property to a PropertySet
[**create_element_property_set_property_definition**](IfcApi.md#create_element_property_set_property_definition) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition | Create a Definition to a Property
[**create_element_property_set_property_definition_unit**](IfcApi.md#create_element_property_set_property_definition_unit) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit | Create a Unit to a Definition
[**create_ifc_property_definition**](IfcApi.md#create_ifc_property_definition) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition | Create a PropertyDefinition on the model
[**create_ifc_unit**](IfcApi.md#create_ifc_unit) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit | Create a Unit on a model
[**create_property_set**](IfcApi.md#create_property_set) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset | Create a PropertySet
[**create_property_set_element_relations**](IfcApi.md#create_property_set_element_relations) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset-element | Create association between PropertySet and element
[**create_raw_elements**](IfcApi.md#create_raw_elements) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/raw | Create elements in an optimized format
[**create_space**](IfcApi.md#create_space) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space | Create a space in the model
[**create_zone**](IfcApi.md#create_zone) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone | Create a zone in the model
[**create_zone_space**](IfcApi.md#create_zone_space) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space | Create a space in a zone
[**delete_element**](IfcApi.md#delete_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | Delete a zone of a model
[**delete_ifc**](IfcApi.md#delete_ifc) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | Delete a model
[**delete_ifc_property**](IfcApi.md#delete_ifc_property) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | Delete a Property of a model
[**delete_ifc_property_definition**](IfcApi.md#delete_ifc_property_definition) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | Delete a PropertyDefinitions of a model
[**delete_ifc_unit**](IfcApi.md#delete_ifc_unit) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | Delete a Unit of a model
[**delete_property_set**](IfcApi.md#delete_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | Delete a PropertySet of a model
[**delete_space**](IfcApi.md#delete_space) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | Delete a space
[**delete_zone**](IfcApi.md#delete_zone) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | Delete a zone of a model
[**delete_zone_space**](IfcApi.md#delete_zone_space) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | Delete a space of a zone
[**export_ifc**](IfcApi.md#export_ifc) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/export | Export IFC
[**full_update_element**](IfcApi.md#full_update_element) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | Update all fields of an element
[**full_update_ifc**](IfcApi.md#full_update_ifc) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | Update all fields of a model
[**full_update_ifc_property**](IfcApi.md#full_update_ifc_property) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | Update some fields of a Property
[**full_update_ifc_property_definition**](IfcApi.md#full_update_ifc_property_definition) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | Update all fields of many PropertyDefinitions of a model
[**full_update_ifc_unit**](IfcApi.md#full_update_ifc_unit) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | Update all fields of a Unit of a model
[**full_update_property_set**](IfcApi.md#full_update_property_set) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | Update all fields of a PropertySet
[**full_update_space**](IfcApi.md#full_update_space) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | Update all fields of a space
[**full_update_zone**](IfcApi.md#full_update_zone) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | Update all fields of a zone
[**full_update_zone_space**](IfcApi.md#full_update_zone_space) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | Update all fields of a space
[**get_classifications_of_element**](IfcApi.md#get_classifications_of_element) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification | Retrieve all classifications of an element
[**get_element**](IfcApi.md#get_element) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | Retrieve an element of a model
[**get_element_property_set**](IfcApi.md#get_element_property_set) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{id} | Retrieve a PropertySet of an element
[**get_element_property_set_properties**](IfcApi.md#get_element_property_set_properties) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property | Retrieve all Properties of a PropertySet
[**get_element_property_set_property**](IfcApi.md#get_element_property_set_property) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{id} | Retrieve a Property of a PropertySet
[**get_element_property_set_property_definition**](IfcApi.md#get_element_property_set_property_definition) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{id} | Retrieve a Definition of a Property
[**get_element_property_set_property_definition_unit**](IfcApi.md#get_element_property_set_property_definition_unit) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit/{id} | Retrieve a Unit of a Definition
[**get_element_property_set_property_definition_units**](IfcApi.md#get_element_property_set_property_definition_units) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit | Retrieve all Units of a Definition
[**get_element_property_set_property_definitions**](IfcApi.md#get_element_property_set_property_definitions) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition | Retrieve all Definitions of a PropertySet
[**get_element_property_sets**](IfcApi.md#get_element_property_sets) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset | Retrieve all PropertySets of an element
[**get_elements**](IfcApi.md#get_elements) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element | Retrieve all elements of a model
[**get_elements_from_classification**](IfcApi.md#get_elements_from_classification) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/{ifc_classification_pk}/element | Retrieve all elements with the classification
[**get_ifc**](IfcApi.md#get_ifc) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | Retrieve one model
[**get_ifc_bvh**](IfcApi.md#get_ifc_bvh) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/map | Get svg file
[**get_ifc_classifications**](IfcApi.md#get_ifc_classifications) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification | Retrieve all classifications in a model
[**get_ifc_gltf**](IfcApi.md#get_ifc_gltf) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/gltf | Get gltf file
[**get_ifc_map**](IfcApi.md#get_ifc_map) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/bvh | Get bvh file
[**get_ifc_properties**](IfcApi.md#get_ifc_properties) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property | Retrieve all Properties of a model
[**get_ifc_property**](IfcApi.md#get_ifc_property) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | Retrieve a Property of a model
[**get_ifc_property_definition**](IfcApi.md#get_ifc_property_definition) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | Retrieve a PropertyDefinition of a model
[**get_ifc_property_definitions**](IfcApi.md#get_ifc_property_definitions) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition | Retrieve all PropertyDefinitions of a model
[**get_ifc_structure**](IfcApi.md#get_ifc_structure) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/structure | Get structure file
[**get_ifc_systems**](IfcApi.md#get_ifc_systems) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/systems | Get systems file
[**get_ifc_unit**](IfcApi.md#get_ifc_unit) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | Retrieve a Unit of a model
[**get_ifc_units**](IfcApi.md#get_ifc_units) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit | Retrieve all Units of a model
[**get_ifcs**](IfcApi.md#get_ifcs) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc | Retrieve all models
[**get_processor_handler**](IfcApi.md#get_processor_handler) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/processorhandler/{id} | Retrieve a processor handler
[**get_processor_handlers**](IfcApi.md#get_processor_handlers) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/processorhandler | Get all processor handlers
[**get_property_set**](IfcApi.md#get_property_set) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | Retrieve a PropertySet of a model
[**get_property_sets**](IfcApi.md#get_property_sets) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset | Retrieve all PropertySets of a model
[**get_raw_elements**](IfcApi.md#get_raw_elements) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/raw | Retrieve all elements in a optimized format
[**get_space**](IfcApi.md#get_space) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | Retrieve one space of the model
[**get_spaces**](IfcApi.md#get_spaces) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space | Retrieve all spaces of the model
[**get_zone**](IfcApi.md#get_zone) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | Retrieve one zone of a model
[**get_zone_space**](IfcApi.md#get_zone_space) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | Retrieve one space of a zone
[**get_zone_spaces**](IfcApi.md#get_zone_spaces) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space | Retrieve all spaces of a zone
[**get_zones**](IfcApi.md#get_zones) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone | Retrieve zones of a model
[**list_classification_element_relations**](IfcApi.md#list_classification_element_relations) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification-element | List all associations between classifications and elements
[**remove_classification_of_element**](IfcApi.md#remove_classification_of_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification/{id} | Remove a classification from an element
[**remove_element_property_set**](IfcApi.md#remove_element_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{id} | Remove a PropertySet from an element
[**remove_element_property_set_property**](IfcApi.md#remove_element_property_set_property) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{id} | Remove a property from a PropertySet
[**remove_element_property_set_property_definition**](IfcApi.md#remove_element_property_set_property_definition) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{id} | Remove a Definition from a Property
[**remove_element_property_set_property_definition_unit**](IfcApi.md#remove_element_property_set_property_definition_unit) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit/{id} | Remove a Unit from a Definition
[**remove_elements_from_classification**](IfcApi.md#remove_elements_from_classification) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/{ifc_classification_pk}/element/{uuid} | Remove the classification from all elements
[**update_element**](IfcApi.md#update_element) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | Update some fields of a zone
[**update_ifc**](IfcApi.md#update_ifc) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | Update some fields of a model
[**update_ifc_files**](IfcApi.md#update_ifc_files) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/files | Update models file (gltf, svg, structure, etc)
[**update_ifc_property**](IfcApi.md#update_ifc_property) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | Update some fields of a Property
[**update_ifc_property_definition**](IfcApi.md#update_ifc_property_definition) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | Update some fields of many PropertyDefinitions of a model
[**update_ifc_unit**](IfcApi.md#update_ifc_unit) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | Update some fields of a Unit of a model
[**update_processor_handler**](IfcApi.md#update_processor_handler) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/processorhandler/{id} | Update the status of a processor handler
[**update_property_set**](IfcApi.md#update_property_set) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | Update some fields of a PropertySet
[**update_space**](IfcApi.md#update_space) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | Update some fields of a space
[**update_zone**](IfcApi.md#update_zone) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | Update some fields of a zone
[**update_zone_space**](IfcApi.md#update_zone_space) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | Update some fields of a space


# **bulk_delete_ifc_classifications**
> bulk_delete_ifc_classifications(cloud_pk, ifc_pk, project_pk)

Remove all classifications from model's elements

             Delete relation between filtered classifications (eg. /classifications?name=untec) and all ifc's elements.             No classification will be deleted on this endpoint, only the relation between ifc's elements and their classification.          Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove all classifications from model's elements
    api_instance.bulk_delete_ifc_classifications(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_ifc_classifications: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove all classifications from model's elements
    api_instance.bulk_delete_ifc_classifications(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_ifc_classifications: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove all classifications from model's elements
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_ifc_properties**
> bulk_delete_ifc_properties(cloud_pk, ifc_pk, project_pk)

Delete many Property of a model

         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted      Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete many Property of a model
    api_instance.bulk_delete_ifc_properties(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_ifc_properties: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete many Property of a model
    api_instance.bulk_delete_ifc_properties(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_ifc_properties: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete many Property of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_ifc_property_definitions**
> bulk_delete_ifc_property_definitions(cloud_pk, ifc_pk, project_pk)

Delete many PropertyDefinitions of a model

         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted      Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete many PropertyDefinitions of a model
    api_instance.bulk_delete_ifc_property_definitions(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_ifc_property_definitions: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete many PropertyDefinitions of a model
    api_instance.bulk_delete_ifc_property_definitions(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_ifc_property_definitions: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete many PropertyDefinitions of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_ifc_units**
> bulk_delete_ifc_units(cloud_pk, ifc_pk, project_pk)

Delete many Units of a model

         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted      Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete many Units of a model
    api_instance.bulk_delete_ifc_units(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_ifc_units: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete many Units of a model
    api_instance.bulk_delete_ifc_units(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_ifc_units: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete many Units of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_property_set**
> bulk_delete_property_set(cloud_pk, ifc_pk, project_pk)

Delete many PropertySet of a model

         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted      Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete many PropertySet of a model
    api_instance.bulk_delete_property_set(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_property_set: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete many PropertySet of a model
    api_instance.bulk_delete_property_set(cloud_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_delete_property_set: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete many PropertySet of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_full_update_elements**
> list[Element] bulk_full_update_elements(cloud_pk, ifc_pk, project_pk, data)

Update many elements at once (only changing fields may be defined)

         Bulk update.         Similar to update, but the body should be a list of objects to patch or put         The response will be a list (in the same order) of updated objects or of errors if any         If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors      Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.Element()] # list[Element] | 

try:
    # Update many elements at once (only changing fields may be defined)
    api_response = api_instance.bulk_full_update_elements(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_full_update_elements: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.Element()] # list[Element] | 

try:
    # Update many elements at once (only changing fields may be defined)
    api_response = api_instance.bulk_full_update_elements(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_full_update_elements: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.Element()] # list[Element] | 

try:
    # Update many elements at once (only changing fields may be defined)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If all updates fail: a list of errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_full_update_ifc_property**
> list[ModelProperty] bulk_full_update_ifc_property(cloud_pk, ifc_pk, project_pk, data)

Update some fields of many properties of a model

         Bulk update.         Similar to update, but the body should be a list of objects to patch or put         The response will be a list (in the same order) of updated objects or of errors if any         If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors      Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.ModelProperty()] # list[ModelProperty] | 

try:
    # Update some fields of many properties of a model
    api_response = api_instance.bulk_full_update_ifc_property(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_full_update_ifc_property: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.ModelProperty()] # list[ModelProperty] | 

try:
    # Update some fields of many properties of a model
    api_response = api_instance.bulk_full_update_ifc_property(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_full_update_ifc_property: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.ModelProperty()] # list[ModelProperty] | 

try:
    # Update some fields of many properties of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | All updates failed: list of errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_remove_classifications_of_element**
> bulk_remove_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk)

Remove many classifications from an element

         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted      Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove many classifications from an element
    api_instance.bulk_remove_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_remove_classifications_of_element: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove many classifications from an element
    api_instance.bulk_remove_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_remove_classifications_of_element: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove many classifications from an element
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_remove_elements_from_classification**
> bulk_remove_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk)

Remove the classifications from all elements

         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted      Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_classification_pk = 'ifc_classification_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove the classifications from all elements
    api_instance.bulk_remove_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_remove_elements_from_classification: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_classification_pk = 'ifc_classification_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove the classifications from all elements
    api_instance.bulk_remove_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_remove_elements_from_classification: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_classification_pk = 'ifc_classification_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove the classifications from all elements
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_elements**
> list[Element] bulk_update_elements(cloud_pk, ifc_pk, project_pk, data)

Update many elements at once (all field must be defined)

         Bulk update.         Similar to update, but the body should be a list of objects to patch or put         The response will be a list (in the same order) of updated objects or of errors if any         If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors      Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.Element()] # list[Element] | 

try:
    # Update many elements at once (all field must be defined)
    api_response = api_instance.bulk_update_elements(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_update_elements: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.Element()] # list[Element] | 

try:
    # Update many elements at once (all field must be defined)
    api_response = api_instance.bulk_update_elements(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_update_elements: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.Element()] # list[Element] | 

try:
    # Update many elements at once (all field must be defined)
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If all updates fail: a list of errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_ifc_property**
> list[ModelProperty] bulk_update_ifc_property(cloud_pk, ifc_pk, project_pk, data)

Update all fields of many properties of a model

         Bulk update.         Similar to update, but the body should be a list of objects to patch or put         The response will be a list (in the same order) of updated objects or of errors if any         If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors      Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.ModelProperty()] # list[ModelProperty] | 

try:
    # Update all fields of many properties of a model
    api_response = api_instance.bulk_update_ifc_property(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_update_ifc_property: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.ModelProperty()] # list[ModelProperty] | 

try:
    # Update all fields of many properties of a model
    api_response = api_instance.bulk_update_ifc_property(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->bulk_update_ifc_property: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.ModelProperty()] # list[ModelProperty] | 

try:
    # Update all fields of many properties of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | All updates failed: list of errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloud_project_ifc_processorhandler_partial_update**
> ProcessorHandler cloud_project_ifc_processorhandler_partial_update(cloud_pk, id, ifc_pk, project_pk, data)



 Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this processor handler.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.ProcessorHandler() # ProcessorHandler | 

try:
    api_response = api_instance.cloud_project_ifc_processorhandler_partial_update(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->cloud_project_ifc_processorhandler_partial_update: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this processor handler.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.ProcessorHandler() # ProcessorHandler | 

try:
    api_response = api_instance.cloud_project_ifc_processorhandler_partial_update(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->cloud_project_ifc_processorhandler_partial_update: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this processor handler.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.ProcessorHandler() # ProcessorHandler | 

try:
    api_response = api_instance.cloud_project_ifc_processorhandler_partial_update(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->cloud_project_ifc_processorhandler_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this processor handler. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**ProcessorHandler**](ProcessorHandler.md)|  | 

### Return type

[**ProcessorHandler**](ProcessorHandler.md)

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

# **create_classification_element_relations**
> create_classification_element_relations(cloud_pk, ifc_pk, project_pk, data)

Create association between existing classification and existing element

Create association between existing classification and existing element Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.ElementClassificationRelation()] # list[ElementClassificationRelation] | 

try:
    # Create association between existing classification and existing element
    api_instance.create_classification_element_relations(cloud_pk, ifc_pk, project_pk, data)
except ApiException as e:
    print("Exception when calling IfcApi->create_classification_element_relations: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.ElementClassificationRelation()] # list[ElementClassificationRelation] | 

try:
    # Create association between existing classification and existing element
    api_instance.create_classification_element_relations(cloud_pk, ifc_pk, project_pk, data)
except ApiException as e:
    print("Exception when calling IfcApi->create_classification_element_relations: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.ElementClassificationRelation()] # list[ElementClassificationRelation] | 

try:
    # Create association between existing classification and existing element
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response is empty |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_classifications_of_element**
> Classification create_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk, data)

Create one or many classifications to an element

 Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Classification() # Classification | 

try:
    # Create one or many classifications to an element
    api_response = api_instance.create_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_classifications_of_element: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Classification() # Classification | 

try:
    # Create one or many classifications to an element
    api_response = api_instance.create_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_classifications_of_element: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Classification() # Classification | 

try:
    # Create one or many classifications to an element
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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_element**
> Element create_element(cloud_pk, ifc_pk, project_pk, data)

Create an element in the model

The IFC file will not be updated. The created element will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Element() # Element | 

try:
    # Create an element in the model
    api_response = api_instance.create_element(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_element: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Element() # Element | 

try:
    # Create an element in the model
    api_response = api_instance.create_element(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_element: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Element() # Element | 

try:
    # Create an element in the model
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
 **data** | [**Element**](Element.md)|  | 

### Return type

[**Element**](Element.md)

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

# **create_element_property_set**
> PropertySet create_element_property_set(cloud_pk, element_uuid, ifc_pk, project_pk, data)

Create a PropertySets to an element

Create a PropertySets that will be automatically linked to the element Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertySet() # PropertySet | 

try:
    # Create a PropertySets to an element
    api_response = api_instance.create_element_property_set(cloud_pk, element_uuid, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_element_property_set: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertySet() # PropertySet | 

try:
    # Create a PropertySets to an element
    api_response = api_instance.create_element_property_set(cloud_pk, element_uuid, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_element_property_set: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertySet() # PropertySet | 

try:
    # Create a PropertySets to an element
    api_response = api_instance.create_element_property_set(cloud_pk, element_uuid, ifc_pk, project_pk, data)
    pprint(api_response)
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

[**PropertySet**](PropertySet.md)

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

# **create_element_property_set_property**
> ModelProperty create_element_property_set_property(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk, data)

Create a property to a PropertySet

 Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = openapi_client.ModelProperty() # ModelProperty | 

try:
    # Create a property to a PropertySet
    api_response = api_instance.create_element_property_set_property(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_element_property_set_property: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = openapi_client.ModelProperty() # ModelProperty | 

try:
    # Create a property to a PropertySet
    api_response = api_instance.create_element_property_set_property(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_element_property_set_property: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = openapi_client.ModelProperty() # ModelProperty | 

try:
    # Create a property to a PropertySet
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_element_property_set_property_definition**
> PropertyDefinition create_element_property_set_property_definition(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk, data)

Create a Definition to a Property

 Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = openapi_client.PropertyDefinition() # PropertyDefinition | 

try:
    # Create a Definition to a Property
    api_response = api_instance.create_element_property_set_property_definition(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_element_property_set_property_definition: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = openapi_client.PropertyDefinition() # PropertyDefinition | 

try:
    # Create a Definition to a Property
    api_response = api_instance.create_element_property_set_property_definition(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_element_property_set_property_definition: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = openapi_client.PropertyDefinition() # PropertyDefinition | 

try:
    # Create a Definition to a Property
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_element_property_set_property_definition_unit**
> Unit create_element_property_set_property_definition_unit(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk, data)

Create a Unit to a Definition

Create a Unit to a Definition Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = openapi_client.Unit() # Unit | 

try:
    # Create a Unit to a Definition
    api_response = api_instance.create_element_property_set_property_definition_unit(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_element_property_set_property_definition_unit: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = openapi_client.Unit() # Unit | 

try:
    # Create a Unit to a Definition
    api_response = api_instance.create_element_property_set_property_definition_unit(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_element_property_set_property_definition_unit: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = openapi_client.Unit() # Unit | 

try:
    # Create a Unit to a Definition
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ifc_property_definition**
> PropertyDefinition create_ifc_property_definition(cloud_pk, ifc_pk, project_pk, data)

Create a PropertyDefinition on the model

 Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertyDefinition() # PropertyDefinition | 

try:
    # Create a PropertyDefinition on the model
    api_response = api_instance.create_ifc_property_definition(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_ifc_property_definition: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertyDefinition() # PropertyDefinition | 

try:
    # Create a PropertyDefinition on the model
    api_response = api_instance.create_ifc_property_definition(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_ifc_property_definition: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertyDefinition() # PropertyDefinition | 

try:
    # Create a PropertyDefinition on the model
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
 **data** | [**PropertyDefinition**](PropertyDefinition.md)|  | 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

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

# **create_ifc_unit**
> Unit create_ifc_unit(cloud_pk, ifc_pk, project_pk, data)

Create a Unit on a model

 Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Unit() # Unit | 

try:
    # Create a Unit on a model
    api_response = api_instance.create_ifc_unit(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_ifc_unit: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Unit() # Unit | 

try:
    # Create a Unit on a model
    api_response = api_instance.create_ifc_unit(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_ifc_unit: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Unit() # Unit | 

try:
    # Create a Unit on a model
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
 **data** | [**Unit**](Unit.md)|  | 

### Return type

[**Unit**](Unit.md)

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

# **create_property_set**
> PropertySet create_property_set(cloud_pk, ifc_pk, project_pk, data)

Create a PropertySet

Create a PropertySet Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertySet() # PropertySet | 

try:
    # Create a PropertySet
    api_response = api_instance.create_property_set(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_property_set: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertySet() # PropertySet | 

try:
    # Create a PropertySet
    api_response = api_instance.create_property_set(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_property_set: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertySet() # PropertySet | 

try:
    # Create a PropertySet
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
 **data** | [**PropertySet**](PropertySet.md)|  | 

### Return type

[**PropertySet**](PropertySet.md)

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

# **create_property_set_element_relations**
> create_property_set_element_relations(cloud_pk, ifc_pk, project_pk, data)

Create association between PropertySet and element

Create association between existing PropertySet and existing element Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.ElementPropertySetRelation()] # list[ElementPropertySetRelation] | 

try:
    # Create association between PropertySet and element
    api_instance.create_property_set_element_relations(cloud_pk, ifc_pk, project_pk, data)
except ApiException as e:
    print("Exception when calling IfcApi->create_property_set_element_relations: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.ElementPropertySetRelation()] # list[ElementPropertySetRelation] | 

try:
    # Create association between PropertySet and element
    api_instance.create_property_set_element_relations(cloud_pk, ifc_pk, project_pk, data)
except ApiException as e:
    print("Exception when calling IfcApi->create_property_set_element_relations: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [openapi_client.ElementPropertySetRelation()] # list[ElementPropertySetRelation] | 

try:
    # Create association between PropertySet and element
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response is empty |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_raw_elements**
> create_raw_elements(cloud_pk, ifc_pk, project_pk, data)

Create elements in an optimized format

         You can use the same optimized structure to post multiple elements, property_sets, properties, definitions and units at once.         If the structure is malformed, an error 500 without more explaination may be returned          Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.RawElements() # RawElements | 

try:
    # Create elements in an optimized format
    api_instance.create_raw_elements(cloud_pk, ifc_pk, project_pk, data)
except ApiException as e:
    print("Exception when calling IfcApi->create_raw_elements: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.RawElements() # RawElements | 

try:
    # Create elements in an optimized format
    api_instance.create_raw_elements(cloud_pk, ifc_pk, project_pk, data)
except ApiException as e:
    print("Exception when calling IfcApi->create_raw_elements: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.RawElements() # RawElements | 

try:
    # Create elements in an optimized format
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
 **data** | [**RawElements**](RawElements.md)|  | 

### Return type

void (empty response body)

### Authorization

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_space**
> Space create_space(cloud_pk, ifc_pk, project_pk, data)

Create a space in the model

The IFC file will not be updated. The created space will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Space() # Space | 

try:
    # Create a space in the model
    api_response = api_instance.create_space(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_space: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Space() # Space | 

try:
    # Create a space in the model
    api_response = api_instance.create_space(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_space: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Space() # Space | 

try:
    # Create a space in the model
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
 **data** | [**Space**](Space.md)|  | 

### Return type

[**Space**](Space.md)

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

# **create_zone**
> Zone create_zone(cloud_pk, ifc_pk, project_pk, data)

Create a zone in the model

The IFC file will not be updated. The created zone will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Zone() # Zone | 

try:
    # Create a zone in the model
    api_response = api_instance.create_zone(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_zone: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Zone() # Zone | 

try:
    # Create a zone in the model
    api_response = api_instance.create_zone(cloud_pk, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_zone: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Zone() # Zone | 

try:
    # Create a zone in the model
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
 **data** | [**Zone**](Zone.md)|  | 

### Return type

[**Zone**](Zone.md)

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

# **create_zone_space**
> ZoneSpace create_zone_space(cloud_pk, ifc_pk, project_pk, zone_pk, data)

Create a space in a zone

The IFC file will not be updated. The created space will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = openapi_client.ZoneSpace() # ZoneSpace | 

try:
    # Create a space in a zone
    api_response = api_instance.create_zone_space(cloud_pk, ifc_pk, project_pk, zone_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_zone_space: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = openapi_client.ZoneSpace() # ZoneSpace | 

try:
    # Create a space in a zone
    api_response = api_instance.create_zone_space(cloud_pk, ifc_pk, project_pk, zone_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->create_zone_space: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = openapi_client.ZoneSpace() # ZoneSpace | 

try:
    # Create a space in a zone
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_element**
> delete_element(cloud_pk, ifc_pk, project_pk, uuid)

Delete a zone of a model

The IFC file will not be updated. The remaining elements are available in API and will be available when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

try:
    # Delete a zone of a model
    api_instance.delete_element(cloud_pk, ifc_pk, project_pk, uuid)
except ApiException as e:
    print("Exception when calling IfcApi->delete_element: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

try:
    # Delete a zone of a model
    api_instance.delete_element(cloud_pk, ifc_pk, project_pk, uuid)
except ApiException as e:
    print("Exception when calling IfcApi->delete_element: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

try:
    # Delete a zone of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ifc**
> delete_ifc(cloud_pk, id, project_pk)

Delete a model

It will delete the related document too Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a model
    api_instance.delete_ifc(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a model
    api_instance.delete_ifc(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Delete a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ifc_property**
> delete_ifc_property(cloud_pk, id, ifc_pk, project_pk)

Delete a Property of a model

Delete a Property of a model Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a Property of a model
    api_instance.delete_ifc_property(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc_property: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a Property of a model
    api_instance.delete_ifc_property(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc_property: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a Property of a model
    api_instance.delete_ifc_property(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property. | 
 **ifc_pk** | **str**|  | 
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

# **delete_ifc_property_definition**
> delete_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk)

Delete a PropertyDefinitions of a model

Delete a PropertyDefinitions of a model Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a PropertyDefinitions of a model
    api_instance.delete_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc_property_definition: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a PropertyDefinitions of a model
    api_instance.delete_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc_property_definition: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a PropertyDefinitions of a model
    api_instance.delete_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property definition. | 
 **ifc_pk** | **str**|  | 
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

# **delete_ifc_unit**
> delete_ifc_unit(cloud_pk, id, ifc_pk, project_pk)

Delete a Unit of a model

Delete a Unit of a model Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a Unit of a model
    api_instance.delete_ifc_unit(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc_unit: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a Unit of a model
    api_instance.delete_ifc_unit(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc_unit: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a Unit of a model
    api_instance.delete_ifc_unit(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_ifc_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this unit. | 
 **ifc_pk** | **str**|  | 
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

# **delete_property_set**
> delete_property_set(cloud_pk, id, ifc_pk, project_pk)

Delete a PropertySet of a model

Delete a PropertySet of a model Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a PropertySet of a model
    api_instance.delete_property_set(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_property_set: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a PropertySet of a model
    api_instance.delete_property_set(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_property_set: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a PropertySet of a model
    api_instance.delete_property_set(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_property_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property set. | 
 **ifc_pk** | **str**|  | 
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

# **delete_space**
> delete_space(cloud_pk, id, ifc_pk, project_pk)

Delete a space

It will not delete related zones. The IFC file will not be updated. The remaining spaces are available in API and will be available when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a space
    api_instance.delete_space(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_space: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a space
    api_instance.delete_space(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_space: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a space
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone**
> delete_zone(cloud_pk, id, ifc_pk, project_pk)

Delete a zone of a model

The IFC file will not be updated. The remaining zones are available in API and will be available when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a zone of a model
    api_instance.delete_zone(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_zone: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a zone of a model
    api_instance.delete_zone(cloud_pk, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_zone: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Delete a zone of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone_space**
> delete_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk)

Delete a space of a zone

The IFC file will not be updated. The remaining spaces are available in API and will be available when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 

try:
    # Delete a space of a zone
    api_instance.delete_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_zone_space: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 

try:
    # Delete a space of a zone
    api_instance.delete_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk)
except ApiException as e:
    print("Exception when calling IfcApi->delete_zone_space: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 

try:
    # Delete a space of a zone
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_ifc**
> IfcExport export_ifc(cloud_pk, id, project_pk, data)

Export IFC

Export IFC as requested in parameters. This call doesn't return the IFC. When the export is finished, a new IFC file with '_export_DD_MM_YYYY' suffix will be created in the same folder than the original IFC. You can query the folder or subscribe to the new document webhook to retrieve the result Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = openapi_client.IfcExport() # IfcExport | 

try:
    # Export IFC
    api_response = api_instance.export_ifc(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->export_ifc: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = openapi_client.IfcExport() # IfcExport | 

try:
    # Export IFC
    api_response = api_instance.export_ifc(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->export_ifc: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = openapi_client.IfcExport() # IfcExport | 

try:
    # Export IFC
    api_response = api_instance.export_ifc(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->export_ifc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc. | 
 **project_pk** | **str**|  | 
 **data** | [**IfcExport**](IfcExport.md)|  | 

### Return type

[**IfcExport**](IfcExport.md)

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

# **full_update_element**
> Element full_update_element(cloud_pk, ifc_pk, project_pk, uuid, data)

Update all fields of an element

Update all fields of a element. The IFC file will not be updated. The created element will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID
data = openapi_client.Element() # Element | 

try:
    # Update all fields of an element
    api_response = api_instance.full_update_element(cloud_pk, ifc_pk, project_pk, uuid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_element: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID
data = openapi_client.Element() # Element | 

try:
    # Update all fields of an element
    api_response = api_instance.full_update_element(cloud_pk, ifc_pk, project_pk, uuid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_element: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID
data = openapi_client.Element() # Element | 

try:
    # Update all fields of an element
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_ifc**
> Ifc full_update_ifc(cloud_pk, id, project_pk, data)

Update all fields of a model

Update all fields of a model Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = openapi_client.Ifc() # Ifc | 

try:
    # Update all fields of a model
    api_response = api_instance.full_update_ifc(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = openapi_client.Ifc() # Ifc | 

try:
    # Update all fields of a model
    api_response = api_instance.full_update_ifc(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = openapi_client.Ifc() # Ifc | 

try:
    # Update all fields of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_ifc_property**
> ModelProperty full_update_ifc_property(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of a Property

Update some fields of a Property Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.ModelProperty() # ModelProperty | 

try:
    # Update some fields of a Property
    api_response = api_instance.full_update_ifc_property(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc_property: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.ModelProperty() # ModelProperty | 

try:
    # Update some fields of a Property
    api_response = api_instance.full_update_ifc_property(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc_property: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.ModelProperty() # ModelProperty | 

try:
    # Update some fields of a Property
    api_response = api_instance.full_update_ifc_property(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**ModelProperty**](ModelProperty.md)|  | 

### Return type

[**ModelProperty**](ModelProperty.md)

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

# **full_update_ifc_property_definition**
> PropertyDefinition full_update_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk, data)

Update all fields of many PropertyDefinitions of a model

 Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertyDefinition() # PropertyDefinition | 

try:
    # Update all fields of many PropertyDefinitions of a model
    api_response = api_instance.full_update_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc_property_definition: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertyDefinition() # PropertyDefinition | 

try:
    # Update all fields of many PropertyDefinitions of a model
    api_response = api_instance.full_update_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc_property_definition: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertyDefinition() # PropertyDefinition | 

try:
    # Update all fields of many PropertyDefinitions of a model
    api_response = api_instance.full_update_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property definition. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**PropertyDefinition**](PropertyDefinition.md)|  | 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

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

# **full_update_ifc_unit**
> Unit full_update_ifc_unit(cloud_pk, id, ifc_pk, project_pk, data)

Update all fields of a Unit of a model

 Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Unit() # Unit | 

try:
    # Update all fields of a Unit of a model
    api_response = api_instance.full_update_ifc_unit(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc_unit: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Unit() # Unit | 

try:
    # Update all fields of a Unit of a model
    api_response = api_instance.full_update_ifc_unit(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc_unit: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Unit() # Unit | 

try:
    # Update all fields of a Unit of a model
    api_response = api_instance.full_update_ifc_unit(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_ifc_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this unit. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**Unit**](Unit.md)|  | 

### Return type

[**Unit**](Unit.md)

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

# **full_update_property_set**
> PropertySet full_update_property_set(cloud_pk, id, ifc_pk, project_pk, data)

Update all fields of a PropertySet

Update all fields of a PropertySet Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertySet() # PropertySet | 

try:
    # Update all fields of a PropertySet
    api_response = api_instance.full_update_property_set(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_property_set: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertySet() # PropertySet | 

try:
    # Update all fields of a PropertySet
    api_response = api_instance.full_update_property_set(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_property_set: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertySet() # PropertySet | 

try:
    # Update all fields of a PropertySet
    api_response = api_instance.full_update_property_set(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_property_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property set. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**PropertySet**](PropertySet.md)|  | 

### Return type

[**PropertySet**](PropertySet.md)

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

# **full_update_space**
> Space full_update_space(cloud_pk, id, ifc_pk, project_pk, data)

Update all fields of a space

Update all fields of a space. The IFC file will not be updated. The created space will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Space() # Space | 

try:
    # Update all fields of a space
    api_response = api_instance.full_update_space(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_space: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Space() # Space | 

try:
    # Update all fields of a space
    api_response = api_instance.full_update_space(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_space: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Space() # Space | 

try:
    # Update all fields of a space
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_zone**
> Zone full_update_zone(cloud_pk, id, ifc_pk, project_pk, data)

Update all fields of a zone

Update all fields of a zone. The IFC file will not be updated. The created zone will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Zone() # Zone | 

try:
    # Update all fields of a zone
    api_response = api_instance.full_update_zone(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_zone: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Zone() # Zone | 

try:
    # Update all fields of a zone
    api_response = api_instance.full_update_zone(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_zone: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Zone() # Zone | 

try:
    # Update all fields of a zone
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_zone_space**
> ZoneSpace full_update_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk, data)

Update all fields of a space

Update all fields of a space. The IFC file will not be updated. The created space will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = openapi_client.ZoneSpace() # ZoneSpace | 

try:
    # Update all fields of a space
    api_response = api_instance.full_update_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_zone_space: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = openapi_client.ZoneSpace() # ZoneSpace | 

try:
    # Update all fields of a space
    api_response = api_instance.full_update_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->full_update_zone_space: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = openapi_client.ZoneSpace() # ZoneSpace | 

try:
    # Update all fields of a space
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classifications_of_element**
> list[Classification] get_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk)

Retrieve all classifications of an element

Retrieve all classifications of an element Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all classifications of an element
    api_response = api_instance.get_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_classifications_of_element: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all classifications of an element
    api_response = api_instance.get_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_classifications_of_element: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all classifications of an element
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element**
> Element get_element(cloud_pk, ifc_pk, project_pk, uuid)

Retrieve an element of a model

Retrieve an element of a model Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

try:
    # Retrieve an element of a model
    api_response = api_instance.get_element(cloud_pk, ifc_pk, project_pk, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

try:
    # Retrieve an element of a model
    api_response = api_instance.get_element(cloud_pk, ifc_pk, project_pk, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

try:
    # Retrieve an element of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_set**
> PropertySet get_element_property_set(cloud_pk, element_uuid, id, ifc_pk, project_pk)

Retrieve a PropertySet of an element

Retrieve a PropertySet of an element Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a PropertySet of an element
    api_response = api_instance.get_element_property_set(cloud_pk, element_uuid, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a PropertySet of an element
    api_response = api_instance.get_element_property_set(cloud_pk, element_uuid, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a PropertySet of an element
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_set_properties**
> list[ModelProperty] get_element_property_set_properties(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk)

Retrieve all Properties of a PropertySet

Retrieve all Properties of a PropertySet Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve all Properties of a PropertySet
    api_response = api_instance.get_element_property_set_properties(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_properties: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve all Properties of a PropertySet
    api_response = api_instance.get_element_property_set_properties(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_properties: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve all Properties of a PropertySet
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_set_property**
> ModelProperty get_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)

Retrieve a Property of a PropertySet

Retrieve a Property of a PropertySet Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve a Property of a PropertySet
    api_response = api_instance.get_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve a Property of a PropertySet
    api_response = api_instance.get_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve a Property of a PropertySet
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_set_property_definition**
> PropertyDefinition get_element_property_set_property_definition(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)

Retrieve a Definition of a Property

Retrieve a Definition of a Property Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve a Definition of a Property
    api_response = api_instance.get_element_property_set_property_definition(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property_definition: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve a Definition of a Property
    api_response = api_instance.get_element_property_set_property_definition(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property_definition: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve a Definition of a Property
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_set_property_definition_unit**
> Unit get_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)

Retrieve a Unit of a Definition

Retrieve a Unit of a Definition Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve a Unit of a Definition
    api_response = api_instance.get_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property_definition_unit: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve a Unit of a Definition
    api_response = api_instance.get_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property_definition_unit: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve a Unit of a Definition
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_set_property_definition_units**
> list[Unit] get_element_property_set_property_definition_units(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)

Retrieve all Units of a Definition

Retrieve all Units of a Definition Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve all Units of a Definition
    api_response = api_instance.get_element_property_set_property_definition_units(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property_definition_units: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve all Units of a Definition
    api_response = api_instance.get_element_property_set_property_definition_units(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property_definition_units: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve all Units of a Definition
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_set_property_definitions**
> list[PropertyDefinition] get_element_property_set_property_definitions(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk)

Retrieve all Definitions of a PropertySet

Retrieve all Definitions of a PropertySet Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve all Definitions of a PropertySet
    api_response = api_instance.get_element_property_set_property_definitions(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property_definitions: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve all Definitions of a PropertySet
    api_response = api_instance.get_element_property_set_property_definitions(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_set_property_definitions: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Retrieve all Definitions of a PropertySet
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_property_sets**
> list[PropertySet] get_element_property_sets(cloud_pk, element_uuid, ifc_pk, project_pk)

Retrieve all PropertySets of an element

Retrieve all PropertySets of an element Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all PropertySets of an element
    api_response = api_instance.get_element_property_sets(cloud_pk, element_uuid, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_sets: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all PropertySets of an element
    api_response = api_instance.get_element_property_sets(cloud_pk, element_uuid, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_element_property_sets: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all PropertySets of an element
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_elements**
> list[Element] get_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)

Retrieve all elements of a model

Retrieve all elements of a model. If not filtered, the json may be very large. To efficently retrieve all elements and their data, see getRawElements Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
type = 'type_example' # str | Filter the returned list by type (optional)
classification = 'classification_example' # str | Filter the returned list by classification (optional)
classification__notation = 'classification__notation_example' # str | Filter the returned list by classification__notation (optional)

try:
    # Retrieve all elements of a model
    api_response = api_instance.get_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_elements: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
type = 'type_example' # str | Filter the returned list by type (optional)
classification = 'classification_example' # str | Filter the returned list by classification (optional)
classification__notation = 'classification__notation_example' # str | Filter the returned list by classification__notation (optional)

try:
    # Retrieve all elements of a model
    api_response = api_instance.get_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_elements: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
type = 'type_example' # str | Filter the returned list by type (optional)
classification = 'classification_example' # str | Filter the returned list by classification (optional)
classification__notation = 'classification__notation_example' # str | Filter the returned list by classification__notation (optional)

try:
    # Retrieve all elements of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_elements_from_classification**
> list[Element] get_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk)

Retrieve all elements with the classification

Retrieve all elements with the classification Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_classification_pk = 'ifc_classification_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all elements with the classification
    api_response = api_instance.get_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_elements_from_classification: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_classification_pk = 'ifc_classification_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all elements with the classification
    api_response = api_instance.get_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_elements_from_classification: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_classification_pk = 'ifc_classification_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all elements with the classification
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc**
> Ifc get_ifc(cloud_pk, id, project_pk)

Retrieve one model

 Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve one model
    api_response = api_instance.get_ifc(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve one model
    api_response = api_instance.get_ifc(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve one model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_bvh**
> get_ifc_bvh(cloud_pk, id, project_pk)

Get svg file

         DEPRECATED: Now, retrieve the file url in the ifc object itself         Returns the map file          Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get svg file
    api_instance.get_ifc_bvh(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_bvh: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get svg file
    api_instance.get_ifc_bvh(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_bvh: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get svg file
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_classifications**
> list[Classification] get_ifc_classifications(cloud_pk, ifc_pk, project_pk)

Retrieve all classifications in a model

Retrieve all classifications in a model Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all classifications in a model
    api_response = api_instance.get_ifc_classifications(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_classifications: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all classifications in a model
    api_response = api_instance.get_ifc_classifications(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_classifications: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all classifications in a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_gltf**
> get_ifc_gltf(cloud_pk, id, project_pk)

Get gltf file

         DEPRECATED: Now, retrieve the file url in the ifc object itself         Returns the gltf file          Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get gltf file
    api_instance.get_ifc_gltf(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_gltf: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get gltf file
    api_instance.get_ifc_gltf(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_gltf: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get gltf file
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_map**
> get_ifc_map(cloud_pk, id, project_pk)

Get bvh file

         DEPRECATED: Now, retrieve the file url in the ifc object itself         Returns the bvh file          Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get bvh file
    api_instance.get_ifc_map(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_map: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get bvh file
    api_instance.get_ifc_map(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_map: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get bvh file
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_properties**
> list[ModelProperty] get_ifc_properties(cloud_pk, ifc_pk, project_pk)

Retrieve all Properties of a model

Retrieve all PropertySets of a model Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all Properties of a model
    api_response = api_instance.get_ifc_properties(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_properties: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all Properties of a model
    api_response = api_instance.get_ifc_properties(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_properties: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all Properties of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_property**
> ModelProperty get_ifc_property(cloud_pk, id, ifc_pk, project_pk)

Retrieve a Property of a model

Retrieve a Property of a model Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a Property of a model
    api_response = api_instance.get_ifc_property(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_property: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a Property of a model
    api_response = api_instance.get_ifc_property(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_property: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a Property of a model
    api_response = api_instance.get_ifc_property(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**ModelProperty**](ModelProperty.md)

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

# **get_ifc_property_definition**
> PropertyDefinition get_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk)

Retrieve a PropertyDefinition of a model

Retrieve a PropertyDefinition of a model Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a PropertyDefinition of a model
    api_response = api_instance.get_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_property_definition: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a PropertyDefinition of a model
    api_response = api_instance.get_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_property_definition: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a PropertyDefinition of a model
    api_response = api_instance.get_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property definition. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

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

# **get_ifc_property_definitions**
> list[PropertyDefinition] get_ifc_property_definitions(cloud_pk, ifc_pk, project_pk)

Retrieve all PropertyDefinitions of a model

Retrieve all PropertyDefinitions of a model Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all PropertyDefinitions of a model
    api_response = api_instance.get_ifc_property_definitions(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_property_definitions: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all PropertyDefinitions of a model
    api_response = api_instance.get_ifc_property_definitions(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_property_definitions: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all PropertyDefinitions of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_structure**
> get_ifc_structure(cloud_pk, id, project_pk)

Get structure file

         DEPRECATED: Now, retrieve the file url in the ifc object itself         Returns the structure file          Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get structure file
    api_instance.get_ifc_structure(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_structure: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get structure file
    api_instance.get_ifc_structure(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_structure: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get structure file
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_systems**
> get_ifc_systems(cloud_pk, id, project_pk)

Get systems file

         DEPRECATED: Now, retrieve the file url in the ifc object itself         Returns the system file          Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get systems file
    api_instance.get_ifc_systems(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_systems: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get systems file
    api_instance.get_ifc_systems(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_systems: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

try:
    # Get systems file
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifc_unit**
> Unit get_ifc_unit(cloud_pk, id, ifc_pk, project_pk)

Retrieve a Unit of a model

Retrieve a Unit of a model Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a Unit of a model
    api_response = api_instance.get_ifc_unit(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_unit: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a Unit of a model
    api_response = api_instance.get_ifc_unit(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_unit: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a Unit of a model
    api_response = api_instance.get_ifc_unit(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this unit. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**Unit**](Unit.md)

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

# **get_ifc_units**
> list[Unit] get_ifc_units(cloud_pk, ifc_pk, project_pk)

Retrieve all Units of a model

Retrieve all Units of a model Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all Units of a model
    api_response = api_instance.get_ifc_units(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_units: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all Units of a model
    api_response = api_instance.get_ifc_units(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifc_units: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all Units of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ifcs**
> list[Ifc] get_ifcs(cloud_pk, project_pk, status=status)

Retrieve all models

Retrieve all models Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
status = 'status_example' # str | Filter the returned list by status (optional)

try:
    # Retrieve all models
    api_response = api_instance.get_ifcs(cloud_pk, project_pk, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifcs: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
status = 'status_example' # str | Filter the returned list by status (optional)

try:
    # Retrieve all models
    api_response = api_instance.get_ifcs(cloud_pk, project_pk, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_ifcs: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
status = 'status_example' # str | Filter the returned list by status (optional)

try:
    # Retrieve all models
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_processor_handler**
> ProcessorHandler get_processor_handler(cloud_pk, id, ifc_pk, project_pk)

Retrieve a processor handler

 Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this processor handler.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a processor handler
    api_response = api_instance.get_processor_handler(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_processor_handler: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this processor handler.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a processor handler
    api_response = api_instance.get_processor_handler(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_processor_handler: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this processor handler.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a processor handler
    api_response = api_instance.get_processor_handler(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_processor_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this processor handler. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**ProcessorHandler**](ProcessorHandler.md)

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

# **get_processor_handlers**
> list[ProcessorHandler] get_processor_handlers(cloud_pk, ifc_pk, project_pk)

Get all processor handlers

 Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Get all processor handlers
    api_response = api_instance.get_processor_handlers(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_processor_handlers: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Get all processor handlers
    api_response = api_instance.get_processor_handlers(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_processor_handlers: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Get all processor handlers
    api_response = api_instance.get_processor_handlers(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_processor_handlers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[ProcessorHandler]**](ProcessorHandler.md)

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

# **get_property_set**
> PropertySet get_property_set(cloud_pk, id, ifc_pk, project_pk)

Retrieve a PropertySet of a model

Retrieve a PropertySet of a model Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a PropertySet of a model
    api_response = api_instance.get_property_set(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_property_set: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a PropertySet of a model
    api_response = api_instance.get_property_set(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_property_set: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve a PropertySet of a model
    api_response = api_instance.get_property_set(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_property_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property set. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**PropertySet**](PropertySet.md)

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

# **get_property_sets**
> list[PropertySet] get_property_sets(cloud_pk, ifc_pk, project_pk)

Retrieve all PropertySets of a model

Retrieve all PropertySets of a model Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all PropertySets of a model
    api_response = api_instance.get_property_sets(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_property_sets: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all PropertySets of a model
    api_response = api_instance.get_property_sets(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_property_sets: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all PropertySets of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_elements**
> RawElements get_raw_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)

Retrieve all elements in a optimized format

         Returns elements, property_sets, properties, definitions and units in a JSON optimized structure          Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
type = 'type_example' # str | Filter the returned list by type (optional)
classification = 'classification_example' # str | Filter the returned list by classification (optional)
classification__notation = 'classification__notation_example' # str | Filter the returned list by classification__notation (optional)

try:
    # Retrieve all elements in a optimized format
    api_response = api_instance.get_raw_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_raw_elements: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
type = 'type_example' # str | Filter the returned list by type (optional)
classification = 'classification_example' # str | Filter the returned list by classification (optional)
classification__notation = 'classification__notation_example' # str | Filter the returned list by classification__notation (optional)

try:
    # Retrieve all elements in a optimized format
    api_response = api_instance.get_raw_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_raw_elements: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
type = 'type_example' # str | Filter the returned list by type (optional)
classification = 'classification_example' # str | Filter the returned list by classification (optional)
classification__notation = 'classification__notation_example' # str | Filter the returned list by classification__notation (optional)

try:
    # Retrieve all elements in a optimized format
    api_response = api_instance.get_raw_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)
    pprint(api_response)
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

[**RawElements**](RawElements.md)

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

# **get_space**
> Space get_space(cloud_pk, id, ifc_pk, project_pk)

Retrieve one space of the model

Retrieve one space of the model Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve one space of the model
    api_response = api_instance.get_space(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_space: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve one space of the model
    api_response = api_instance.get_space(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_space: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve one space of the model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spaces**
> list[Space] get_spaces(cloud_pk, ifc_pk, project_pk)

Retrieve all spaces of the model

Retrieve all spaces of the model Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all spaces of the model
    api_response = api_instance.get_spaces(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_spaces: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all spaces of the model
    api_response = api_instance.get_spaces(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_spaces: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve all spaces of the model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone**
> Zone get_zone(cloud_pk, id, ifc_pk, project_pk)

Retrieve one zone of a model

Retrieve one zone of a model Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve one zone of a model
    api_response = api_instance.get_zone(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_zone: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve one zone of a model
    api_response = api_instance.get_zone(cloud_pk, id, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_zone: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Retrieve one zone of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_space**
> ZoneSpace get_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk)

Retrieve one space of a zone

Retrieve one space of a zone Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 

try:
    # Retrieve one space of a zone
    api_response = api_instance.get_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_zone_space: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 

try:
    # Retrieve one space of a zone
    api_response = api_instance.get_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_zone_space: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 

try:
    # Retrieve one space of a zone
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_spaces**
> list[ZoneSpace] get_zone_spaces(cloud_pk, ifc_pk, project_pk, zone_pk)

Retrieve all spaces of a zone

Retrieve all spaces of a zone Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 

try:
    # Retrieve all spaces of a zone
    api_response = api_instance.get_zone_spaces(cloud_pk, ifc_pk, project_pk, zone_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_zone_spaces: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 

try:
    # Retrieve all spaces of a zone
    api_response = api_instance.get_zone_spaces(cloud_pk, ifc_pk, project_pk, zone_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_zone_spaces: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 

try:
    # Retrieve all spaces of a zone
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zones**
> list[Zone] get_zones(cloud_pk, ifc_pk, project_pk, color=color)

Retrieve zones of a model

Retrieve parent zones of a model. Children zones we'll be in the 'zones' field Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
color = 'color_example' # str | Filter the returned list by color (optional)

try:
    # Retrieve zones of a model
    api_response = api_instance.get_zones(cloud_pk, ifc_pk, project_pk, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_zones: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
color = 'color_example' # str | Filter the returned list by color (optional)

try:
    # Retrieve zones of a model
    api_response = api_instance.get_zones(cloud_pk, ifc_pk, project_pk, color=color)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->get_zones: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
color = 'color_example' # str | Filter the returned list by color (optional)

try:
    # Retrieve zones of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_classification_element_relations**
> list[ElementClassificationRelation] list_classification_element_relations(cloud_pk, ifc_pk, project_pk)

List all associations between classifications and elements

List all associations between classifications and elements Required scopes: ifc:read

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # List all associations between classifications and elements
    api_response = api_instance.list_classification_element_relations(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->list_classification_element_relations: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # List all associations between classifications and elements
    api_response = api_instance.list_classification_element_relations(cloud_pk, ifc_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->list_classification_element_relations: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # List all associations between classifications and elements
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_classification_of_element**
> remove_classification_of_element(cloud_pk, element_uuid, id, ifc_pk, project_pk)

Remove a classification from an element

The classification will not be deleted Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove a classification from an element
    api_instance.remove_classification_of_element(cloud_pk, element_uuid, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_classification_of_element: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove a classification from an element
    api_instance.remove_classification_of_element(cloud_pk, element_uuid, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_classification_of_element: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this classification.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove a classification from an element
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_element_property_set**
> remove_element_property_set(cloud_pk, element_uuid, id, ifc_pk, project_pk)

Remove a PropertySet from an element

Delete the relation between the element and the property set. Does not delete any object Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove a PropertySet from an element
    api_instance.remove_element_property_set(cloud_pk, element_uuid, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_element_property_set: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove a PropertySet from an element
    api_instance.remove_element_property_set(cloud_pk, element_uuid, id, ifc_pk, project_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_element_property_set: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    # Remove a PropertySet from an element
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_element_property_set_property**
> remove_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)

Remove a property from a PropertySet

 Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Remove a property from a PropertySet
    api_instance.remove_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_element_property_set_property: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Remove a property from a PropertySet
    api_instance.remove_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_element_property_set_property: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Remove a property from a PropertySet
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_element_property_set_property_definition**
> remove_element_property_set_property_definition(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)

Remove a Definition from a Property

 Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Remove a Definition from a Property
    api_instance.remove_element_property_set_property_definition(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_element_property_set_property_definition: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Remove a Definition from a Property
    api_instance.remove_element_property_set_property_definition(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_element_property_set_property_definition: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Remove a Definition from a Property
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_element_property_set_property_definition_unit**
> remove_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)

Remove a Unit from a Definition

Remove a Unit from a Definition Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Remove a Unit from a Definition
    api_instance.remove_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_element_property_set_property_definition_unit: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Remove a Unit from a Definition
    api_instance.remove_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
except ApiException as e:
    print("Exception when calling IfcApi->remove_element_property_set_property_definition_unit: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 

try:
    # Remove a Unit from a Definition
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_elements_from_classification**
> remove_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk, uuid)

Remove the classification from all elements

Remove the classification from all elements. No element nor classification will be deleted Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_classification_pk = 'ifc_classification_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

try:
    # Remove the classification from all elements
    api_instance.remove_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk, uuid)
except ApiException as e:
    print("Exception when calling IfcApi->remove_elements_from_classification: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_classification_pk = 'ifc_classification_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

try:
    # Remove the classification from all elements
    api_instance.remove_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk, uuid)
except ApiException as e:
    print("Exception when calling IfcApi->remove_elements_from_classification: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_classification_pk = 'ifc_classification_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

try:
    # Remove the classification from all elements
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
 **uuid** | **str**| IFC element or element type UUID | 

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

# **update_element**
> Element update_element(cloud_pk, ifc_pk, project_pk, uuid, data)

Update some fields of a zone

Update some fields of a zone. The IFC file will not be updated. The created element will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID
data = openapi_client.Element() # Element | 

try:
    # Update some fields of a zone
    api_response = api_instance.update_element(cloud_pk, ifc_pk, project_pk, uuid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_element: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID
data = openapi_client.Element() # Element | 

try:
    # Update some fields of a zone
    api_response = api_instance.update_element(cloud_pk, ifc_pk, project_pk, uuid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_element: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID
data = openapi_client.Element() # Element | 

try:
    # Update some fields of a zone
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ifc**
> Ifc update_ifc(cloud_pk, id, project_pk, data)

Update some fields of a model

Update some fields of a model Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = openapi_client.Ifc() # Ifc | 

try:
    # Update some fields of a model
    api_response = api_instance.update_ifc(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = openapi_client.Ifc() # Ifc | 

try:
    # Update some fields of a model
    api_response = api_instance.update_ifc(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = openapi_client.Ifc() # Ifc | 

try:
    # Update some fields of a model
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ifc_files**
> IfcFiles update_ifc_files(cloud_pk, id, project_pk, structure_file=structure_file, systems_file=systems_file, map_file=map_file, gltf_file=gltf_file, bvh_tree_file=bvh_tree_file, viewer_360_file=viewer_360_file)

Update models file (gltf, svg, structure, etc)

         Patch ifc files (gltf, structure, svg, etc)          Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
structure_file = '/path/to/file' # file |  (optional)
systems_file = '/path/to/file' # file |  (optional)
map_file = '/path/to/file' # file |  (optional)
gltf_file = '/path/to/file' # file |  (optional)
bvh_tree_file = '/path/to/file' # file |  (optional)
viewer_360_file = '/path/to/file' # file |  (optional)

try:
    # Update models file (gltf, svg, structure, etc)
    api_response = api_instance.update_ifc_files(cloud_pk, id, project_pk, structure_file=structure_file, systems_file=systems_file, map_file=map_file, gltf_file=gltf_file, bvh_tree_file=bvh_tree_file, viewer_360_file=viewer_360_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_files: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
structure_file = '/path/to/file' # file |  (optional)
systems_file = '/path/to/file' # file |  (optional)
map_file = '/path/to/file' # file |  (optional)
gltf_file = '/path/to/file' # file |  (optional)
bvh_tree_file = '/path/to/file' # file |  (optional)
viewer_360_file = '/path/to/file' # file |  (optional)

try:
    # Update models file (gltf, svg, structure, etc)
    api_response = api_instance.update_ifc_files(cloud_pk, id, project_pk, structure_file=structure_file, systems_file=systems_file, map_file=map_file, gltf_file=gltf_file, bvh_tree_file=bvh_tree_file, viewer_360_file=viewer_360_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_files: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
structure_file = '/path/to/file' # file |  (optional)
systems_file = '/path/to/file' # file |  (optional)
map_file = '/path/to/file' # file |  (optional)
gltf_file = '/path/to/file' # file |  (optional)
bvh_tree_file = '/path/to/file' # file |  (optional)
viewer_360_file = '/path/to/file' # file |  (optional)

try:
    # Update models file (gltf, svg, structure, etc)
    api_response = api_instance.update_ifc_files(cloud_pk, id, project_pk, structure_file=structure_file, systems_file=systems_file, map_file=map_file, gltf_file=gltf_file, bvh_tree_file=bvh_tree_file, viewer_360_file=viewer_360_file)
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
 **viewer_360_file** | **file**|  | [optional] 

### Return type

[**IfcFiles**](IfcFiles.md)

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

# **update_ifc_property**
> ModelProperty update_ifc_property(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of a Property

Update some fields of a Property Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.ModelProperty() # ModelProperty | 

try:
    # Update some fields of a Property
    api_response = api_instance.update_ifc_property(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_property: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.ModelProperty() # ModelProperty | 

try:
    # Update some fields of a Property
    api_response = api_instance.update_ifc_property(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_property: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.ModelProperty() # ModelProperty | 

try:
    # Update some fields of a Property
    api_response = api_instance.update_ifc_property(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**ModelProperty**](ModelProperty.md)|  | 

### Return type

[**ModelProperty**](ModelProperty.md)

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

# **update_ifc_property_definition**
> PropertyDefinition update_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of many PropertyDefinitions of a model

 Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertyDefinition() # PropertyDefinition | 

try:
    # Update some fields of many PropertyDefinitions of a model
    api_response = api_instance.update_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_property_definition: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertyDefinition() # PropertyDefinition | 

try:
    # Update some fields of many PropertyDefinitions of a model
    api_response = api_instance.update_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_property_definition: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertyDefinition() # PropertyDefinition | 

try:
    # Update some fields of many PropertyDefinitions of a model
    api_response = api_instance.update_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_property_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property definition. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**PropertyDefinition**](PropertyDefinition.md)|  | 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

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

# **update_ifc_unit**
> Unit update_ifc_unit(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of a Unit of a model

 Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Unit() # Unit | 

try:
    # Update some fields of a Unit of a model
    api_response = api_instance.update_ifc_unit(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_unit: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Unit() # Unit | 

try:
    # Update some fields of a Unit of a model
    api_response = api_instance.update_ifc_unit(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_unit: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Unit() # Unit | 

try:
    # Update some fields of a Unit of a model
    api_response = api_instance.update_ifc_unit(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_ifc_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this unit. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**Unit**](Unit.md)|  | 

### Return type

[**Unit**](Unit.md)

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

# **update_processor_handler**
> ProcessorHandler update_processor_handler(cloud_pk, id, ifc_pk, project_pk, data)

Update the status of a processor handler

 Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this processor handler.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.ProcessorHandler() # ProcessorHandler | 

try:
    # Update the status of a processor handler
    api_response = api_instance.update_processor_handler(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_processor_handler: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this processor handler.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.ProcessorHandler() # ProcessorHandler | 

try:
    # Update the status of a processor handler
    api_response = api_instance.update_processor_handler(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_processor_handler: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this processor handler.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.ProcessorHandler() # ProcessorHandler | 

try:
    # Update the status of a processor handler
    api_response = api_instance.update_processor_handler(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_processor_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this processor handler. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**ProcessorHandler**](ProcessorHandler.md)|  | 

### Return type

[**ProcessorHandler**](ProcessorHandler.md)

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

# **update_property_set**
> PropertySet update_property_set(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of a PropertySet

Update some fields of a PropertySet Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertySet() # PropertySet | 

try:
    # Update some fields of a PropertySet
    api_response = api_instance.update_property_set(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_property_set: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertySet() # PropertySet | 

try:
    # Update some fields of a PropertySet
    api_response = api_instance.update_property_set(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_property_set: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.PropertySet() # PropertySet | 

try:
    # Update some fields of a PropertySet
    api_response = api_instance.update_property_set(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_property_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this property set. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**PropertySet**](PropertySet.md)|  | 

### Return type

[**PropertySet**](PropertySet.md)

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

# **update_space**
> Space update_space(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of a space

Update some fields of a space. The IFC file will not be updated. The created space will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Space() # Space | 

try:
    # Update some fields of a space
    api_response = api_instance.update_space(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_space: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Space() # Space | 

try:
    # Update some fields of a space
    api_response = api_instance.update_space(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_space: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Space() # Space | 

try:
    # Update some fields of a space
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zone**
> Zone update_zone(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of a zone

Update some fields of a zone. The IFC file will not be updated. The created zone will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Zone() # Zone | 

try:
    # Update some fields of a zone
    api_response = api_instance.update_zone(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_zone: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Zone() # Zone | 

try:
    # Update some fields of a zone
    api_response = api_instance.update_zone(cloud_pk, id, ifc_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_zone: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = openapi_client.Zone() # Zone | 

try:
    # Update some fields of a zone
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zone_space**
> ZoneSpace update_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk, data)

Update some fields of a space

Update some fields of a space. The IFC file will not be updated. The created space will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* OAuth Authentication (BIMDataConnect):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = openapi_client.ZoneSpace() # ZoneSpace | 

try:
    # Update some fields of a space
    api_response = api_instance.update_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_zone_space: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = openapi_client.ZoneSpace() # ZoneSpace | 

try:
    # Update some fields of a space
    api_response = api_instance.update_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IfcApi->update_zone_space: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: BIMDataConnect
configuration.access_token = 'YOUR_ACCESS_TOKEN'
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: client_credentials
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api-beta.bimdata.io
configuration.host = "https://api-beta.bimdata.io"
# Create an instance of the API class
api_instance = openapi_client.IfcApi(openapi_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = openapi_client.ZoneSpace() # ZoneSpace | 

try:
    # Update some fields of a space
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

[BIMDataConnect](../README.md#BIMDataConnect), [Bearer](../README.md#Bearer), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

