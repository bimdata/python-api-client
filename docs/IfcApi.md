# bimdata_api_client.IfcApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ifc_errors_deprecated**](IfcApi.md#add_ifc_errors_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/errors | Add errors to model
[**bulk_delete_ifc_classifications_deprecated**](IfcApi.md#bulk_delete_ifc_classifications_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/list_destroy | Remove all classifications from model&#39;s elements
[**bulk_delete_ifc_properties_deprecated**](IfcApi.md#bulk_delete_ifc_properties_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/bulk_destroy | Delete many Property of a model
[**bulk_delete_ifc_property_definitions_deprecated**](IfcApi.md#bulk_delete_ifc_property_definitions_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/bulk_destroy | Delete many PropertyDefinitions of a model
[**bulk_delete_ifc_units_deprecated**](IfcApi.md#bulk_delete_ifc_units_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/bulk_destroy | Delete many Units of a model
[**bulk_delete_property_set_deprecated**](IfcApi.md#bulk_delete_property_set_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/bulk_destroy | Delete many PropertySet of a model
[**bulk_full_update_elements_deprecated**](IfcApi.md#bulk_full_update_elements_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/bulk_update | Update many elements at once (only changing fields may be defined)
[**bulk_full_update_ifc_property_deprecated**](IfcApi.md#bulk_full_update_ifc_property_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/bulk_update | Update some fields of many properties of a model
[**bulk_remove_classifications_of_element_deprecated**](IfcApi.md#bulk_remove_classifications_of_element_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification/bulk_destroy | Remove many classifications from an element
[**bulk_remove_documents_of_element_deprecated**](IfcApi.md#bulk_remove_documents_of_element_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/documents/bulk_destroy | Remove many documents from an element
[**bulk_remove_elements_from_classification_deprecated**](IfcApi.md#bulk_remove_elements_from_classification_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/{model_classification_pk}/element/bulk_destroy | Remove the classifications from all elements
[**bulk_update_elements_deprecated**](IfcApi.md#bulk_update_elements_deprecated) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/bulk_update | Update many elements at once (all field must be defined)
[**bulk_update_ifc_property_deprecated**](IfcApi.md#bulk_update_ifc_property_deprecated) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/bulk_update | Update all fields of many properties of a model
[**create_access_token_deprecated**](IfcApi.md#create_access_token_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/access_token | Create a token for this model
[**create_building_deprecated**](IfcApi.md#create_building_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/building | Create a building of a model
[**create_building_plan_deprecated**](IfcApi.md#create_building_plan_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/building/{building_uuid}/plan/add | Create a relation between a 2d model and a building
[**create_checker_deprecated**](IfcApi.md#create_checker_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker | Create a checker to a model
[**create_checker_result_deprecated**](IfcApi.md#create_checker_result_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result | Create a CheckerResult
[**create_classification_element_relations_deprecated**](IfcApi.md#create_classification_element_relations_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification-element | Create association between existing classification and existing element
[**create_classifications_of_element_deprecated**](IfcApi.md#create_classifications_of_element_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification | Create one or many classifications to an element
[**create_element_deprecated**](IfcApi.md#create_element_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element | Create an element in the model
[**create_element_property_set_deprecated**](IfcApi.md#create_element_property_set_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset | Create a PropertySets to an element
[**create_element_property_set_property_definition_deprecated**](IfcApi.md#create_element_property_set_property_definition_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition | Create a Definition to a Property
[**create_element_property_set_property_definition_unit_deprecated**](IfcApi.md#create_element_property_set_property_definition_unit_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit | Create a Unit to a Definition
[**create_element_property_set_property_deprecated**](IfcApi.md#create_element_property_set_property_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property | Create a property to a PropertySet
[**create_ifc_deprecated**](IfcApi.md#create_ifc_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/create-model | Make a PDF or Image file a Model
[**create_ifc_property_definition_deprecated**](IfcApi.md#create_ifc_property_definition_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition | Create a PropertyDefinition on the model
[**create_ifc_unit_deprecated**](IfcApi.md#create_ifc_unit_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit | Create a Unit on a model
[**create_layer_deprecated**](IfcApi.md#create_layer_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/layer | Create a layer in the model
[**create_meta_building_deprecated**](IfcApi.md#create_meta_building_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/create-metabuilding | Create an empty 3D Model
[**create_property_set_deprecated**](IfcApi.md#create_property_set_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset | Create one or many PropertySet
[**create_property_set_element_relations_deprecated**](IfcApi.md#create_property_set_element_relations_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset-element | Create association between PropertySet and element
[**create_raw_elements_deprecated**](IfcApi.md#create_raw_elements_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/raw | Create elements in an optimized format
[**create_space_deprecated**](IfcApi.md#create_space_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space | Create a space in the model
[**create_storey_deprecated**](IfcApi.md#create_storey_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/storey | Create a storey of a model
[**create_storey_plan_deprecated**](IfcApi.md#create_storey_plan_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/storey/{storey_uuid}/plan/add | Create a relation between a 2d model and a storey
[**create_system_deprecated**](IfcApi.md#create_system_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/system | Create a system in the model
[**create_zone_deprecated**](IfcApi.md#create_zone_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone | Create a zone in the model
[**create_zone_space_deprecated**](IfcApi.md#create_zone_space_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space | Create a space in a zone
[**delete_access_token_deprecated**](IfcApi.md#delete_access_token_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/access_token/{token} | Delete a token
[**delete_building_deprecated**](IfcApi.md#delete_building_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/building/{uuid} | Delete a building of a model
[**delete_building_plan_deprecated**](IfcApi.md#delete_building_plan_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/building/{building_uuid}/plan/{id} | Delete the relation between a 2d model and a building
[**delete_checker_deprecated**](IfcApi.md#delete_checker_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id} | Delete a checker of a model
[**delete_checker_result_deprecated**](IfcApi.md#delete_checker_result_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result/{id} | Delete a CheckerResult
[**delete_element_deprecated**](IfcApi.md#delete_element_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | Delete an element of a model
[**delete_ifc_deprecated**](IfcApi.md#delete_ifc_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | Delete a model
[**delete_ifc_property_definition_deprecated**](IfcApi.md#delete_ifc_property_definition_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | Delete a PropertyDefinitions of a model
[**delete_ifc_property_deprecated**](IfcApi.md#delete_ifc_property_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | Delete a Property of a model
[**delete_ifc_unit_deprecated**](IfcApi.md#delete_ifc_unit_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | Delete a Unit of a model
[**delete_ifc_without_doc_deprecated**](IfcApi.md#delete_ifc_without_doc_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/delete-model | Delete the Model without deleting the related document
[**delete_layer_deprecated**](IfcApi.md#delete_layer_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/layer/{id} | Delete a layer of a model
[**delete_property_set_deprecated**](IfcApi.md#delete_property_set_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | Delete a PropertySet of a model
[**delete_space_deprecated**](IfcApi.md#delete_space_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | Delete a space
[**delete_storey_deprecated**](IfcApi.md#delete_storey_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/storey/{uuid} | Delete a storey of a model
[**delete_storey_plan_deprecated**](IfcApi.md#delete_storey_plan_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/storey/{storey_uuid}/plan/{id} | Delete the relation between a 2d model and a storey
[**delete_system_deprecated**](IfcApi.md#delete_system_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/system/{uuid} | Delete a system of a model
[**delete_zone_deprecated**](IfcApi.md#delete_zone_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | Delete a zone of a model
[**delete_zone_space_deprecated**](IfcApi.md#delete_zone_space_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | Delete a space of a zone
[**export_ifc_deprecated**](IfcApi.md#export_ifc_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/export | Export IFC
[**full_update_element_deprecated**](IfcApi.md#full_update_element_deprecated) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | Update all fields of an element
[**get_access_token_deprecated**](IfcApi.md#get_access_token_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/access_token/{token} | Retrieve one token created for this model
[**get_access_tokens_deprecated**](IfcApi.md#get_access_tokens_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/access_token | Retrieve all tokens created for this model
[**get_building_deprecated**](IfcApi.md#get_building_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/building/{uuid} | Retrieve a building of a model
[**get_building_plan_positioning_deprecated**](IfcApi.md#get_building_plan_positioning_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/building/{building_uuid}/plan/{id}/positioning | Retrieve the postioning of the plan in the building
[**get_buildings_deprecated**](IfcApi.md#get_buildings_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/building | Retrieve all buildings of a model
[**get_checker_deprecated**](IfcApi.md#get_checker_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id} | Retrieve a checker of a model
[**get_checker_result_deprecated**](IfcApi.md#get_checker_result_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result/{id} | Retrieve one CheckerResult
[**get_checker_results_deprecated**](IfcApi.md#get_checker_results_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result | Retrieve all CheckerResults
[**get_checkers_deprecated**](IfcApi.md#get_checkers_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker | Retrieve all checkers of a model
[**get_classifications_of_element_deprecated**](IfcApi.md#get_classifications_of_element_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification | Retrieve all classifications of an element
[**get_documents_of_element_deprecated**](IfcApi.md#get_documents_of_element_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/documents | Retrieve all documents of an element
[**get_element_deprecated**](IfcApi.md#get_element_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | Retrieve an element of a model
[**get_element_linked_documents_deprecated**](IfcApi.md#get_element_linked_documents_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/documents | Retrieve all documents linked to any element
[**get_element_property_set_deprecated**](IfcApi.md#get_element_property_set_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{id} | Retrieve a PropertySet of an element
[**get_element_property_set_properties_deprecated**](IfcApi.md#get_element_property_set_properties_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property | Retrieve all Properties of a PropertySet
[**get_element_property_set_property_definition_deprecated**](IfcApi.md#get_element_property_set_property_definition_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{id} | Retrieve a Definition of a Property
[**get_element_property_set_property_definition_unit_deprecated**](IfcApi.md#get_element_property_set_property_definition_unit_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit/{id} | Retrieve a Unit of a Definition
[**get_element_property_set_property_definition_units_deprecated**](IfcApi.md#get_element_property_set_property_definition_units_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit | Retrieve all Units of a Definition
[**get_element_property_set_property_definitions_deprecated**](IfcApi.md#get_element_property_set_property_definitions_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition | Retrieve all Definitions of a PropertySet
[**get_element_property_set_property_deprecated**](IfcApi.md#get_element_property_set_property_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{id} | Retrieve a Property of a PropertySet
[**get_element_property_sets_deprecated**](IfcApi.md#get_element_property_sets_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset | Retrieve all PropertySets of an element
[**get_elements_deprecated**](IfcApi.md#get_elements_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element | Retrieve all elements of a model
[**get_elements_from_classification_deprecated**](IfcApi.md#get_elements_from_classification_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/{model_classification_pk}/element | Retrieve all elements with the classification
[**get_ifc_classifications_deprecated**](IfcApi.md#get_ifc_classifications_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification | Retrieve all classifications in a model
[**get_ifc_deprecated**](IfcApi.md#get_ifc_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | Retrieve one model
[**get_ifc_material_deprecated**](IfcApi.md#get_ifc_material_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/material/{id} | Retrieve a material of a model
[**get_ifc_materials_deprecated**](IfcApi.md#get_ifc_materials_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/material | Retrieve all materials of a model
[**get_ifc_properties_deprecated**](IfcApi.md#get_ifc_properties_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property | Retrieve all Properties of a model
[**get_ifc_property_definition_deprecated**](IfcApi.md#get_ifc_property_definition_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | Retrieve a PropertyDefinition of a model
[**get_ifc_property_definitions_deprecated**](IfcApi.md#get_ifc_property_definitions_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition | Retrieve all PropertyDefinitions of a model
[**get_ifc_property_deprecated**](IfcApi.md#get_ifc_property_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | Retrieve a Property of a model
[**get_ifc_unit_deprecated**](IfcApi.md#get_ifc_unit_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | Retrieve a Unit of a model
[**get_ifc_units_deprecated**](IfcApi.md#get_ifc_units_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit | Retrieve all Units of a model
[**get_ifcs_deprecated**](IfcApi.md#get_ifcs_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc | Retrieve all models
[**get_layer_deprecated**](IfcApi.md#get_layer_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/layer/{id} | Retrieve a layer of a model
[**get_layers_deprecated**](IfcApi.md#get_layers_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/layer | Retrieve all layers of a model
[**get_material_deprecated**](IfcApi.md#get_material_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/material/{id} | Retrieve a material of a model
[**get_materials_deprecated**](IfcApi.md#get_materials_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/material | Retrieve all materials of a model
[**get_processor_handler_deprecated**](IfcApi.md#get_processor_handler_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/processorhandler/{id} | Retrieve a processor handler
[**get_processor_handlers_deprecated**](IfcApi.md#get_processor_handlers_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/processorhandler | Get all processor handlers
[**get_property_set_deprecated**](IfcApi.md#get_property_set_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | Retrieve a PropertySet of a model
[**get_property_sets_deprecated**](IfcApi.md#get_property_sets_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset | Retrieve all PropertySets of a model
[**get_raw_elements_deprecated**](IfcApi.md#get_raw_elements_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/raw | Retrieve all elements in a optimized format
[**get_simple_element_deprecated**](IfcApi.md#get_simple_element_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid}/simple | Retrieve an element of a model with a simple value representation
[**get_simple_elements_deprecated**](IfcApi.md#get_simple_elements_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/simple | Retrieve all elements of a model with a simple value representation
[**get_space_deprecated**](IfcApi.md#get_space_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | Retrieve one space of the model
[**get_spaces_deprecated**](IfcApi.md#get_spaces_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space | Retrieve all spaces of the model
[**get_storey_deprecated**](IfcApi.md#get_storey_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/storey/{uuid} | Retrieve a storey of a model
[**get_storey_plan_positioning_deprecated**](IfcApi.md#get_storey_plan_positioning_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/storey/{storey_uuid}/plan/{id}/positioning | Retrieve the postioning of the plan in the storey
[**get_storeys_deprecated**](IfcApi.md#get_storeys_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/storey | Retrieve all storeys of a model
[**get_system_deprecated**](IfcApi.md#get_system_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/system/{uuid} | Retrieve a system of a model
[**get_systems_deprecated**](IfcApi.md#get_systems_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/system | Retrieve all systems of a model
[**get_zone_deprecated**](IfcApi.md#get_zone_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | Retrieve one zone of a model
[**get_zone_space_deprecated**](IfcApi.md#get_zone_space_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | Retrieve one space of a zone
[**get_zone_spaces_deprecated**](IfcApi.md#get_zone_spaces_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space | Retrieve all spaces of a zone
[**get_zones_deprecated**](IfcApi.md#get_zones_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone | Retrieve zones of a model
[**launch_new_check_deprecated**](IfcApi.md#launch_new_check_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id}/launch-check | Launch a new check on the model
[**link_documents_of_element_deprecated**](IfcApi.md#link_documents_of_element_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/documents | Link one or many documents to an element
[**list_classification_element_relations_deprecated**](IfcApi.md#list_classification_element_relations_deprecated) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification-element | List all associations between classifications and elements
[**merge_ifcs_deprecated**](IfcApi.md#merge_ifcs_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/merge | Merge IFC files
[**optimize_ifc_deprecated**](IfcApi.md#optimize_ifc_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/optimize | Optimize the IFC
[**remove_all_element_property_set_deprecated**](IfcApi.md#remove_all_element_property_set_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/all | Remove all property sets from element
[**remove_classification_of_element_deprecated**](IfcApi.md#remove_classification_of_element_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification/{id} | Remove a classification from an element
[**remove_document_of_element_deprecated**](IfcApi.md#remove_document_of_element_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/documents/{id} | Remove a documents from an element
[**remove_element_property_set_deprecated**](IfcApi.md#remove_element_property_set_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{id} | Remove a PropertySet from an element
[**remove_element_property_set_property_definition_deprecated**](IfcApi.md#remove_element_property_set_property_definition_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{id} | Delete a Definition to a Property
[**remove_element_property_set_property_definition_unit_deprecated**](IfcApi.md#remove_element_property_set_property_definition_unit_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit/{id} | Remove a Unit from a Definition
[**remove_element_property_set_property_deprecated**](IfcApi.md#remove_element_property_set_property_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{id} | Remove a property from a PropertySet
[**remove_elements_from_classification_deprecated**](IfcApi.md#remove_elements_from_classification_deprecated) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/{model_classification_pk}/element/{uuid} | Remove the classification from all elements
[**reprocess_ifc_deprecated**](IfcApi.md#reprocess_ifc_deprecated) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/reprocess | Reprocess Model file
[**update_access_token_deprecated**](IfcApi.md#update_access_token_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/access_token/{token} | Update some fields of a token
[**update_building_deprecated**](IfcApi.md#update_building_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/building/{uuid} | Update some fields of a building
[**update_building_plan_positioning_deprecated**](IfcApi.md#update_building_plan_positioning_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/building/{building_uuid}/plan/{id}/positioning | Update the postioning of the plan in the building
[**update_checker_deprecated**](IfcApi.md#update_checker_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id} | Update some fields of a checker of a model
[**update_checker_result_deprecated**](IfcApi.md#update_checker_result_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result/{id} | Update some fields of a CheckerResult
[**update_element_deprecated**](IfcApi.md#update_element_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | Update some fields of an element
[**update_element_property_set_property_deprecated**](IfcApi.md#update_element_property_set_property_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{id} | Update a property from an element
[**update_ifc_deprecated**](IfcApi.md#update_ifc_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | Update some fields of a model
[**update_ifc_files_deprecated**](IfcApi.md#update_ifc_files_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/files | Update models file (gltf, svg, structure, etc)
[**update_ifc_property_definition_deprecated**](IfcApi.md#update_ifc_property_definition_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | Update some fields of many PropertyDefinitions of a model
[**update_ifc_property_deprecated**](IfcApi.md#update_ifc_property_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | Update some fields of a Property
[**update_ifc_unit_deprecated**](IfcApi.md#update_ifc_unit_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | Update some fields of a Unit of a model
[**update_layer_deprecated**](IfcApi.md#update_layer_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/layer/{id} | Update some fields of a layer
[**update_order_building_plan_deprecated**](IfcApi.md#update_order_building_plan_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/building/{building_uuid}/plan/order | Update order of all plan of a building
[**update_order_storey_plan_deprecated**](IfcApi.md#update_order_storey_plan_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/storey/{storey_uuid}/plan/order | Update order of all plan of a storey
[**update_order_storeys_deprecated**](IfcApi.md#update_order_storeys_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/storey/order | Update order of all storey of a model
[**update_processor_handler_deprecated**](IfcApi.md#update_processor_handler_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/processorhandler/{id} | Update the status of a processor handler
[**update_property_set_deprecated**](IfcApi.md#update_property_set_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | Update some fields of a PropertySet
[**update_space_deprecated**](IfcApi.md#update_space_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | Update some fields of a space
[**update_storey_deprecated**](IfcApi.md#update_storey_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/storey/{uuid} | Update some fields of a storey
[**update_storey_plan_positioning_deprecated**](IfcApi.md#update_storey_plan_positioning_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/storey/{storey_uuid}/plan/{id}/positioning | Update the postioning of the plan in the storey
[**update_system_deprecated**](IfcApi.md#update_system_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/system/{uuid} | Update some fields of a system
[**update_zone_deprecated**](IfcApi.md#update_zone_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | Update some fields of a zone
[**update_zone_space_deprecated**](IfcApi.md#update_zone_space_deprecated) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | Update some fields of a space


# **add_ifc_errors_deprecated**
> ModelErrors add_ifc_errors_deprecated(cloud_pk, id, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
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
        api_response = api_instance.add_ifc_errors_deprecated(cloud_pk, id, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->add_ifc_errors_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add errors to model
        api_response = api_instance.add_ifc_errors_deprecated(cloud_pk, id, project_pk, model_errors_request=model_errors_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->add_ifc_errors_deprecated: %s\n" % e)
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

# **bulk_delete_ifc_classifications_deprecated**
> bulk_delete_ifc_classifications_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    ifc_pk = 1 # int | 
    project_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Remove all classifications from model's elements
        api_instance.bulk_delete_ifc_classifications_deprecated(cloud_pk, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->bulk_delete_ifc_classifications_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **ifc_pk** | **int**|  |
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

# **bulk_delete_ifc_properties_deprecated**
> bulk_delete_ifc_properties_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete many Property of a model
        api_instance.bulk_delete_ifc_properties_deprecated(cloud_pk, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->bulk_delete_ifc_properties_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **bulk_delete_ifc_property_definitions_deprecated**
> bulk_delete_ifc_property_definitions_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete many PropertyDefinitions of a model
        api_instance.bulk_delete_ifc_property_definitions_deprecated(cloud_pk, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->bulk_delete_ifc_property_definitions_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **bulk_delete_ifc_units_deprecated**
> bulk_delete_ifc_units_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete many Units of a model
        api_instance.bulk_delete_ifc_units_deprecated(cloud_pk, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->bulk_delete_ifc_units_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **bulk_delete_property_set_deprecated**
> bulk_delete_property_set_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete many PropertySet of a model
        api_instance.bulk_delete_property_set_deprecated(cloud_pk, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->bulk_delete_property_set_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **bulk_full_update_elements_deprecated**
> [Element] bulk_full_update_elements_deprecated(cloud_pk, ifc_pk, project_pk, element_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
                        value={
                            "key": None,
                        },
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
                            value={
                                "key": None,
                            },
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
        api_response = api_instance.bulk_full_update_elements_deprecated(cloud_pk, ifc_pk, project_pk, element_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->bulk_full_update_elements_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update many elements at once (only changing fields may be defined)
        api_response = api_instance.bulk_full_update_elements_deprecated(cloud_pk, ifc_pk, project_pk, element_request, classification=classification, classification__notation=classification__notation, type=type)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->bulk_full_update_elements_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **bulk_full_update_ifc_property_deprecated**
> [ModelProperty] bulk_full_update_ifc_property_deprecated(cloud_pk, ifc_pk, project_pk, property_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
            value={
                "key": None,
            },
        ),
    ] # [PropertyRequest] | 

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of many properties of a model
        api_response = api_instance.bulk_full_update_ifc_property_deprecated(cloud_pk, ifc_pk, project_pk, property_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->bulk_full_update_ifc_property_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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
**400** | All updates failed: list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_remove_classifications_of_element_deprecated**
> bulk_remove_classifications_of_element_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Remove many classifications from an element
        api_instance.bulk_remove_classifications_of_element_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->bulk_remove_classifications_of_element_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **bulk_remove_documents_of_element_deprecated**
> bulk_remove_documents_of_element_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Remove many documents from an element
        api_instance.bulk_remove_documents_of_element_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->bulk_remove_documents_of_element_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **bulk_remove_elements_from_classification_deprecated**
> bulk_remove_elements_from_classification_deprecated(cloud_pk, ifc_pk, model_classification_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
    model_classification_pk = 1 # int | A unique integer value identifying this classification.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Remove the classifications from all elements
        api_instance.bulk_remove_elements_from_classification_deprecated(cloud_pk, ifc_pk, model_classification_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->bulk_remove_elements_from_classification_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
 **model_classification_pk** | **int**| A unique integer value identifying this classification. |
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

# **bulk_update_elements_deprecated**
> [Element] bulk_update_elements_deprecated(cloud_pk, ifc_pk, project_pk, element_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
                        value={
                            "key": None,
                        },
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
                            value={
                                "key": None,
                            },
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
        api_response = api_instance.bulk_update_elements_deprecated(cloud_pk, ifc_pk, project_pk, element_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->bulk_update_elements_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update many elements at once (all field must be defined)
        api_response = api_instance.bulk_update_elements_deprecated(cloud_pk, ifc_pk, project_pk, element_request, classification=classification, classification__notation=classification__notation, type=type)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->bulk_update_elements_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **bulk_update_ifc_property_deprecated**
> [ModelProperty] bulk_update_ifc_property_deprecated(cloud_pk, ifc_pk, project_pk, property_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
            value={
                "key": None,
            },
        ),
    ] # [PropertyRequest] | 

    # example passing only required values which don't have defaults set
    try:
        # Update all fields of many properties of a model
        api_response = api_instance.bulk_update_ifc_property_deprecated(cloud_pk, ifc_pk, project_pk, property_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->bulk_update_ifc_property_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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
**400** | All updates failed: list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_access_token_deprecated**
> IfcAccessToken create_access_token_deprecated(cloud_pk, ifc_pk, project_pk)

Create a token for this model

Tokens are read_only by default and are valid 1 day  Required scopes: ifc:token_manage, model:token_manage

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    ifc_access_token_request = IfcAccessTokenRequest(
        read_only=True,
        expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # IfcAccessTokenRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a token for this model
        api_response = api_instance.create_access_token_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_access_token_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a token for this model
        api_response = api_instance.create_access_token_deprecated(cloud_pk, ifc_pk, project_pk, ifc_access_token_request=ifc_access_token_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_access_token_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_building_deprecated**
> Building create_building_deprecated(cloud_pk, ifc_pk, project_pk, storey_building_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    storey_building_request = StoreyBuildingRequest(
        name="name_example",
    ) # StoreyBuildingRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a building of a model
        api_response = api_instance.create_building_deprecated(cloud_pk, ifc_pk, project_pk, storey_building_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_building_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_building_plan_deprecated**
> Building create_building_plan_deprecated(building_uuid, cloud_pk, ifc_pk, project_pk, building_model_plan_request)

Create a relation between a 2d model and a building

Create a relation between a 2d model and a building. The model type must be one of : ('DWG', 'DXF', 'PDF', 'JPEG', 'PNG')  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    building_uuid = "building_uuid_example" # str | 
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    building_model_plan_request = BuildingModelPlanRequest(
        id=1,
    ) # BuildingModelPlanRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a relation between a 2d model and a building
        api_response = api_instance.create_building_plan_deprecated(building_uuid, cloud_pk, ifc_pk, project_pk, building_model_plan_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_building_plan_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_uuid** | **str**|  |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_checker_deprecated**
> IfcChecker create_checker_deprecated(cloud_pk, ifc_pk, project_pk)

Create a checker to a model

A checker is a link between a checkplan and a model. A checker can launch a check multiple time and store all the results  Required scopes: check:write, ifc:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
from bimdata_api_client.model.ifc_checker import IfcChecker
from bimdata_api_client.model.ifc_checker_request import IfcCheckerRequest
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    ifc_checker_request = IfcCheckerRequest(
        name="name_example",
        checkplan_id=1,
    ) # IfcCheckerRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a checker to a model
        api_response = api_instance.create_checker_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_checker_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a checker to a model
        api_response = api_instance.create_checker_deprecated(cloud_pk, ifc_pk, project_pk, ifc_checker_request=ifc_checker_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_checker_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **ifc_checker_request** | [**IfcCheckerRequest**](IfcCheckerRequest.md)|  | [optional]

### Return type

[**IfcChecker**](IfcChecker.md)

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

# **create_checker_result_deprecated**
> CheckerResult create_checker_result_deprecated(checker_pk, cloud_pk, ifc_pk, project_pk)

Create a CheckerResult

TCreate a CheckerResult  Required scopes: check:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
from bimdata_api_client.model.checker_result_request import CheckerResultRequest
from bimdata_api_client.model.checker_result import CheckerResult
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
    api_instance = ifc_api.IfcApi(api_client)
    checker_pk = 1 # int | A unique integer value identifying this ifc checker.
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    checker_result_request = CheckerResultRequest(
        status="C",
        result="result_example",
        collisions="collisions_example",
        error_detail="error_detail_example",
    ) # CheckerResultRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a CheckerResult
        api_response = api_instance.create_checker_result_deprecated(checker_pk, cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_checker_result_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a CheckerResult
        api_response = api_instance.create_checker_result_deprecated(checker_pk, cloud_pk, ifc_pk, project_pk, checker_result_request=checker_result_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_checker_result_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checker_pk** | **int**| A unique integer value identifying this ifc checker. |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **checker_result_request** | [**CheckerResultRequest**](CheckerResultRequest.md)|  | [optional]

### Return type

[**CheckerResult**](CheckerResult.md)

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

# **create_classification_element_relations_deprecated**
> create_classification_element_relations_deprecated(cloud_pk, ifc_pk, project_pk, element_classification_relation_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        api_instance.create_classification_element_relations_deprecated(cloud_pk, ifc_pk, project_pk, element_classification_relation_request)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_classification_element_relations_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_classifications_of_element_deprecated**
> [Classification] create_classifications_of_element_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, classification_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        api_response = api_instance.create_classifications_of_element_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, classification_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_classifications_of_element_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_element_deprecated**
> [Element] create_element_deprecated(cloud_pk, ifc_pk, project_pk, element_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
                        value={
                            "key": None,
                        },
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
                            value={
                                "key": None,
                            },
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
        api_response = api_instance.create_element_deprecated(cloud_pk, ifc_pk, project_pk, element_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_element_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an element in the model
        api_response = api_instance.create_element_deprecated(cloud_pk, ifc_pk, project_pk, element_request, classification=classification, classification__notation=classification__notation, type=type)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_element_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_element_property_set_deprecated**
> PropertySet create_element_property_set_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | 
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
                value={
                    "key": None,
                },
            ),
        ],
    ) # PropertySetRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a PropertySets to an element
        api_response = api_instance.create_element_property_set_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_element_property_set_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a PropertySets to an element
        api_response = api_instance.create_element_property_set_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, property_set_request=property_set_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_element_property_set_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**|  |
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

# **create_element_property_set_property_definition_deprecated**
> PropertyDefinition create_element_property_set_property_definition_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        api_response = api_instance.create_element_property_set_property_definition_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_element_property_set_property_definition_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Definition to a Property
        api_response = api_instance.create_element_property_set_property_definition_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk, property_definition_request=property_definition_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_element_property_set_property_definition_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_element_property_set_property_definition_unit_deprecated**
> Unit create_element_property_set_property_definition_unit_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk, unit_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        conversion_baseunit=UnitRequest(),
        elements={
            "key": None,
        },
        is_default=True,
    ) # UnitRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Unit to a Definition
        api_response = api_instance.create_element_property_set_property_definition_unit_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk, unit_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_element_property_set_property_definition_unit_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_element_property_set_property_deprecated**
> ModelProperty create_element_property_set_property_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk, property_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        value={
            "key": None,
        },
    ) # PropertyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a property to a PropertySet
        api_response = api_instance.create_element_property_set_property_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk, property_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_element_property_set_property_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_ifc_deprecated**
> Model create_ifc_deprecated(cloud_pk, project_pk, create_model_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    project_pk = 1 # int | 
    create_model_request = CreateModelRequest(
        document_id=1,
    ) # CreateModelRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Make a PDF or Image file a Model
        api_response = api_instance.create_ifc_deprecated(cloud_pk, project_pk, create_model_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_ifc_deprecated: %s\n" % e)
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

# **create_ifc_property_definition_deprecated**
> [PropertyDefinition] create_ifc_property_definition_deprecated(cloud_pk, ifc_pk, project_pk, property_definition_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        api_response = api_instance.create_ifc_property_definition_deprecated(cloud_pk, ifc_pk, project_pk, property_definition_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_ifc_property_definition_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_ifc_unit_deprecated**
> [Unit] create_ifc_unit_deprecated(cloud_pk, ifc_pk, project_pk, unit_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
            conversion_baseunit=UnitRequest(),
            elements={
                "key": None,
            },
            is_default=True,
        ),
    ] # [UnitRequest] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Unit on a model
        api_response = api_instance.create_ifc_unit_deprecated(cloud_pk, ifc_pk, project_pk, unit_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_ifc_unit_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_layer_deprecated**
> Layer create_layer_deprecated(cloud_pk, ifc_pk, project_pk, layer_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        api_response = api_instance.create_layer_deprecated(cloud_pk, ifc_pk, project_pk, layer_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_layer_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_meta_building_deprecated**
> Model create_meta_building_deprecated(cloud_pk, project_pk, create_building_by_name_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    project_pk = 1 # int | 
    create_building_by_name_request = CreateBuildingByNameRequest(
        name="name_example",
    ) # CreateBuildingByNameRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create an empty 3D Model
        api_response = api_instance.create_meta_building_deprecated(cloud_pk, project_pk, create_building_by_name_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_meta_building_deprecated: %s\n" % e)
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

# **create_property_set_deprecated**
> [PropertySet] create_property_set_deprecated(cloud_pk, ifc_pk, project_pk, property_set_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
                    value={
                        "key": None,
                    },
                ),
            ],
        ),
    ] # [PropertySetRequest] | 

    # example passing only required values which don't have defaults set
    try:
        # Create one or many PropertySet
        api_response = api_instance.create_property_set_deprecated(cloud_pk, ifc_pk, project_pk, property_set_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_property_set_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_property_set_element_relations_deprecated**
> create_property_set_element_relations_deprecated(cloud_pk, ifc_pk, project_pk, element_property_set_relation_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        api_instance.create_property_set_element_relations_deprecated(cloud_pk, ifc_pk, project_pk, element_property_set_relation_request)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_property_set_element_relations_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_raw_elements_deprecated**
> create_raw_elements_deprecated(cloud_pk, ifc_pk, project_pk, raw_elements_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    raw_elements_request = RawElementsRequest(
        units=[
            RawUnitRequest(
                name="name_example",
                type="type_example",
                unit_type="unit_type_example",
                prefix="prefix_example",
                elements={
                    "key": None,
                },
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
                        value={
                            "key": None,
                        },
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
        api_instance.create_raw_elements_deprecated(cloud_pk, ifc_pk, project_pk, raw_elements_request)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_raw_elements_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_space_deprecated**
> [Space] create_space_deprecated(cloud_pk, ifc_pk, project_pk, space_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    space_request = [
        SpaceRequest(
            name="name_example",
            longname="longname_example",
            uuid="uuid_example",
        ),
    ] # [SpaceRequest] | 

    # example passing only required values which don't have defaults set
    try:
        # Create a space in the model
        api_response = api_instance.create_space_deprecated(cloud_pk, ifc_pk, project_pk, space_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_space_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_storey_deprecated**
> Storey create_storey_deprecated(cloud_pk, ifc_pk, project_pk, storey_building_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    storey_building_request = StoreyBuildingRequest(
        name="name_example",
    ) # StoreyBuildingRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a storey of a model
        api_response = api_instance.create_storey_deprecated(cloud_pk, ifc_pk, project_pk, storey_building_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_storey_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_storey_plan_deprecated**
> Storey create_storey_plan_deprecated(cloud_pk, ifc_pk, project_pk, storey_uuid, storey_model_plan_request)

Create a relation between a 2d model and a storey

Create a relation between a 2d model and a storey. The model type must be one of : ('DWG', 'DXF', 'PDF', 'JPEG', 'PNG')  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    storey_uuid = "storey_uuid_example" # str | 
    storey_model_plan_request = StoreyModelPlanRequest(
        id=1,
    ) # StoreyModelPlanRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a relation between a 2d model and a storey
        api_response = api_instance.create_storey_plan_deprecated(cloud_pk, ifc_pk, project_pk, storey_uuid, storey_model_plan_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_storey_plan_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_system_deprecated**
> System create_system_deprecated(cloud_pk, ifc_pk, project_pk, system_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        api_response = api_instance.create_system_deprecated(cloud_pk, ifc_pk, project_pk, system_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_system_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_zone_deprecated**
> [Zone] create_zone_deprecated(cloud_pk, ifc_pk, project_pk, zone_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    zone_request = [
        ZoneRequest(
            name="name_example",
            uuid="uuid_example",
            zones=[],
            parent_id=1,
            spaces=[
                SpaceRequest(
                    name="name_example",
                    longname="longname_example",
                    uuid="uuid_example",
                ),
            ],
            color="color_example",
        ),
    ] # [ZoneRequest] | 
    color = "color_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a zone in the model
        api_response = api_instance.create_zone_deprecated(cloud_pk, ifc_pk, project_pk, zone_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_zone_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a zone in the model
        api_response = api_instance.create_zone_deprecated(cloud_pk, ifc_pk, project_pk, zone_request, color=color)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_zone_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **create_zone_space_deprecated**
> ZoneSpace create_zone_space_deprecated(cloud_pk, ifc_pk, project_pk, zone_pk, zone_space_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    zone_pk = 1 # int | A unique integer value identifying this zone.
    zone_space_request = ZoneSpaceRequest(
        name="name_example",
        longname="longname_example",
        uuid="uuid_example",
    ) # ZoneSpaceRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a space in a zone
        api_response = api_instance.create_zone_space_deprecated(cloud_pk, ifc_pk, project_pk, zone_pk, zone_space_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->create_zone_space_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_access_token_deprecated**
> delete_access_token_deprecated(cloud_pk, ifc_pk, project_pk, token)

Delete a token

Deleting a token will revoke it.  Required scopes: ifc:token_manage, model:token_manage

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    token = "token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a token
        api_instance.delete_access_token_deprecated(cloud_pk, ifc_pk, project_pk, token)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_access_token_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_building_deprecated**
> delete_building_deprecated(cloud_pk, ifc_pk, project_pk, uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a building of a model
        api_instance.delete_building_deprecated(cloud_pk, ifc_pk, project_pk, uuid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_building_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_building_plan_deprecated**
> delete_building_plan_deprecated(building_uuid, cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    building_uuid = "building_uuid_example" # str | 
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this element.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete the relation between a 2d model and a building
        api_instance.delete_building_plan_deprecated(building_uuid, cloud_pk, id, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_building_plan_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_uuid** | **str**|  |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this element. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_checker_deprecated**
> delete_checker_deprecated(cloud_pk, id, ifc_pk, project_pk)

Delete a checker of a model

A checker is a link between a checkplan and a model. A checker can launch a check multiple time and store all the results  Required scopes: check:write, ifc:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this ifc checker.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a checker of a model
        api_instance.delete_checker_deprecated(cloud_pk, id, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_checker_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this ifc checker. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_checker_result_deprecated**
> delete_checker_result_deprecated(checker_pk, cloud_pk, id, ifc_pk, project_pk)

Delete a CheckerResult

Delete a CheckerResult  Required scopes: check:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    checker_pk = 1 # int | A unique integer value identifying this ifc checker.
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this checker result.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a CheckerResult
        api_instance.delete_checker_result_deprecated(checker_pk, cloud_pk, id, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_checker_result_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checker_pk** | **int**| A unique integer value identifying this ifc checker. |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this checker result. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_element_deprecated**
> delete_element_deprecated(cloud_pk, ifc_pk, project_pk, uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an element of a model
        api_instance.delete_element_deprecated(cloud_pk, ifc_pk, project_pk, uuid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_element_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_ifc_deprecated**
> delete_ifc_deprecated(cloud_pk, id, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a model
        api_instance.delete_ifc_deprecated(cloud_pk, id, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_ifc_deprecated: %s\n" % e)
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

# **delete_ifc_property_definition_deprecated**
> delete_ifc_property_definition_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property definition.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a PropertyDefinitions of a model
        api_instance.delete_ifc_property_definition_deprecated(cloud_pk, id, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_ifc_property_definition_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property definition. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_ifc_property_deprecated**
> delete_ifc_property_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Property of a model
        api_instance.delete_ifc_property_deprecated(cloud_pk, id, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_ifc_property_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_ifc_unit_deprecated**
> delete_ifc_unit_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this unit.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Unit of a model
        api_instance.delete_ifc_unit_deprecated(cloud_pk, id, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_ifc_unit_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this unit. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_ifc_without_doc_deprecated**
> delete_ifc_without_doc_deprecated(cloud_pk, id, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the Model without deleting the related document
        api_instance.delete_ifc_without_doc_deprecated(cloud_pk, id, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_ifc_without_doc_deprecated: %s\n" % e)
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

# **delete_layer_deprecated**
> delete_layer_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this layer.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a layer of a model
        api_instance.delete_layer_deprecated(cloud_pk, id, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_layer_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this layer. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_property_set_deprecated**
> delete_property_set_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property set.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a PropertySet of a model
        api_instance.delete_property_set_deprecated(cloud_pk, id, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_property_set_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property set. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_space_deprecated**
> delete_space_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this space.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a space
        api_instance.delete_space_deprecated(cloud_pk, id, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_space_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this space. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_storey_deprecated**
> delete_storey_deprecated(cloud_pk, ifc_pk, project_pk, uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a storey of a model
        api_instance.delete_storey_deprecated(cloud_pk, ifc_pk, project_pk, uuid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_storey_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_storey_plan_deprecated**
> delete_storey_plan_deprecated(cloud_pk, id, ifc_pk, project_pk, storey_uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this element.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    storey_uuid = "storey_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete the relation between a 2d model and a storey
        api_instance.delete_storey_plan_deprecated(cloud_pk, id, ifc_pk, project_pk, storey_uuid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_storey_plan_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this element. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_system_deprecated**
> delete_system_deprecated(cloud_pk, ifc_pk, project_pk, uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a system of a model
        api_instance.delete_system_deprecated(cloud_pk, ifc_pk, project_pk, uuid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_system_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_zone_deprecated**
> delete_zone_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this zone.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Delete a zone of a model
        api_instance.delete_zone_deprecated(cloud_pk, id, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_zone_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this zone. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **delete_zone_space_deprecated**
> delete_zone_space_deprecated(cloud_pk, id, ifc_pk, project_pk, zone_pk)

Delete a space of a zone

The IFC file will not be updated. The remaining spaces are available in API and will be available when exporting an IFC file  Required scopes: ifc:write, model:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this space.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    zone_pk = 1 # int | A unique integer value identifying this zone.

    # example passing only required values which don't have defaults set
    try:
        # Delete a space of a zone
        api_instance.delete_zone_space_deprecated(cloud_pk, id, ifc_pk, project_pk, zone_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->delete_zone_space_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this space. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **export_ifc_deprecated**
> IfcExport export_ifc_deprecated(cloud_pk, id, project_pk, ifc_export_request)

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
from bimdata_api_client.api import ifc_api
from bimdata_api_client.model.ifc_export_request import IfcExportRequest
from bimdata_api_client.model.ifc_export import IfcExport
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
    api_instance = ifc_api.IfcApi(api_client)
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
        api_response = api_instance.export_ifc_deprecated(cloud_pk, id, project_pk, ifc_export_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->export_ifc_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **id** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**|  |
 **ifc_export_request** | [**IfcExportRequest**](IfcExportRequest.md)|  |

### Return type

[**IfcExport**](IfcExport.md)

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

# **full_update_element_deprecated**
> Element full_update_element_deprecated(cloud_pk, ifc_pk, project_pk, uuid, element_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
                    value={
                        "key": None,
                    },
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
                        value={
                            "key": None,
                        },
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
        api_response = api_instance.full_update_element_deprecated(cloud_pk, ifc_pk, project_pk, uuid, element_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->full_update_element_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_access_token_deprecated**
> IfcAccessToken get_access_token_deprecated(cloud_pk, ifc_pk, project_pk, token)

Retrieve one token created for this model

Retrieve one token created for this model  Required scopes: ifc:token_manage, model:token_manage

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    token = "token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve one token created for this model
        api_response = api_instance.get_access_token_deprecated(cloud_pk, ifc_pk, project_pk, token)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_access_token_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_access_tokens_deprecated**
> [IfcAccessToken] get_access_tokens_deprecated(cloud_pk, ifc_pk, project_pk)

Retrieve all tokens created for this model

Retrieve all tokens created for this model  Required scopes: ifc:token_manage, model:token_manage

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all tokens created for this model
        api_response = api_instance.get_access_tokens_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_access_tokens_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_building_deprecated**
> Building get_building_deprecated(cloud_pk, ifc_pk, project_pk, uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a building of a model
        api_response = api_instance.get_building_deprecated(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_building_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_building_plan_positioning_deprecated**
> PositioningPlan get_building_plan_positioning_deprecated(building_uuid, cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    building_uuid = "building_uuid_example" # str | 
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this element.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the postioning of the plan in the building
        api_response = api_instance.get_building_plan_positioning_deprecated(building_uuid, cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_building_plan_positioning_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_uuid** | **str**|  |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this element. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_buildings_deprecated**
> [Building] get_buildings_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all buildings of a model
        api_response = api_instance.get_buildings_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_buildings_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_checker_deprecated**
> IfcChecker get_checker_deprecated(cloud_pk, id, ifc_pk, project_pk)

Retrieve a checker of a model

A checker is a link between a checkplan and a model. A checker can launch a check multiple time and store all the results  Required scopes: check:read, ifc:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
from bimdata_api_client.model.ifc_checker import IfcChecker
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this ifc checker.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a checker of a model
        api_response = api_instance.get_checker_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_checker_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this ifc checker. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**IfcChecker**](IfcChecker.md)

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

# **get_checker_result_deprecated**
> CheckerResult get_checker_result_deprecated(checker_pk, cloud_pk, id, ifc_pk, project_pk)

Retrieve one CheckerResult

Retrieve one CheckerResult  Required scopes: check:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
from bimdata_api_client.model.checker_result import CheckerResult
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
    api_instance = ifc_api.IfcApi(api_client)
    checker_pk = 1 # int | A unique integer value identifying this ifc checker.
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this checker result.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve one CheckerResult
        api_response = api_instance.get_checker_result_deprecated(checker_pk, cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_checker_result_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checker_pk** | **int**| A unique integer value identifying this ifc checker. |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this checker result. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**CheckerResult**](CheckerResult.md)

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

# **get_checker_results_deprecated**
> [CheckerResult] get_checker_results_deprecated(checker_pk, cloud_pk, ifc_pk, project_pk)

Retrieve all CheckerResults

Retrieve all CheckerResults  Required scopes: check:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
from bimdata_api_client.model.checker_result import CheckerResult
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
    api_instance = ifc_api.IfcApi(api_client)
    checker_pk = 1 # int | A unique integer value identifying this ifc checker.
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all CheckerResults
        api_response = api_instance.get_checker_results_deprecated(checker_pk, cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_checker_results_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checker_pk** | **int**| A unique integer value identifying this ifc checker. |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[CheckerResult]**](CheckerResult.md)

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

# **get_checkers_deprecated**
> [IfcChecker] get_checkers_deprecated(cloud_pk, ifc_pk, project_pk)

Retrieve all checkers of a model

A checker is a link between a checkplan and a model. A checker can launch a check multiple time and store all the results  Required scopes: check:read, ifc:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
from bimdata_api_client.model.ifc_checker import IfcChecker
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all checkers of a model
        api_response = api_instance.get_checkers_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_checkers_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

### Return type

[**[IfcChecker]**](IfcChecker.md)

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

# **get_classifications_of_element_deprecated**
> [Classification] get_classifications_of_element_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all classifications of an element
        api_response = api_instance.get_classifications_of_element_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_classifications_of_element_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_documents_of_element_deprecated**
> [Document] get_documents_of_element_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all documents of an element
        api_response = api_instance.get_documents_of_element_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_documents_of_element_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_element_deprecated**
> Element get_element_deprecated(cloud_pk, ifc_pk, project_pk, uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an element of a model
        api_response = api_instance.get_element_deprecated(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_element_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_element_linked_documents_deprecated**
> [DocumentWithElementList] get_element_linked_documents_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    classification = "classification_example" # str |  (optional)
    classification__notation = "classification__notation_example" # str |  (optional)
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all documents linked to any element
        api_response = api_instance.get_element_linked_documents_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_element_linked_documents_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve all documents linked to any element
        api_response = api_instance.get_element_linked_documents_deprecated(cloud_pk, ifc_pk, project_pk, classification=classification, classification__notation=classification__notation, type=type)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_element_linked_documents_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_element_property_set_deprecated**
> PropertySet get_element_property_set_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this property set.
    ifc_pk = 1 # int | 
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a PropertySet of an element
        api_response = api_instance.get_element_property_set_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_element_property_set_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this property set. |
 **ifc_pk** | **int**|  |
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

# **get_element_property_set_properties_deprecated**
> [ModelProperty] get_element_property_set_properties_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all Properties of a PropertySet
        api_response = api_instance.get_element_property_set_properties_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_element_property_set_properties_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_element_property_set_property_definition_deprecated**
> PropertyDefinition get_element_property_set_property_definition_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this property definition.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_pk = 1 # int | A unique integer value identifying this property.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Definition of a Property
        api_response = api_instance.get_element_property_set_property_definition_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_element_property_set_property_definition_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this property definition. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_element_property_set_property_definition_unit_deprecated**
> Unit get_element_property_set_property_definition_unit_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this unit.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_pk = 1 # int | A unique integer value identifying this property.
    propertydefinition_pk = 1 # int | A unique integer value identifying this property definition.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Unit of a Definition
        api_response = api_instance.get_element_property_set_property_definition_unit_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_element_property_set_property_definition_unit_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this unit. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_element_property_set_property_definition_units_deprecated**
> [Unit] get_element_property_set_property_definition_units_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_pk = 1 # int | A unique integer value identifying this property.
    propertydefinition_pk = 1 # int | A unique integer value identifying this property definition.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all Units of a Definition
        api_response = api_instance.get_element_property_set_property_definition_units_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_element_property_set_property_definition_units_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_element_property_set_property_definitions_deprecated**
> [PropertyDefinition] get_element_property_set_property_definitions_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_pk = 1 # int | A unique integer value identifying this property.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all Definitions of a PropertySet
        api_response = api_instance.get_element_property_set_property_definitions_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk, property_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_element_property_set_property_definitions_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_element_property_set_property_deprecated**
> ModelProperty get_element_property_set_property_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this property.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Property of a PropertySet
        api_response = api_instance.get_element_property_set_property_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_element_property_set_property_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this property. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_element_property_sets_deprecated**
> [PropertySet] get_element_property_sets_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | 
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all PropertySets of an element
        api_response = api_instance.get_element_property_sets_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_element_property_sets_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**|  |
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

# **get_elements_deprecated**
> [Element] get_elements_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    classification = "classification_example" # str |  (optional)
    classification__notation = "classification__notation_example" # str |  (optional)
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all elements of a model
        api_response = api_instance.get_elements_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_elements_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve all elements of a model
        api_response = api_instance.get_elements_deprecated(cloud_pk, ifc_pk, project_pk, classification=classification, classification__notation=classification__notation, type=type)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_elements_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_elements_from_classification_deprecated**
> [Element] get_elements_from_classification_deprecated(cloud_pk, ifc_pk, model_classification_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
    model_classification_pk = 1 # int | A unique integer value identifying this classification.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all elements with the classification
        api_response = api_instance.get_elements_from_classification_deprecated(cloud_pk, ifc_pk, model_classification_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_elements_from_classification_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
 **model_classification_pk** | **int**| A unique integer value identifying this classification. |
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

# **get_ifc_classifications_deprecated**
> [Classification] get_ifc_classifications_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    ifc_pk = 1 # int | 
    project_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all classifications in a model
        api_response = api_instance.get_ifc_classifications_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_ifc_classifications_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **ifc_pk** | **int**|  |
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

# **get_ifc_deprecated**
> Model get_ifc_deprecated(cloud_pk, id, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve one model
        api_response = api_instance.get_ifc_deprecated(cloud_pk, id, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_ifc_deprecated: %s\n" % e)
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

# **get_ifc_material_deprecated**
> Material get_ifc_material_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this material.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a material of a model
        api_response = api_instance.get_ifc_material_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_ifc_material_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this material. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_ifc_materials_deprecated**
> [Material] get_ifc_materials_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all materials of a model
        api_response = api_instance.get_ifc_materials_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_ifc_materials_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_ifc_properties_deprecated**
> [ModelProperty] get_ifc_properties_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all Properties of a model
        api_response = api_instance.get_ifc_properties_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_ifc_properties_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_ifc_property_definition_deprecated**
> PropertyDefinition get_ifc_property_definition_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property definition.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a PropertyDefinition of a model
        api_response = api_instance.get_ifc_property_definition_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_ifc_property_definition_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property definition. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_ifc_property_definitions_deprecated**
> [PropertyDefinition] get_ifc_property_definitions_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all PropertyDefinitions of a model
        api_response = api_instance.get_ifc_property_definitions_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_ifc_property_definitions_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_ifc_property_deprecated**
> ModelProperty get_ifc_property_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Property of a model
        api_response = api_instance.get_ifc_property_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_ifc_property_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_ifc_unit_deprecated**
> Unit get_ifc_unit_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this unit.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Unit of a model
        api_response = api_instance.get_ifc_unit_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_ifc_unit_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this unit. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_ifc_units_deprecated**
> [Unit] get_ifc_units_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all Units of a model
        api_response = api_instance.get_ifc_units_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_ifc_units_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_ifcs_deprecated**
> [Model] get_ifcs_deprecated(cloud_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    project_pk = 1 # int | 
    source = "EXPORT" # str |  (optional)
    status = [
        "C",
    ] # [str] |  (optional)
    type = [
        "BFX",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all models
        api_response = api_instance.get_ifcs_deprecated(cloud_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_ifcs_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve all models
        api_response = api_instance.get_ifcs_deprecated(cloud_pk, project_pk, source=source, status=status, type=type)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_ifcs_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **project_pk** | **int**|  |
 **source** | **str**|  | [optional]
 **status** | **[str]**|  | [optional]
 **type** | **[str]**|  | [optional]

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

# **get_layer_deprecated**
> Layer get_layer_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this layer.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a layer of a model
        api_response = api_instance.get_layer_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_layer_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this layer. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_layers_deprecated**
> [Layer] get_layers_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all layers of a model
        api_response = api_instance.get_layers_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_layers_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_material_deprecated**
> Material get_material_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this material.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a material of a model
        api_response = api_instance.get_material_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_material_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this material. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_materials_deprecated**
> [Material] get_materials_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all materials of a model
        api_response = api_instance.get_materials_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_materials_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_processor_handler_deprecated**
> ProcessorHandler get_processor_handler_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this processor handler.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a processor handler
        api_response = api_instance.get_processor_handler_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_processor_handler_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this processor handler. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_processor_handlers_deprecated**
> [ProcessorHandler] get_processor_handlers_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Get all processor handlers
        api_response = api_instance.get_processor_handlers_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_processor_handlers_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_property_set_deprecated**
> PropertySet get_property_set_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property set.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a PropertySet of a model
        api_response = api_instance.get_property_set_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_property_set_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property set. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_property_sets_deprecated**
> [PropertySet] get_property_sets_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all PropertySets of a model
        api_response = api_instance.get_property_sets_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_property_sets_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_raw_elements_deprecated**
> RawElements get_raw_elements_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all elements in a optimized format
        api_response = api_instance.get_raw_elements_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_raw_elements_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **get_simple_element_deprecated**
> SimpleElement get_simple_element_deprecated(cloud_pk, ifc_pk, project_pk, uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an element of a model with a simple value representation
        api_response = api_instance.get_simple_element_deprecated(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_simple_element_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_simple_elements_deprecated**
> SimpleElement get_simple_elements_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all elements of a model with a simple value representation
        api_response = api_instance.get_simple_elements_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_simple_elements_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |

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

# **get_space_deprecated**
> Space get_space_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this space.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve one space of the model
        api_response = api_instance.get_space_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_space_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this space. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_spaces_deprecated**
> [Space] get_spaces_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all spaces of the model
        api_response = api_instance.get_spaces_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_spaces_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_storey_deprecated**
> Storey get_storey_deprecated(cloud_pk, ifc_pk, project_pk, uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a storey of a model
        api_response = api_instance.get_storey_deprecated(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_storey_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_storey_plan_positioning_deprecated**
> PositioningPlan get_storey_plan_positioning_deprecated(cloud_pk, id, ifc_pk, project_pk, storey_uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this element.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    storey_uuid = "storey_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the postioning of the plan in the storey
        api_response = api_instance.get_storey_plan_positioning_deprecated(cloud_pk, id, ifc_pk, project_pk, storey_uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_storey_plan_positioning_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this element. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_storeys_deprecated**
> [Storey] get_storeys_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all storeys of a model
        api_response = api_instance.get_storeys_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_storeys_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_system_deprecated**
> System get_system_deprecated(cloud_pk, ifc_pk, project_pk, uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a system of a model
        api_response = api_instance.get_system_deprecated(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_system_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_systems_deprecated**
> [System] get_systems_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all systems of a model
        api_response = api_instance.get_systems_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_systems_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_zone_deprecated**
> Zone get_zone_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this zone.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve one zone of a model
        api_response = api_instance.get_zone_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_zone_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this zone. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_zone_space_deprecated**
> ZoneSpace get_zone_space_deprecated(cloud_pk, id, ifc_pk, project_pk, zone_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this space.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    zone_pk = 1 # int | A unique integer value identifying this zone.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve one space of a zone
        api_response = api_instance.get_zone_space_deprecated(cloud_pk, id, ifc_pk, project_pk, zone_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_zone_space_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this space. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_zone_spaces_deprecated**
> [ZoneSpace] get_zone_spaces_deprecated(cloud_pk, ifc_pk, project_pk, zone_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    zone_pk = 1 # int | A unique integer value identifying this zone.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all spaces of a zone
        api_response = api_instance.get_zone_spaces_deprecated(cloud_pk, ifc_pk, project_pk, zone_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_zone_spaces_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **get_zones_deprecated**
> [Zone] get_zones_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    color = "color_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve zones of a model
        api_response = api_instance.get_zones_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_zones_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve zones of a model
        api_response = api_instance.get_zones_deprecated(cloud_pk, ifc_pk, project_pk, color=color)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->get_zones_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **launch_new_check_deprecated**
> launch_new_check_deprecated(cloud_pk, id, ifc_pk, project_pk)

Launch a new check on the model

A nex check will be played with the current state of elements, properties, etc.  Required scopes: check:write, ifc:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
from bimdata_api_client.model.ifc_checker_request import IfcCheckerRequest
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this ifc checker.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    ifc_checker_request = IfcCheckerRequest(
        name="name_example",
        checkplan_id=1,
    ) # IfcCheckerRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Launch a new check on the model
        api_instance.launch_new_check_deprecated(cloud_pk, id, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->launch_new_check_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Launch a new check on the model
        api_instance.launch_new_check_deprecated(cloud_pk, id, ifc_pk, project_pk, ifc_checker_request=ifc_checker_request)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->launch_new_check_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this ifc checker. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **ifc_checker_request** | [**IfcCheckerRequest**](IfcCheckerRequest.md)|  | [optional]

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

# **link_documents_of_element_deprecated**
> [Document] link_documents_of_element_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Link one or many documents to an element
        api_response = api_instance.link_documents_of_element_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->link_documents_of_element_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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
**400** | All creates failed: list of errors |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_classification_element_relations_deprecated**
> [ElementClassificationRelation] list_classification_element_relations_deprecated(cloud_pk, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # List all associations between classifications and elements
        api_response = api_instance.list_classification_element_relations_deprecated(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->list_classification_element_relations_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **merge_ifcs_deprecated**
> merge_ifcs_deprecated(cloud_pk, project_pk, ifc_merge_request)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
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
        api_instance.merge_ifcs_deprecated(cloud_pk, project_pk, ifc_merge_request)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->merge_ifcs_deprecated: %s\n" % e)
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

# **optimize_ifc_deprecated**
> optimize_ifc_deprecated(cloud_pk, id, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 
    ifc_optimize_request = IfcOptimizeRequest(
        floating_point_reduction=9,
    ) # IfcOptimizeRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Optimize the IFC
        api_instance.optimize_ifc_deprecated(cloud_pk, id, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->optimize_ifc_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Optimize the IFC
        api_instance.optimize_ifc_deprecated(cloud_pk, id, project_pk, ifc_optimize_request=ifc_optimize_request)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->optimize_ifc_deprecated: %s\n" % e)
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

# **remove_all_element_property_set_deprecated**
> remove_all_element_property_set_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    ifc_pk = 1 # int | 
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Remove all property sets from element
        api_instance.remove_all_element_property_set_deprecated(cloud_pk, element_uuid, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->remove_all_element_property_set_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **ifc_pk** | **int**|  |
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

# **remove_classification_of_element_deprecated**
> remove_classification_of_element_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this classification.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Remove a classification from an element
        api_instance.remove_classification_of_element_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->remove_classification_of_element_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this classification. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **remove_document_of_element_deprecated**
> remove_document_of_element_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this document.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Remove a documents from an element
        api_instance.remove_document_of_element_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->remove_document_of_element_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this document. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **remove_element_property_set_deprecated**
> remove_element_property_set_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this property set.
    ifc_pk = 1 # int | 
    project_pk = 1 # int | A unique integer value identifying this project.

    # example passing only required values which don't have defaults set
    try:
        # Remove a PropertySet from an element
        api_instance.remove_element_property_set_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->remove_element_property_set_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this property set. |
 **ifc_pk** | **int**|  |
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

# **remove_element_property_set_property_definition_deprecated**
> remove_element_property_set_property_definition_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this property definition.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_pk = 1 # int | A unique integer value identifying this property.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Definition to a Property
        api_instance.remove_element_property_set_property_definition_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertyset_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->remove_element_property_set_property_definition_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this property definition. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **remove_element_property_set_property_definition_unit_deprecated**
> remove_element_property_set_property_definition_unit_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this unit.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    property_pk = 1 # int | A unique integer value identifying this property.
    propertydefinition_pk = 1 # int | A unique integer value identifying this property definition.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Remove a Unit from a Definition
        api_instance.remove_element_property_set_property_definition_unit_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, property_pk, propertydefinition_pk, propertyset_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->remove_element_property_set_property_definition_unit_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this unit. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **remove_element_property_set_property_deprecated**
> remove_element_property_set_property_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this property.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    propertyset_pk = 1 # int | A unique integer value identifying this property set.

    # example passing only required values which don't have defaults set
    try:
        # Remove a property from a PropertySet
        api_instance.remove_element_property_set_property_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->remove_element_property_set_property_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this property. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **remove_elements_from_classification_deprecated**
> remove_elements_from_classification_deprecated(cloud_pk, ifc_pk, model_classification_pk, project_pk, uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    ifc_pk = 1 # int | A unique integer value identifying this model.
    model_classification_pk = 1 # int | A unique integer value identifying this classification.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove the classification from all elements
        api_instance.remove_elements_from_classification_deprecated(cloud_pk, ifc_pk, model_classification_pk, project_pk, uuid)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->remove_elements_from_classification_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**|  |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
 **model_classification_pk** | **int**| A unique integer value identifying this classification. |
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

# **reprocess_ifc_deprecated**
> reprocess_ifc_deprecated(cloud_pk, id, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Reprocess Model file
        api_instance.reprocess_ifc_deprecated(cloud_pk, id, project_pk)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->reprocess_ifc_deprecated: %s\n" % e)
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

# **update_access_token_deprecated**
> IfcAccessToken update_access_token_deprecated(cloud_pk, ifc_pk, project_pk, token)

Update some fields of a token

You can update the expiration date or the read_only field  Required scopes: ifc:token_manage, model:token_manage

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    token = "token_example" # str | 
    patched_ifc_access_token_request = PatchedIfcAccessTokenRequest(
        read_only=True,
        expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # PatchedIfcAccessTokenRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a token
        api_response = api_instance.update_access_token_deprecated(cloud_pk, ifc_pk, project_pk, token)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_access_token_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a token
        api_response = api_instance.update_access_token_deprecated(cloud_pk, ifc_pk, project_pk, token, patched_ifc_access_token_request=patched_ifc_access_token_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_access_token_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_building_deprecated**
> Building update_building_deprecated(cloud_pk, ifc_pk, project_pk, uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 
    patched_storey_building_request = PatchedStoreyBuildingRequest(
        name="name_example",
    ) # PatchedStoreyBuildingRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a building
        api_response = api_instance.update_building_deprecated(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_building_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a building
        api_response = api_instance.update_building_deprecated(cloud_pk, ifc_pk, project_pk, uuid, patched_storey_building_request=patched_storey_building_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_building_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_building_plan_positioning_deprecated**
> PositioningPlan update_building_plan_positioning_deprecated(building_uuid, cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    building_uuid = "building_uuid_example" # str | 
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this element.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        api_response = api_instance.update_building_plan_positioning_deprecated(building_uuid, cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_building_plan_positioning_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the postioning of the plan in the building
        api_response = api_instance.update_building_plan_positioning_deprecated(building_uuid, cloud_pk, id, ifc_pk, project_pk, patched_positioning_plan_request=patched_positioning_plan_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_building_plan_positioning_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_uuid** | **str**|  |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this element. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_checker_deprecated**
> IfcChecker update_checker_deprecated(cloud_pk, id, ifc_pk, project_pk)

Update some fields of a checker of a model

A checker is a link between a checkplan and a model. A checker can launch a check multiple time and store all the results  Required scopes: check:write, ifc:read

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
from bimdata_api_client.model.ifc_checker import IfcChecker
from bimdata_api_client.model.patched_ifc_checker_request import PatchedIfcCheckerRequest
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this ifc checker.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_ifc_checker_request = PatchedIfcCheckerRequest(
        name="name_example",
        checkplan_id=1,
    ) # PatchedIfcCheckerRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a checker of a model
        api_response = api_instance.update_checker_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_checker_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a checker of a model
        api_response = api_instance.update_checker_deprecated(cloud_pk, id, ifc_pk, project_pk, patched_ifc_checker_request=patched_ifc_checker_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_checker_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this ifc checker. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **patched_ifc_checker_request** | [**PatchedIfcCheckerRequest**](PatchedIfcCheckerRequest.md)|  | [optional]

### Return type

[**IfcChecker**](IfcChecker.md)

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

# **update_checker_result_deprecated**
> CheckerResult update_checker_result_deprecated(checker_pk, cloud_pk, id, ifc_pk, project_pk)

Update some fields of a CheckerResult

Update some fields of a CheckerResult  Required scopes: check:write

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (BIMData_Connect):
* OAuth Authentication (BIMData_Connect):
* Api Key Authentication (Bearer):

```python
import time
import bimdata_api_client
from bimdata_api_client.api import ifc_api
from bimdata_api_client.model.patched_checker_result_request import PatchedCheckerResultRequest
from bimdata_api_client.model.checker_result import CheckerResult
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
    api_instance = ifc_api.IfcApi(api_client)
    checker_pk = 1 # int | A unique integer value identifying this ifc checker.
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this checker result.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_checker_result_request = PatchedCheckerResultRequest(
        status="C",
        result="result_example",
        collisions="collisions_example",
        error_detail="error_detail_example",
    ) # PatchedCheckerResultRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a CheckerResult
        api_response = api_instance.update_checker_result_deprecated(checker_pk, cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_checker_result_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a CheckerResult
        api_response = api_instance.update_checker_result_deprecated(checker_pk, cloud_pk, id, ifc_pk, project_pk, patched_checker_result_request=patched_checker_result_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_checker_result_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checker_pk** | **int**| A unique integer value identifying this ifc checker. |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this checker result. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
 **project_pk** | **int**| A unique integer value identifying this project. |
 **patched_checker_result_request** | [**PatchedCheckerResultRequest**](PatchedCheckerResultRequest.md)|  | [optional]

### Return type

[**CheckerResult**](CheckerResult.md)

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

# **update_element_deprecated**
> Element update_element_deprecated(cloud_pk, ifc_pk, project_pk, uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
                    value={
                        "key": None,
                    },
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
                        value={
                            "key": None,
                        },
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
        api_response = api_instance.update_element_deprecated(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_element_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of an element
        api_response = api_instance.update_element_deprecated(cloud_pk, ifc_pk, project_pk, uuid, patched_element_request=patched_element_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_element_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_element_property_set_property_deprecated**
> ModelProperty update_element_property_set_property_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    element_uuid = "element_uuid_example" # str | 
    id = 1 # int | A unique integer value identifying this property.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        value={
            "key": None,
        },
    ) # PatchedPropertyRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a property from an element
        api_response = api_instance.update_element_property_set_property_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_element_property_set_property_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a property from an element
        api_response = api_instance.update_element_property_set_property_deprecated(cloud_pk, element_uuid, id, ifc_pk, project_pk, propertyset_pk, patched_property_request=patched_property_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_element_property_set_property_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **element_uuid** | **str**|  |
 **id** | **int**| A unique integer value identifying this property. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_ifc_deprecated**
> Model update_ifc_deprecated(cloud_pk, id, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
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
    ) # PatchedModelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a model
        api_response = api_instance.update_ifc_deprecated(cloud_pk, id, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_ifc_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a model
        api_response = api_instance.update_ifc_deprecated(cloud_pk, id, project_pk, patched_model_request=patched_model_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_ifc_deprecated: %s\n" % e)
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

# **update_ifc_files_deprecated**
> ModelFiles update_ifc_files_deprecated(cloud_pk, id, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | 
    id = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | 
    structure_file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)
    systems_file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)
    map_file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)
    gltf_file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)
    gltf_with_openings_file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)
    bvh_tree_file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)
    viewer_360_file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)
    xkt_file = open('/path/to/file', 'rb') # file_type, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update models file (gltf, svg, structure, etc)
        api_response = api_instance.update_ifc_files_deprecated(cloud_pk, id, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_ifc_files_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update models file (gltf, svg, structure, etc)
        api_response = api_instance.update_ifc_files_deprecated(cloud_pk, id, project_pk, structure_file=structure_file, systems_file=systems_file, map_file=map_file, gltf_file=gltf_file, gltf_with_openings_file=gltf_with_openings_file, bvh_tree_file=bvh_tree_file, viewer_360_file=viewer_360_file, xkt_file=xkt_file)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_ifc_files_deprecated: %s\n" % e)
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
 **gltf_with_openings_file** | **file_type, none_type**|  | [optional]
 **bvh_tree_file** | **file_type, none_type**|  | [optional]
 **viewer_360_file** | **file_type, none_type**|  | [optional]
 **xkt_file** | **file_type, none_type**|  | [optional]

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

# **update_ifc_property_definition_deprecated**
> PropertyDefinition update_ifc_property_definition_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property definition.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        api_response = api_instance.update_ifc_property_definition_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_ifc_property_definition_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of many PropertyDefinitions of a model
        api_response = api_instance.update_ifc_property_definition_deprecated(cloud_pk, id, ifc_pk, project_pk, patched_property_definition_request=patched_property_definition_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_ifc_property_definition_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property definition. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_ifc_property_deprecated**
> ModelProperty update_ifc_property_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_property_request = PatchedPropertyRequest(
        definition=PropertyDefinitionRequest(
            unit=None,
            name="name_example",
            description="description_example",
            type="type_example",
            value_type="value_type_example",
        ),
        value={
            "key": None,
        },
    ) # PatchedPropertyRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a Property
        api_response = api_instance.update_ifc_property_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_ifc_property_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a Property
        api_response = api_instance.update_ifc_property_deprecated(cloud_pk, id, ifc_pk, project_pk, patched_property_request=patched_property_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_ifc_property_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_ifc_unit_deprecated**
> Unit update_ifc_unit_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this unit.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        conversion_baseunit=UnitRequest(
            type="type_example",
            name="name_example",
            unit_type="unit_type_example",
            prefix="prefix_example",
            dimensions=[
                3.14,
            ],
            conversion_factor=3.14,
            conversion_baseunit=UnitRequest(),
            elements={
                "key": None,
            },
            is_default=True,
        ),
        elements={
            "key": None,
        },
        is_default=True,
    ) # PatchedUnitRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a Unit of a model
        api_response = api_instance.update_ifc_unit_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_ifc_unit_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a Unit of a model
        api_response = api_instance.update_ifc_unit_deprecated(cloud_pk, id, ifc_pk, project_pk, patched_unit_request=patched_unit_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_ifc_unit_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this unit. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_layer_deprecated**
> Layer update_layer_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this layer.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        api_response = api_instance.update_layer_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_layer_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a layer
        api_response = api_instance.update_layer_deprecated(cloud_pk, id, ifc_pk, project_pk, patched_layer_request=patched_layer_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_layer_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this layer. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_order_building_plan_deprecated**
> Storey update_order_building_plan_deprecated(building_uuid, cloud_pk, ifc_pk, project_pk, request_body)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    building_uuid = "building_uuid_example" # str | 
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Update order of all plan of a building
        api_response = api_instance.update_order_building_plan_deprecated(building_uuid, cloud_pk, ifc_pk, project_pk, request_body)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_order_building_plan_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building_uuid** | **str**|  |
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_order_storey_plan_deprecated**
> Storey update_order_storey_plan_deprecated(cloud_pk, ifc_pk, project_pk, storey_uuid, request_body)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    storey_uuid = "storey_uuid_example" # str | 
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Update order of all plan of a storey
        api_response = api_instance.update_order_storey_plan_deprecated(cloud_pk, ifc_pk, project_pk, storey_uuid, request_body)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_order_storey_plan_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_order_storeys_deprecated**
> [Storey] update_order_storeys_deprecated(cloud_pk, ifc_pk, project_pk, request_body)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    request_body = [
        "request_body_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # Update order of all storey of a model
        api_response = api_instance.update_order_storeys_deprecated(cloud_pk, ifc_pk, project_pk, request_body)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_order_storeys_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_processor_handler_deprecated**
> ProcessorHandler update_processor_handler_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this processor handler.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_processor_handler_request = PatchedProcessorHandlerRequest(
        status="C",
        detail_message="detail_message_example",
    ) # PatchedProcessorHandlerRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the status of a processor handler
        api_response = api_instance.update_processor_handler_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_processor_handler_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the status of a processor handler
        api_response = api_instance.update_processor_handler_deprecated(cloud_pk, id, ifc_pk, project_pk, patched_processor_handler_request=patched_processor_handler_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_processor_handler_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this processor handler. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_property_set_deprecated**
> PropertySet update_property_set_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this property set.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
                value={
                    "key": None,
                },
            ),
        ],
    ) # PatchedPropertySetRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a PropertySet
        api_response = api_instance.update_property_set_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_property_set_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a PropertySet
        api_response = api_instance.update_property_set_deprecated(cloud_pk, id, ifc_pk, project_pk, patched_property_set_request=patched_property_set_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_property_set_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this property set. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_space_deprecated**
> Space update_space_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this space.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_space_request = PatchedSpaceRequest(
        name="name_example",
        longname="longname_example",
        uuid="uuid_example",
    ) # PatchedSpaceRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a space
        api_response = api_instance.update_space_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_space_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a space
        api_response = api_instance.update_space_deprecated(cloud_pk, id, ifc_pk, project_pk, patched_space_request=patched_space_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_space_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this space. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_storey_deprecated**
> Storey update_storey_deprecated(cloud_pk, ifc_pk, project_pk, uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    uuid = "uuid_example" # str | 
    patched_storey_building_request = PatchedStoreyBuildingRequest(
        name="name_example",
    ) # PatchedStoreyBuildingRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a storey
        api_response = api_instance.update_storey_deprecated(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_storey_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a storey
        api_response = api_instance.update_storey_deprecated(cloud_pk, ifc_pk, project_pk, uuid, patched_storey_building_request=patched_storey_building_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_storey_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_storey_plan_positioning_deprecated**
> PositioningPlan update_storey_plan_positioning_deprecated(cloud_pk, id, ifc_pk, project_pk, storey_uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this element.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        api_response = api_instance.update_storey_plan_positioning_deprecated(cloud_pk, id, ifc_pk, project_pk, storey_uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_storey_plan_positioning_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the postioning of the plan in the storey
        api_response = api_instance.update_storey_plan_positioning_deprecated(cloud_pk, id, ifc_pk, project_pk, storey_uuid, patched_positioning_plan_request=patched_positioning_plan_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_storey_plan_positioning_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this element. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_system_deprecated**
> System update_system_deprecated(cloud_pk, ifc_pk, project_pk, uuid)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    ifc_pk = 1 # int | A unique integer value identifying this model.
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
        api_response = api_instance.update_system_deprecated(cloud_pk, ifc_pk, project_pk, uuid)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_system_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a system
        api_response = api_instance.update_system_deprecated(cloud_pk, ifc_pk, project_pk, uuid, patched_system_request=patched_system_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_system_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_zone_deprecated**
> Zone update_zone_deprecated(cloud_pk, id, ifc_pk, project_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this zone.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    patched_zone_request = PatchedZoneRequest(
        name="name_example",
        uuid="uuid_example",
        zones=[
            ZoneRequest(
                name="name_example",
                uuid="uuid_example",
                zones=[],
                parent_id=1,
                spaces=[
                    SpaceRequest(
                        name="name_example",
                        longname="longname_example",
                        uuid="uuid_example",
                    ),
                ],
                color="color_example",
            ),
        ],
        parent_id=1,
        spaces=[
            SpaceRequest(
                name="name_example",
                longname="longname_example",
                uuid="uuid_example",
            ),
        ],
        color="color_example",
    ) # PatchedZoneRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a zone
        api_response = api_instance.update_zone_deprecated(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_zone_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a zone
        api_response = api_instance.update_zone_deprecated(cloud_pk, id, ifc_pk, project_pk, patched_zone_request=patched_zone_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_zone_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this zone. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

# **update_zone_space_deprecated**
> ZoneSpace update_zone_space_deprecated(cloud_pk, id, ifc_pk, project_pk, zone_pk)

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
from bimdata_api_client.api import ifc_api
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
    api_instance = ifc_api.IfcApi(api_client)
    cloud_pk = 1 # int | A unique integer value identifying this cloud.
    id = 1 # int | A unique integer value identifying this space.
    ifc_pk = 1 # int | A unique integer value identifying this model.
    project_pk = 1 # int | A unique integer value identifying this project.
    zone_pk = 1 # int | A unique integer value identifying this zone.
    patched_zone_space_request = PatchedZoneSpaceRequest(
        name="name_example",
        longname="longname_example",
        uuid="uuid_example",
    ) # PatchedZoneSpaceRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update some fields of a space
        api_response = api_instance.update_zone_space_deprecated(cloud_pk, id, ifc_pk, project_pk, zone_pk)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_zone_space_deprecated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update some fields of a space
        api_response = api_instance.update_zone_space_deprecated(cloud_pk, id, ifc_pk, project_pk, zone_pk, patched_zone_space_request=patched_zone_space_request)
        pprint(api_response)
    except bimdata_api_client.ApiException as e:
        print("Exception when calling IfcApi->update_zone_space_deprecated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **int**| A unique integer value identifying this cloud. |
 **id** | **int**| A unique integer value identifying this space. |
 **ifc_pk** | **int**| A unique integer value identifying this model. |
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

