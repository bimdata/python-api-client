# bimdata_api_client.IfcApi

All URIs are relative to *https://api.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ifc_errors**](IfcApi.md#add_ifc_errors) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/errors | Add errors to IFC
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
[**create_access_token**](IfcApi.md#create_access_token) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/access_token | Create a token for this model
[**create_classification_element_relations**](IfcApi.md#create_classification_element_relations) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification-element | Create association between existing classification and existing element
[**create_classifications_of_element**](IfcApi.md#create_classifications_of_element) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification | Create one or many classifications to an element
[**create_element**](IfcApi.md#create_element) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element | Create an element in the model
[**create_element_property_set**](IfcApi.md#create_element_property_set) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset | Create a PropertySets to an element
[**create_element_property_set_property**](IfcApi.md#create_element_property_set_property) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property | Create a property to a PropertySet
[**create_element_property_set_property_definition**](IfcApi.md#create_element_property_set_property_definition) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition | Create a Definition to a Property
[**create_element_property_set_property_definition_unit**](IfcApi.md#create_element_property_set_property_definition_unit) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit | Create a Unit to a Definition
[**create_ifc_property_definition**](IfcApi.md#create_ifc_property_definition) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition | Create a PropertyDefinition on the model
[**create_ifc_unit**](IfcApi.md#create_ifc_unit) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit | Create a Unit on a model
[**create_layer**](IfcApi.md#create_layer) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/layer | Create a layer in the model
[**create_property_set**](IfcApi.md#create_property_set) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset | Create a PropertySet
[**create_property_set_element_relations**](IfcApi.md#create_property_set_element_relations) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset-element | Create association between PropertySet and element
[**create_raw_elements**](IfcApi.md#create_raw_elements) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/raw | Create elements in an optimized format
[**create_space**](IfcApi.md#create_space) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space | Create a space in the model
[**create_system**](IfcApi.md#create_system) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/system | Create a system in the model
[**create_zone**](IfcApi.md#create_zone) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone | Create a zone in the model
[**create_zone_space**](IfcApi.md#create_zone_space) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space | Create a space in a zone
[**delete_access_token**](IfcApi.md#delete_access_token) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/access_token/{token} | Delete a token
[**delete_element**](IfcApi.md#delete_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | Delete an element of a model
[**delete_ifc**](IfcApi.md#delete_ifc) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | Delete a model
[**delete_ifc_property**](IfcApi.md#delete_ifc_property) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | Delete a Property of a model
[**delete_ifc_property_definition**](IfcApi.md#delete_ifc_property_definition) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | Delete a PropertyDefinitions of a model
[**delete_ifc_unit**](IfcApi.md#delete_ifc_unit) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | Delete a Unit of a model
[**delete_layer**](IfcApi.md#delete_layer) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/layer/{id} | Delete a layer of a model
[**delete_property_set**](IfcApi.md#delete_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | Delete a PropertySet of a model
[**delete_space**](IfcApi.md#delete_space) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | Delete a space
[**delete_system**](IfcApi.md#delete_system) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/system/{uuid} | Delete a system of a model
[**delete_zone**](IfcApi.md#delete_zone) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | Delete a zone of a model
[**delete_zone_space**](IfcApi.md#delete_zone_space) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | Delete a space of a zone
[**export_ifc**](IfcApi.md#export_ifc) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/export | Export IFC
[**full_update_element**](IfcApi.md#full_update_element) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | Update all fields of an element
[**get_access_token**](IfcApi.md#get_access_token) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/access_token/{token} | Retrieve one token created for this model
[**get_access_tokens**](IfcApi.md#get_access_tokens) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/access_token | Retrieve all tokens created for this model
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
[**get_ifc_classifications**](IfcApi.md#get_ifc_classifications) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification | Retrieve all classifications in a model
[**get_ifc_material**](IfcApi.md#get_ifc_material) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/material/{id} | Retrieve a material of a model
[**get_ifc_materials**](IfcApi.md#get_ifc_materials) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/material | Retrieve all materials of a model
[**get_ifc_properties**](IfcApi.md#get_ifc_properties) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property | Retrieve all Properties of a model
[**get_ifc_property**](IfcApi.md#get_ifc_property) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | Retrieve a Property of a model
[**get_ifc_property_definition**](IfcApi.md#get_ifc_property_definition) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | Retrieve a PropertyDefinition of a model
[**get_ifc_property_definitions**](IfcApi.md#get_ifc_property_definitions) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition | Retrieve all PropertyDefinitions of a model
[**get_ifc_unit**](IfcApi.md#get_ifc_unit) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | Retrieve a Unit of a model
[**get_ifc_units**](IfcApi.md#get_ifc_units) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit | Retrieve all Units of a model
[**get_ifcs**](IfcApi.md#get_ifcs) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc | Retrieve all models
[**get_layer**](IfcApi.md#get_layer) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/layer/{id} | Retrieve a layer of a model
[**get_layers**](IfcApi.md#get_layers) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/layer | Retrieve all layers of a model
[**get_material**](IfcApi.md#get_material) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/material/{id} | Retrieve a material of a model
[**get_materials**](IfcApi.md#get_materials) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/material | Retrieve all materials of a model
[**get_processor_handler**](IfcApi.md#get_processor_handler) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/processorhandler/{id} | Retrieve a processor handler
[**get_processor_handlers**](IfcApi.md#get_processor_handlers) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/processorhandler | Get all processor handlers
[**get_property_set**](IfcApi.md#get_property_set) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | Retrieve a PropertySet of a model
[**get_property_sets**](IfcApi.md#get_property_sets) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset | Retrieve all PropertySets of a model
[**get_raw_elements**](IfcApi.md#get_raw_elements) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/raw | Retrieve all elements in a optimized format
[**get_simple_element**](IfcApi.md#get_simple_element) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid}/simple | Retrieve an element of a model with a simple value representation
[**get_simple_elements**](IfcApi.md#get_simple_elements) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/simple | Retrieve all elements of a model with a simple value representation
[**get_space**](IfcApi.md#get_space) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | Retrieve one space of the model
[**get_spaces**](IfcApi.md#get_spaces) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space | Retrieve all spaces of the model
[**get_system**](IfcApi.md#get_system) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/system/{uuid} | Retrieve a system of a model
[**get_systems**](IfcApi.md#get_systems) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/system | Retrieve all systems of a model
[**get_zone**](IfcApi.md#get_zone) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | Retrieve one zone of a model
[**get_zone_space**](IfcApi.md#get_zone_space) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | Retrieve one space of a zone
[**get_zone_spaces**](IfcApi.md#get_zone_spaces) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space | Retrieve all spaces of a zone
[**get_zones**](IfcApi.md#get_zones) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone | Retrieve zones of a model
[**list_classification_element_relations**](IfcApi.md#list_classification_element_relations) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification-element | List all associations between classifications and elements
[**merge_ifcs**](IfcApi.md#merge_ifcs) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/merge | Merge IFC files
[**optimize_ifc**](IfcApi.md#optimize_ifc) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/optimize | Optimize the IFC
[**remove_all_element_property_set**](IfcApi.md#remove_all_element_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/all | Remove all property sets from element
[**remove_classification_of_element**](IfcApi.md#remove_classification_of_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification/{id} | Remove a classification from an element
[**remove_element_property_set**](IfcApi.md#remove_element_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{id} | Remove a PropertySet from an element
[**remove_element_property_set_property**](IfcApi.md#remove_element_property_set_property) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{id} | Remove a property from a PropertySet
[**remove_element_property_set_property_definition**](IfcApi.md#remove_element_property_set_property_definition) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{id} | Remove a Definition from a Property
[**remove_element_property_set_property_definition_unit**](IfcApi.md#remove_element_property_set_property_definition_unit) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit/{id} | Remove a Unit from a Definition
[**remove_elements_from_classification**](IfcApi.md#remove_elements_from_classification) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/{ifc_classification_pk}/element/{uuid} | Remove the classification from all elements
[**reprocess_ifc**](IfcApi.md#reprocess_ifc) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/reprocess | Reprocess IFC file
[**update_access_token**](IfcApi.md#update_access_token) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/access_token/{token} | Update some fields of a token
[**update_element**](IfcApi.md#update_element) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | Update some fields of an element
[**update_element_property_set_property**](IfcApi.md#update_element_property_set_property) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{id} | Update a property from an element
[**update_ifc**](IfcApi.md#update_ifc) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | Update some fields of a model
[**update_ifc_files**](IfcApi.md#update_ifc_files) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/files | Update models file (gltf, svg, structure, etc)
[**update_ifc_property**](IfcApi.md#update_ifc_property) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | Update some fields of a Property
[**update_ifc_property_definition**](IfcApi.md#update_ifc_property_definition) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | Update some fields of many PropertyDefinitions of a model
[**update_ifc_unit**](IfcApi.md#update_ifc_unit) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | Update some fields of a Unit of a model
[**update_layer**](IfcApi.md#update_layer) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/layer/{id} | Update some fields of a layer
[**update_processor_handler**](IfcApi.md#update_processor_handler) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/processorhandler/{id} | Update the status of a processor handler
[**update_property_set**](IfcApi.md#update_property_set) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | Update some fields of a PropertySet
[**update_space**](IfcApi.md#update_space) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | Update some fields of a space
[**update_system**](IfcApi.md#update_system) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/system/{uuid} | Update some fields of a system
[**update_zone**](IfcApi.md#update_zone) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | Update some fields of a zone
[**update_zone_space**](IfcApi.md#update_zone_space) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | Update some fields of a space


# **add_ifc_errors**
> IfcErrors add_ifc_errors(cloud_pk, id, project_pk, data)

Add errors to IFC

IFC errors are warnings and errors during IFC process. They alert about missing elements or malformed files Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcErrors() # IfcErrors | 

    try:
        # Add errors to IFC
        api_response = api_instance.add_ifc_errors(cloud_pk, id, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->add_ifc_errors: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcErrors() # IfcErrors | 

    try:
        # Add errors to IFC
        api_response = api_instance.add_ifc_errors(cloud_pk, id, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->add_ifc_errors: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcErrors() # IfcErrors | 

    try:
        # Add errors to IFC
        api_response = api_instance.add_ifc_errors(cloud_pk, id, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->add_ifc_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc. | 
 **project_pk** | **str**|  | 
 **data** | [**IfcErrors**](IfcErrors.md)|  | 

### Return type

[**IfcErrors**](IfcErrors.md)

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

# **bulk_delete_ifc_classifications**
> bulk_delete_ifc_classifications(cloud_pk, ifc_pk, project_pk)

Remove all classifications from model's elements

             Delete relation between filtered classifications (eg. /classifications?name=untec) and all ifc's elements.             No classification will be deleted on this endpoint, only the relation between ifc's elements and their classification.  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Remove all classifications from model's elements
        api_instance.bulk_delete_ifc_classifications(cloud_pk, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->bulk_delete_ifc_classifications: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_ifc_properties**
> bulk_delete_ifc_properties(cloud_pk, ifc_pk, project_pk)

Delete many Property of a model

         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Delete many Property of a model
        api_instance.bulk_delete_ifc_properties(cloud_pk, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->bulk_delete_ifc_properties: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_ifc_property_definitions**
> bulk_delete_ifc_property_definitions(cloud_pk, ifc_pk, project_pk)

Delete many PropertyDefinitions of a model

         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Delete many PropertyDefinitions of a model
        api_instance.bulk_delete_ifc_property_definitions(cloud_pk, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->bulk_delete_ifc_property_definitions: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_ifc_units**
> bulk_delete_ifc_units(cloud_pk, ifc_pk, project_pk)

Delete many Units of a model

         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Delete many Units of a model
        api_instance.bulk_delete_ifc_units(cloud_pk, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->bulk_delete_ifc_units: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_property_set**
> bulk_delete_property_set(cloud_pk, ifc_pk, project_pk)

Delete many PropertySet of a model

         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Delete many PropertySet of a model
        api_instance.bulk_delete_property_set(cloud_pk, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->bulk_delete_property_set: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_full_update_elements**
> list[Element] bulk_full_update_elements(cloud_pk, ifc_pk, project_pk, data)

Update many elements at once (only changing fields may be defined)

         Bulk update.         Similar to update, but the body should be a list of objects to patch or put         The response will be a list (in the same order) of updated objects or of errors if any         If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Element()] # list[Element] | 

    try:
        # Update many elements at once (only changing fields may be defined)
        api_response = api_instance.bulk_full_update_elements(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->bulk_full_update_elements: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Element()] # list[Element] | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Element()] # list[Element] | 

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

# **bulk_full_update_ifc_property**
> list[ModelProperty] bulk_full_update_ifc_property(cloud_pk, ifc_pk, project_pk, data)

Update some fields of many properties of a model

         Bulk update.         Similar to update, but the body should be a list of objects to patch or put         The response will be a list (in the same order) of updated objects or of errors if any         If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ModelProperty()] # list[ModelProperty] | 

    try:
        # Update some fields of many properties of a model
        api_response = api_instance.bulk_full_update_ifc_property(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->bulk_full_update_ifc_property: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ModelProperty()] # list[ModelProperty] | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ModelProperty()] # list[ModelProperty] | 

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

# **bulk_remove_classifications_of_element**
> bulk_remove_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk)

Remove many classifications from an element

         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_remove_elements_from_classification**
> bulk_remove_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk)

Remove the classifications from all elements

         Bulk delete.         You should send a list of ids in the body.         These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_elements**
> list[Element] bulk_update_elements(cloud_pk, ifc_pk, project_pk, data)

Update many elements at once (all field must be defined)

         Bulk update.         Similar to update, but the body should be a list of objects to patch or put         The response will be a list (in the same order) of updated objects or of errors if any         If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Element()] # list[Element] | 

    try:
        # Update many elements at once (all field must be defined)
        api_response = api_instance.bulk_update_elements(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->bulk_update_elements: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Element()] # list[Element] | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Element()] # list[Element] | 

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

# **bulk_update_ifc_property**
> list[ModelProperty] bulk_update_ifc_property(cloud_pk, ifc_pk, project_pk, data)

Update all fields of many properties of a model

 Bulk update. Similar to update, but the body should be a list of objects to patch or put The response will be a list (in the same order) of updated objects or of errors if any If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors 

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ModelProperty()] # list[ModelProperty] | 

    try:
        # Update all fields of many properties of a model
        api_response = api_instance.bulk_update_ifc_property(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->bulk_update_ifc_property: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ModelProperty()] # list[ModelProperty] | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ModelProperty()] # list[ModelProperty] | 

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

# **create_access_token**
> IfcAccessToken create_access_token(cloud_pk, ifc_pk, project_pk, data)

Create a token for this model

Tokens are read_only by default and are valid 1 day Required scopes: ifc:token_manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcAccessToken() # IfcAccessToken | 

    try:
        # Create a token for this model
        api_response = api_instance.create_access_token(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_access_token: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcAccessToken() # IfcAccessToken | 

    try:
        # Create a token for this model
        api_response = api_instance.create_access_token(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_access_token: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcAccessToken() # IfcAccessToken | 

    try:
        # Create a token for this model
        api_response = api_instance.create_access_token(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**IfcAccessToken**](IfcAccessToken.md)|  | 

### Return type

[**IfcAccessToken**](IfcAccessToken.md)

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

# **create_classification_element_relations**
> create_classification_element_relations(cloud_pk, ifc_pk, project_pk, data)

Create association between existing classification and existing element

Create association between existing classification and existing element Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ElementClassificationRelation()] # list[ElementClassificationRelation] | 

    try:
        # Create association between existing classification and existing element
        api_instance.create_classification_element_relations(cloud_pk, ifc_pk, project_pk, data)
    except ApiException as e:
        print("Exception when calling IfcApi->create_classification_element_relations: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ElementClassificationRelation()] # list[ElementClassificationRelation] | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ElementClassificationRelation()] # list[ElementClassificationRelation] | 

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

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response is empty |  -  |
**204** | Nothing to do, the array was empty |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_classifications_of_element**
> list[Classification] create_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk, data)

Create one or many classifications to an element

         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors      If classification created already exists, it will just be added to item's classifications and will not be duplicated  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Classification()] # list[Classification] | 

    try:
        # Create one or many classifications to an element
        api_response = api_instance.create_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_classifications_of_element: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Classification()] # list[Classification] | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Classification()] # list[Classification] | 

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

# **create_element**
> list[Element] create_element(cloud_pk, ifc_pk, project_pk, data)

Create an element in the model

         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Element()] # list[Element] | 

    try:
        # Create an element in the model
        api_response = api_instance.create_element(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_element: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Element()] # list[Element] | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Element()] # list[Element] | 

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
 **data** | [**list[Element]**](Element.md)|  | 

### Return type

[**list[Element]**](Element.md)

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

# **create_element_property_set**
> PropertySet create_element_property_set(cloud_pk, element_uuid, ifc_pk, project_pk, data)

Create a PropertySets to an element

Create a PropertySets that will be automatically linked to the element Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.PropertySet() # PropertySet | 

    try:
        # Create a PropertySets to an element
        api_response = api_instance.create_element_property_set(cloud_pk, element_uuid, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_element_property_set: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.PropertySet() # PropertySet | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.PropertySet() # PropertySet | 

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

# **create_element_property_set_property**
> ModelProperty create_element_property_set_property(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk, data)

Create a property to a PropertySet

 Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.ModelProperty() # ModelProperty | 

    try:
        # Create a property to a PropertySet
        api_response = api_instance.create_element_property_set_property(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_element_property_set_property: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.ModelProperty() # ModelProperty | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.ModelProperty() # ModelProperty | 

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

# **create_element_property_set_property_definition**
> PropertyDefinition create_element_property_set_property_definition(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk, data)

Create a Definition to a Property

 Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.PropertyDefinition() # PropertyDefinition | 

    try:
        # Create a Definition to a Property
        api_response = api_instance.create_element_property_set_property_definition(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_element_property_set_property_definition: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.PropertyDefinition() # PropertyDefinition | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.PropertyDefinition() # PropertyDefinition | 

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

# **create_element_property_set_property_definition_unit**
> Unit create_element_property_set_property_definition_unit(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk, data)

Create a Unit to a Definition

Create a Unit to a Definition Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.Unit() # Unit | 

    try:
        # Create a Unit to a Definition
        api_response = api_instance.create_element_property_set_property_definition_unit(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_element_property_set_property_definition_unit: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.Unit() # Unit | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
property_pk = 'property_pk_example' # str | 
propertydefinition_pk = 'propertydefinition_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.Unit() # Unit | 

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

# **create_ifc_property_definition**
> list[PropertyDefinition] create_ifc_property_definition(cloud_pk, ifc_pk, project_pk, data)

Create a PropertyDefinition on the model

         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.PropertyDefinition()] # list[PropertyDefinition] | 

    try:
        # Create a PropertyDefinition on the model
        api_response = api_instance.create_ifc_property_definition(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_ifc_property_definition: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.PropertyDefinition()] # list[PropertyDefinition] | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.PropertyDefinition()] # list[PropertyDefinition] | 

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
 **data** | [**list[PropertyDefinition]**](PropertyDefinition.md)|  | 

### Return type

[**list[PropertyDefinition]**](PropertyDefinition.md)

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

# **create_ifc_unit**
> list[Unit] create_ifc_unit(cloud_pk, ifc_pk, project_pk, data)

Create a Unit on a model

         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Unit()] # list[Unit] | 

    try:
        # Create a Unit on a model
        api_response = api_instance.create_ifc_unit(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_ifc_unit: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Unit()] # list[Unit] | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Unit()] # list[Unit] | 

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
 **data** | [**list[Unit]**](Unit.md)|  | 

### Return type

[**list[Unit]**](Unit.md)

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

# **create_layer**
> Layer create_layer(cloud_pk, ifc_pk, project_pk, data)

Create a layer in the model

The IFC file will not be updated. The created layer will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Layer() # Layer | 

    try:
        # Create a layer in the model
        api_response = api_instance.create_layer(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_layer: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Layer() # Layer | 

    try:
        # Create a layer in the model
        api_response = api_instance.create_layer(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_layer: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Layer() # Layer | 

    try:
        # Create a layer in the model
        api_response = api_instance.create_layer(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**Layer**](Layer.md)|  | 

### Return type

[**Layer**](Layer.md)

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

# **create_property_set**
> list[PropertySet] create_property_set(cloud_pk, ifc_pk, project_pk, data)

Create a PropertySet

         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.PropertySet()] # list[PropertySet] | 

    try:
        # Create a PropertySet
        api_response = api_instance.create_property_set(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_property_set: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.PropertySet()] # list[PropertySet] | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.PropertySet()] # list[PropertySet] | 

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
 **data** | [**list[PropertySet]**](PropertySet.md)|  | 

### Return type

[**list[PropertySet]**](PropertySet.md)

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

# **create_property_set_element_relations**
> create_property_set_element_relations(cloud_pk, ifc_pk, project_pk, data)

Create association between PropertySet and element

Create association between existing PropertySet and existing element Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ElementPropertySetRelation()] # list[ElementPropertySetRelation] | 

    try:
        # Create association between PropertySet and element
        api_instance.create_property_set_element_relations(cloud_pk, ifc_pk, project_pk, data)
    except ApiException as e:
        print("Exception when calling IfcApi->create_property_set_element_relations: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ElementPropertySetRelation()] # list[ElementPropertySetRelation] | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.ElementPropertySetRelation()] # list[ElementPropertySetRelation] | 

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

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response is empty |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_raw_elements**
> create_raw_elements(cloud_pk, ifc_pk, project_pk, data)

Create elements in an optimized format

         You can use the same optimized structure to post multiple elements, property_sets, properties, definitions and units at once.         For performance reasons, we do not check the validity of the json. If the json is malformed, an error 500 without more explaination may be returned instead of a 400.  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.RawElements() # RawElements | 

    try:
        # Create elements in an optimized format
        api_instance.create_raw_elements(cloud_pk, ifc_pk, project_pk, data)
    except ApiException as e:
        print("Exception when calling IfcApi->create_raw_elements: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.RawElements() # RawElements | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.RawElements() # RawElements | 

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

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Empty response |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_space**
> list[Space] create_space(cloud_pk, ifc_pk, project_pk, data)

Create a space in the model

         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Space()] # list[Space] | 

    try:
        # Create a space in the model
        api_response = api_instance.create_space(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_space: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Space()] # list[Space] | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Space()] # list[Space] | 

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
 **data** | [**list[Space]**](Space.md)|  | 

### Return type

[**list[Space]**](Space.md)

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

# **create_system**
> System create_system(cloud_pk, ifc_pk, project_pk, data)

Create a system in the model

The IFC file will not be updated. The created system will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.System() # System | 

    try:
        # Create a system in the model
        api_response = api_instance.create_system(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_system: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.System() # System | 

    try:
        # Create a system in the model
        api_response = api_instance.create_system(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_system: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.System() # System | 

    try:
        # Create a system in the model
        api_response = api_instance.create_system(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**System**](System.md)|  | 

### Return type

[**System**](System.md)

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

# **create_zone**
> list[Zone] create_zone(cloud_pk, ifc_pk, project_pk, data)

Create a zone in the model

         Bulk create available.         You can either post an object or a list of objects.         Is you post a list, the response will be a list (in the same order) of created objects or of errors if any         If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors  The IFC file will not be updated. The created zone will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Zone()] # list[Zone] | 

    try:
        # Create a zone in the model
        api_response = api_instance.create_zone(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_zone: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Zone()] # list[Zone] | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = [bimdata_api_client.Zone()] # list[Zone] | 

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
 **data** | [**list[Zone]**](Zone.md)|  | 

### Return type

[**list[Zone]**](Zone.md)

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

# **create_zone_space**
> ZoneSpace create_zone_space(cloud_pk, ifc_pk, project_pk, zone_pk, data)

Create a space in a zone

The IFC file will not be updated. The created space will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = bimdata_api_client.ZoneSpace() # ZoneSpace | 

    try:
        # Create a space in a zone
        api_response = api_instance.create_zone_space(cloud_pk, ifc_pk, project_pk, zone_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->create_zone_space: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = bimdata_api_client.ZoneSpace() # ZoneSpace | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = bimdata_api_client.ZoneSpace() # ZoneSpace | 

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

# **delete_access_token**
> delete_access_token(cloud_pk, ifc_pk, project_pk, token)

Delete a token

Deleting a token will revoke it. Required scopes: ifc:token_manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
token = 'token_example' # str | 

    try:
        # Delete a token
        api_instance.delete_access_token(cloud_pk, ifc_pk, project_pk, token)
    except ApiException as e:
        print("Exception when calling IfcApi->delete_access_token: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
token = 'token_example' # str | 

    try:
        # Delete a token
        api_instance.delete_access_token(cloud_pk, ifc_pk, project_pk, token)
    except ApiException as e:
        print("Exception when calling IfcApi->delete_access_token: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
token = 'token_example' # str | 

    try:
        # Delete a token
        api_instance.delete_access_token(cloud_pk, ifc_pk, project_pk, token)
    except ApiException as e:
        print("Exception when calling IfcApi->delete_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **token** | **str**|  | 

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

# **delete_element**
> delete_element(cloud_pk, ifc_pk, project_pk, uuid)

Delete an element of a model

The IFC file will not be updated. The remaining elements are available in API and will be available when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

    try:
        # Delete an element of a model
        api_instance.delete_element(cloud_pk, ifc_pk, project_pk, uuid)
    except ApiException as e:
        print("Exception when calling IfcApi->delete_element: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

    try:
        # Delete an element of a model
        api_instance.delete_element(cloud_pk, ifc_pk, project_pk, uuid)
    except ApiException as e:
        print("Exception when calling IfcApi->delete_element: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

    try:
        # Delete an element of a model
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

# **delete_ifc**
> delete_ifc(cloud_pk, id, project_pk)

Delete a model

It will delete the related document too Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a model
        api_instance.delete_ifc(cloud_pk, id, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->delete_ifc: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **delete_ifc_property**
> delete_ifc_property(cloud_pk, id, ifc_pk, project_pk)

Delete a Property of a model

Delete a Property of a model Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **delete_ifc_property_definition**
> delete_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk)

Delete a PropertyDefinitions of a model

Delete a PropertyDefinitions of a model Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **delete_ifc_unit**
> delete_ifc_unit(cloud_pk, id, ifc_pk, project_pk)

Delete a Unit of a model

Delete a Unit of a model Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **delete_layer**
> delete_layer(cloud_pk, id, ifc_pk, project_pk)

Delete a layer of a model

The IFC file will not be updated. The remaining layers are available in API and will be available when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this layer.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a layer of a model
        api_instance.delete_layer(cloud_pk, id, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->delete_layer: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this layer.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a layer of a model
        api_instance.delete_layer(cloud_pk, id, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->delete_layer: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this layer.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a layer of a model
        api_instance.delete_layer(cloud_pk, id, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->delete_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this layer. | 
 **ifc_pk** | **str**|  | 
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

# **delete_property_set**
> delete_property_set(cloud_pk, id, ifc_pk, project_pk)

Delete a PropertySet of a model

Delete a PropertySet of a model Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **delete_space**
> delete_space(cloud_pk, id, ifc_pk, project_pk)

Delete a space

It will not delete related zones. The IFC file will not be updated. The remaining spaces are available in API and will be available when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **delete_system**
> delete_system(cloud_pk, ifc_pk, project_pk, uuid)

Delete a system of a model

The IFC file will not be updated. The remaining systems are available in API and will be available when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC sytem or system type UUID

    try:
        # Delete a system of a model
        api_instance.delete_system(cloud_pk, ifc_pk, project_pk, uuid)
    except ApiException as e:
        print("Exception when calling IfcApi->delete_system: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC sytem or system type UUID

    try:
        # Delete a system of a model
        api_instance.delete_system(cloud_pk, ifc_pk, project_pk, uuid)
    except ApiException as e:
        print("Exception when calling IfcApi->delete_system: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC sytem or system type UUID

    try:
        # Delete a system of a model
        api_instance.delete_system(cloud_pk, ifc_pk, project_pk, uuid)
    except ApiException as e:
        print("Exception when calling IfcApi->delete_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **uuid** | **str**| IFC sytem or system type UUID | 

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

# **delete_zone**
> delete_zone(cloud_pk, id, ifc_pk, project_pk)

Delete a zone of a model

The IFC file will not be updated. The remaining zones are available in API and will be available when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **delete_zone_space**
> delete_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk)

Delete a space of a zone

The IFC file will not be updated. The remaining spaces are available in API and will be available when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **export_ifc**
> IfcExport export_ifc(cloud_pk, id, project_pk, data)

Export IFC

Export IFC as requested in parameters. When the export is finished, a new IFC file with will be created in the same folder than the original IFC. You can query the folder or subscribe to the new document webhook to retrieve the result Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcExport() # IfcExport | 

    try:
        # Export IFC
        api_response = api_instance.export_ifc(cloud_pk, id, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->export_ifc: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcExport() # IfcExport | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcExport() # IfcExport | 

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

# **full_update_element**
> Element full_update_element(cloud_pk, ifc_pk, project_pk, uuid, data)

Update all fields of an element

Update all fields of an element. The IFC file will not be updated. The created element will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID
data = bimdata_api_client.Element() # Element | 

    try:
        # Update all fields of an element
        api_response = api_instance.full_update_element(cloud_pk, ifc_pk, project_pk, uuid, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->full_update_element: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID
data = bimdata_api_client.Element() # Element | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID
data = bimdata_api_client.Element() # Element | 

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

# **get_access_token**
> IfcAccessToken get_access_token(cloud_pk, ifc_pk, project_pk, token)

Retrieve one token created for this model

Retrieve one token created for this model Required scopes: ifc:token_manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
token = 'token_example' # str | 

    try:
        # Retrieve one token created for this model
        api_response = api_instance.get_access_token(cloud_pk, ifc_pk, project_pk, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_access_token: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
token = 'token_example' # str | 

    try:
        # Retrieve one token created for this model
        api_response = api_instance.get_access_token(cloud_pk, ifc_pk, project_pk, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_access_token: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
token = 'token_example' # str | 

    try:
        # Retrieve one token created for this model
        api_response = api_instance.get_access_token(cloud_pk, ifc_pk, project_pk, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **token** | **str**|  | 

### Return type

[**IfcAccessToken**](IfcAccessToken.md)

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

# **get_access_tokens**
> list[IfcAccessToken] get_access_tokens(cloud_pk, ifc_pk, project_pk)

Retrieve all tokens created for this model

Retrieve all tokens created for this model Required scopes: ifc:token_manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all tokens created for this model
        api_response = api_instance.get_access_tokens(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_access_tokens: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all tokens created for this model
        api_response = api_instance.get_access_tokens(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_access_tokens: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all tokens created for this model
        api_response = api_instance.get_access_tokens(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_access_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[IfcAccessToken]**](IfcAccessToken.md)

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

# **get_classifications_of_element**
> list[Classification] get_classifications_of_element(cloud_pk, element_uuid, ifc_pk, project_pk)

Retrieve all classifications of an element

Retrieve all classifications of an element Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_element**
> Element get_element(cloud_pk, ifc_pk, project_pk, uuid)

Retrieve an element of a model

Retrieve an element of a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_element_property_set**
> PropertySet get_element_property_set(cloud_pk, element_uuid, id, ifc_pk, project_pk)

Retrieve a PropertySet of an element

Retrieve a PropertySet of an element Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_element_property_set_properties**
> list[ModelProperty] get_element_property_set_properties(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk)

Retrieve all Properties of a PropertySet

Retrieve all Properties of a PropertySet Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_element_property_set_property**
> ModelProperty get_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)

Retrieve a Property of a PropertySet

Retrieve a Property of a PropertySet Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_element_property_set_property_definition**
> PropertyDefinition get_element_property_set_property_definition(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)

Retrieve a Definition of a Property

Retrieve a Definition of a Property Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_element_property_set_property_definition_unit**
> Unit get_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)

Retrieve a Unit of a Definition

Retrieve a Unit of a Definition Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_element_property_set_property_definition_units**
> list[Unit] get_element_property_set_property_definition_units(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)

Retrieve all Units of a Definition

Retrieve all Units of a Definition Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_element_property_set_property_definitions**
> list[PropertyDefinition] get_element_property_set_property_definitions(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk)

Retrieve all Definitions of a PropertySet

Retrieve all Definitions of a PropertySet Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_element_property_sets**
> list[PropertySet] get_element_property_sets(cloud_pk, element_uuid, ifc_pk, project_pk)

Retrieve all PropertySets of an element

Retrieve all PropertySets of an element Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_elements**
> list[Element] get_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)

Retrieve all elements of a model

Retrieve all elements of a model. If not filtered, the json may be very large. To efficently retrieve all elements and their data, see getRawElements Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_elements_from_classification**
> list[Element] get_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk)

Retrieve all elements with the classification

Retrieve all elements with the classification Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_ifc**
> Ifc get_ifc(cloud_pk, id, project_pk)

Retrieve one model

 Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_ifc_classifications**
> list[Classification] get_ifc_classifications(cloud_pk, ifc_pk, project_pk)

Retrieve all classifications in a model

Retrieve all classifications in a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_ifc_material**
> Material get_ifc_material(cloud_pk, id, ifc_pk, project_pk)

Retrieve a material of a model

Retrieve a material of a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this material.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve a material of a model
        api_response = api_instance.get_ifc_material(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_ifc_material: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this material.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve a material of a model
        api_response = api_instance.get_ifc_material(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_ifc_material: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this material.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve a material of a model
        api_response = api_instance.get_ifc_material(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_ifc_material: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this material. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**Material**](Material.md)

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

# **get_ifc_materials**
> list[Material] get_ifc_materials(cloud_pk, ifc_pk, project_pk)

Retrieve all materials of a model

Retrieve all materials of a model. Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all materials of a model
        api_response = api_instance.get_ifc_materials(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_ifc_materials: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all materials of a model
        api_response = api_instance.get_ifc_materials(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_ifc_materials: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all materials of a model
        api_response = api_instance.get_ifc_materials(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_ifc_materials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Material]**](Material.md)

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

# **get_ifc_properties**
> list[ModelProperty] get_ifc_properties(cloud_pk, ifc_pk, project_pk)

Retrieve all Properties of a model

Retrieve all PropertySets of a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_ifc_property**
> ModelProperty get_ifc_property(cloud_pk, id, ifc_pk, project_pk)

Retrieve a Property of a model

Retrieve a Property of a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_ifc_property_definition**
> PropertyDefinition get_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk)

Retrieve a PropertyDefinition of a model

Retrieve a PropertyDefinition of a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_ifc_property_definitions**
> list[PropertyDefinition] get_ifc_property_definitions(cloud_pk, ifc_pk, project_pk)

Retrieve all PropertyDefinitions of a model

Retrieve all PropertyDefinitions of a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_ifc_unit**
> Unit get_ifc_unit(cloud_pk, id, ifc_pk, project_pk)

Retrieve a Unit of a model

Retrieve a Unit of a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_ifc_units**
> list[Unit] get_ifc_units(cloud_pk, ifc_pk, project_pk)

Retrieve all Units of a model

Retrieve all Units of a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_ifcs**
> list[Ifc] get_ifcs(cloud_pk, project_pk, status=status, source=source)

Retrieve all models

Retrieve all models Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
status = 'status_example' # str | Filter the returned list by status (optional)
source = 'source_example' # str | Filter the returned list by source (optional)

    try:
        # Retrieve all models
        api_response = api_instance.get_ifcs(cloud_pk, project_pk, status=status, source=source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_ifcs: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
status = 'status_example' # str | Filter the returned list by status (optional)
source = 'source_example' # str | Filter the returned list by source (optional)

    try:
        # Retrieve all models
        api_response = api_instance.get_ifcs(cloud_pk, project_pk, status=status, source=source)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_ifcs: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
status = 'status_example' # str | Filter the returned list by status (optional)
source = 'source_example' # str | Filter the returned list by source (optional)

    try:
        # Retrieve all models
        api_response = api_instance.get_ifcs(cloud_pk, project_pk, status=status, source=source)
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
 **source** | **str**| Filter the returned list by source | [optional] 

### Return type

[**list[Ifc]**](Ifc.md)

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

# **get_layer**
> Layer get_layer(cloud_pk, id, ifc_pk, project_pk)

Retrieve a layer of a model

Retrieve a layer of a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this layer.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve a layer of a model
        api_response = api_instance.get_layer(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_layer: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this layer.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve a layer of a model
        api_response = api_instance.get_layer(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_layer: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this layer.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve a layer of a model
        api_response = api_instance.get_layer(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this layer. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**Layer**](Layer.md)

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

# **get_layers**
> list[Layer] get_layers(cloud_pk, ifc_pk, project_pk)

Retrieve all layers of a model

Retrieve all layers of a model. Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all layers of a model
        api_response = api_instance.get_layers(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_layers: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all layers of a model
        api_response = api_instance.get_layers(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_layers: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all layers of a model
        api_response = api_instance.get_layers(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Layer]**](Layer.md)

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

# **get_material**
> Material get_material(cloud_pk, element_uuid, id, ifc_pk, project_pk)

Retrieve a material of a model

Retrieve a material of a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this material.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve a material of a model
        api_response = api_instance.get_material(cloud_pk, element_uuid, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_material: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this material.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve a material of a model
        api_response = api_instance.get_material(cloud_pk, element_uuid, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_material: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this material.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve a material of a model
        api_response = api_instance.get_material(cloud_pk, element_uuid, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_material: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **id** | **int**| A unique integer value identifying this material. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**Material**](Material.md)

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

# **get_materials**
> list[Material] get_materials(cloud_pk, element_uuid, ifc_pk, project_pk)

Retrieve all materials of a model

Retrieve all materials of a model. Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all materials of a model
        api_response = api_instance.get_materials(cloud_pk, element_uuid, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_materials: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all materials of a model
        api_response = api_instance.get_materials(cloud_pk, element_uuid, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_materials: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all materials of a model
        api_response = api_instance.get_materials(cloud_pk, element_uuid, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_materials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **element_uuid** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Material]**](Material.md)

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

# **get_processor_handler**
> ProcessorHandler get_processor_handler(cloud_pk, id, ifc_pk, project_pk)

Retrieve a processor handler

 Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_processor_handlers**
> list[ProcessorHandler] get_processor_handlers(cloud_pk, ifc_pk, project_pk)

Get all processor handlers

 Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_property_set**
> PropertySet get_property_set(cloud_pk, id, ifc_pk, project_pk)

Retrieve a PropertySet of a model

Retrieve a PropertySet of a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_property_sets**
> list[PropertySet] get_property_sets(cloud_pk, ifc_pk, project_pk)

Retrieve all PropertySets of a model

Retrieve all PropertySets of a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_raw_elements**
> RawElements get_raw_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)

Retrieve all elements in a optimized format

         Returns elements, property_sets, properties, definitions and units in a JSON optimized structure  Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_simple_element**
> SimpleElement get_simple_element(cloud_pk, ifc_pk, project_pk, uuid)

Retrieve an element of a model with a simple value representation

         Retrieve an element of a model with a simple value representation         Format response :             {                 :element_uuid: {                     \"attributes\": {                         :property_name: value,                         :property_name: value                     },                     :property_set_name: {                         :property_name: value,                         :property_name: value                     }                 }             }  Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

    try:
        # Retrieve an element of a model with a simple value representation
        api_response = api_instance.get_simple_element(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_simple_element: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

    try:
        # Retrieve an element of a model with a simple value representation
        api_response = api_instance.get_simple_element(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_simple_element: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID

    try:
        # Retrieve an element of a model with a simple value representation
        api_response = api_instance.get_simple_element(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_simple_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **uuid** | **str**| IFC element or element type UUID | 

### Return type

[**SimpleElement**](SimpleElement.md)

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

# **get_simple_elements**
> SimpleElement get_simple_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)

Retrieve all elements of a model with a simple value representation

         Retrieve all elements of a model with a simple value representation         Format response :             {                 :element_uuid: {                     \"attributes\": {                         :property_name: value,                         :property_name: value                     },                     :property_set_name: {                         :property_name: value,                         :property_name: value                     }                 }             }  Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
type = 'type_example' # str | Filter the returned list by type (optional)
classification = 'classification_example' # str | Filter the returned list by classification (optional)
classification__notation = 'classification__notation_example' # str | Filter the returned list by classification__notation (optional)

    try:
        # Retrieve all elements of a model with a simple value representation
        api_response = api_instance.get_simple_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_simple_elements: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
type = 'type_example' # str | Filter the returned list by type (optional)
classification = 'classification_example' # str | Filter the returned list by classification (optional)
classification__notation = 'classification__notation_example' # str | Filter the returned list by classification__notation (optional)

    try:
        # Retrieve all elements of a model with a simple value representation
        api_response = api_instance.get_simple_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_simple_elements: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
type = 'type_example' # str | Filter the returned list by type (optional)
classification = 'classification_example' # str | Filter the returned list by classification (optional)
classification__notation = 'classification__notation_example' # str | Filter the returned list by classification__notation (optional)

    try:
        # Retrieve all elements of a model with a simple value representation
        api_response = api_instance.get_simple_elements(cloud_pk, ifc_pk, project_pk, type=type, classification=classification, classification__notation=classification__notation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_simple_elements: %s\n" % e)
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

[**SimpleElement**](SimpleElement.md)

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

# **get_space**
> Space get_space(cloud_pk, id, ifc_pk, project_pk)

Retrieve one space of the model

Retrieve one space of the model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_spaces**
> list[Space] get_spaces(cloud_pk, ifc_pk, project_pk)

Retrieve all spaces of the model

Retrieve all spaces of the model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_system**
> System get_system(cloud_pk, ifc_pk, project_pk, uuid)

Retrieve a system of a model

Retrieve a system of a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC sytem or system type UUID

    try:
        # Retrieve a system of a model
        api_response = api_instance.get_system(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_system: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC sytem or system type UUID

    try:
        # Retrieve a system of a model
        api_response = api_instance.get_system(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_system: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC sytem or system type UUID

    try:
        # Retrieve a system of a model
        api_response = api_instance.get_system(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **uuid** | **str**| IFC sytem or system type UUID | 

### Return type

[**System**](System.md)

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

# **get_systems**
> list[System] get_systems(cloud_pk, ifc_pk, project_pk)

Retrieve all systems of a model

Retrieve all systems of a model. Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all systems of a model
        api_response = api_instance.get_systems(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_systems: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all systems of a model
        api_response = api_instance.get_systems(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_systems: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all systems of a model
        api_response = api_instance.get_systems(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->get_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[System]**](System.md)

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

# **get_zone**
> Zone get_zone(cloud_pk, id, ifc_pk, project_pk)

Retrieve one zone of a model

Retrieve one zone of a model Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_zone_space**
> ZoneSpace get_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk)

Retrieve one space of a zone

Retrieve one space of a zone Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_zone_spaces**
> list[ZoneSpace] get_zone_spaces(cloud_pk, ifc_pk, project_pk, zone_pk)

Retrieve all spaces of a zone

Retrieve all spaces of a zone Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **get_zones**
> list[Zone] get_zones(cloud_pk, ifc_pk, project_pk, color=color)

Retrieve zones of a model

Retrieve parent zones of a model. Children zones we'll be in the 'zones' field Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **list_classification_element_relations**
> list[ElementClassificationRelation] list_classification_element_relations(cloud_pk, ifc_pk, project_pk)

List all associations between classifications and elements

List all associations between classifications and elements Required scopes: ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **merge_ifcs**
> merge_ifcs(cloud_pk, project_pk, data)

Merge IFC files

Merge IFC files. The merged IFC file will be put in the same folder that the first IFC of the list Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcMerge() # IfcMerge | 

    try:
        # Merge IFC files
        api_instance.merge_ifcs(cloud_pk, project_pk, data)
    except ApiException as e:
        print("Exception when calling IfcApi->merge_ifcs: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcMerge() # IfcMerge | 

    try:
        # Merge IFC files
        api_instance.merge_ifcs(cloud_pk, project_pk, data)
    except ApiException as e:
        print("Exception when calling IfcApi->merge_ifcs: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcMerge() # IfcMerge | 

    try:
        # Merge IFC files
        api_instance.merge_ifcs(cloud_pk, project_pk, data)
    except ApiException as e:
        print("Exception when calling IfcApi->merge_ifcs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**IfcMerge**](IfcMerge.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **optimize_ifc**
> optimize_ifc(cloud_pk, id, project_pk, data)

Optimize the IFC

Optimize the IFC. A new optimized IFC file will be put in the same folder that the original IFC Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcOptimize() # IfcOptimize | 

    try:
        # Optimize the IFC
        api_instance.optimize_ifc(cloud_pk, id, project_pk, data)
    except ApiException as e:
        print("Exception when calling IfcApi->optimize_ifc: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcOptimize() # IfcOptimize | 

    try:
        # Optimize the IFC
        api_instance.optimize_ifc(cloud_pk, id, project_pk, data)
    except ApiException as e:
        print("Exception when calling IfcApi->optimize_ifc: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcOptimize() # IfcOptimize | 

    try:
        # Optimize the IFC
        api_instance.optimize_ifc(cloud_pk, id, project_pk, data)
    except ApiException as e:
        print("Exception when calling IfcApi->optimize_ifc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc. | 
 **project_pk** | **str**|  | 
 **data** | [**IfcOptimize**](IfcOptimize.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_element_property_set**
> remove_all_element_property_set(cloud_pk, element_uuid, ifc_pk, project_pk)

Remove all property sets from element

Remove all property sets from element. Property Sets will not be deleted, just detached from element Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Remove all property sets from element
        api_instance.remove_all_element_property_set(cloud_pk, element_uuid, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->remove_all_element_property_set: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Remove all property sets from element
        api_instance.remove_all_element_property_set(cloud_pk, element_uuid, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->remove_all_element_property_set: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Remove all property sets from element
        api_instance.remove_all_element_property_set(cloud_pk, element_uuid, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->remove_all_element_property_set: %s\n" % e)
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

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_classification_of_element**
> remove_classification_of_element(cloud_pk, element_uuid, id, ifc_pk, project_pk)

Remove a classification from an element

The classification will not be deleted Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **remove_element_property_set**
> remove_element_property_set(cloud_pk, element_uuid, id, ifc_pk, project_pk)

Remove a PropertySet from an element

Delete the relation between the element and the property set. Does not delete any object Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **remove_element_property_set_property**
> remove_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)

Remove a property from a PropertySet

 Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **remove_element_property_set_property_definition**
> remove_element_property_set_property_definition(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)

Remove a Definition from a Property

 Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **remove_element_property_set_property_definition_unit**
> remove_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)

Remove a Unit from a Definition

Remove a Unit from a Definition Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **remove_elements_from_classification**
> remove_elements_from_classification(cloud_pk, ifc_classification_pk, ifc_pk, project_pk, uuid)

Remove the classification from all elements

Remove the classification from all elements. No element nor classification will be deleted Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
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

# **reprocess_ifc**
> reprocess_ifc(cloud_pk, id, project_pk)

Reprocess IFC file

Reprocess the IFC. All data that are not in the original IFC files will be lost Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

    try:
        # Reprocess IFC file
        api_instance.reprocess_ifc(cloud_pk, id, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->reprocess_ifc: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

    try:
        # Reprocess IFC file
        api_instance.reprocess_ifc(cloud_pk, id, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->reprocess_ifc: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 

    try:
        # Reprocess IFC file
        api_instance.reprocess_ifc(cloud_pk, id, project_pk)
    except ApiException as e:
        print("Exception when calling IfcApi->reprocess_ifc: %s\n" % e)
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

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_token**
> IfcAccessToken update_access_token(cloud_pk, ifc_pk, project_pk, token, data)

Update some fields of a token

You can update the expiration date or the read_only field Required scopes: ifc:token_manage

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
token = 'token_example' # str | 
data = bimdata_api_client.IfcAccessToken() # IfcAccessToken | 

    try:
        # Update some fields of a token
        api_response = api_instance.update_access_token(cloud_pk, ifc_pk, project_pk, token, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_access_token: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
token = 'token_example' # str | 
data = bimdata_api_client.IfcAccessToken() # IfcAccessToken | 

    try:
        # Update some fields of a token
        api_response = api_instance.update_access_token(cloud_pk, ifc_pk, project_pk, token, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_access_token: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
token = 'token_example' # str | 
data = bimdata_api_client.IfcAccessToken() # IfcAccessToken | 

    try:
        # Update some fields of a token
        api_response = api_instance.update_access_token(cloud_pk, ifc_pk, project_pk, token, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **token** | **str**|  | 
 **data** | [**IfcAccessToken**](IfcAccessToken.md)|  | 

### Return type

[**IfcAccessToken**](IfcAccessToken.md)

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

# **update_element**
> Element update_element(cloud_pk, ifc_pk, project_pk, uuid, data)

Update some fields of an element

Update some fields of an element. The IFC file will not be updated. The created element will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID
data = bimdata_api_client.Element() # Element | 

    try:
        # Update some fields of an element
        api_response = api_instance.update_element(cloud_pk, ifc_pk, project_pk, uuid, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_element: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID
data = bimdata_api_client.Element() # Element | 

    try:
        # Update some fields of an element
        api_response = api_instance.update_element(cloud_pk, ifc_pk, project_pk, uuid, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_element: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC element or element type UUID
data = bimdata_api_client.Element() # Element | 

    try:
        # Update some fields of an element
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

# **update_element_property_set_property**
> ModelProperty update_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk, data)

Update a property from an element

Update a property value from an element. If the element is the only one to have this property, the property will be update in place. If many elements share this property, a new property will be created to replace the property for this element. Keeping the property for all other elements. If you want to update the property of all elements, see updateIfcProperty Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.ModelProperty() # ModelProperty | 

    try:
        # Update a property from an element
        api_response = api_instance.update_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_element_property_set_property: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.ModelProperty() # ModelProperty | 

    try:
        # Update a property from an element
        api_response = api_instance.update_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_element_property_set_property: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
element_uuid = 'element_uuid_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
propertyset_pk = 'propertyset_pk_example' # str | 
data = bimdata_api_client.ModelProperty() # ModelProperty | 

    try:
        # Update a property from an element
        api_response = api_instance.update_element_property_set_property(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_element_property_set_property: %s\n" % e)
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
 **data** | [**ModelProperty**](ModelProperty.md)|  | 

### Return type

[**ModelProperty**](ModelProperty.md)

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

# **update_ifc**
> Ifc update_ifc(cloud_pk, id, project_pk, data)

Update some fields of a model

Update some fields of a model Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Ifc() # Ifc | 

    try:
        # Update some fields of a model
        api_response = api_instance.update_ifc(cloud_pk, id, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_ifc: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Ifc() # Ifc | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Ifc() # Ifc | 

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

# **update_ifc_files**
> IfcFiles update_ifc_files(cloud_pk, id, project_pk, structure_file=structure_file, systems_file=systems_file, map_file=map_file, gltf_file=gltf_file, gltf_with_openings_file=gltf_with_openings_file, bvh_tree_file=bvh_tree_file, viewer_360_file=viewer_360_file, xkt_file=xkt_file)

Update models file (gltf, svg, structure, etc)

         Patch ifc files (gltf, structure, svg, etc)  Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
structure_file = '/path/to/file' # file |  (optional)
systems_file = '/path/to/file' # file |  (optional)
map_file = '/path/to/file' # file |  (optional)
gltf_file = '/path/to/file' # file |  (optional)
gltf_with_openings_file = '/path/to/file' # file |  (optional)
bvh_tree_file = '/path/to/file' # file |  (optional)
viewer_360_file = '/path/to/file' # file |  (optional)
xkt_file = '/path/to/file' # file |  (optional)

    try:
        # Update models file (gltf, svg, structure, etc)
        api_response = api_instance.update_ifc_files(cloud_pk, id, project_pk, structure_file=structure_file, systems_file=systems_file, map_file=map_file, gltf_file=gltf_file, gltf_with_openings_file=gltf_with_openings_file, bvh_tree_file=bvh_tree_file, viewer_360_file=viewer_360_file, xkt_file=xkt_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_ifc_files: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
structure_file = '/path/to/file' # file |  (optional)
systems_file = '/path/to/file' # file |  (optional)
map_file = '/path/to/file' # file |  (optional)
gltf_file = '/path/to/file' # file |  (optional)
gltf_with_openings_file = '/path/to/file' # file |  (optional)
bvh_tree_file = '/path/to/file' # file |  (optional)
viewer_360_file = '/path/to/file' # file |  (optional)
xkt_file = '/path/to/file' # file |  (optional)

    try:
        # Update models file (gltf, svg, structure, etc)
        api_response = api_instance.update_ifc_files(cloud_pk, id, project_pk, structure_file=structure_file, systems_file=systems_file, map_file=map_file, gltf_file=gltf_file, gltf_with_openings_file=gltf_with_openings_file, bvh_tree_file=bvh_tree_file, viewer_360_file=viewer_360_file, xkt_file=xkt_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_ifc_files: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc.
project_pk = 'project_pk_example' # str | 
structure_file = '/path/to/file' # file |  (optional)
systems_file = '/path/to/file' # file |  (optional)
map_file = '/path/to/file' # file |  (optional)
gltf_file = '/path/to/file' # file |  (optional)
gltf_with_openings_file = '/path/to/file' # file |  (optional)
bvh_tree_file = '/path/to/file' # file |  (optional)
viewer_360_file = '/path/to/file' # file |  (optional)
xkt_file = '/path/to/file' # file |  (optional)

    try:
        # Update models file (gltf, svg, structure, etc)
        api_response = api_instance.update_ifc_files(cloud_pk, id, project_pk, structure_file=structure_file, systems_file=systems_file, map_file=map_file, gltf_file=gltf_file, gltf_with_openings_file=gltf_with_openings_file, bvh_tree_file=bvh_tree_file, viewer_360_file=viewer_360_file, xkt_file=xkt_file)
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
 **gltf_with_openings_file** | **file**|  | [optional] 
 **bvh_tree_file** | **file**|  | [optional] 
 **viewer_360_file** | **file**|  | [optional] 
 **xkt_file** | **file**|  | [optional] 

### Return type

[**IfcFiles**](IfcFiles.md)

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

# **update_ifc_property**
> ModelProperty update_ifc_property(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of a Property

Update some fields of a Property Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.ModelProperty() # ModelProperty | 

    try:
        # Update some fields of a Property
        api_response = api_instance.update_ifc_property(cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_ifc_property: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.ModelProperty() # ModelProperty | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.ModelProperty() # ModelProperty | 

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

# **update_ifc_property_definition**
> PropertyDefinition update_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of many PropertyDefinitions of a model

 Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.PropertyDefinition() # PropertyDefinition | 

    try:
        # Update some fields of many PropertyDefinitions of a model
        api_response = api_instance.update_ifc_property_definition(cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_ifc_property_definition: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.PropertyDefinition() # PropertyDefinition | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property definition.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.PropertyDefinition() # PropertyDefinition | 

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

# **update_ifc_unit**
> Unit update_ifc_unit(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of a Unit of a model

 Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Unit() # Unit | 

    try:
        # Update some fields of a Unit of a model
        api_response = api_instance.update_ifc_unit(cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_ifc_unit: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Unit() # Unit | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this unit.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Unit() # Unit | 

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

# **update_layer**
> Layer update_layer(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of a layer

Update some fields of a layer. The IFC file will not be updated. The created layer will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this layer.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Layer() # Layer | 

    try:
        # Update some fields of a layer
        api_response = api_instance.update_layer(cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_layer: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this layer.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Layer() # Layer | 

    try:
        # Update some fields of a layer
        api_response = api_instance.update_layer(cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_layer: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this layer.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Layer() # Layer | 

    try:
        # Update some fields of a layer
        api_response = api_instance.update_layer(cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this layer. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**Layer**](Layer.md)|  | 

### Return type

[**Layer**](Layer.md)

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

# **update_processor_handler**
> ProcessorHandler update_processor_handler(cloud_pk, id, ifc_pk, project_pk, data)

Update the status of a processor handler

 Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this processor handler.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.ProcessorHandler() # ProcessorHandler | 

    try:
        # Update the status of a processor handler
        api_response = api_instance.update_processor_handler(cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_processor_handler: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this processor handler.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.ProcessorHandler() # ProcessorHandler | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this processor handler.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.ProcessorHandler() # ProcessorHandler | 

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

# **update_property_set**
> PropertySet update_property_set(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of a PropertySet

Update some fields of a PropertySet Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.PropertySet() # PropertySet | 

    try:
        # Update some fields of a PropertySet
        api_response = api_instance.update_property_set(cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_property_set: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.PropertySet() # PropertySet | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this property set.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.PropertySet() # PropertySet | 

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

# **update_space**
> Space update_space(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of a space

Update some fields of a space. The IFC file will not be updated. The created space will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Space() # Space | 

    try:
        # Update some fields of a space
        api_response = api_instance.update_space(cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_space: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Space() # Space | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Space() # Space | 

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

# **update_system**
> System update_system(cloud_pk, ifc_pk, project_pk, uuid, data)

Update some fields of a system

Update some fields of a system. The IFC file will not be updated. The created system will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC sytem or system type UUID
data = bimdata_api_client.System() # System | 

    try:
        # Update some fields of a system
        api_response = api_instance.update_system(cloud_pk, ifc_pk, project_pk, uuid, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_system: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC sytem or system type UUID
data = bimdata_api_client.System() # System | 

    try:
        # Update some fields of a system
        api_response = api_instance.update_system(cloud_pk, ifc_pk, project_pk, uuid, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_system: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
uuid = 'uuid_example' # str | IFC sytem or system type UUID
data = bimdata_api_client.System() # System | 

    try:
        # Update some fields of a system
        api_response = api_instance.update_system(cloud_pk, ifc_pk, project_pk, uuid, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **uuid** | **str**| IFC sytem or system type UUID | 
 **data** | [**System**](System.md)|  | 

### Return type

[**System**](System.md)

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

# **update_zone**
> Zone update_zone(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of a zone

Update some fields of a zone. The IFC file will not be updated. The created zone will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Zone() # Zone | 

    try:
        # Update some fields of a zone
        api_response = api_instance.update_zone(cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_zone: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Zone() # Zone | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this zone.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Zone() # Zone | 

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

# **update_zone_space**
> ZoneSpace update_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk, data)

Update some fields of a space

Update some fields of a space. The IFC file will not be updated. The created space will be accessible over the API and when exporting an IFC file Required scopes: ifc:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = bimdata_api_client.ZoneSpace() # ZoneSpace | 

    try:
        # Update some fields of a space
        api_response = api_instance.update_zone_space(cloud_pk, id, ifc_pk, project_pk, zone_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IfcApi->update_zone_space: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = bimdata_api_client.ZoneSpace() # ZoneSpace | 

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
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.IfcApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this space.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
zone_pk = 'zone_pk_example' # str | 
data = bimdata_api_client.ZoneSpace() # ZoneSpace | 

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

