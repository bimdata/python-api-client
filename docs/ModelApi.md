# bimdata_api_client.ModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_model_errors**](ModelApi.md#add_model_errors) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{id}/errors | Add errors to model
[**add_zone_space**](ModelApi.md#add_zone_space) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/zone/{zone_pk}/space/add | Add a space to a zone
[**bulk_delete_model_classifications**](ModelApi.md#bulk_delete_model_classifications) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/classification/list_destroy | Remove all classifications from model&#39;s elements
[**bulk_delete_model_properties**](ModelApi.md#bulk_delete_model_properties) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/property/bulk_destroy | Delete many Property of a model
[**bulk_delete_model_property_definitions**](ModelApi.md#bulk_delete_model_property_definitions) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/propertydefinition/bulk_destroy | Delete many PropertyDefinitions of a model
[**bulk_delete_model_units**](ModelApi.md#bulk_delete_model_units) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/unit/bulk_destroy | Delete many Units of a model
[**bulk_delete_property_set**](ModelApi.md#bulk_delete_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/propertyset/bulk_destroy | Delete many PropertySet of a model
[**bulk_full_update_elements**](ModelApi.md#bulk_full_update_elements) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/bulk_update | Update many elements at once (only changing fields may be defined)
[**bulk_full_update_model_property**](ModelApi.md#bulk_full_update_model_property) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/property/bulk_update | Update some fields of many properties of a model
[**bulk_remove_classifications_of_element**](ModelApi.md#bulk_remove_classifications_of_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/classification/bulk_destroy | Remove many classifications from an element
[**bulk_remove_documents_of_element**](ModelApi.md#bulk_remove_documents_of_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/documents/bulk_destroy | Remove many documents from an element
[**bulk_remove_elements_from_classification**](ModelApi.md#bulk_remove_elements_from_classification) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/classification/{model_classification_pk}/element/bulk_destroy | Remove the classifications from all elements
[**bulk_update_elements**](ModelApi.md#bulk_update_elements) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/bulk_update | Update many elements at once (all field must be defined)
[**bulk_update_model_property**](ModelApi.md#bulk_update_model_property) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/property/bulk_update | Update all fields of many properties of a model
[**create_access_token**](ModelApi.md#create_access_token) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/access_token | Create a token for this model
[**create_building**](ModelApi.md#create_building) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/building | Create a building of a model
[**create_building_plan**](ModelApi.md#create_building_plan) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/building/{building_uuid}/plan/add | Create a relation between a 2d model and a building
[**create_classification_element_relations**](ModelApi.md#create_classification_element_relations) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/classification-element | Create association between existing classification and existing element
[**create_classifications_of_element**](ModelApi.md#create_classifications_of_element) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/classification | Create one or many classifications to an element
[**create_drawing**](ModelApi.md#create_drawing) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/drawing | Create a drawing in the model
[**create_element**](ModelApi.md#create_element) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element | Create an element in the model
[**create_element_property_set**](ModelApi.md#create_element_property_set) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset | Create a PropertySets to an element
[**create_element_property_set_property**](ModelApi.md#create_element_property_set_property) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property | Create a property to a PropertySet
[**create_element_property_set_property_definition**](ModelApi.md#create_element_property_set_property_definition) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition | Create a Definition to a Property
[**create_element_property_set_property_definition_unit**](ModelApi.md#create_element_property_set_property_definition_unit) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit | Create a Unit to a Definition
[**create_layer**](ModelApi.md#create_layer) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/layer | Create a layer in the model
[**create_mask2_d**](ModelApi.md#create_mask2_d) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/model/{id}/mask-2d | Create or update a 2D mask for the model
[**create_meta_building**](ModelApi.md#create_meta_building) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/create-metabuilding | Create an empty 3D Model
[**create_model**](ModelApi.md#create_model) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/create-model | Make a PDF or Image file a Model
[**create_model_property_definition**](ModelApi.md#create_model_property_definition) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/propertydefinition | Create a PropertyDefinition on the model
[**create_model_unit**](ModelApi.md#create_model_unit) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/unit | Create a Unit on a model
[**create_multi_page_model**](ModelApi.md#create_multi_page_model) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{id}/create-multipage-model | Create a multi page model
[**create_photosphere**](ModelApi.md#create_photosphere) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/create-photosphere | Create a photopshere model from an image file
[**create_photosphere_building**](ModelApi.md#create_photosphere_building) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/create-photosphere-building | Create an empty Photosphere Building Model
[**create_property_set**](ModelApi.md#create_property_set) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/propertyset | Create one or many PropertySet
[**create_property_set_element_relations**](ModelApi.md#create_property_set_element_relations) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/propertyset-element | Create association between PropertySet and element
[**create_raw_elements**](ModelApi.md#create_raw_elements) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/raw | Create elements in an optimized format
[**create_space**](ModelApi.md#create_space) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/space | Create a space in the model
[**create_storey**](ModelApi.md#create_storey) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/storey | Create a storey of a model
[**create_storey_plan**](ModelApi.md#create_storey_plan) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/storey/{storey_uuid}/plan/add | Create a relation between a 2d model and a storey
[**create_system**](ModelApi.md#create_system) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/system | Create a system in the model
[**create_tileset**](ModelApi.md#create_tileset) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{id}/tileset | Create the tileset of the model and upload all files
[**create_xkt_file**](ModelApi.md#create_xkt_file) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{id}/xkt-file | Create an xkt file for the model. Overrides existing file with same version
[**create_zone**](ModelApi.md#create_zone) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/zone | Create a zone in the model
[**create_zone_space**](ModelApi.md#create_zone_space) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/zone/{zone_pk}/space | Create a space in a zone
[**delete_access_token**](ModelApi.md#delete_access_token) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/access_token/{token} | Delete a token
[**delete_building**](ModelApi.md#delete_building) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/building/{uuid} | Delete a building of a model
[**delete_building_plan**](ModelApi.md#delete_building_plan) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/building/{building_uuid}/plan/{id} | Delete the relation between a 2d model and a building
[**delete_drawing**](ModelApi.md#delete_drawing) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/drawing/{id} | Delete a drawing of a model
[**delete_element**](ModelApi.md#delete_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{uuid} | Delete an element of a model
[**delete_layer**](ModelApi.md#delete_layer) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/layer/{id} | Delete a layer of a model
[**delete_mask2_d**](ModelApi.md#delete_mask2_d) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{id}/mask-2d | Delete the 2D mask for the model
[**delete_model**](ModelApi.md#delete_model) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{id} | Delete a model
[**delete_model_property**](ModelApi.md#delete_model_property) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/property/{id} | Delete a Property of a model
[**delete_model_property_definition**](ModelApi.md#delete_model_property_definition) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/propertydefinition/{id} | Delete a PropertyDefinitions of a model
[**delete_model_unit**](ModelApi.md#delete_model_unit) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/unit/{id} | Delete a Unit of a model
[**delete_model_without_doc**](ModelApi.md#delete_model_without_doc) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{id}/delete-model | Delete the Model without deleting the related document
[**delete_property_set**](ModelApi.md#delete_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/propertyset/{id} | Delete a PropertySet of a model
[**delete_space**](ModelApi.md#delete_space) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/space/{id} | Delete a space
[**delete_storey**](ModelApi.md#delete_storey) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/storey/{uuid} | Delete a storey of a model
[**delete_storey_plan**](ModelApi.md#delete_storey_plan) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/storey/{storey_uuid}/plan/{id} | Delete the relation between a 2d model and a storey
[**delete_system**](ModelApi.md#delete_system) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/system/{uuid} | Delete a system of a model
[**delete_zone**](ModelApi.md#delete_zone) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/zone/{id} | Delete a zone of a model
[**delete_zone_space**](ModelApi.md#delete_zone_space) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/zone/{zone_pk}/space/{id} | Delete the relation between a space and a zone
[**export_ifc**](ModelApi.md#export_ifc) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{id}/export | Export IFC
[**full_update_element**](ModelApi.md#full_update_element) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{uuid} | Update all fields of an element
[**get_access_token**](ModelApi.md#get_access_token) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/access_token/{token} | Retrieve one token created for this model
[**get_access_tokens**](ModelApi.md#get_access_tokens) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/access_token | Retrieve all tokens created for this model
[**get_building**](ModelApi.md#get_building) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/building/{uuid} | Retrieve a building of a model
[**get_building_plan_positioning**](ModelApi.md#get_building_plan_positioning) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/building/{building_uuid}/plan/{id}/positioning | Retrieve the postioning of the plan in the building
[**get_buildings**](ModelApi.md#get_buildings) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/building | Retrieve all buildings of a model
[**get_classifications_of_element**](ModelApi.md#get_classifications_of_element) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/classification | Retrieve all classifications of an element
[**get_documents_of_element**](ModelApi.md#get_documents_of_element) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/documents | Retrieve all documents of an element
[**get_drawing**](ModelApi.md#get_drawing) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/drawing/{id} | Retrieve a drawing of a model
[**get_drawings**](ModelApi.md#get_drawings) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/drawing | Retrieve all drawings of a model
[**get_element**](ModelApi.md#get_element) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{uuid} | Retrieve an element of a model
[**get_element_linked_documents**](ModelApi.md#get_element_linked_documents) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/documents | Retrieve all documents linked to any element
[**get_element_property_set**](ModelApi.md#get_element_property_set) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{id} | Retrieve a PropertySet of an element
[**get_element_property_set_properties**](ModelApi.md#get_element_property_set_properties) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property | Retrieve all Properties of a PropertySet
[**get_element_property_set_property**](ModelApi.md#get_element_property_set_property) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{id} | Retrieve a Property of a PropertySet
[**get_element_property_set_property_definition**](ModelApi.md#get_element_property_set_property_definition) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{id} | Retrieve a Definition of a Property
[**get_element_property_set_property_definition_unit**](ModelApi.md#get_element_property_set_property_definition_unit) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit/{id} | Retrieve a Unit of a Definition
[**get_element_property_set_property_definition_units**](ModelApi.md#get_element_property_set_property_definition_units) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit | Retrieve all Units of a Definition
[**get_element_property_set_property_definitions**](ModelApi.md#get_element_property_set_property_definitions) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition | Retrieve all Definitions of a PropertySet
[**get_element_property_sets**](ModelApi.md#get_element_property_sets) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset | Retrieve all PropertySets of an element
[**get_elements**](ModelApi.md#get_elements) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element | Retrieve all elements of a model
[**get_elements_from_classification**](ModelApi.md#get_elements_from_classification) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/classification/{model_classification_pk}/element | Retrieve all elements with the classification
[**get_layer**](ModelApi.md#get_layer) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/layer/{id} | Retrieve a layer of a model
[**get_layers**](ModelApi.md#get_layers) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/layer | Retrieve all layers of a model
[**get_material**](ModelApi.md#get_material) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/material/{id} | Retrieve a material of a model
[**get_materials**](ModelApi.md#get_materials) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/material | Retrieve all materials of a model
[**get_model**](ModelApi.md#get_model) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{id} | Retrieve one model
[**get_model_classifications**](ModelApi.md#get_model_classifications) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/classification | Retrieve all classifications in a model
[**get_model_material**](ModelApi.md#get_model_material) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/material/{id} | Retrieve a material of a model
[**get_model_materials**](ModelApi.md#get_model_materials) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/material | Retrieve all materials of a model
[**get_model_properties**](ModelApi.md#get_model_properties) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/property | Retrieve all Properties of a model
[**get_model_property**](ModelApi.md#get_model_property) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/property/{id} | Retrieve a Property of a model
[**get_model_property_definition**](ModelApi.md#get_model_property_definition) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/propertydefinition/{id} | Retrieve a PropertyDefinition of a model
[**get_model_property_definitions**](ModelApi.md#get_model_property_definitions) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/propertydefinition | Retrieve all PropertyDefinitions of a model
[**get_model_unit**](ModelApi.md#get_model_unit) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/unit/{id} | Retrieve a Unit of a model
[**get_model_units**](ModelApi.md#get_model_units) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/unit | Retrieve all Units of a model
[**get_models**](ModelApi.md#get_models) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model | Retrieve all models
[**get_processor_handler**](ModelApi.md#get_processor_handler) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/processorhandler/{id} | Retrieve a processor handler
[**get_processor_handlers**](ModelApi.md#get_processor_handlers) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/processorhandler | Get all processor handlers
[**get_property_set**](ModelApi.md#get_property_set) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/propertyset/{id} | Retrieve a PropertySet of a model
[**get_property_sets**](ModelApi.md#get_property_sets) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/propertyset | Retrieve all PropertySets of a model
[**get_raw_elements**](ModelApi.md#get_raw_elements) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/raw | Retrieve all elements in a optimized format
[**get_simple_element**](ModelApi.md#get_simple_element) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{uuid}/simple | Retrieve an element of a model with a simple value representation
[**get_simple_elements**](ModelApi.md#get_simple_elements) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/simple | Retrieve all elements of a model with a simple value representation
[**get_space**](ModelApi.md#get_space) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/space/{id} | Retrieve one space of the model
[**get_spaces**](ModelApi.md#get_spaces) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/space | Retrieve all spaces of the model
[**get_storey**](ModelApi.md#get_storey) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/storey/{uuid} | Retrieve a storey of a model
[**get_storey_plan_positioning**](ModelApi.md#get_storey_plan_positioning) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/storey/{storey_uuid}/plan/{id}/positioning | Retrieve the postioning of the plan in the storey
[**get_storeys**](ModelApi.md#get_storeys) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/storey | Retrieve all storeys of a model
[**get_system**](ModelApi.md#get_system) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/system/{uuid} | Retrieve a system of a model
[**get_systems**](ModelApi.md#get_systems) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/system | Retrieve all systems of a model
[**get_tileset**](ModelApi.md#get_tileset) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{id}/tileset | Retrieve the tileset of the model
[**get_zone**](ModelApi.md#get_zone) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/zone/{id} | Retrieve one zone of a model
[**get_zone_space**](ModelApi.md#get_zone_space) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/zone/{zone_pk}/space/{id} | Retrieve one space of a zone
[**get_zone_spaces**](ModelApi.md#get_zone_spaces) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/zone/{zone_pk}/space | Retrieve all spaces of a zone
[**get_zones**](ModelApi.md#get_zones) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/zone | Retrieve zones of a model
[**link_documents_of_element**](ModelApi.md#link_documents_of_element) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/documents | Link one or many documents to an element
[**list_classification_element_relations**](ModelApi.md#list_classification_element_relations) | **GET** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/classification-element | List all associations between classifications and elements
[**merge_ifcs**](ModelApi.md#merge_ifcs) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/merge | Merge IFC files
[**optimize_ifc**](ModelApi.md#optimize_ifc) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{id}/optimize | Optimize the IFC
[**remove_all_element_property_set**](ModelApi.md#remove_all_element_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/all | Remove all property sets from element
[**remove_classification_of_element**](ModelApi.md#remove_classification_of_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/classification/{id} | Remove a classification from an element
[**remove_document_of_element**](ModelApi.md#remove_document_of_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/documents/{id} | Remove a documents from an element
[**remove_element_property_set**](ModelApi.md#remove_element_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{id} | Remove a PropertySet from an element
[**remove_element_property_set_property**](ModelApi.md#remove_element_property_set_property) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{id} | Remove a property from a PropertySet
[**remove_element_property_set_property_definition**](ModelApi.md#remove_element_property_set_property_definition) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{id} | Delete a Definition to a Property
[**remove_element_property_set_property_definition_unit**](ModelApi.md#remove_element_property_set_property_definition_unit) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit/{id} | Remove a Unit from a Definition
[**remove_elements_from_classification**](ModelApi.md#remove_elements_from_classification) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/classification/{model_classification_pk}/element/{uuid} | Remove the classification from all elements
[**reprocess_model**](ModelApi.md#reprocess_model) | **POST** /cloud/{cloud_pk}/project/{project_pk}/model/{id}/reprocess | Reprocess Model file
[**update_access_token**](ModelApi.md#update_access_token) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/access_token/{token} | Update some fields of a token
[**update_building**](ModelApi.md#update_building) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/building/{uuid} | Update some fields of a building
[**update_building_plan_positioning**](ModelApi.md#update_building_plan_positioning) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/building/{building_uuid}/plan/{id}/positioning | Update the postioning of the plan in the building
[**update_drawing**](ModelApi.md#update_drawing) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/drawing/{id} | Update some fields of a drawing
[**update_element**](ModelApi.md#update_element) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{uuid} | Update some fields of an element
[**update_element_property_set_property**](ModelApi.md#update_element_property_set_property) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{id} | Update a property from an element
[**update_layer**](ModelApi.md#update_layer) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/layer/{id} | Update some fields of a layer
[**update_model**](ModelApi.md#update_model) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{id} | Update some fields of a model
[**update_model_files**](ModelApi.md#update_model_files) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{id}/files | Update models file (gltf, svg, structure, etc)
[**update_model_property**](ModelApi.md#update_model_property) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/property/{id} | Update some fields of a Property
[**update_model_property_definition**](ModelApi.md#update_model_property_definition) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/propertydefinition/{id} | Update some fields of many PropertyDefinitions of a model
[**update_model_unit**](ModelApi.md#update_model_unit) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/unit/{id} | Update some fields of a Unit of a model
[**update_order_building_plan**](ModelApi.md#update_order_building_plan) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/building/{building_uuid}/plan/order | Update order of all plan of a building
[**update_order_storey_plan**](ModelApi.md#update_order_storey_plan) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/storey/{storey_uuid}/plan/order | Update order of all plan of a storey
[**update_order_storeys**](ModelApi.md#update_order_storeys) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/storey/order | Update order of all storey of a model
[**update_processor_handler**](ModelApi.md#update_processor_handler) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/processorhandler/{id} | Update the status of a processor handler
[**update_property_set**](ModelApi.md#update_property_set) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/propertyset/{id} | Update some fields of a PropertySet
[**update_space**](ModelApi.md#update_space) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/space/{id} | Update some fields of a space
[**update_storey**](ModelApi.md#update_storey) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/storey/{uuid} | Update some fields of a storey
[**update_storey_plan_positioning**](ModelApi.md#update_storey_plan_positioning) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/storey/{storey_uuid}/plan/{id}/positioning | Update the postioning of the plan in the storey
[**update_system**](ModelApi.md#update_system) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/system/{uuid} | Update some fields of a system
[**update_zone**](ModelApi.md#update_zone) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/zone/{id} | Update some fields of a zone
[**update_zone_space**](ModelApi.md#update_zone_space) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/model/{model_pk}/zone/{zone_pk}/space/{id} | Update some fields of a space


# **add_model_errors**
> ModelErrors add_model_errors(cloud_pk, id, project_pk)

Add errors to model

Model errors are warnings and errors during model process. They alert about missing elements or malformed files  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.model_errors import ModelErrors
from bimdata_api_client.model.model_errors_request import ModelErrorsRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 
    model_errors_request = ModelErrorsRequest(
        errors=[
            "errors_example",
        ],
        warnings=[
            "warnings_example",
        ],
    ) # ModelErrorsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add errors to model
        api_response = api_instance.add_model_errors(cloud_pk, id, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->add_model_errors: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add errors to model
        api_response = api_instance.add_model_errors(cloud_pk, id, project_pk, model_errors_request=model_errors_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->add_model_errors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |
 **model_errors_request** | [**ModelErrorsRequest**](ModelErrorsRequest.md)|  | [optional]

### Return type

[**ModelErrors**](ModelErrors.md)

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

# **add_zone_space**
> ZoneSpace add_zone_space(cloud_pk, model_pk, project_pk, zone_pk, zone_space_relation_request)

Add a space to a zone

Add a space to a zone. The IFC file will not be updated. The created space will be accessible over the API and when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.zone_space_relation_request import ZoneSpaceRelationRequest
from bimdata_api_client.model.zone_space import ZoneSpace
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    zone_pk = 1 # int | A unique integer value identifying this zone.
    zone_space_relation_request = ZoneSpaceRelationRequest(
        id=1,
        order=0,
    ) # ZoneSpaceRelationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Add a space to a zone
        api_response = api_instance.add_zone_space(cloud_pk, model_pk, project_pk, zone_pk, zone_space_relation_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->add_zone_space: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **zone_pk** | **int**| A unique integer value identifying this zone. |
 **zone_space_relation_request** | [**ZoneSpaceRelationRequest**](ZoneSpaceRelationRequest.md)|  |

### Return type

[**ZoneSpace**](ZoneSpace.md)

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

# **bulk_delete_model_classifications**
> bulk_delete_model_classifications(cloud_pk, model_pk, project_pk)

Remove all classifications from model's elements

Delete relation between filtered classifications (eg. /classifications?name=untec) and all mode's elements. No classification will be deleted on this endpoint, only the relation between model's elements and their classification.  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.classification_request import ClassificationRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    model_pk = 1 # int | 
    project_pk = 1 # int | 
    classification_request = ClassificationRequest(
        name="name_example",
        notation="notation_example",
        title="title_example",
    ) # ClassificationRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove all classifications from model's elements
        api_instance.bulk_delete_model_classifications(cloud_pk, model_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_delete_model_classifications: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove all classifications from model's elements
        api_instance.bulk_delete_model_classifications(cloud_pk, model_pk, project_pk, classification_request=classification_request)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_delete_model_classifications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **model_pk** | **int**|  |
 **project_pk** | **int**|  |
 **classification_request** | [**ClassificationRequest**](ClassificationRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **bulk_delete_model_properties**
> bulk_delete_model_properties(cloud_pk, model_pk, project_pk, request_body)

Delete many Property of a model

 Bulk delete. You must send a list of ids in the body. These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted   Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Delete many Property of a model
        api_instance.bulk_delete_model_properties(cloud_pk, model_pk, project_pk, request_body)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_delete_model_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **request_body** | **[int]**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **bulk_delete_model_property_definitions**
> bulk_delete_model_property_definitions(cloud_pk, model_pk, project_pk, request_body)

Delete many PropertyDefinitions of a model

 Bulk delete. You must send a list of ids in the body. These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted   Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Delete many PropertyDefinitions of a model
        api_instance.bulk_delete_model_property_definitions(cloud_pk, model_pk, project_pk, request_body)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_delete_model_property_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **request_body** | **[int]**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **bulk_delete_model_units**
> bulk_delete_model_units(cloud_pk, model_pk, project_pk, request_body)

Delete many Units of a model

 Bulk delete. You must send a list of ids in the body. These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted   Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Delete many Units of a model
        api_instance.bulk_delete_model_units(cloud_pk, model_pk, project_pk, request_body)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_delete_model_units: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **request_body** | **[int]**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **bulk_delete_property_set**
> bulk_delete_property_set(cloud_pk, model_pk, project_pk, request_body)

Delete many PropertySet of a model

 Bulk delete. You must send a list of ids in the body. These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted   Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Delete many PropertySet of a model
        api_instance.bulk_delete_property_set(cloud_pk, model_pk, project_pk, request_body)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_delete_property_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **request_body** | **[int]**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **bulk_full_update_elements**
> [Element] bulk_full_update_elements(cloud_pk, model_pk, project_pk, element_request)

Update many elements at once (only changing fields may be defined)

 Bulk update. Similar to update, but the body should be a list of objects to patch or put The response will be a list (in the same order) of updated objects or of errors if any If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors   Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.element_request import ElementRequest
from bimdata_api_client.model.element import Element
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    element_request = [
        ElementRequest(
            uuid="uuid_example",
            type="type_example",
            attributes=PropertySetRequest(
                name="name_example",
                description="description_example",
                type="type_example",
                properties=[
                    PropertyRequest(
                        definition=PropertyDefinitionRequest(
                            unit=None,
                            name="name_example",
                            description="description_example",
                            type="type_example",
                            value_type="value_type_example",
                        ),
                        value=None,
                    ),
                ],
            ),
            property_sets=[
                PropertySetRequest(
                    name="name_example",
                    description="description_example",
                    type="type_example",
                    properties=[
                        PropertyRequest(
                            definition=PropertyDefinitionRequest(
                                unit=None,
                                name="name_example",
                                description="description_example",
                                type="type_example",
                                value_type="value_type_example",
                            ),
                            value=None,
                        ),
                    ],
                ),
            ],
            classifications=[
                ClassificationRequest(
                    name="name_example",
                    notation="notation_example",
                    title="title_example",
                ),
            ],
            layers=[
                LayerElementRequest(
                    name="name_example",
                    identifier="identifier_example",
                    description="description_example",
                ),
            ],
        ),
    ] # [ElementRequest] | 
    classification = "classification_example" # str |  (optional)
    classification__notation = "classification__notation_example" # str |  (optional)
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update many elements at once (only changing fields may be defined)
        api_response = api_instance.bulk_full_update_elements(cloud_pk, model_pk, project_pk, element_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_full_update_elements: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update many elements at once (only changing fields may be defined)
        api_response = api_instance.bulk_full_update_elements(cloud_pk, model_pk, project_pk, element_request, classification=classification, classification__notation=classification__notation, type=type)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_full_update_elements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **element_request** | [**[ElementRequest]**](ElementRequest.md)|  |
 **classification** | **str**|  | [optional]
 **classification__notation** | **str**|  | [optional]
 **type** | **str**|  | [optional]

### Return type

[**[Element]**](Element.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If all updates fail: a list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_full_update_model_property**
> [ModelProperty] bulk_full_update_model_property(cloud_pk, model_pk, project_pk, property_request)

Update some fields of many properties of a model

 Bulk update. Similar to update, but the body should be a list of objects to patch or put The response will be a list (in the same order) of updated objects or of errors if any If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors   Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_request import PropertyRequest
from bimdata_api_client.model.model_property import ModelProperty
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_request = [
        PropertyRequest(
            definition=PropertyDefinitionRequest(
                unit=None,
                name="name_example",
                description="description_example",
                type="type_example",
                value_type="value_type_example",
            ),
            value=None,
        ),
    ] # [PropertyRequest] | 

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of many properties of a model
        api_response = api_instance.bulk_full_update_model_property(cloud_pk, model_pk, project_pk, property_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_full_update_model_property: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **property_request** | [**[PropertyRequest]**](PropertyRequest.md)|  |

### Return type

[**[ModelProperty]**](ModelProperty.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | All updates failed: a list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_remove_classifications_of_element**
> bulk_remove_classifications_of_element(cloud_pk, element_uuid, model_pk, project_pk, request_body)

Remove many classifications from an element

 Bulk delete. You must send a list of ids in the body. These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted   Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Remove many classifications from an element
        api_instance.bulk_remove_classifications_of_element(cloud_pk, element_uuid, model_pk, project_pk, request_body)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_remove_classifications_of_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **request_body** | **[int]**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **bulk_remove_documents_of_element**
> bulk_remove_documents_of_element(cloud_pk, element_uuid, model_pk, project_pk, request_body)

Remove many documents from an element

 Bulk delete. You must send a list of ids in the body. These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted   Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Remove many documents from an element
        api_instance.bulk_remove_documents_of_element(cloud_pk, element_uuid, model_pk, project_pk, request_body)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_remove_documents_of_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **request_body** | **[int]**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **bulk_remove_elements_from_classification**
> bulk_remove_elements_from_classification(cloud_pk, model_classification_pk, model_pk, project_pk, request_body)

Remove the classifications from all elements

 Bulk delete. You must send a list of ids in the body. These ids (or relations with these ids in case of many-to-many relation deletion) will be deleted   Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    model_classification_pk = 1 # int | A unique integer value identifying this classification.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Remove the classifications from all elements
        api_instance.bulk_remove_elements_from_classification(cloud_pk, model_classification_pk, model_pk, project_pk, request_body)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_remove_elements_from_classification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **model_classification_pk** | **int**| A unique integer value identifying this classification. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **request_body** | **[int]**|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **bulk_update_elements**
> [Element] bulk_update_elements(cloud_pk, model_pk, project_pk, element_request)

Update many elements at once (all field must be defined)

 Bulk update. Similar to update, but the body should be a list of objects to patch or put The response will be a list (in the same order) of updated objects or of errors if any If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors   Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.element_request import ElementRequest
from bimdata_api_client.model.element import Element
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    element_request = [
        ElementRequest(
            uuid="uuid_example",
            type="type_example",
            attributes=PropertySetRequest(
                name="name_example",
                description="description_example",
                type="type_example",
                properties=[
                    PropertyRequest(
                        definition=PropertyDefinitionRequest(
                            unit=None,
                            name="name_example",
                            description="description_example",
                            type="type_example",
                            value_type="value_type_example",
                        ),
                        value=None,
                    ),
                ],
            ),
            property_sets=[
                PropertySetRequest(
                    name="name_example",
                    description="description_example",
                    type="type_example",
                    properties=[
                        PropertyRequest(
                            definition=PropertyDefinitionRequest(
                                unit=None,
                                name="name_example",
                                description="description_example",
                                type="type_example",
                                value_type="value_type_example",
                            ),
                            value=None,
                        ),
                    ],
                ),
            ],
            classifications=[
                ClassificationRequest(
                    name="name_example",
                    notation="notation_example",
                    title="title_example",
                ),
            ],
            layers=[
                LayerElementRequest(
                    name="name_example",
                    identifier="identifier_example",
                    description="description_example",
                ),
            ],
        ),
    ] # [ElementRequest] | 
    classification = "classification_example" # str |  (optional)
    classification__notation = "classification__notation_example" # str |  (optional)
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update many elements at once (all field must be defined)
        api_response = api_instance.bulk_update_elements(cloud_pk, model_pk, project_pk, element_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_update_elements: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update many elements at once (all field must be defined)
        api_response = api_instance.bulk_update_elements(cloud_pk, model_pk, project_pk, element_request, classification=classification, classification__notation=classification__notation, type=type)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_update_elements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **element_request** | [**[ElementRequest]**](ElementRequest.md)|  |
 **classification** | **str**|  | [optional]
 **classification__notation** | **str**|  | [optional]
 **type** | **str**|  | [optional]

### Return type

[**[Element]**](Element.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If all updates fail: a list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_model_property**
> [ModelProperty] bulk_update_model_property(cloud_pk, model_pk, project_pk, property_request)

Update all fields of many properties of a model

 Bulk update. Similar to update, but the body should be a list of objects to patch or put The response will be a list (in the same order) of updated objects or of errors if any If at least one update succeeded, the status code will be 200. If every update failed, the status code we'll be 400 with the list of errors 

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_request import PropertyRequest
from bimdata_api_client.model.model_property import ModelProperty
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_request = [
        PropertyRequest(
            definition=PropertyDefinitionRequest(
                unit=None,
                name="name_example",
                description="description_example",
                type="type_example",
                value_type="value_type_example",
            ),
            value=None,
        ),
    ] # [PropertyRequest] | 

    # example passing only required values which don't have defaults set
    try:
        # Update all fields of many properties of a model
        api_response = api_instance.bulk_update_model_property(cloud_pk, model_pk, project_pk, property_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->bulk_update_model_property: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **property_request** | [**[PropertyRequest]**](PropertyRequest.md)|  |

### Return type

[**[ModelProperty]**](ModelProperty.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | All updates failed: a list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_access_token**
> IfcAccessToken create_access_token(cloud_pk, model_pk, project_pk)

Create a token for this model

DEPECRATED: Use ProjectAccessToken instead  Required scopes: ifc:token_manage, model:token_manage

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.ifc_access_token import IfcAccessToken
from bimdata_api_client.model.ifc_access_token_request import IfcAccessTokenRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    ifc_access_token_request = IfcAccessTokenRequest(
        read_only=True,
        expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # IfcAccessTokenRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a token for this model
        api_response = api_instance.create_access_token(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_access_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a token for this model
        api_response = api_instance.create_access_token(cloud_pk, model_pk, project_pk, ifc_access_token_request=ifc_access_token_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **ifc_access_token_request** | [**IfcAccessTokenRequest**](IfcAccessTokenRequest.md)|  | [optional]

### Return type

[**IfcAccessToken**](IfcAccessToken.md)

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

# **create_building**
> Building create_building(cloud_pk, model_pk, project_pk, storey_building_request)

Create a building of a model

Create a building of a model.  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.building import Building
from bimdata_api_client.model.storey_building_request import StoreyBuildingRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    storey_building_request = StoreyBuildingRequest(
        name="name_example",
    ) # StoreyBuildingRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a building of a model
        api_response = api_instance.create_building(cloud_pk, model_pk, project_pk, storey_building_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_building: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **storey_building_request** | [**StoreyBuildingRequest**](StoreyBuildingRequest.md)|  |

### Return type

[**Building**](Building.md)

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

# **create_building_plan**
> Building create_building_plan(building_uuid, cloud_pk, model_pk, project_pk, building_model_plan_request)

Create a relation between a 2d model and a building

Create a relation between a 2d model and a building. The model type must be one of : ('DWG', 'DXF', 'PDF', 'JPEG', 'PNG', 'PHOTOSPHERE')  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.building import Building
from bimdata_api_client.model.building_model_plan_request import BuildingModelPlanRequest
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
    api_instance = model_api.ModelApi(api_client)
    building_uuid = "building_uuid_example" # str | 
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    building_model_plan_request = BuildingModelPlanRequest(
        id=1,
    ) # BuildingModelPlanRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a relation between a 2d model and a building
        api_response = api_instance.create_building_plan(building_uuid, cloud_pk, model_pk, project_pk, building_model_plan_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_building_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_uuid** | **str**|  |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **building_model_plan_request** | [**BuildingModelPlanRequest**](BuildingModelPlanRequest.md)|  |

### Return type

[**Building**](Building.md)

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

# **create_classification_element_relations**
> create_classification_element_relations(cloud_pk, model_pk, project_pk, element_classification_relation_request)

Create association between existing classification and existing element

Create association between existing classification and existing element  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.element_classification_relation_request import ElementClassificationRelationRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    element_classification_relation_request = [
        ElementClassificationRelationRequest(
            element_uuid="element_uuid_example",
            classification_id=1,
        ),
    ] # [ElementClassificationRelationRequest] | 

    # example passing only required values which don't have defaults set
    try:
        # Create association between existing classification and existing element
        api_instance.create_classification_element_relations(cloud_pk, model_pk, project_pk, element_classification_relation_request)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_classification_element_relations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **element_classification_relation_request** | [**[ElementClassificationRelationRequest]**](ElementClassificationRelationRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | No response body |  -  |
**204** | No response body |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_classifications_of_element**
> [Classification] create_classifications_of_element(cloud_pk, element_uuid, model_pk, project_pk, classification_request)

Create one or many classifications to an element

 Bulk create available. You can either post an object or a list of objects. Is you post a list, the response will be a list (in the same order) of created objects or of errors if any If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors If classification created already exists, it will just be added to item's classifications and will not be duplicated  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.classification import Classification
from bimdata_api_client.model.classification_request import ClassificationRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    classification_request = [
        ClassificationRequest(
            name="name_example",
            notation="notation_example",
            title="title_example",
        ),
    ] # [ClassificationRequest] | 

    # example passing only required values which don't have defaults set
    try:
        # Create one or many classifications to an element
        api_response = api_instance.create_classifications_of_element(cloud_pk, element_uuid, model_pk, project_pk, classification_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_classifications_of_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **classification_request** | [**[ClassificationRequest]**](ClassificationRequest.md)|  |

### Return type

[**[Classification]**](Classification.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | All creates failed: list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drawing**
> Drawing create_drawing(cloud_pk, model_pk, project_pk, drawing_request)

Create a drawing in the model

Create a drawing in the model  Required scopes: model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.drawing_request import DrawingRequest
from bimdata_api_client.model.drawing import Drawing
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    drawing_request = DrawingRequest(
        content="content_example",
    ) # DrawingRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a drawing in the model
        api_response = api_instance.create_drawing(cloud_pk, model_pk, project_pk, drawing_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_drawing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **drawing_request** | [**DrawingRequest**](DrawingRequest.md)|  |

### Return type

[**Drawing**](Drawing.md)

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

# **create_element**
> [Element] create_element(cloud_pk, model_pk, project_pk, element_request)

Create an element in the model

 Bulk create available. You can either post an object or a list of objects. Is you post a list, the response will be a list (in the same order) of created objects or of errors if any If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors  The IFC file will not be updated. The created element will be accessible over the API and when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.element_request import ElementRequest
from bimdata_api_client.model.element import Element
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    element_request = [
        ElementRequest(
            uuid="uuid_example",
            type="type_example",
            attributes=PropertySetRequest(
                name="name_example",
                description="description_example",
                type="type_example",
                properties=[
                    PropertyRequest(
                        definition=PropertyDefinitionRequest(
                            unit=None,
                            name="name_example",
                            description="description_example",
                            type="type_example",
                            value_type="value_type_example",
                        ),
                        value=None,
                    ),
                ],
            ),
            property_sets=[
                PropertySetRequest(
                    name="name_example",
                    description="description_example",
                    type="type_example",
                    properties=[
                        PropertyRequest(
                            definition=PropertyDefinitionRequest(
                                unit=None,
                                name="name_example",
                                description="description_example",
                                type="type_example",
                                value_type="value_type_example",
                            ),
                            value=None,
                        ),
                    ],
                ),
            ],
            classifications=[
                ClassificationRequest(
                    name="name_example",
                    notation="notation_example",
                    title="title_example",
                ),
            ],
            layers=[
                LayerElementRequest(
                    name="name_example",
                    identifier="identifier_example",
                    description="description_example",
                ),
            ],
        ),
    ] # [ElementRequest] | 
    classification = "classification_example" # str |  (optional)
    classification__notation = "classification__notation_example" # str |  (optional)
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an element in the model
        api_response = api_instance.create_element(cloud_pk, model_pk, project_pk, element_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_element: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an element in the model
        api_response = api_instance.create_element(cloud_pk, model_pk, project_pk, element_request, classification=classification, classification__notation=classification__notation, type=type)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **element_request** | [**[ElementRequest]**](ElementRequest.md)|  |
 **classification** | **str**|  | [optional]
 **classification__notation** | **str**|  | [optional]
 **type** | **str**|  | [optional]

### Return type

[**[Element]**](Element.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If all creates fail: a list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_element_property_set**
> PropertySet create_element_property_set(cloud_pk, element_uuid, model_pk, project_pk)

Create a PropertySets to an element

Create a PropertySets that will be automatically linked to the element  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_set import PropertySet
from bimdata_api_client.model.property_set_request import PropertySetRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | 
    project_pk = 1 # int | A unique integer value identifying this project.
    property_set_request = PropertySetRequest(
        name="name_example",
        description="description_example",
        type="type_example",
        properties=[
            PropertyRequest(
                definition=PropertyDefinitionRequest(
                    unit=None,
                    name="name_example",
                    description="description_example",
                    type="type_example",
                    value_type="value_type_example",
                ),
                value=None,
            ),
        ],
    ) # PropertySetRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a PropertySets to an element
        api_response = api_instance.create_element_property_set(cloud_pk, element_uuid, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_element_property_set: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a PropertySets to an element
        api_response = api_instance.create_element_property_set(cloud_pk, element_uuid, model_pk, project_pk, property_set_request=property_set_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_element_property_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**|  |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **property_set_request** | [**PropertySetRequest**](PropertySetRequest.md)|  | [optional]

### Return type

[**PropertySet**](PropertySet.md)

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

# **create_element_property_set_property**
> ModelProperty create_element_property_set_property(cloud_pk, element_uuid, model_pk, project_pk, propertyset_pk, property_request)

Create a property to a PropertySet

Create a property to a PropertySet  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_request import PropertyRequest
from bimdata_api_client.model.model_property import ModelProperty
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.
    property_request = PropertyRequest(
        definition=PropertyDefinitionRequest(
            unit=None,
            name="name_example",
            description="description_example",
            type="type_example",
            value_type="value_type_example",
        ),
        value=None,
    ) # PropertyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a property to a PropertySet
        api_response = api_instance.create_element_property_set_property(cloud_pk, element_uuid, model_pk, project_pk, propertyset_pk, property_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_element_property_set_property: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **propertyset_pk** | **int**| A unique integer value identifying this property set. |
 **property_request** | [**PropertyRequest**](PropertyRequest.md)|  |

### Return type

[**ModelProperty**](ModelProperty.md)

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

# **create_element_property_set_property_definition**
> PropertyDefinition create_element_property_set_property_definition(cloud_pk, element_uuid, model_pk, project_pk, property_pk, propertyset_pk)

Create a Definition to a Property

Create a Definition to a Property  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_definition import PropertyDefinition
from bimdata_api_client.model.property_definition_request import PropertyDefinitionRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_pk = 1 # int | A unique integer value identifying this property.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.
    property_definition_request = PropertyDefinitionRequest(
        unit=None,
        name="name_example",
        description="description_example",
        type="type_example",
        value_type="value_type_example",
    ) # PropertyDefinitionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Definition to a Property
        api_response = api_instance.create_element_property_set_property_definition(cloud_pk, element_uuid, model_pk, project_pk, property_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_element_property_set_property_definition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Definition to a Property
        api_response = api_instance.create_element_property_set_property_definition(cloud_pk, element_uuid, model_pk, project_pk, property_pk, propertyset_pk, property_definition_request=property_definition_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_element_property_set_property_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **property_pk** | **int**| A unique integer value identifying this property. |
 **propertyset_pk** | **int**| A unique integer value identifying this property set. |
 **property_definition_request** | [**PropertyDefinitionRequest**](PropertyDefinitionRequest.md)|  | [optional]

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

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

# **create_element_property_set_property_definition_unit**
> Unit create_element_property_set_property_definition_unit(cloud_pk, element_uuid, model_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk, unit_request)

Create a Unit to a Definition

Create a Unit to a Definition  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.unit_request import UnitRequest
from bimdata_api_client.model.unit import Unit
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_pk = 1 # int | A unique integer value identifying this property.
    propertydefinition_pk = 1 # int | A unique integer value identifying this property definition.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.
    unit_request = UnitRequest(
        type="type_example",
        name="name_example",
        unit_type="unit_type_example",
        prefix="prefix_example",
        dimensions=[
            3.14,
        ],
        conversion_factor=3.14,
        conversion_baseunit=Unit(
            type="type_example",
            name="name_example",
            unit_type="unit_type_example",
            prefix="prefix_example",
            dimensions=[
                3.14,
            ],
            conversion_factor=3.14,
            conversion_baseunit=Unit(),
            elements=None,
            is_default=True,
        ),
        elements=None,
        is_default=True,
    ) # UnitRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Unit to a Definition
        api_response = api_instance.create_element_property_set_property_definition_unit(cloud_pk, element_uuid, model_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk, unit_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_element_property_set_property_definition_unit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **property_pk** | **int**| A unique integer value identifying this property. |
 **propertydefinition_pk** | **int**| A unique integer value identifying this property definition. |
 **propertyset_pk** | **int**| A unique integer value identifying this property set. |
 **unit_request** | [**UnitRequest**](UnitRequest.md)|  |

### Return type

[**Unit**](Unit.md)

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

# **create_layer**
> Layer create_layer(cloud_pk, model_pk, project_pk, layer_request)

Create a layer in the model

The IFC file will not be updated. The created layer will be accessible over the API and when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.layer_request import LayerRequest
from bimdata_api_client.model.layer import Layer
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    layer_request = LayerRequest(
        name="name_example",
        identifier="identifier_example",
        description="description_example",
        elements=[
            "elements_example",
        ],
    ) # LayerRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a layer in the model
        api_response = api_instance.create_layer(cloud_pk, model_pk, project_pk, layer_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_layer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **layer_request** | [**LayerRequest**](LayerRequest.md)|  |

### Return type

[**Layer**](Layer.md)

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

# **create_mask2_d**
> Mask2D create_mask2_d(cloud_pk, id, project_pk, mask2_d_request)

Create or update a 2D mask for the model

Create or update a 2D mask for the model. Only available for PDF, JPEG and PNG models

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.mask2_d import Mask2D
from bimdata_api_client.model.mask2_d_request import Mask2DRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 
    mask2_d_request = Mask2DRequest(
        crop_path=[
            [
                3.14,
            ],
        ],
    ) # Mask2DRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update a 2D mask for the model
        api_response = api_instance.create_mask2_d(cloud_pk, id, project_pk, mask2_d_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_mask2_d: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |
 **mask2_d_request** | [**Mask2DRequest**](Mask2DRequest.md)|  |

### Return type

[**Mask2D**](Mask2D.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**201** |  |  -  |
**400** | Bad request, model type not supported. |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_meta_building**
> Model create_meta_building(cloud_pk, project_pk, create_building_by_name_request)

Create an empty 3D Model

Create an empty 3D Model to be used in BIMData services  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.create_building_by_name_request import CreateBuildingByNameRequest
from bimdata_api_client.model.model import Model
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    project_pk = 1 # int | 
    create_building_by_name_request = CreateBuildingByNameRequest(
        name="name_example",
    ) # CreateBuildingByNameRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create an empty 3D Model
        api_response = api_instance.create_meta_building(cloud_pk, project_pk, create_building_by_name_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_meta_building: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **project_pk** | **int**|  |
 **create_building_by_name_request** | [**CreateBuildingByNameRequest**](CreateBuildingByNameRequest.md)|  |

### Return type

[**Model**](Model.md)

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

# **create_model**
> Model create_model(cloud_pk, project_pk, create_model_request)

Make a PDF or Image file a Model

Make a PDF or Image file a Model to be used in BIMData services. If a model already exists, this route does nothing and returns a 201 with the model  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.create_model_request import CreateModelRequest
from bimdata_api_client.model.model import Model
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    project_pk = 1 # int | 
    create_model_request = CreateModelRequest(
        document_id=1,
    ) # CreateModelRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Make a PDF or Image file a Model
        api_response = api_instance.create_model(cloud_pk, project_pk, create_model_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **project_pk** | **int**|  |
 **create_model_request** | [**CreateModelRequest**](CreateModelRequest.md)|  |

### Return type

[**Model**](Model.md)

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

# **create_model_property_definition**
> [PropertyDefinition] create_model_property_definition(cloud_pk, model_pk, project_pk, property_definition_request)

Create a PropertyDefinition on the model

 Bulk create available. You can either post an object or a list of objects. Is you post a list, the response will be a list (in the same order) of created objects or of errors if any If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors   Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_definition import PropertyDefinition
from bimdata_api_client.model.property_definition_request import PropertyDefinitionRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_definition_request = [
        PropertyDefinitionRequest(
            unit=None,
            name="name_example",
            description="description_example",
            type="type_example",
            value_type="value_type_example",
        ),
    ] # [PropertyDefinitionRequest] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a PropertyDefinition on the model
        api_response = api_instance.create_model_property_definition(cloud_pk, model_pk, project_pk, property_definition_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_model_property_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **property_definition_request** | [**[PropertyDefinitionRequest]**](PropertyDefinitionRequest.md)|  |

### Return type

[**[PropertyDefinition]**](PropertyDefinition.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | All creates failed: list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_model_unit**
> [Unit] create_model_unit(cloud_pk, model_pk, project_pk, unit_request)

Create a Unit on a model

 Bulk create available. You can either post an object or a list of objects. Is you post a list, the response will be a list (in the same order) of created objects or of errors if any If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors   Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.unit_request import UnitRequest
from bimdata_api_client.model.unit import Unit
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    unit_request = [
        UnitRequest(
            type="type_example",
            name="name_example",
            unit_type="unit_type_example",
            prefix="prefix_example",
            dimensions=[
                3.14,
            ],
            conversion_factor=3.14,
            conversion_baseunit=Unit(
                type="type_example",
                name="name_example",
                unit_type="unit_type_example",
                prefix="prefix_example",
                dimensions=[
                    3.14,
                ],
                conversion_factor=3.14,
                conversion_baseunit=Unit(),
                elements=None,
                is_default=True,
            ),
            elements=None,
            is_default=True,
        ),
    ] # [UnitRequest] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Unit on a model
        api_response = api_instance.create_model_unit(cloud_pk, model_pk, project_pk, unit_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_model_unit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **unit_request** | [**[UnitRequest]**](UnitRequest.md)|  |

### Return type

[**[Unit]**](Unit.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | All creates failed: list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multi_page_model**
> Model create_multi_page_model(cloud_pk, id, project_pk, create_multi_page_model_request)

Create a multi page model

Create a multi page model  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.create_multi_page_model_request import CreateMultiPageModelRequest
from bimdata_api_client.model.model import Model
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 
    create_multi_page_model_request = CreateMultiPageModelRequest(
        map_files=[
            open('/path/to/file', 'rb'),
        ],
        layout_names=[
            "layout_names_example",
        ],
    ) # CreateMultiPageModelRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a multi page model
        api_response = api_instance.create_multi_page_model(cloud_pk, id, project_pk, create_multi_page_model_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_multi_page_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |
 **create_multi_page_model_request** | [**CreateMultiPageModelRequest**](CreateMultiPageModelRequest.md)|  |

### Return type

[**Model**](Model.md)

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

# **create_photosphere**
> Model create_photosphere(cloud_pk, project_pk, create_model_request)

Create a photopshere model from an image file

Create a photosphere model to be used in BIMData services  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.create_model_request import CreateModelRequest
from bimdata_api_client.model.model import Model
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    project_pk = 1 # int | 
    create_model_request = CreateModelRequest(
        document_id=1,
    ) # CreateModelRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a photopshere model from an image file
        api_response = api_instance.create_photosphere(cloud_pk, project_pk, create_model_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_photosphere: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **project_pk** | **int**|  |
 **create_model_request** | [**CreateModelRequest**](CreateModelRequest.md)|  |

### Return type

[**Model**](Model.md)

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

# **create_photosphere_building**
> Model create_photosphere_building(cloud_pk, project_pk, create_building_by_name_request)

Create an empty Photosphere Building Model

Create an empty Photosphere Building Model  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.create_building_by_name_request import CreateBuildingByNameRequest
from bimdata_api_client.model.model import Model
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    project_pk = 1 # int | 
    create_building_by_name_request = CreateBuildingByNameRequest(
        name="name_example",
    ) # CreateBuildingByNameRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create an empty Photosphere Building Model
        api_response = api_instance.create_photosphere_building(cloud_pk, project_pk, create_building_by_name_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_photosphere_building: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **project_pk** | **int**|  |
 **create_building_by_name_request** | [**CreateBuildingByNameRequest**](CreateBuildingByNameRequest.md)|  |

### Return type

[**Model**](Model.md)

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

# **create_property_set**
> [PropertySet] create_property_set(cloud_pk, model_pk, project_pk, property_set_request)

Create one or many PropertySet

 Bulk create available. You can either post an object or a list of objects. Is you post a list, the response will be a list (in the same order) of created objects or of errors if any If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors   Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_set import PropertySet
from bimdata_api_client.model.property_set_request import PropertySetRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_set_request = [
        PropertySetRequest(
            name="name_example",
            description="description_example",
            type="type_example",
            properties=[
                PropertyRequest(
                    definition=PropertyDefinitionRequest(
                        unit=None,
                        name="name_example",
                        description="description_example",
                        type="type_example",
                        value_type="value_type_example",
                    ),
                    value=None,
                ),
            ],
        ),
    ] # [PropertySetRequest] | 

    # example passing only required values which don't have defaults set
    try:
        # Create one or many PropertySet
        api_response = api_instance.create_property_set(cloud_pk, model_pk, project_pk, property_set_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_property_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **property_set_request** | [**[PropertySetRequest]**](PropertySetRequest.md)|  |

### Return type

[**[PropertySet]**](PropertySet.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | All creates failed: list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_property_set_element_relations**
> create_property_set_element_relations(cloud_pk, model_pk, project_pk, element_property_set_relation_request)

Create association between PropertySet and element

Create association between PropertySet and element  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.element_property_set_relation_request import ElementPropertySetRelationRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    element_property_set_relation_request = [
        ElementPropertySetRelationRequest(
            element_uuid="element_uuid_example",
            property_set_id=1,
        ),
    ] # [ElementPropertySetRelationRequest] | 

    # example passing only required values which don't have defaults set
    try:
        # Create association between PropertySet and element
        api_instance.create_property_set_element_relations(cloud_pk, model_pk, project_pk, element_property_set_relation_request)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_property_set_element_relations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **element_property_set_relation_request** | [**[ElementPropertySetRelationRequest]**](ElementPropertySetRelationRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | No response body |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_raw_elements**
> create_raw_elements(cloud_pk, model_pk, project_pk, raw_elements_request)

Create elements in an optimized format

Create many elements in an optimized format to reduce JSON size and avoid redudancy. The IFC file will not be updated. The created elements will be accessible over the API and when exporting an IFC file. You can use the same optimized structure to post multiple elements, property_sets, properties, definitions and units at once. For performance reasons, we do not check the validity of the json. If the json is malformed, an error 500 without more explaination may be returned instead of a 400.  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.raw_elements_request import RawElementsRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    raw_elements_request = RawElementsRequest(
        units=[
            RawUnitRequest(
                name="name_example",
                type="type_example",
                unit_type="unit_type_example",
                prefix="prefix_example",
                elements=None,
                conversion_factor=3.14,
                dimensions=[
                    3.14,
                ],
                conversion_baseunit_index=1,
                is_default=True,
            ),
        ],
        definitions=[
            RawDefinitionRequest(
                description="description_example",
                name="name_example",
                type="type_example",
                value_type="value_type_example",
                unit_id=1,
            ),
        ],
        property_sets=[
            RawPropertySetRequest(
                description="description_example",
                name="name_example",
                type="type_example",
                properties=[
                    RawPropertyRequest(
                        value=None,
                        def_id=1,
                    ),
                ],
            ),
        ],
        classifications=[
            RawClassificationRequest(
                type="type_example",
                notation="notation_example",
                description="description_example",
            ),
        ],
        layers=[
            RawLayerRequest(
                name="name_example",
                description="description_example",
                identifier="identifier_example",
            ),
        ],
        systems=[
            RawSystemRequest(
                uuid="uuid_example",
                name="name_example",
                description="description_example",
                object_type="object_type_example",
            ),
        ],
        materials=None,
        elements=[
            RawElementRequest(
                uuid="uuid_example",
                type="type_example",
                attributes=1,
                material_list=[
                    1,
                ],
                psets=[
                    1,
                ],
                classifications=[
                    1,
                ],
                layers=[
                    1,
                ],
                systems=[
                    1,
                ],
            ),
        ],
    ) # RawElementsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create elements in an optimized format
        api_instance.create_raw_elements(cloud_pk, model_pk, project_pk, raw_elements_request)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_raw_elements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **raw_elements_request** | [**RawElementsRequest**](RawElementsRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | No response body |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_space**
> [Space] create_space(cloud_pk, model_pk, project_pk, space_request)

Create a space in the model

 Bulk create available. You can either post an object or a list of objects. Is you post a list, the response will be a list (in the same order) of created objects or of errors if any If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors  The IFC file will not be updated. The created space will be accessible over the API and when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.space import Space
from bimdata_api_client.model.space_request import SpaceRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    space_request = [
        SpaceRequest(
            name="name_example",
            longname="longname_example",
            uuid="uuid_example",
            geometry=[
                GeometryPointRequest(
                    x=3.14,
                    y=3.14,
                    z=3.14,
                ),
            ],
        ),
    ] # [SpaceRequest] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a space in the model
        api_response = api_instance.create_space(cloud_pk, model_pk, project_pk, space_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_space: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **space_request** | [**[SpaceRequest]**](SpaceRequest.md)|  |

### Return type

[**[Space]**](Space.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | All creates failed: list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_storey**
> Storey create_storey(cloud_pk, model_pk, project_pk, storey_building_request)

Create a storey of a model

Create a storey of a model.  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.storey import Storey
from bimdata_api_client.model.storey_building_request import StoreyBuildingRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    storey_building_request = StoreyBuildingRequest(
        name="name_example",
    ) # StoreyBuildingRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a storey of a model
        api_response = api_instance.create_storey(cloud_pk, model_pk, project_pk, storey_building_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_storey: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **storey_building_request** | [**StoreyBuildingRequest**](StoreyBuildingRequest.md)|  |

### Return type

[**Storey**](Storey.md)

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

# **create_storey_plan**
> Storey create_storey_plan(cloud_pk, model_pk, project_pk, storey_uuid, storey_model_plan_request)

Create a relation between a 2d model and a storey

Create a relation between a 2d model and a storey. The model type must be one of : ('DWG', 'DXF', 'PDF', 'JPEG', 'PNG', 'PHOTOSPHERE')  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.storey_model_plan_request import StoreyModelPlanRequest
from bimdata_api_client.model.storey import Storey
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    storey_uuid = "storey_uuid_example" # str | 
    storey_model_plan_request = StoreyModelPlanRequest(
        id=1,
    ) # StoreyModelPlanRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a relation between a 2d model and a storey
        api_response = api_instance.create_storey_plan(cloud_pk, model_pk, project_pk, storey_uuid, storey_model_plan_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_storey_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **storey_uuid** | **str**|  |
 **storey_model_plan_request** | [**StoreyModelPlanRequest**](StoreyModelPlanRequest.md)|  |

### Return type

[**Storey**](Storey.md)

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

# **create_system**
> System create_system(cloud_pk, model_pk, project_pk, system_request)

Create a system in the model

The IFC file will not be updated. The created system will be accessible over the API and when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.system_request import SystemRequest
from bimdata_api_client.model.system import System
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    system_request = SystemRequest(
        uuid="uuid_example",
        name="name_example",
        object_type="object_type_example",
        description="description_example",
        elements=[
            "elements_example",
        ],
    ) # SystemRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a system in the model
        api_response = api_instance.create_system(cloud_pk, model_pk, project_pk, system_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **system_request** | [**SystemRequest**](SystemRequest.md)|  |

### Return type

[**System**](System.md)

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

# **create_tileset**
> create_tileset(cloud_pk, id, project_pk)

Create the tileset of the model and upload all files

This route is internaly used by BIMData, you probably don't want to use it  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Create the tileset of the model and upload all files
        api_instance.create_tileset(cloud_pk, id, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_tileset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |

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
**201** | No response body |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_xkt_file**
> XktFile create_xkt_file(cloud_pk, id, project_pk, version, file)

Create an xkt file for the model. Overrides existing file with same version

This route does not accept JSON, only files as x-www-form-urlencoded  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.xkt_file import XktFile
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 
    version = 0 # int | 
    file = open('/path/to/file', 'rb') # file_type | 
    chunks = [
        open('/path/to/file', 'rb'),
    ] # [file_type] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an xkt file for the model. Overrides existing file with same version
        api_response = api_instance.create_xkt_file(cloud_pk, id, project_pk, version, file)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_xkt_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an xkt file for the model. Overrides existing file with same version
        api_response = api_instance.create_xkt_file(cloud_pk, id, project_pk, version, file, chunks=chunks)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_xkt_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |
 **version** | **int**|  |
 **file** | **file_type**|  |
 **chunks** | **[file_type]**|  | [optional]

### Return type

[**XktFile**](XktFile.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

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

# **create_zone**
> [Zone] create_zone(cloud_pk, model_pk, project_pk, zone_request)

Create a zone in the model

 Bulk create available. You can either post an object or a list of objects. Is you post a list, the response will be a list (in the same order) of created objects or of errors if any If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors  The IFC file will not be updated. The created zone will be accessible over the API and when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.zone_request import ZoneRequest
from bimdata_api_client.model.zone import Zone
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    zone_request = [
        ZoneRequest(
            name="name_example",
            uuid="uuid_example",
            zones=[
                Zone(
                    name="name_example",
                    uuid="uuid_example",
                    zones=[],
                    parent_id=1,
                    spaces=[
                        ZoneSpace(
                            name="name_example",
                            longname="longname_example",
                            uuid="uuid_example",
                            geometry=[
                                GeometryPoint(
                                    x=3.14,
                                    y=3.14,
                                    z=3.14,
                                ),
                            ],
                            order=0,
                        ),
                    ],
                    color="color_example",
                    order=0,
                    storey_uuid="storey_uuid_example",
                ),
            ],
            parent_id=1,
            spaces=[
                ZoneSpaceRequest(
                    name="name_example",
                    longname="longname_example",
                    uuid="uuid_example",
                    geometry=[
                        GeometryPointRequest(
                            x=3.14,
                            y=3.14,
                            z=3.14,
                        ),
                    ],
                    order=0,
                ),
            ],
            color="color_example",
            order=0,
            storey_uuid="storey_uuid_example",
        ),
    ] # [ZoneRequest] | 
    color = "color_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a zone in the model
        api_response = api_instance.create_zone(cloud_pk, model_pk, project_pk, zone_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_zone: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a zone in the model
        api_response = api_instance.create_zone(cloud_pk, model_pk, project_pk, zone_request, color=color)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_zone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **zone_request** | [**[ZoneRequest]**](ZoneRequest.md)|  |
 **color** | **str**|  | [optional]

### Return type

[**[Zone]**](Zone.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | If all creates fail: a list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_zone_space**
> ZoneSpace create_zone_space(cloud_pk, model_pk, project_pk, zone_pk, zone_space_request)

Create a space in a zone

The IFC file will not be updated. The created space will be accessible over the API and when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.zone_space_request import ZoneSpaceRequest
from bimdata_api_client.model.zone_space import ZoneSpace
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    zone_pk = 1 # int | A unique integer value identifying this zone.
    zone_space_request = ZoneSpaceRequest(
        name="name_example",
        longname="longname_example",
        uuid="uuid_example",
        geometry=[
            GeometryPointRequest(
                x=3.14,
                y=3.14,
                z=3.14,
            ),
        ],
        order=0,
    ) # ZoneSpaceRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a space in a zone
        api_response = api_instance.create_zone_space(cloud_pk, model_pk, project_pk, zone_pk, zone_space_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->create_zone_space: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **zone_pk** | **int**| A unique integer value identifying this zone. |
 **zone_space_request** | [**ZoneSpaceRequest**](ZoneSpaceRequest.md)|  |

### Return type

[**ZoneSpace**](ZoneSpace.md)

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

# **delete_access_token**
> delete_access_token(cloud_pk, model_pk, project_pk, token)

Delete a token

DEPECRATED: Use ProjectAccessToken instead  Required scopes: ifc:token_manage, model:token_manage

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    token = "token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a token
        api_instance.delete_access_token(cloud_pk, model_pk, project_pk, token)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **token** | **str**|  |

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

# **delete_building**
> delete_building(cloud_pk, model_pk, project_pk, uuid)

Delete a building of a model

Delete a building of a model  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a building of a model
        api_instance.delete_building(cloud_pk, model_pk, project_pk, uuid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_building: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |

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

# **delete_building_plan**
> delete_building_plan(building_uuid, cloud_pk, id, model_pk, project_pk)

Delete the relation between a 2d model and a building

Delete the relation between a 2d model and a building  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    building_uuid = "building_uuid_example" # str | 
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this element.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete the relation between a 2d model and a building
        api_instance.delete_building_plan(building_uuid, cloud_pk, id, model_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_building_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_uuid** | **str**|  |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this element. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **delete_drawing**
> delete_drawing(cloud_pk, id, model_pk, project_pk)

Delete a drawing of a model

Delete a drawing of a model  Required scopes: model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this drawing.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a drawing of a model
        api_instance.delete_drawing(cloud_pk, id, model_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_drawing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this drawing. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **delete_element**
> delete_element(cloud_pk, model_pk, project_pk, uuid)

Delete an element of a model

The IFC file will not be updated. The remaining elements are available in API and will be available when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an element of a model
        api_instance.delete_element(cloud_pk, model_pk, project_pk, uuid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |

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

# **delete_layer**
> delete_layer(cloud_pk, id, model_pk, project_pk)

Delete a layer of a model

The IFC file will not be updated. The remaining layers are available in API and will be available when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this layer.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a layer of a model
        api_instance.delete_layer(cloud_pk, id, model_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_layer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this layer. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **delete_mask2_d**
> delete_mask2_d(cloud_pk, id, project_pk)

Delete the 2D mask for the model

Delete the 2D mask for the model.

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the 2D mask for the model
        api_instance.delete_mask2_d(cloud_pk, id, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_mask2_d: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |

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
**404** | This model has no 2d mask yet. |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model**
> delete_model(cloud_pk, id, project_pk)

Delete a model

It will also delete the related document  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a model
        api_instance.delete_model(cloud_pk, id, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |

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

# **delete_model_property**
> delete_model_property(cloud_pk, id, model_pk, project_pk)

Delete a Property of a model

Delete a Property of a model  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Property of a model
        api_instance.delete_model_property(cloud_pk, id, model_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_model_property: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **delete_model_property_definition**
> delete_model_property_definition(cloud_pk, id, model_pk, project_pk)

Delete a PropertyDefinitions of a model

Delete a PropertyDefinitions of a model  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property definition.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a PropertyDefinitions of a model
        api_instance.delete_model_property_definition(cloud_pk, id, model_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_model_property_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property definition. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **delete_model_unit**
> delete_model_unit(cloud_pk, id, model_pk, project_pk)

Delete a Unit of a model

Delete a Unit of a model  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this unit.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Unit of a model
        api_instance.delete_model_unit(cloud_pk, id, model_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_model_unit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this unit. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **delete_model_without_doc**
> delete_model_without_doc(cloud_pk, id, project_pk)

Delete the Model without deleting the related document

Delete the Model without deleting the related document  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the Model without deleting the related document
        api_instance.delete_model_without_doc(cloud_pk, id, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_model_without_doc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |

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

# **delete_property_set**
> delete_property_set(cloud_pk, id, model_pk, project_pk)

Delete a PropertySet of a model

Delete a PropertySet of a model  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property set.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a PropertySet of a model
        api_instance.delete_property_set(cloud_pk, id, model_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_property_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property set. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **delete_space**
> delete_space(cloud_pk, id, model_pk, project_pk)

Delete a space

It will not delete related zones. The IFC file will not be updated. The remaining spaces are available in API and will be available when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this space.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a space
        api_instance.delete_space(cloud_pk, id, model_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_space: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this space. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **delete_storey**
> delete_storey(cloud_pk, model_pk, project_pk, uuid)

Delete a storey of a model

Delete a storey of a model  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a storey of a model
        api_instance.delete_storey(cloud_pk, model_pk, project_pk, uuid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_storey: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |

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

# **delete_storey_plan**
> delete_storey_plan(cloud_pk, id, model_pk, project_pk, storey_uuid)

Delete the relation between a 2d model and a storey

Delete the relation between a 2d model and a storey  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this element.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    storey_uuid = "storey_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the relation between a 2d model and a storey
        api_instance.delete_storey_plan(cloud_pk, id, model_pk, project_pk, storey_uuid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_storey_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this element. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **storey_uuid** | **str**|  |

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

# **delete_system**
> delete_system(cloud_pk, model_pk, project_pk, uuid)

Delete a system of a model

The IFC file will not be updated. The remaining systems are available in API and will be available when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a system of a model
        api_instance.delete_system(cloud_pk, model_pk, project_pk, uuid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |

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

# **delete_zone**
> delete_zone(cloud_pk, id, model_pk, project_pk)

Delete a zone of a model

The IFC file will not be updated. The remaining zones are available in API and will be available when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this zone.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a zone of a model
        api_instance.delete_zone(cloud_pk, id, model_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_zone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this zone. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **delete_zone_space**
> delete_zone_space(cloud_pk, id, model_pk, project_pk, zone_pk)

Delete the relation between a space and a zone

Delete the relation between a space and a zone. The IFC file will not be updated. The remaining spaces are available in API and will be available when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this space.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    zone_pk = 1 # int | A unique integer value identifying this zone.

    # example passing only required values which don't have defaults set
    try:
        # Delete the relation between a space and a zone
        api_instance.delete_zone_space(cloud_pk, id, model_pk, project_pk, zone_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->delete_zone_space: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this space. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **zone_pk** | **int**| A unique integer value identifying this zone. |

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

# **export_ifc**
> export_ifc(cloud_pk, id, project_pk, ifc_export_request)

Export IFC

Only works for IFC files. Export IFC as requested in parameters. When the export is finished, a new IFC file with will be created in the same folder than the original IFC. You can query the folder or subscribe to the new document webhook to retrieve the result  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.ifc_export_request import IfcExportRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 
    ifc_export_request = IfcExportRequest(
        classifications="UPDATED",
        zones="UPDATED",
        properties="UPDATED",
        systems="UPDATED",
        layers="UPDATED",
        materials="UPDATED",
        attributes="UPDATED",
        structure="UPDATED",
        uuids=[
            "uuids_example",
        ],
        file_name="file_name_example",
    ) # IfcExportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Export IFC
        api_instance.export_ifc(cloud_pk, id, project_pk, ifc_export_request)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->export_ifc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |
 **ifc_export_request** | [**IfcExportRequest**](IfcExportRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **full_update_element**
> Element full_update_element(cloud_pk, model_pk, project_pk, uuid, element_request)

Update all fields of an element

Update all fields of an element. The IFC file will not be updated. The created element will be accessible over the API and when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.element_request import ElementRequest
from bimdata_api_client.model.element import Element
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 
    element_request = ElementRequest(
        uuid="uuid_example",
        type="type_example",
        attributes=PropertySetRequest(
            name="name_example",
            description="description_example",
            type="type_example",
            properties=[
                PropertyRequest(
                    definition=PropertyDefinitionRequest(
                        unit=None,
                        name="name_example",
                        description="description_example",
                        type="type_example",
                        value_type="value_type_example",
                    ),
                    value=None,
                ),
            ],
        ),
        property_sets=[
            PropertySetRequest(
                name="name_example",
                description="description_example",
                type="type_example",
                properties=[
                    PropertyRequest(
                        definition=PropertyDefinitionRequest(
                            unit=None,
                            name="name_example",
                            description="description_example",
                            type="type_example",
                            value_type="value_type_example",
                        ),
                        value=None,
                    ),
                ],
            ),
        ],
        classifications=[
            ClassificationRequest(
                name="name_example",
                notation="notation_example",
                title="title_example",
            ),
        ],
        layers=[
            LayerElementRequest(
                name="name_example",
                identifier="identifier_example",
                description="description_example",
            ),
        ],
    ) # ElementRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update all fields of an element
        api_response = api_instance.full_update_element(cloud_pk, model_pk, project_pk, uuid, element_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->full_update_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |
 **element_request** | [**ElementRequest**](ElementRequest.md)|  |

### Return type

[**Element**](Element.md)

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

# **get_access_token**
> IfcAccessToken get_access_token(cloud_pk, model_pk, project_pk, token)

Retrieve one token created for this model

DEPECRATED: Use ProjectAccessToken instead  Required scopes: ifc:token_manage, model:token_manage

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.ifc_access_token import IfcAccessToken
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    token = "token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve one token created for this model
        api_response = api_instance.get_access_token(cloud_pk, model_pk, project_pk, token)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **token** | **str**|  |

### Return type

[**IfcAccessToken**](IfcAccessToken.md)

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

# **get_access_tokens**
> [IfcAccessToken] get_access_tokens(cloud_pk, model_pk, project_pk)

Retrieve all tokens created for this model

DEPECRATED: Use ProjectAccessToken instead  Required scopes: ifc:token_manage, model:token_manage

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.ifc_access_token import IfcAccessToken
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all tokens created for this model
        api_response = api_instance.get_access_tokens(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_access_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[IfcAccessToken]**](IfcAccessToken.md)

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

# **get_building**
> Building get_building(cloud_pk, model_pk, project_pk, uuid)

Retrieve a building of a model

Retrieve a building of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.building import Building
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a building of a model
        api_response = api_instance.get_building(cloud_pk, model_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_building: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |

### Return type

[**Building**](Building.md)

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

# **get_building_plan_positioning**
> PositioningPlan get_building_plan_positioning(building_uuid, cloud_pk, id, model_pk, project_pk)

Retrieve the postioning of the plan in the building

Retrieve the postioning of the plan in the building  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.positioning_plan import PositioningPlan
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
    api_instance = model_api.ModelApi(api_client)
    building_uuid = "building_uuid_example" # str | 
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this element.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the postioning of the plan in the building
        api_response = api_instance.get_building_plan_positioning(building_uuid, cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_building_plan_positioning: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_uuid** | **str**|  |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this element. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**PositioningPlan**](PositioningPlan.md)

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

# **get_buildings**
> [Building] get_buildings(cloud_pk, model_pk, project_pk)

Retrieve all buildings of a model

Retrieve all buildings of a model.  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.building import Building
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all buildings of a model
        api_response = api_instance.get_buildings(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_buildings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[Building]**](Building.md)

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

# **get_classifications_of_element**
> [Classification] get_classifications_of_element(cloud_pk, element_uuid, model_pk, project_pk)

Retrieve all classifications of an element

Retrieve all classifications of an element  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.classification import Classification
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all classifications of an element
        api_response = api_instance.get_classifications_of_element(cloud_pk, element_uuid, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_classifications_of_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[Classification]**](Classification.md)

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

# **get_documents_of_element**
> [Document] get_documents_of_element(cloud_pk, element_uuid, model_pk, project_pk)

Retrieve all documents of an element

Retrieve all documents of an element  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.document import Document
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all documents of an element
        api_response = api_instance.get_documents_of_element(cloud_pk, element_uuid, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_documents_of_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[Document]**](Document.md)

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

# **get_drawing**
> Drawing get_drawing(cloud_pk, id, model_pk, project_pk)

Retrieve a drawing of a model

Retrieve a drawing of a model  Required scopes: model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.drawing import Drawing
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this drawing.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a drawing of a model
        api_response = api_instance.get_drawing(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_drawing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this drawing. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**Drawing**](Drawing.md)

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

# **get_drawings**
> [Drawing] get_drawings(cloud_pk, model_pk, project_pk)

Retrieve all drawings of a model

Retrieve all drawings of a model.  Required scopes: model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.drawing import Drawing
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all drawings of a model
        api_response = api_instance.get_drawings(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_drawings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[Drawing]**](Drawing.md)

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

# **get_element**
> Element get_element(cloud_pk, model_pk, project_pk, uuid)

Retrieve an element of a model

Retrieve an element of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.element import Element
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an element of a model
        api_response = api_instance.get_element(cloud_pk, model_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |

### Return type

[**Element**](Element.md)

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

# **get_element_linked_documents**
> [DocumentWithElementList] get_element_linked_documents(cloud_pk, model_pk, project_pk)

Retrieve all documents linked to any element

Retrieve all documents linked to any element with the list of uuids  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.document_with_element_list import DocumentWithElementList
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    classification = "classification_example" # str |  (optional)
    classification__notation = "classification__notation_example" # str |  (optional)
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all documents linked to any element
        api_response = api_instance.get_element_linked_documents(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_element_linked_documents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve all documents linked to any element
        api_response = api_instance.get_element_linked_documents(cloud_pk, model_pk, project_pk, classification=classification, classification__notation=classification__notation, type=type)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_element_linked_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **classification** | **str**|  | [optional]
 **classification__notation** | **str**|  | [optional]
 **type** | **str**|  | [optional]

### Return type

[**[DocumentWithElementList]**](DocumentWithElementList.md)

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

# **get_element_property_set**
> PropertySet get_element_property_set(cloud_pk, element_uuid, id, model_pk, project_pk)

Retrieve a PropertySet of an element

Retrieve a PropertySet of an element  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_set import PropertySet
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this property set.
    model_pk = 1 # int | 
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a PropertySet of an element
        api_response = api_instance.get_element_property_set(cloud_pk, element_uuid, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_element_property_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this property set. |
 **model_pk** | **int**|  |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**PropertySet**](PropertySet.md)

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

# **get_element_property_set_properties**
> [ModelProperty] get_element_property_set_properties(cloud_pk, element_uuid, model_pk, project_pk, propertyset_pk)

Retrieve all Properties of a PropertySet

Retrieve all Properties of a PropertySet  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.model_property import ModelProperty
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all Properties of a PropertySet
        api_response = api_instance.get_element_property_set_properties(cloud_pk, element_uuid, model_pk, project_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_element_property_set_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **propertyset_pk** | **int**| A unique integer value identifying this property set. |

### Return type

[**[ModelProperty]**](ModelProperty.md)

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

# **get_element_property_set_property**
> ModelProperty get_element_property_set_property(cloud_pk, element_uuid, id, model_pk, project_pk, propertyset_pk)

Retrieve a Property of a PropertySet

Retrieve a Property of a PropertySet  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.model_property import ModelProperty
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this property.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Property of a PropertySet
        api_response = api_instance.get_element_property_set_property(cloud_pk, element_uuid, id, model_pk, project_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_element_property_set_property: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this property. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **propertyset_pk** | **int**| A unique integer value identifying this property set. |

### Return type

[**ModelProperty**](ModelProperty.md)

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

# **get_element_property_set_property_definition**
> PropertyDefinition get_element_property_set_property_definition(cloud_pk, element_uuid, id, model_pk, project_pk, property_pk, propertyset_pk)

Retrieve a Definition of a Property

Retrieve a Definition of a Property  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_definition import PropertyDefinition
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this property definition.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_pk = 1 # int | A unique integer value identifying this property.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Definition of a Property
        api_response = api_instance.get_element_property_set_property_definition(cloud_pk, element_uuid, id, model_pk, project_pk, property_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_element_property_set_property_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this property definition. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **property_pk** | **int**| A unique integer value identifying this property. |
 **propertyset_pk** | **int**| A unique integer value identifying this property set. |

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

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

# **get_element_property_set_property_definition_unit**
> Unit get_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, model_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)

Retrieve a Unit of a Definition

Retrieve a Unit of a Definition  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.unit import Unit
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this unit.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_pk = 1 # int | A unique integer value identifying this property.
    propertydefinition_pk = 1 # int | A unique integer value identifying this property definition.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Unit of a Definition
        api_response = api_instance.get_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, model_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_element_property_set_property_definition_unit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this unit. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **property_pk** | **int**| A unique integer value identifying this property. |
 **propertydefinition_pk** | **int**| A unique integer value identifying this property definition. |
 **propertyset_pk** | **int**| A unique integer value identifying this property set. |

### Return type

[**Unit**](Unit.md)

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

# **get_element_property_set_property_definition_units**
> [Unit] get_element_property_set_property_definition_units(cloud_pk, element_uuid, model_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)

Retrieve all Units of a Definition

Retrieve all Units of a Definition  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.unit import Unit
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_pk = 1 # int | A unique integer value identifying this property.
    propertydefinition_pk = 1 # int | A unique integer value identifying this property definition.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all Units of a Definition
        api_response = api_instance.get_element_property_set_property_definition_units(cloud_pk, element_uuid, model_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_element_property_set_property_definition_units: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **property_pk** | **int**| A unique integer value identifying this property. |
 **propertydefinition_pk** | **int**| A unique integer value identifying this property definition. |
 **propertyset_pk** | **int**| A unique integer value identifying this property set. |

### Return type

[**[Unit]**](Unit.md)

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

# **get_element_property_set_property_definitions**
> [PropertyDefinition] get_element_property_set_property_definitions(cloud_pk, element_uuid, model_pk, project_pk, property_pk, propertyset_pk)

Retrieve all Definitions of a PropertySet

Retrieve all Definitions of a PropertySet  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_definition import PropertyDefinition
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_pk = 1 # int | A unique integer value identifying this property.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all Definitions of a PropertySet
        api_response = api_instance.get_element_property_set_property_definitions(cloud_pk, element_uuid, model_pk, project_pk, property_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_element_property_set_property_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **property_pk** | **int**| A unique integer value identifying this property. |
 **propertyset_pk** | **int**| A unique integer value identifying this property set. |

### Return type

[**[PropertyDefinition]**](PropertyDefinition.md)

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

# **get_element_property_sets**
> [PropertySet] get_element_property_sets(cloud_pk, element_uuid, model_pk, project_pk)

Retrieve all PropertySets of an element

Retrieve all PropertySets of an element  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_set import PropertySet
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | 
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all PropertySets of an element
        api_response = api_instance.get_element_property_sets(cloud_pk, element_uuid, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_element_property_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**|  |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[PropertySet]**](PropertySet.md)

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

# **get_elements**
> [Element] get_elements(cloud_pk, model_pk, project_pk)

Retrieve all elements of a model

Retrieve all elements of a model. If not filtered, the json may be very large. To efficently retrieve all elements and their data, see getRawElements  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.element import Element
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    classification = "classification_example" # str |  (optional)
    classification__notation = "classification__notation_example" # str |  (optional)
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all elements of a model
        api_response = api_instance.get_elements(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_elements: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve all elements of a model
        api_response = api_instance.get_elements(cloud_pk, model_pk, project_pk, classification=classification, classification__notation=classification__notation, type=type)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_elements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **classification** | **str**|  | [optional]
 **classification__notation** | **str**|  | [optional]
 **type** | **str**|  | [optional]

### Return type

[**[Element]**](Element.md)

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

# **get_elements_from_classification**
> [Element] get_elements_from_classification(cloud_pk, model_classification_pk, model_pk, project_pk)

Retrieve all elements with the classification

Retrieve all elements with the classification  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.element import Element
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    model_classification_pk = 1 # int | A unique integer value identifying this classification.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all elements with the classification
        api_response = api_instance.get_elements_from_classification(cloud_pk, model_classification_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_elements_from_classification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **model_classification_pk** | **int**| A unique integer value identifying this classification. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[Element]**](Element.md)

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

# **get_layer**
> Layer get_layer(cloud_pk, id, model_pk, project_pk)

Retrieve a layer of a model

Retrieve a layer of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.layer import Layer
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this layer.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a layer of a model
        api_response = api_instance.get_layer(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_layer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this layer. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**Layer**](Layer.md)

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

# **get_layers**
> [Layer] get_layers(cloud_pk, model_pk, project_pk)

Retrieve all layers of a model

Retrieve all layers of a model.  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.layer import Layer
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all layers of a model
        api_response = api_instance.get_layers(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_layers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[Layer]**](Layer.md)

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

# **get_material**
> Material get_material(cloud_pk, element_uuid, id, model_pk, project_pk)

Retrieve a material of a model

Retrieve a material of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.material import Material
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this material.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a material of a model
        api_response = api_instance.get_material(cloud_pk, element_uuid, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_material: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this material. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**Material**](Material.md)

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

# **get_materials**
> [Material] get_materials(cloud_pk, element_uuid, model_pk, project_pk)

Retrieve all materials of a model

Retrieve all materials of a model.  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.material import Material
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all materials of a model
        api_response = api_instance.get_materials(cloud_pk, element_uuid, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_materials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[Material]**](Material.md)

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

# **get_model**
> Model get_model(cloud_pk, id, project_pk)

Retrieve one model

Retrieve one model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.model import Model
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve one model
        api_response = api_instance.get_model(cloud_pk, id, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |

### Return type

[**Model**](Model.md)

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

# **get_model_classifications**
> [Classification] get_model_classifications(cloud_pk, model_pk, project_pk)

Retrieve all classifications in a model

Retrieve all classifications in a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.classification import Classification
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    model_pk = 1 # int | 
    project_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all classifications in a model
        api_response = api_instance.get_model_classifications(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_model_classifications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **model_pk** | **int**|  |
 **project_pk** | **int**|  |

### Return type

[**[Classification]**](Classification.md)

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

# **get_model_material**
> Material get_model_material(cloud_pk, id, model_pk, project_pk)

Retrieve a material of a model

Retrieve a material of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.material import Material
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this material.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a material of a model
        api_response = api_instance.get_model_material(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_model_material: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this material. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**Material**](Material.md)

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

# **get_model_materials**
> [Material] get_model_materials(cloud_pk, model_pk, project_pk)

Retrieve all materials of a model

Retrieve all materials of a model.  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.material import Material
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all materials of a model
        api_response = api_instance.get_model_materials(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_model_materials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[Material]**](Material.md)

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

# **get_model_properties**
> [ModelProperty] get_model_properties(cloud_pk, model_pk, project_pk)

Retrieve all Properties of a model

Retrieve all PropertySets of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.model_property import ModelProperty
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all Properties of a model
        api_response = api_instance.get_model_properties(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_model_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[ModelProperty]**](ModelProperty.md)

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

# **get_model_property**
> ModelProperty get_model_property(cloud_pk, id, model_pk, project_pk)

Retrieve a Property of a model

Retrieve a Property of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.model_property import ModelProperty
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Property of a model
        api_response = api_instance.get_model_property(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_model_property: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**ModelProperty**](ModelProperty.md)

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

# **get_model_property_definition**
> PropertyDefinition get_model_property_definition(cloud_pk, id, model_pk, project_pk)

Retrieve a PropertyDefinition of a model

Retrieve a PropertyDefinition of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_definition import PropertyDefinition
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property definition.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a PropertyDefinition of a model
        api_response = api_instance.get_model_property_definition(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_model_property_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property definition. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

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

# **get_model_property_definitions**
> [PropertyDefinition] get_model_property_definitions(cloud_pk, model_pk, project_pk)

Retrieve all PropertyDefinitions of a model

Retrieve all PropertyDefinitions of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_definition import PropertyDefinition
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all PropertyDefinitions of a model
        api_response = api_instance.get_model_property_definitions(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_model_property_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[PropertyDefinition]**](PropertyDefinition.md)

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

# **get_model_unit**
> Unit get_model_unit(cloud_pk, id, model_pk, project_pk)

Retrieve a Unit of a model

Retrieve a Unit of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.unit import Unit
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this unit.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Unit of a model
        api_response = api_instance.get_model_unit(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_model_unit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this unit. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**Unit**](Unit.md)

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

# **get_model_units**
> [Unit] get_model_units(cloud_pk, model_pk, project_pk)

Retrieve all Units of a model

Retrieve all Units of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.unit import Unit
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all Units of a model
        api_response = api_instance.get_model_units(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_model_units: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[Unit]**](Unit.md)

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

# **get_models**
> [Model] get_models(cloud_pk, project_pk)

Retrieve all models

Retrieve all models. The field `type` allows you to discriminate which kind of model it is.  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.model import Model
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    project_pk = 1 # int | 
    source = "EXPORT" # str | * `UPLOAD` - UPLOAD * `SPLIT` - SPLIT * `MERGE` - MERGE * `EXPORT` - EXPORT * `OPTIMIZED` - OPTIMIZED (optional)
    status = [
        "C",
    ] # [str] | * `C` - completed * `D` - deleted * `P` - pending * `W` - waiting * `I` - in process * `E` - errored * `X` - won't fix (optional)
    type = [
        "DWG",
    ] # [str] | * `IFC` - IFC * `DWG` - DWG * `DXF` - DXF * `GLTF` - GLTF * `PDF` - PDF * `JPEG` - JPEG * `PNG` - PNG * `OBJ` - OBJ * `POINT_CLOUD` - POINT_CLOUD * `METABUILDING` - METABUILDING * `PHOTOSPHERE` - PHOTOSPHERE * `PHOTOSPHERE_BUILDING` - PHOTOSPHERE_BUILDING (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all models
        api_response = api_instance.get_models(cloud_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_models: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve all models
        api_response = api_instance.get_models(cloud_pk, project_pk, source=source, status=status, type=type)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_models: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **project_pk** | **int**|  |
 **source** | **str**| * &#x60;UPLOAD&#x60; - UPLOAD * &#x60;SPLIT&#x60; - SPLIT * &#x60;MERGE&#x60; - MERGE * &#x60;EXPORT&#x60; - EXPORT * &#x60;OPTIMIZED&#x60; - OPTIMIZED | [optional]
 **status** | **[str]**| * &#x60;C&#x60; - completed * &#x60;D&#x60; - deleted * &#x60;P&#x60; - pending * &#x60;W&#x60; - waiting * &#x60;I&#x60; - in process * &#x60;E&#x60; - errored * &#x60;X&#x60; - won&#39;t fix | [optional]
 **type** | **[str]**| * &#x60;IFC&#x60; - IFC * &#x60;DWG&#x60; - DWG * &#x60;DXF&#x60; - DXF * &#x60;GLTF&#x60; - GLTF * &#x60;PDF&#x60; - PDF * &#x60;JPEG&#x60; - JPEG * &#x60;PNG&#x60; - PNG * &#x60;OBJ&#x60; - OBJ * &#x60;POINT_CLOUD&#x60; - POINT_CLOUD * &#x60;METABUILDING&#x60; - METABUILDING * &#x60;PHOTOSPHERE&#x60; - PHOTOSPHERE * &#x60;PHOTOSPHERE_BUILDING&#x60; - PHOTOSPHERE_BUILDING | [optional]

### Return type

[**[Model]**](Model.md)

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

# **get_processor_handler**
> ProcessorHandler get_processor_handler(cloud_pk, id, model_pk, project_pk)

Retrieve a processor handler

Retrieve a processor handler  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.processor_handler import ProcessorHandler
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this processor handler.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a processor handler
        api_response = api_instance.get_processor_handler(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_processor_handler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this processor handler. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**ProcessorHandler**](ProcessorHandler.md)

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

# **get_processor_handlers**
> [ProcessorHandler] get_processor_handlers(cloud_pk, model_pk, project_pk)

Get all processor handlers

Get all processor handlers  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.processor_handler import ProcessorHandler
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Get all processor handlers
        api_response = api_instance.get_processor_handlers(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_processor_handlers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[ProcessorHandler]**](ProcessorHandler.md)

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

# **get_property_set**
> PropertySet get_property_set(cloud_pk, id, model_pk, project_pk)

Retrieve a PropertySet of a model

Retrieve a PropertySet of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_set import PropertySet
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property set.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a PropertySet of a model
        api_response = api_instance.get_property_set(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_property_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property set. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**PropertySet**](PropertySet.md)

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

# **get_property_sets**
> [PropertySet] get_property_sets(cloud_pk, model_pk, project_pk)

Retrieve all PropertySets of a model

Retrieve all PropertySets of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_set import PropertySet
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all PropertySets of a model
        api_response = api_instance.get_property_sets(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_property_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[PropertySet]**](PropertySet.md)

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

# **get_raw_elements**
> RawElements get_raw_elements(cloud_pk, model_pk, project_pk)

Retrieve all elements in a optimized format

Instead of a nested representation, this route respond with a flat structure and indices pointing to related object. The IFC file will not be updated. The created elements will be accessible over the API and when exporting an IFC file. Returns elements, property_sets, properties, definitions and units in a JSON optimized structure  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.raw_elements import RawElements
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    classification = "classification_example" # str |  (optional)
    classification__notation = "classification__notation_example" # str |  (optional)
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all elements in a optimized format
        api_response = api_instance.get_raw_elements(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_raw_elements: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve all elements in a optimized format
        api_response = api_instance.get_raw_elements(cloud_pk, model_pk, project_pk, classification=classification, classification__notation=classification__notation, type=type)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_raw_elements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **classification** | **str**|  | [optional]
 **classification__notation** | **str**|  | [optional]
 **type** | **str**|  | [optional]

### Return type

[**RawElements**](RawElements.md)

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

# **get_simple_element**
> SimpleElement get_simple_element(cloud_pk, model_pk, project_pk, uuid)

Retrieve an element of a model with a simple value representation

Retrieve an element of a model with a simple value representation  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.simple_element import SimpleElement
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an element of a model with a simple value representation
        api_response = api_instance.get_simple_element(cloud_pk, model_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_simple_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |

### Return type

[**SimpleElement**](SimpleElement.md)

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

# **get_simple_elements**
> SimpleElement get_simple_elements(cloud_pk, model_pk, project_pk)

Retrieve all elements of a model with a simple value representation

Retrieve all elements of a model with a simple value representation  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.simple_element import SimpleElement
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    classification = "classification_example" # str |  (optional)
    classification__notation = "classification__notation_example" # str |  (optional)
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all elements of a model with a simple value representation
        api_response = api_instance.get_simple_elements(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_simple_elements: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve all elements of a model with a simple value representation
        api_response = api_instance.get_simple_elements(cloud_pk, model_pk, project_pk, classification=classification, classification__notation=classification__notation, type=type)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_simple_elements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **classification** | **str**|  | [optional]
 **classification__notation** | **str**|  | [optional]
 **type** | **str**|  | [optional]

### Return type

[**SimpleElement**](SimpleElement.md)

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

# **get_space**
> Space get_space(cloud_pk, id, model_pk, project_pk)

Retrieve one space of the model

Retrieve one space of the model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.space import Space
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this space.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve one space of the model
        api_response = api_instance.get_space(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_space: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this space. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**Space**](Space.md)

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

# **get_spaces**
> [Space] get_spaces(cloud_pk, model_pk, project_pk)

Retrieve all spaces of the model

Retrieve all spaces of the model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.space import Space
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all spaces of the model
        api_response = api_instance.get_spaces(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_spaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[Space]**](Space.md)

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

# **get_storey**
> Storey get_storey(cloud_pk, model_pk, project_pk, uuid)

Retrieve a storey of a model

Retrieve a storey of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.storey import Storey
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a storey of a model
        api_response = api_instance.get_storey(cloud_pk, model_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_storey: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |

### Return type

[**Storey**](Storey.md)

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

# **get_storey_plan_positioning**
> PositioningPlan get_storey_plan_positioning(cloud_pk, id, model_pk, project_pk, storey_uuid)

Retrieve the postioning of the plan in the storey

Retrieve the postioning of the plan in the storey  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.positioning_plan import PositioningPlan
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this element.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    storey_uuid = "storey_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the postioning of the plan in the storey
        api_response = api_instance.get_storey_plan_positioning(cloud_pk, id, model_pk, project_pk, storey_uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_storey_plan_positioning: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this element. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **storey_uuid** | **str**|  |

### Return type

[**PositioningPlan**](PositioningPlan.md)

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

# **get_storeys**
> [Storey] get_storeys(cloud_pk, model_pk, project_pk)

Retrieve all storeys of a model

Retrieve all storeys of a model.  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.storey import Storey
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all storeys of a model
        api_response = api_instance.get_storeys(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_storeys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[Storey]**](Storey.md)

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

# **get_system**
> System get_system(cloud_pk, model_pk, project_pk, uuid)

Retrieve a system of a model

Retrieve a system of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.system import System
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a system of a model
        api_response = api_instance.get_system(cloud_pk, model_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |

### Return type

[**System**](System.md)

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

# **get_systems**
> [System] get_systems(cloud_pk, model_pk, project_pk)

Retrieve all systems of a model

Retrieve all systems of a model.  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.system import System
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all systems of a model
        api_response = api_instance.get_systems(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_systems: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[System]**](System.md)

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

# **get_tileset**
> get_tileset(cloud_pk, id, project_pk)

Retrieve the tileset of the model

This is only availble if the model is a POINT_CLOUD  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 
    tile_format = "pnts" # str |  (optional) if omitted the server will use the default value of "pnts"

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the tileset of the model
        api_instance.get_tileset(cloud_pk, id, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_tileset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the tileset of the model
        api_instance.get_tileset(cloud_pk, id, project_pk, tile_format=tile_format)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_tileset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |
 **tile_format** | **str**|  | [optional] if omitted the server will use the default value of "pnts"

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
**200** | No response body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone**
> Zone get_zone(cloud_pk, id, model_pk, project_pk)

Retrieve one zone of a model

Retrieve one zone of a model  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.zone import Zone
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this zone.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve one zone of a model
        api_response = api_instance.get_zone(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_zone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this zone. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**Zone**](Zone.md)

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

# **get_zone_space**
> ZoneSpace get_zone_space(cloud_pk, id, model_pk, project_pk, zone_pk)

Retrieve one space of a zone

Retrieve one space of a zone  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.zone_space import ZoneSpace
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this space.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    zone_pk = 1 # int | A unique integer value identifying this zone.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve one space of a zone
        api_response = api_instance.get_zone_space(cloud_pk, id, model_pk, project_pk, zone_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_zone_space: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this space. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **zone_pk** | **int**| A unique integer value identifying this zone. |

### Return type

[**ZoneSpace**](ZoneSpace.md)

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

# **get_zone_spaces**
> [ZoneSpace] get_zone_spaces(cloud_pk, model_pk, project_pk, zone_pk)

Retrieve all spaces of a zone

Retrieve all spaces of a zone  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.zone_space import ZoneSpace
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    zone_pk = 1 # int | A unique integer value identifying this zone.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all spaces of a zone
        api_response = api_instance.get_zone_spaces(cloud_pk, model_pk, project_pk, zone_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_zone_spaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **zone_pk** | **int**| A unique integer value identifying this zone. |

### Return type

[**[ZoneSpace]**](ZoneSpace.md)

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

# **get_zones**
> [Zone] get_zones(cloud_pk, model_pk, project_pk)

Retrieve zones of a model

Retrieve parent zones of a model. Children zones we'll be in the 'zones' field  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.zone import Zone
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    color = "color_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve zones of a model
        api_response = api_instance.get_zones(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_zones: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve zones of a model
        api_response = api_instance.get_zones(cloud_pk, model_pk, project_pk, color=color)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->get_zones: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **color** | **str**|  | [optional]

### Return type

[**[Zone]**](Zone.md)

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

# **link_documents_of_element**
> [Document] link_documents_of_element(cloud_pk, element_uuid, model_pk, project_pk, request_body)

Link one or many documents to an element

 Bulk relation create available. You can either post an id or a list of ids. Is you post a list, the response will be a list (in the same order) of created relation or of errors if any If at least one create succeeded, the status code will be 201. If every create failed, the status code we'll be 400 with the list of errors   Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.document import Document
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Link one or many documents to an element
        api_response = api_instance.link_documents_of_element(cloud_pk, element_uuid, model_pk, project_pk, request_body)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->link_documents_of_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **request_body** | **[int]**|  |

### Return type

[**[Document]**](Document.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | All creates failed: list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_classification_element_relations**
> [ElementClassificationRelation] list_classification_element_relations(cloud_pk, model_pk, project_pk)

List all associations between classifications and elements

List all associations between classifications and elements  Required scopes: ifc:read, model:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.element_classification_relation import ElementClassificationRelation
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # List all associations between classifications and elements
        api_response = api_instance.list_classification_element_relations(cloud_pk, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->list_classification_element_relations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[ElementClassificationRelation]**](ElementClassificationRelation.md)

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

# **merge_ifcs**
> merge_ifcs(cloud_pk, project_pk, ifc_merge_request)

Merge IFC files

Only works for IFC files. Merge IFC files. The merged IFC file will be put in the same folder that the first IFC of the list  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.ifc_merge_request import IfcMergeRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    project_pk = 1 # int | 
    ifc_merge_request = IfcMergeRequest(
        ifc_ids=[
            1,
        ],
        floating_point_reduction=9,
        export_name="export_name_example",
    ) # IfcMergeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Merge IFC files
        api_instance.merge_ifcs(cloud_pk, project_pk, ifc_merge_request)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->merge_ifcs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **project_pk** | **int**|  |
 **ifc_merge_request** | [**IfcMergeRequest**](IfcMergeRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **optimize_ifc**
> optimize_ifc(cloud_pk, id, project_pk)

Optimize the IFC

Only works for IFC files. Optimize the IFC. A new optimized IFC file will be put in the same folder that the original IFC  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.ifc_optimize_request import IfcOptimizeRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 
    ifc_optimize_request = IfcOptimizeRequest(
        floating_point_reduction=9,
    ) # IfcOptimizeRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Optimize the IFC
        api_instance.optimize_ifc(cloud_pk, id, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->optimize_ifc: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Optimize the IFC
        api_instance.optimize_ifc(cloud_pk, id, project_pk, ifc_optimize_request=ifc_optimize_request)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->optimize_ifc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |
 **ifc_optimize_request** | [**IfcOptimizeRequest**](IfcOptimizeRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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

# **remove_all_element_property_set**
> remove_all_element_property_set(cloud_pk, element_uuid, model_pk, project_pk)

Remove all property sets from element

Remove all property sets from element. Property Sets will not be deleted, just detached from element  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    model_pk = 1 # int | 
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Remove all property sets from element
        api_instance.remove_all_element_property_set(cloud_pk, element_uuid, model_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->remove_all_element_property_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **model_pk** | **int**|  |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **remove_classification_of_element**
> remove_classification_of_element(cloud_pk, element_uuid, id, model_pk, project_pk)

Remove a classification from an element

The classification will not be deleted  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this classification.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Remove a classification from an element
        api_instance.remove_classification_of_element(cloud_pk, element_uuid, id, model_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->remove_classification_of_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this classification. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **remove_document_of_element**
> remove_document_of_element(cloud_pk, element_uuid, id, model_pk, project_pk)

Remove a documents from an element

The document will not be deleted  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this document.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Remove a documents from an element
        api_instance.remove_document_of_element(cloud_pk, element_uuid, id, model_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->remove_document_of_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this document. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **remove_element_property_set**
> remove_element_property_set(cloud_pk, element_uuid, id, model_pk, project_pk)

Remove a PropertySet from an element

Delete the relation between the element and the property set. Does not delete any object  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this property set.
    model_pk = 1 # int | 
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Remove a PropertySet from an element
        api_instance.remove_element_property_set(cloud_pk, element_uuid, id, model_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->remove_element_property_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this property set. |
 **model_pk** | **int**|  |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **remove_element_property_set_property**
> remove_element_property_set_property(cloud_pk, element_uuid, id, model_pk, project_pk, propertyset_pk)

Remove a property from a PropertySet

Remove a property from a PropertySet  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this property.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Remove a property from a PropertySet
        api_instance.remove_element_property_set_property(cloud_pk, element_uuid, id, model_pk, project_pk, propertyset_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->remove_element_property_set_property: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this property. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **propertyset_pk** | **int**| A unique integer value identifying this property set. |

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

# **remove_element_property_set_property_definition**
> remove_element_property_set_property_definition(cloud_pk, element_uuid, id, model_pk, project_pk, property_pk, propertyset_pk)

Delete a Definition to a Property

Delete a Definition to a Property  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this property definition.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_pk = 1 # int | A unique integer value identifying this property.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Definition to a Property
        api_instance.remove_element_property_set_property_definition(cloud_pk, element_uuid, id, model_pk, project_pk, property_pk, propertyset_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->remove_element_property_set_property_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this property definition. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **property_pk** | **int**| A unique integer value identifying this property. |
 **propertyset_pk** | **int**| A unique integer value identifying this property set. |

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

# **remove_element_property_set_property_definition_unit**
> remove_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, model_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)

Remove a Unit from a Definition

Remove a Unit from a Definition  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this unit.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_pk = 1 # int | A unique integer value identifying this property.
    propertydefinition_pk = 1 # int | A unique integer value identifying this property definition.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Remove a Unit from a Definition
        api_instance.remove_element_property_set_property_definition_unit(cloud_pk, element_uuid, id, model_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->remove_element_property_set_property_definition_unit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this unit. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **property_pk** | **int**| A unique integer value identifying this property. |
 **propertydefinition_pk** | **int**| A unique integer value identifying this property definition. |
 **propertyset_pk** | **int**| A unique integer value identifying this property set. |

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

# **remove_elements_from_classification**
> remove_elements_from_classification(cloud_pk, model_classification_pk, model_pk, project_pk, uuid)

Remove the classification from all elements

Remove the classification from all elements. No element nor classification will be deleted  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    model_classification_pk = 1 # int | A unique integer value identifying this classification.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove the classification from all elements
        api_instance.remove_elements_from_classification(cloud_pk, model_classification_pk, model_pk, project_pk, uuid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->remove_elements_from_classification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **model_classification_pk** | **int**| A unique integer value identifying this classification. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |

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

# **reprocess_model**
> reprocess_model(cloud_pk, id, project_pk)

Reprocess Model file

Reprocess the model. All data that are not in the original model files will be lost  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Reprocess Model file
        api_instance.reprocess_model(cloud_pk, id, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->reprocess_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |

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

# **update_access_token**
> IfcAccessToken update_access_token(cloud_pk, model_pk, project_pk, token)

Update some fields of a token

DEPECRATED: Use ProjectAccessToken instead  Required scopes: ifc:token_manage, model:token_manage

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.ifc_access_token import IfcAccessToken
from bimdata_api_client.model.patched_ifc_access_token_request import PatchedIfcAccessTokenRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    token = "token_example" # str | 
    patched_ifc_access_token_request = PatchedIfcAccessTokenRequest(
        read_only=True,
        expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # PatchedIfcAccessTokenRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a token
        api_response = api_instance.update_access_token(cloud_pk, model_pk, project_pk, token)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_access_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a token
        api_response = api_instance.update_access_token(cloud_pk, model_pk, project_pk, token, patched_ifc_access_token_request=patched_ifc_access_token_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **token** | **str**|  |
 **patched_ifc_access_token_request** | [**PatchedIfcAccessTokenRequest**](PatchedIfcAccessTokenRequest.md)|  | [optional]

### Return type

[**IfcAccessToken**](IfcAccessToken.md)

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

# **update_building**
> Building update_building(cloud_pk, model_pk, project_pk, uuid)

Update some fields of a building

Update some fields of a building  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.building import Building
from bimdata_api_client.model.patched_storey_building_request import PatchedStoreyBuildingRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 
    patched_storey_building_request = PatchedStoreyBuildingRequest(
        name="name_example",
        bimdata_elevation=3.14,
    ) # PatchedStoreyBuildingRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a building
        api_response = api_instance.update_building(cloud_pk, model_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_building: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a building
        api_response = api_instance.update_building(cloud_pk, model_pk, project_pk, uuid, patched_storey_building_request=patched_storey_building_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_building: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |
 **patched_storey_building_request** | [**PatchedStoreyBuildingRequest**](PatchedStoreyBuildingRequest.md)|  | [optional]

### Return type

[**Building**](Building.md)

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

# **update_building_plan_positioning**
> PositioningPlan update_building_plan_positioning(building_uuid, cloud_pk, id, model_pk, project_pk)

Update the postioning of the plan in the building

Update the postioning of the plan in the building  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.patched_positioning_plan_request import PatchedPositioningPlanRequest
from bimdata_api_client.model.positioning_plan import PositioningPlan
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
    api_instance = model_api.ModelApi(api_client)
    building_uuid = "building_uuid_example" # str | 
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this element.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_positioning_plan_request = PatchedPositioningPlanRequest(
        translation_x=3.14,
        translation_y=3.14,
        rotate_z=3.14,
        scale=3.14,
        opacity=3.14,
    ) # PatchedPositioningPlanRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the postioning of the plan in the building
        api_response = api_instance.update_building_plan_positioning(building_uuid, cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_building_plan_positioning: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the postioning of the plan in the building
        api_response = api_instance.update_building_plan_positioning(building_uuid, cloud_pk, id, model_pk, project_pk, patched_positioning_plan_request=patched_positioning_plan_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_building_plan_positioning: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_uuid** | **str**|  |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this element. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **patched_positioning_plan_request** | [**PatchedPositioningPlanRequest**](PatchedPositioningPlanRequest.md)|  | [optional]

### Return type

[**PositioningPlan**](PositioningPlan.md)

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

# **update_drawing**
> Drawing update_drawing(cloud_pk, id, model_pk, project_pk)

Update some fields of a drawing

Update some fields of a drawing  Required scopes: model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.drawing import Drawing
from bimdata_api_client.model.patched_drawing_request import PatchedDrawingRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this drawing.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_drawing_request = PatchedDrawingRequest(
        content="content_example",
    ) # PatchedDrawingRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a drawing
        api_response = api_instance.update_drawing(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_drawing: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a drawing
        api_response = api_instance.update_drawing(cloud_pk, id, model_pk, project_pk, patched_drawing_request=patched_drawing_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_drawing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this drawing. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **patched_drawing_request** | [**PatchedDrawingRequest**](PatchedDrawingRequest.md)|  | [optional]

### Return type

[**Drawing**](Drawing.md)

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

# **update_element**
> Element update_element(cloud_pk, model_pk, project_pk, uuid)

Update some fields of an element

Update some fields of an element. The IFC file will not be updated. The created element will be accessible over the API and when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.patched_element_request import PatchedElementRequest
from bimdata_api_client.model.element import Element
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 
    patched_element_request = PatchedElementRequest(
        uuid="uuid_example",
        type="type_example",
        attributes=PropertySetRequest(
            name="name_example",
            description="description_example",
            type="type_example",
            properties=[
                PropertyRequest(
                    definition=PropertyDefinitionRequest(
                        unit=None,
                        name="name_example",
                        description="description_example",
                        type="type_example",
                        value_type="value_type_example",
                    ),
                    value=None,
                ),
            ],
        ),
        property_sets=[
            PropertySetRequest(
                name="name_example",
                description="description_example",
                type="type_example",
                properties=[
                    PropertyRequest(
                        definition=PropertyDefinitionRequest(
                            unit=None,
                            name="name_example",
                            description="description_example",
                            type="type_example",
                            value_type="value_type_example",
                        ),
                        value=None,
                    ),
                ],
            ),
        ],
        classifications=[
            ClassificationRequest(
                name="name_example",
                notation="notation_example",
                title="title_example",
            ),
        ],
        layers=[
            LayerElementRequest(
                name="name_example",
                identifier="identifier_example",
                description="description_example",
            ),
        ],
    ) # PatchedElementRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of an element
        api_response = api_instance.update_element(cloud_pk, model_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_element: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of an element
        api_response = api_instance.update_element(cloud_pk, model_pk, project_pk, uuid, patched_element_request=patched_element_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_element: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |
 **patched_element_request** | [**PatchedElementRequest**](PatchedElementRequest.md)|  | [optional]

### Return type

[**Element**](Element.md)

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

# **update_element_property_set_property**
> ModelProperty update_element_property_set_property(cloud_pk, element_uuid, id, model_pk, project_pk, propertyset_pk)

Update a property from an element

Update a property value from an element. If the element is the only one to have this property, the property will be update in place. If many elements share this property, a new property will be created to replace the property for this element. Keeping the property for all other elements. If you want to update the property of all elements, see updateIfcProperty  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.patched_property_request import PatchedPropertyRequest
from bimdata_api_client.model.model_property import ModelProperty
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this property.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.
    patched_property_request = PatchedPropertyRequest(
        definition=PropertyDefinitionRequest(
            unit=None,
            name="name_example",
            description="description_example",
            type="type_example",
            value_type="value_type_example",
        ),
        value=None,
    ) # PatchedPropertyRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a property from an element
        api_response = api_instance.update_element_property_set_property(cloud_pk, element_uuid, id, model_pk, project_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_element_property_set_property: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a property from an element
        api_response = api_instance.update_element_property_set_property(cloud_pk, element_uuid, id, model_pk, project_pk, propertyset_pk, patched_property_request=patched_property_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_element_property_set_property: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this property. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **propertyset_pk** | **int**| A unique integer value identifying this property set. |
 **patched_property_request** | [**PatchedPropertyRequest**](PatchedPropertyRequest.md)|  | [optional]

### Return type

[**ModelProperty**](ModelProperty.md)

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

# **update_layer**
> Layer update_layer(cloud_pk, id, model_pk, project_pk)

Update some fields of a layer

Update some fields of a layer. The IFC file will not be updated. The created layer will be accessible over the API and when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.patched_layer_request import PatchedLayerRequest
from bimdata_api_client.model.layer import Layer
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this layer.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_layer_request = PatchedLayerRequest(
        name="name_example",
        identifier="identifier_example",
        description="description_example",
        elements=[
            "elements_example",
        ],
    ) # PatchedLayerRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a layer
        api_response = api_instance.update_layer(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_layer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a layer
        api_response = api_instance.update_layer(cloud_pk, id, model_pk, project_pk, patched_layer_request=patched_layer_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_layer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this layer. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **patched_layer_request** | [**PatchedLayerRequest**](PatchedLayerRequest.md)|  | [optional]

### Return type

[**Layer**](Layer.md)

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

# **update_model**
> Model update_model(cloud_pk, id, project_pk)

Update some fields of a model

Update some fields of a model  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.patched_model_request import PatchedModelRequest
from bimdata_api_client.model.model import Model
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 
    patched_model_request = PatchedModelRequest(
        name="name_example",
        source="UPLOAD",
        world_position=[
            3.14,
        ],
        size_ratio=3.14,
        archived=True,
        version="version_example",
        north_vector=[
            [
                3.14,
            ],
        ],
        recommanded_2d_angle=3.14,
        layout_name="layout_name_example",
    ) # PatchedModelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a model
        api_response = api_instance.update_model(cloud_pk, id, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_model: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a model
        api_response = api_instance.update_model(cloud_pk, id, project_pk, patched_model_request=patched_model_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |
 **patched_model_request** | [**PatchedModelRequest**](PatchedModelRequest.md)|  | [optional]

### Return type

[**Model**](Model.md)

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

# **update_model_files**
> ModelFiles update_model_files(cloud_pk, id, project_pk)

Update models file (gltf, svg, structure, etc)

This route does not accept JSON, only files as x-www-form-urlencoded  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.model_files import ModelFiles
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 
    structure_file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)
    systems_file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)
    map_file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)
    gltf_file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)
    preview_file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)
    xkt_file = open('/path/to/file', 'rb') # file_type, none_type | DEPRECATED. xkt file url is now in xkt_files field with its version number (optional)
    binary_2d_file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update models file (gltf, svg, structure, etc)
        api_response = api_instance.update_model_files(cloud_pk, id, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_model_files: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update models file (gltf, svg, structure, etc)
        api_response = api_instance.update_model_files(cloud_pk, id, project_pk, structure_file=structure_file, systems_file=systems_file, map_file=map_file, gltf_file=gltf_file, preview_file=preview_file, xkt_file=xkt_file, binary_2d_file=binary_2d_file)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_model_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |
 **structure_file** | **file_type, none_type**|  | [optional]
 **systems_file** | **file_type, none_type**|  | [optional]
 **map_file** | **file_type, none_type**|  | [optional]
 **gltf_file** | **file_type, none_type**|  | [optional]
 **preview_file** | **file_type, none_type**|  | [optional]
 **xkt_file** | **file_type, none_type**| DEPRECATED. xkt file url is now in xkt_files field with its version number | [optional]
 **binary_2d_file** | **file_type, none_type**|  | [optional]

### Return type

[**ModelFiles**](ModelFiles.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BIMData_Connect](../README.md#BIMData_Connect), [BIMData_Connect](../README.md#BIMData_Connect), [Bearer](../README.md#Bearer)

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

# **update_model_property**
> ModelProperty update_model_property(cloud_pk, id, model_pk, project_pk)

Update some fields of a Property

Update some fields of a Property  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.patched_property_request import PatchedPropertyRequest
from bimdata_api_client.model.model_property import ModelProperty
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_property_request = PatchedPropertyRequest(
        definition=PropertyDefinitionRequest(
            unit=None,
            name="name_example",
            description="description_example",
            type="type_example",
            value_type="value_type_example",
        ),
        value=None,
    ) # PatchedPropertyRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a Property
        api_response = api_instance.update_model_property(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_model_property: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a Property
        api_response = api_instance.update_model_property(cloud_pk, id, model_pk, project_pk, patched_property_request=patched_property_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_model_property: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **patched_property_request** | [**PatchedPropertyRequest**](PatchedPropertyRequest.md)|  | [optional]

### Return type

[**ModelProperty**](ModelProperty.md)

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

# **update_model_property_definition**
> PropertyDefinition update_model_property_definition(cloud_pk, id, model_pk, project_pk)

Update some fields of many PropertyDefinitions of a model

Update some fields of many PropertyDefinitions of a model  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_definition import PropertyDefinition
from bimdata_api_client.model.patched_property_definition_request import PatchedPropertyDefinitionRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property definition.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_property_definition_request = PatchedPropertyDefinitionRequest(
        unit=None,
        name="name_example",
        description="description_example",
        type="type_example",
        value_type="value_type_example",
    ) # PatchedPropertyDefinitionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of many PropertyDefinitions of a model
        api_response = api_instance.update_model_property_definition(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_model_property_definition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of many PropertyDefinitions of a model
        api_response = api_instance.update_model_property_definition(cloud_pk, id, model_pk, project_pk, patched_property_definition_request=patched_property_definition_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_model_property_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property definition. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **patched_property_definition_request** | [**PatchedPropertyDefinitionRequest**](PatchedPropertyDefinitionRequest.md)|  | [optional]

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

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

# **update_model_unit**
> Unit update_model_unit(cloud_pk, id, model_pk, project_pk)

Update some fields of a Unit of a model

Update some fields of a Unit of a model  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.unit import Unit
from bimdata_api_client.model.patched_unit_request import PatchedUnitRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this unit.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_unit_request = PatchedUnitRequest(
        type="type_example",
        name="name_example",
        unit_type="unit_type_example",
        prefix="prefix_example",
        dimensions=[
            3.14,
        ],
        conversion_factor=3.14,
        conversion_baseunit=Unit(
            type="type_example",
            name="name_example",
            unit_type="unit_type_example",
            prefix="prefix_example",
            dimensions=[
                3.14,
            ],
            conversion_factor=3.14,
            conversion_baseunit=Unit(),
            elements=None,
            is_default=True,
        ),
        elements=None,
        is_default=True,
    ) # PatchedUnitRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a Unit of a model
        api_response = api_instance.update_model_unit(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_model_unit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a Unit of a model
        api_response = api_instance.update_model_unit(cloud_pk, id, model_pk, project_pk, patched_unit_request=patched_unit_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_model_unit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this unit. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **patched_unit_request** | [**PatchedUnitRequest**](PatchedUnitRequest.md)|  | [optional]

### Return type

[**Unit**](Unit.md)

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

# **update_order_building_plan**
> Storey update_order_building_plan(building_uuid, cloud_pk, model_pk, project_pk, request_body)

Update order of all plan of a building

Update order of all plan of a building  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.storey import Storey
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
    api_instance = model_api.ModelApi(api_client)
    building_uuid = "building_uuid_example" # str | 
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Update order of all plan of a building
        api_response = api_instance.update_order_building_plan(building_uuid, cloud_pk, model_pk, project_pk, request_body)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_order_building_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_uuid** | **str**|  |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **request_body** | **[int]**|  |

### Return type

[**Storey**](Storey.md)

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

# **update_order_storey_plan**
> Storey update_order_storey_plan(cloud_pk, model_pk, project_pk, storey_uuid, request_body)

Update order of all plan of a storey

Update order of all plan of a storey  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.storey import Storey
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    storey_uuid = "storey_uuid_example" # str | 
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Update order of all plan of a storey
        api_response = api_instance.update_order_storey_plan(cloud_pk, model_pk, project_pk, storey_uuid, request_body)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_order_storey_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **storey_uuid** | **str**|  |
 **request_body** | **[int]**|  |

### Return type

[**Storey**](Storey.md)

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

# **update_order_storeys**
> [Storey] update_order_storeys(cloud_pk, model_pk, project_pk, request_body)

Update order of all storey of a model

Update order of all storey of a model  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.storey import Storey
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    request_body = [
        "request_body_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # Update order of all storey of a model
        api_response = api_instance.update_order_storeys(cloud_pk, model_pk, project_pk, request_body)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_order_storeys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **request_body** | **[str]**|  |

### Return type

[**[Storey]**](Storey.md)

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

# **update_processor_handler**
> ProcessorHandler update_processor_handler(cloud_pk, id, model_pk, project_pk)

Update the status of a processor handler

Update the status of a processor handler  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.patched_processor_handler_request import PatchedProcessorHandlerRequest
from bimdata_api_client.model.processor_handler import ProcessorHandler
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this processor handler.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_processor_handler_request = PatchedProcessorHandlerRequest(
        status="C",
        detail_message="detail_message_example",
    ) # PatchedProcessorHandlerRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the status of a processor handler
        api_response = api_instance.update_processor_handler(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_processor_handler: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the status of a processor handler
        api_response = api_instance.update_processor_handler(cloud_pk, id, model_pk, project_pk, patched_processor_handler_request=patched_processor_handler_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_processor_handler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this processor handler. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **patched_processor_handler_request** | [**PatchedProcessorHandlerRequest**](PatchedProcessorHandlerRequest.md)|  | [optional]

### Return type

[**ProcessorHandler**](ProcessorHandler.md)

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

# **update_property_set**
> PropertySet update_property_set(cloud_pk, id, model_pk, project_pk)

Update some fields of a PropertySet

Update some fields of a PropertySet  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.property_set import PropertySet
from bimdata_api_client.model.patched_property_set_request import PatchedPropertySetRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property set.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_property_set_request = PatchedPropertySetRequest(
        name="name_example",
        description="description_example",
        type="type_example",
        properties=[
            PropertyRequest(
                definition=PropertyDefinitionRequest(
                    unit=None,
                    name="name_example",
                    description="description_example",
                    type="type_example",
                    value_type="value_type_example",
                ),
                value=None,
            ),
        ],
    ) # PatchedPropertySetRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a PropertySet
        api_response = api_instance.update_property_set(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_property_set: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a PropertySet
        api_response = api_instance.update_property_set(cloud_pk, id, model_pk, project_pk, patched_property_set_request=patched_property_set_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_property_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property set. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **patched_property_set_request** | [**PatchedPropertySetRequest**](PatchedPropertySetRequest.md)|  | [optional]

### Return type

[**PropertySet**](PropertySet.md)

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

# **update_space**
> Space update_space(cloud_pk, id, model_pk, project_pk)

Update some fields of a space

Update some fields of a space. The IFC file will not be updated. The created space will be accessible over the API and when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.patched_space_request import PatchedSpaceRequest
from bimdata_api_client.model.space import Space
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this space.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_space_request = PatchedSpaceRequest(
        name="name_example",
        longname="longname_example",
        uuid="uuid_example",
        geometry=[
            GeometryPointRequest(
                x=3.14,
                y=3.14,
                z=3.14,
            ),
        ],
    ) # PatchedSpaceRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a space
        api_response = api_instance.update_space(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_space: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a space
        api_response = api_instance.update_space(cloud_pk, id, model_pk, project_pk, patched_space_request=patched_space_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_space: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this space. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **patched_space_request** | [**PatchedSpaceRequest**](PatchedSpaceRequest.md)|  | [optional]

### Return type

[**Space**](Space.md)

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

# **update_storey**
> Storey update_storey(cloud_pk, model_pk, project_pk, uuid)

Update some fields of a storey

Update some fields of a storey  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.storey import Storey
from bimdata_api_client.model.patched_storey_building_request import PatchedStoreyBuildingRequest
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 
    patched_storey_building_request = PatchedStoreyBuildingRequest(
        name="name_example",
        bimdata_elevation=3.14,
    ) # PatchedStoreyBuildingRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a storey
        api_response = api_instance.update_storey(cloud_pk, model_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_storey: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a storey
        api_response = api_instance.update_storey(cloud_pk, model_pk, project_pk, uuid, patched_storey_building_request=patched_storey_building_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_storey: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |
 **patched_storey_building_request** | [**PatchedStoreyBuildingRequest**](PatchedStoreyBuildingRequest.md)|  | [optional]

### Return type

[**Storey**](Storey.md)

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

# **update_storey_plan_positioning**
> PositioningPlan update_storey_plan_positioning(cloud_pk, id, model_pk, project_pk, storey_uuid)

Update the postioning of the plan in the storey

Update the postioning of the plan in the storey  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.patched_positioning_plan_request import PatchedPositioningPlanRequest
from bimdata_api_client.model.positioning_plan import PositioningPlan
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this element.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    storey_uuid = "storey_uuid_example" # str | 
    patched_positioning_plan_request = PatchedPositioningPlanRequest(
        translation_x=3.14,
        translation_y=3.14,
        rotate_z=3.14,
        scale=3.14,
        opacity=3.14,
    ) # PatchedPositioningPlanRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the postioning of the plan in the storey
        api_response = api_instance.update_storey_plan_positioning(cloud_pk, id, model_pk, project_pk, storey_uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_storey_plan_positioning: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the postioning of the plan in the storey
        api_response = api_instance.update_storey_plan_positioning(cloud_pk, id, model_pk, project_pk, storey_uuid, patched_positioning_plan_request=patched_positioning_plan_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_storey_plan_positioning: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this element. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **storey_uuid** | **str**|  |
 **patched_positioning_plan_request** | [**PatchedPositioningPlanRequest**](PatchedPositioningPlanRequest.md)|  | [optional]

### Return type

[**PositioningPlan**](PositioningPlan.md)

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

# **update_system**
> System update_system(cloud_pk, model_pk, project_pk, uuid)

Update some fields of a system

Update some fields of a system. The IFC file will not be updated. The created system will be accessible over the API and when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.patched_system_request import PatchedSystemRequest
from bimdata_api_client.model.system import System
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 
    patched_system_request = PatchedSystemRequest(
        uuid="uuid_example",
        name="name_example",
        object_type="object_type_example",
        description="description_example",
        elements=[
            "elements_example",
        ],
    ) # PatchedSystemRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a system
        api_response = api_instance.update_system(cloud_pk, model_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a system
        api_response = api_instance.update_system(cloud_pk, model_pk, project_pk, uuid, patched_system_request=patched_system_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **uuid** | **str**|  |
 **patched_system_request** | [**PatchedSystemRequest**](PatchedSystemRequest.md)|  | [optional]

### Return type

[**System**](System.md)

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

# **update_zone**
> Zone update_zone(cloud_pk, id, model_pk, project_pk)

Update some fields of a zone

Update some fields of a zone. The IFC file will not be updated. The created zone will be accessible over the API and when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.patched_zone_request import PatchedZoneRequest
from bimdata_api_client.model.zone import Zone
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this zone.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_zone_request = PatchedZoneRequest(
        name="name_example",
        uuid="uuid_example",
        zones=[
            Zone(
                name="name_example",
                uuid="uuid_example",
                zones=[],
                parent_id=1,
                spaces=[
                    ZoneSpace(
                        name="name_example",
                        longname="longname_example",
                        uuid="uuid_example",
                        geometry=[
                            GeometryPoint(
                                x=3.14,
                                y=3.14,
                                z=3.14,
                            ),
                        ],
                        order=0,
                    ),
                ],
                color="color_example",
                order=0,
                storey_uuid="storey_uuid_example",
            ),
        ],
        parent_id=1,
        spaces=[
            ZoneSpaceRequest(
                name="name_example",
                longname="longname_example",
                uuid="uuid_example",
                geometry=[
                    GeometryPointRequest(
                        x=3.14,
                        y=3.14,
                        z=3.14,
                    ),
                ],
                order=0,
            ),
        ],
        color="color_example",
        order=0,
        storey_uuid="storey_uuid_example",
    ) # PatchedZoneRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a zone
        api_response = api_instance.update_zone(cloud_pk, id, model_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_zone: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a zone
        api_response = api_instance.update_zone(cloud_pk, id, model_pk, project_pk, patched_zone_request=patched_zone_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_zone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this zone. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **patched_zone_request** | [**PatchedZoneRequest**](PatchedZoneRequest.md)|  | [optional]

### Return type

[**Zone**](Zone.md)

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

# **update_zone_space**
> ZoneSpace update_zone_space(cloud_pk, id, model_pk, project_pk, zone_pk)

Update some fields of a space

Update some fields of a space. The IFC file will not be updated. The created space will be accessible over the API and when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import model_api
from bimdata_api_client.model.patched_zone_space_request import PatchedZoneSpaceRequest
from bimdata_api_client.model.zone_space import ZoneSpace
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
    api_instance = model_api.ModelApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this space.
    model_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    zone_pk = 1 # int | A unique integer value identifying this zone.
    patched_zone_space_request = PatchedZoneSpaceRequest(
        name="name_example",
        longname="longname_example",
        uuid="uuid_example",
        geometry=[
            GeometryPointRequest(
                x=3.14,
                y=3.14,
                z=3.14,
            ),
        ],
        order=0,
    ) # PatchedZoneSpaceRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a space
        api_response = api_instance.update_zone_space(cloud_pk, id, model_pk, project_pk, zone_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_zone_space: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a space
        api_response = api_instance.update_zone_space(cloud_pk, id, model_pk, project_pk, zone_pk, patched_zone_space_request=patched_zone_space_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling ModelApi->update_zone_space: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this space. |
 **model_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **zone_pk** | **int**| A unique integer value identifying this zone. |
 **patched_zone_space_request** | [**PatchedZoneSpaceRequest**](PatchedZoneSpaceRequest.md)|  | [optional]

### Return type

[**ZoneSpace**](ZoneSpace.md)

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

