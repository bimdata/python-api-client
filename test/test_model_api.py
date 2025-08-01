"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1 (v1)
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import bimdata_api_client
from bimdata_api_client.api.model_api import ModelApi  # noqa: E501


class TestModelApi(unittest.TestCase):
    """ModelApi unit test stubs"""

    def setUp(self):
        self.api = ModelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_model_errors(self):
        """Test case for add_model_errors

        Add errors to model  # noqa: E501
        """
        pass

    def test_add_zone_space(self):
        """Test case for add_zone_space

        Add a space to a zone  # noqa: E501
        """
        pass

    def test_bulk_delete_model_classifications(self):
        """Test case for bulk_delete_model_classifications

        Remove all classifications from model's elements  # noqa: E501
        """
        pass

    def test_bulk_delete_model_properties(self):
        """Test case for bulk_delete_model_properties

        Delete many Property of a model  # noqa: E501
        """
        pass

    def test_bulk_delete_model_property_definitions(self):
        """Test case for bulk_delete_model_property_definitions

        Delete many PropertyDefinitions of a model  # noqa: E501
        """
        pass

    def test_bulk_delete_model_units(self):
        """Test case for bulk_delete_model_units

        Delete many Units of a model  # noqa: E501
        """
        pass

    def test_bulk_delete_property_set(self):
        """Test case for bulk_delete_property_set

        Delete many PropertySet of a model  # noqa: E501
        """
        pass

    def test_bulk_full_update_elements(self):
        """Test case for bulk_full_update_elements

        Update many elements at once (only changing fields may be defined)  # noqa: E501
        """
        pass

    def test_bulk_full_update_model_property(self):
        """Test case for bulk_full_update_model_property

        Update some fields of many properties of a model  # noqa: E501
        """
        pass

    def test_bulk_remove_classifications_of_element(self):
        """Test case for bulk_remove_classifications_of_element

        Remove many classifications from an element  # noqa: E501
        """
        pass

    def test_bulk_remove_documents_of_element(self):
        """Test case for bulk_remove_documents_of_element

        Remove many documents from an element  # noqa: E501
        """
        pass

    def test_bulk_remove_elements_from_classification(self):
        """Test case for bulk_remove_elements_from_classification

        Remove the classifications from all elements  # noqa: E501
        """
        pass

    def test_bulk_update_elements(self):
        """Test case for bulk_update_elements

        Update many elements at once (all field must be defined)  # noqa: E501
        """
        pass

    def test_bulk_update_model_property(self):
        """Test case for bulk_update_model_property

        Update all fields of many properties of a model  # noqa: E501
        """
        pass

    def test_create_access_token(self):
        """Test case for create_access_token

        Create a token for this model  # noqa: E501
        """
        pass

    def test_create_building(self):
        """Test case for create_building

        Create a building of a model  # noqa: E501
        """
        pass

    def test_create_building_plan(self):
        """Test case for create_building_plan

        Create a relation between a 2d model and a building  # noqa: E501
        """
        pass

    def test_create_classification_element_relations(self):
        """Test case for create_classification_element_relations

        Create association between existing classification and existing element  # noqa: E501
        """
        pass

    def test_create_classifications_of_element(self):
        """Test case for create_classifications_of_element

        Create one or many classifications to an element  # noqa: E501
        """
        pass

    def test_create_drawing(self):
        """Test case for create_drawing

        Create a drawing in the model  # noqa: E501
        """
        pass

    def test_create_element(self):
        """Test case for create_element

        Create an element in the model  # noqa: E501
        """
        pass

    def test_create_element_property_set(self):
        """Test case for create_element_property_set

        Create a PropertySets to an element  # noqa: E501
        """
        pass

    def test_create_element_property_set_property(self):
        """Test case for create_element_property_set_property

        Create a property to a PropertySet  # noqa: E501
        """
        pass

    def test_create_element_property_set_property_definition(self):
        """Test case for create_element_property_set_property_definition

        Create a Definition to a Property  # noqa: E501
        """
        pass

    def test_create_element_property_set_property_definition_unit(self):
        """Test case for create_element_property_set_property_definition_unit

        Create a Unit to a Definition  # noqa: E501
        """
        pass

    def test_create_label(self):
        """Test case for create_label

        Create a label in the model  # noqa: E501
        """
        pass

    def test_create_layer(self):
        """Test case for create_layer

        Create a layer in the model  # noqa: E501
        """
        pass

    def test_create_mask2_d(self):
        """Test case for create_mask2_d

        Create or update a 2D mask for the model  # noqa: E501
        """
        pass

    def test_create_meta_building(self):
        """Test case for create_meta_building

        Create an empty 3D Model  # noqa: E501
        """
        pass

    def test_create_model(self):
        """Test case for create_model

        Make a PDF or Image file a Model  # noqa: E501
        """
        pass

    def test_create_model_property_definition(self):
        """Test case for create_model_property_definition

        Create a PropertyDefinition on the model  # noqa: E501
        """
        pass

    def test_create_model_unit(self):
        """Test case for create_model_unit

        Create a Unit on a model  # noqa: E501
        """
        pass

    def test_create_multi_page_model(self):
        """Test case for create_multi_page_model

        Create a multi page model  # noqa: E501
        """
        pass

    def test_create_photosphere(self):
        """Test case for create_photosphere

        Create a photopshere model from an image file  # noqa: E501
        """
        pass

    def test_create_photosphere_building(self):
        """Test case for create_photosphere_building

        Create an empty Photosphere Building Model  # noqa: E501
        """
        pass

    def test_create_property_set(self):
        """Test case for create_property_set

        Create one or many PropertySet  # noqa: E501
        """
        pass

    def test_create_property_set_element_relations(self):
        """Test case for create_property_set_element_relations

        Create association between PropertySet and element  # noqa: E501
        """
        pass

    def test_create_raw_elements(self):
        """Test case for create_raw_elements

        Create elements in an optimized format  # noqa: E501
        """
        pass

    def test_create_space(self):
        """Test case for create_space

        Create a space in the model  # noqa: E501
        """
        pass

    def test_create_storey(self):
        """Test case for create_storey

        Create a storey of a model  # noqa: E501
        """
        pass

    def test_create_storey_plan(self):
        """Test case for create_storey_plan

        Create a relation between a 2d model and a storey  # noqa: E501
        """
        pass

    def test_create_system(self):
        """Test case for create_system

        Create a system in the model  # noqa: E501
        """
        pass

    def test_create_tileset(self):
        """Test case for create_tileset

        Create the tileset of the model and upload all files  # noqa: E501
        """
        pass

    def test_create_xkt_file(self):
        """Test case for create_xkt_file

        Create an xkt file for the model. Overrides existing file with same version  # noqa: E501
        """
        pass

    def test_create_zone(self):
        """Test case for create_zone

        Create a zone in the model  # noqa: E501
        """
        pass

    def test_create_zone_space(self):
        """Test case for create_zone_space

        Create a space in a zone  # noqa: E501
        """
        pass

    def test_delete_access_token(self):
        """Test case for delete_access_token

        Delete a token  # noqa: E501
        """
        pass

    def test_delete_building(self):
        """Test case for delete_building

        Delete a building of a model  # noqa: E501
        """
        pass

    def test_delete_building_plan(self):
        """Test case for delete_building_plan

        Delete the relation between a 2d model and a building  # noqa: E501
        """
        pass

    def test_delete_drawing(self):
        """Test case for delete_drawing

        Delete a drawing of a model  # noqa: E501
        """
        pass

    def test_delete_element(self):
        """Test case for delete_element

        Delete an element of a model  # noqa: E501
        """
        pass

    def test_delete_label(self):
        """Test case for delete_label

        Delete a label  # noqa: E501
        """
        pass

    def test_delete_layer(self):
        """Test case for delete_layer

        Delete a layer of a model  # noqa: E501
        """
        pass

    def test_delete_mask2_d(self):
        """Test case for delete_mask2_d

        Delete the 2D mask for the model  # noqa: E501
        """
        pass

    def test_delete_model(self):
        """Test case for delete_model

        Delete a model  # noqa: E501
        """
        pass

    def test_delete_model_property(self):
        """Test case for delete_model_property

        Delete a Property of a model  # noqa: E501
        """
        pass

    def test_delete_model_property_definition(self):
        """Test case for delete_model_property_definition

        Delete a PropertyDefinitions of a model  # noqa: E501
        """
        pass

    def test_delete_model_unit(self):
        """Test case for delete_model_unit

        Delete a Unit of a model  # noqa: E501
        """
        pass

    def test_delete_model_without_doc(self):
        """Test case for delete_model_without_doc

        Delete the Model without deleting the related document  # noqa: E501
        """
        pass

    def test_delete_property_set(self):
        """Test case for delete_property_set

        Delete a PropertySet of a model  # noqa: E501
        """
        pass

    def test_delete_space(self):
        """Test case for delete_space

        Delete a space  # noqa: E501
        """
        pass

    def test_delete_storey(self):
        """Test case for delete_storey

        Delete a storey of a model  # noqa: E501
        """
        pass

    def test_delete_storey_plan(self):
        """Test case for delete_storey_plan

        Delete the relation between a 2d model and a storey  # noqa: E501
        """
        pass

    def test_delete_system(self):
        """Test case for delete_system

        Delete a system of a model  # noqa: E501
        """
        pass

    def test_delete_zone(self):
        """Test case for delete_zone

        Delete a zone of a model  # noqa: E501
        """
        pass

    def test_delete_zone_space(self):
        """Test case for delete_zone_space

        Delete the relation between a space and a zone  # noqa: E501
        """
        pass

    def test_export_ifc(self):
        """Test case for export_ifc

        Export IFC  # noqa: E501
        """
        pass

    def test_full_update_element(self):
        """Test case for full_update_element

        Update all fields of an element  # noqa: E501
        """
        pass

    def test_get_access_token(self):
        """Test case for get_access_token

        Retrieve one token created for this model  # noqa: E501
        """
        pass

    def test_get_access_tokens(self):
        """Test case for get_access_tokens

        Retrieve all tokens created for this model  # noqa: E501
        """
        pass

    def test_get_building(self):
        """Test case for get_building

        Retrieve a building of a model  # noqa: E501
        """
        pass

    def test_get_building_plan_positioning(self):
        """Test case for get_building_plan_positioning

        Retrieve the postioning of the plan in the building  # noqa: E501
        """
        pass

    def test_get_buildings(self):
        """Test case for get_buildings

        Retrieve all buildings of a model  # noqa: E501
        """
        pass

    def test_get_classifications_of_element(self):
        """Test case for get_classifications_of_element

        Retrieve all classifications of an element  # noqa: E501
        """
        pass

    def test_get_documents_of_element(self):
        """Test case for get_documents_of_element

        Retrieve all documents of an element  # noqa: E501
        """
        pass

    def test_get_drawing(self):
        """Test case for get_drawing

        Retrieve a drawing of a model  # noqa: E501
        """
        pass

    def test_get_drawings(self):
        """Test case for get_drawings

        Retrieve all drawings of a model  # noqa: E501
        """
        pass

    def test_get_element(self):
        """Test case for get_element

        Retrieve an element of a model  # noqa: E501
        """
        pass

    def test_get_element_linked_documents(self):
        """Test case for get_element_linked_documents

        Retrieve all documents linked to any element  # noqa: E501
        """
        pass

    def test_get_element_property_set(self):
        """Test case for get_element_property_set

        Retrieve a PropertySet of an element  # noqa: E501
        """
        pass

    def test_get_element_property_set_properties(self):
        """Test case for get_element_property_set_properties

        Retrieve all Properties of a PropertySet  # noqa: E501
        """
        pass

    def test_get_element_property_set_property(self):
        """Test case for get_element_property_set_property

        Retrieve a Property of a PropertySet  # noqa: E501
        """
        pass

    def test_get_element_property_set_property_definition(self):
        """Test case for get_element_property_set_property_definition

        Retrieve a Definition of a Property  # noqa: E501
        """
        pass

    def test_get_element_property_set_property_definition_unit(self):
        """Test case for get_element_property_set_property_definition_unit

        Retrieve a Unit of a Definition  # noqa: E501
        """
        pass

    def test_get_element_property_set_property_definition_units(self):
        """Test case for get_element_property_set_property_definition_units

        Retrieve all Units of a Definition  # noqa: E501
        """
        pass

    def test_get_element_property_set_property_definitions(self):
        """Test case for get_element_property_set_property_definitions

        Retrieve all Definitions of a PropertySet  # noqa: E501
        """
        pass

    def test_get_element_property_sets(self):
        """Test case for get_element_property_sets

        Retrieve all PropertySets of an element  # noqa: E501
        """
        pass

    def test_get_elements(self):
        """Test case for get_elements

        Retrieve all elements of a model  # noqa: E501
        """
        pass

    def test_get_elements_from_classification(self):
        """Test case for get_elements_from_classification

        Retrieve all elements with the classification  # noqa: E501
        """
        pass

    def test_get_label(self):
        """Test case for get_label

        Retrieve one label of the model  # noqa: E501
        """
        pass

    def test_get_labels(self):
        """Test case for get_labels

        Retrieve all labels of the model  # noqa: E501
        """
        pass

    def test_get_layer(self):
        """Test case for get_layer

        Retrieve a layer of a model  # noqa: E501
        """
        pass

    def test_get_layers(self):
        """Test case for get_layers

        Retrieve all layers of a model  # noqa: E501
        """
        pass

    def test_get_material(self):
        """Test case for get_material

        Retrieve a material of a model  # noqa: E501
        """
        pass

    def test_get_materials(self):
        """Test case for get_materials

        Retrieve all materials of a model  # noqa: E501
        """
        pass

    def test_get_model(self):
        """Test case for get_model

        Retrieve one model  # noqa: E501
        """
        pass

    def test_get_model_classifications(self):
        """Test case for get_model_classifications

        Retrieve all classifications in a model  # noqa: E501
        """
        pass

    def test_get_model_material(self):
        """Test case for get_model_material

        Retrieve a material of a model  # noqa: E501
        """
        pass

    def test_get_model_materials(self):
        """Test case for get_model_materials

        Retrieve all materials of a model  # noqa: E501
        """
        pass

    def test_get_model_properties(self):
        """Test case for get_model_properties

        Retrieve all Properties of a model  # noqa: E501
        """
        pass

    def test_get_model_property(self):
        """Test case for get_model_property

        Retrieve a Property of a model  # noqa: E501
        """
        pass

    def test_get_model_property_definition(self):
        """Test case for get_model_property_definition

        Retrieve a PropertyDefinition of a model  # noqa: E501
        """
        pass

    def test_get_model_property_definitions(self):
        """Test case for get_model_property_definitions

        Retrieve all PropertyDefinitions of a model  # noqa: E501
        """
        pass

    def test_get_model_unit(self):
        """Test case for get_model_unit

        Retrieve a Unit of a model  # noqa: E501
        """
        pass

    def test_get_model_units(self):
        """Test case for get_model_units

        Retrieve all Units of a model  # noqa: E501
        """
        pass

    def test_get_models(self):
        """Test case for get_models

        Retrieve all models  # noqa: E501
        """
        pass

    def test_get_processor_handler(self):
        """Test case for get_processor_handler

        Retrieve a processor handler  # noqa: E501
        """
        pass

    def test_get_processor_handlers(self):
        """Test case for get_processor_handlers

        Get all processor handlers  # noqa: E501
        """
        pass

    def test_get_properties_types(self):
        """Test case for get_properties_types

        Retrieve all property types and their value type used in this model  # noqa: E501
        """
        pass

    def test_get_property_set(self):
        """Test case for get_property_set

        Retrieve a PropertySet of a model  # noqa: E501
        """
        pass

    def test_get_property_sets(self):
        """Test case for get_property_sets

        Retrieve all PropertySets of a model  # noqa: E501
        """
        pass

    def test_get_raw_elements(self):
        """Test case for get_raw_elements

        Retrieve all elements in a optimized format  # noqa: E501
        """
        pass

    def test_get_simple_element(self):
        """Test case for get_simple_element

        Retrieve an element of a model with a simple value representation  # noqa: E501
        """
        pass

    def test_get_simple_elements(self):
        """Test case for get_simple_elements

        Retrieve all elements of a model with a simple value representation  # noqa: E501
        """
        pass

    def test_get_space(self):
        """Test case for get_space

        Retrieve one space of the model  # noqa: E501
        """
        pass

    def test_get_spaces(self):
        """Test case for get_spaces

        Retrieve all spaces of the model  # noqa: E501
        """
        pass

    def test_get_storey(self):
        """Test case for get_storey

        Retrieve a storey of a model  # noqa: E501
        """
        pass

    def test_get_storey_plan_positioning(self):
        """Test case for get_storey_plan_positioning

        Retrieve the postioning of the plan in the storey  # noqa: E501
        """
        pass

    def test_get_storeys(self):
        """Test case for get_storeys

        Retrieve all storeys of a model  # noqa: E501
        """
        pass

    def test_get_system(self):
        """Test case for get_system

        Retrieve a system of a model  # noqa: E501
        """
        pass

    def test_get_systems(self):
        """Test case for get_systems

        Retrieve all systems of a model  # noqa: E501
        """
        pass

    def test_get_tileset(self):
        """Test case for get_tileset

        Retrieve the tileset of the model  # noqa: E501
        """
        pass

    def test_get_types(self):
        """Test case for get_types

        Retrieve all IFC Types used in this model  # noqa: E501
        """
        pass

    def test_get_zone(self):
        """Test case for get_zone

        Retrieve one zone of a model  # noqa: E501
        """
        pass

    def test_get_zone_space(self):
        """Test case for get_zone_space

        Retrieve one space of a zone  # noqa: E501
        """
        pass

    def test_get_zone_spaces(self):
        """Test case for get_zone_spaces

        Retrieve all spaces of a zone  # noqa: E501
        """
        pass

    def test_get_zones(self):
        """Test case for get_zones

        Retrieve zones of a model  # noqa: E501
        """
        pass

    def test_link_documents_of_element(self):
        """Test case for link_documents_of_element

        Link one or many documents to an element  # noqa: E501
        """
        pass

    def test_list_classification_element_relations(self):
        """Test case for list_classification_element_relations

        List all associations between classifications and elements  # noqa: E501
        """
        pass

    def test_merge_ifcs(self):
        """Test case for merge_ifcs

        Merge IFC files  # noqa: E501
        """
        pass

    def test_optimize_ifc(self):
        """Test case for optimize_ifc

        Optimize the IFC  # noqa: E501
        """
        pass

    def test_remove_all_element_property_set(self):
        """Test case for remove_all_element_property_set

        Remove all property sets from element  # noqa: E501
        """
        pass

    def test_remove_classification_of_element(self):
        """Test case for remove_classification_of_element

        Remove a classification from an element  # noqa: E501
        """
        pass

    def test_remove_document_of_element(self):
        """Test case for remove_document_of_element

        Remove a documents from an element  # noqa: E501
        """
        pass

    def test_remove_element_property_set(self):
        """Test case for remove_element_property_set

        Remove a PropertySet from an element  # noqa: E501
        """
        pass

    def test_remove_element_property_set_property(self):
        """Test case for remove_element_property_set_property

        Remove a property from a PropertySet  # noqa: E501
        """
        pass

    def test_remove_element_property_set_property_definition(self):
        """Test case for remove_element_property_set_property_definition

        Delete a Definition to a Property  # noqa: E501
        """
        pass

    def test_remove_element_property_set_property_definition_unit(self):
        """Test case for remove_element_property_set_property_definition_unit

        Remove a Unit from a Definition  # noqa: E501
        """
        pass

    def test_remove_elements_from_classification(self):
        """Test case for remove_elements_from_classification

        Remove the classification from all elements  # noqa: E501
        """
        pass

    def test_reprocess_model(self):
        """Test case for reprocess_model

        Reprocess Model file  # noqa: E501
        """
        pass

    def test_update_access_token(self):
        """Test case for update_access_token

        Update some fields of a token  # noqa: E501
        """
        pass

    def test_update_building(self):
        """Test case for update_building

        Update some fields of a building  # noqa: E501
        """
        pass

    def test_update_building_plan_positioning(self):
        """Test case for update_building_plan_positioning

        Update the postioning of the plan in the building  # noqa: E501
        """
        pass

    def test_update_drawing(self):
        """Test case for update_drawing

        Update some fields of a drawing  # noqa: E501
        """
        pass

    def test_update_element(self):
        """Test case for update_element

        Update some fields of an element  # noqa: E501
        """
        pass

    def test_update_element_property_set_property(self):
        """Test case for update_element_property_set_property

        Update a property from an element  # noqa: E501
        """
        pass

    def test_update_label(self):
        """Test case for update_label

        Update some fields of a label  # noqa: E501
        """
        pass

    def test_update_layer(self):
        """Test case for update_layer

        Update some fields of a layer  # noqa: E501
        """
        pass

    def test_update_mask2_d(self):
        """Test case for update_mask2_d

        Partial update of a 2D mask for the model  # noqa: E501
        """
        pass

    def test_update_model(self):
        """Test case for update_model

        Update some fields of a model  # noqa: E501
        """
        pass

    def test_update_model_files(self):
        """Test case for update_model_files

        Update models file (gltf, svg, structure, etc)  # noqa: E501
        """
        pass

    def test_update_model_property(self):
        """Test case for update_model_property

        Update some fields of a Property  # noqa: E501
        """
        pass

    def test_update_model_property_definition(self):
        """Test case for update_model_property_definition

        Update some fields of many PropertyDefinitions of a model  # noqa: E501
        """
        pass

    def test_update_model_transform(self):
        """Test case for update_model_transform

        Update model transform  # noqa: E501
        """
        pass

    def test_update_model_unit(self):
        """Test case for update_model_unit

        Update some fields of a Unit of a model  # noqa: E501
        """
        pass

    def test_update_order_building_plan(self):
        """Test case for update_order_building_plan

        Update order of all plan of a building  # noqa: E501
        """
        pass

    def test_update_order_storey_plan(self):
        """Test case for update_order_storey_plan

        Update order of all plan of a storey  # noqa: E501
        """
        pass

    def test_update_order_storeys(self):
        """Test case for update_order_storeys

        Update order of all storey of a model  # noqa: E501
        """
        pass

    def test_update_processor_handler(self):
        """Test case for update_processor_handler

        Update the status of a processor handler  # noqa: E501
        """
        pass

    def test_update_property_set(self):
        """Test case for update_property_set

        Update some fields of a PropertySet  # noqa: E501
        """
        pass

    def test_update_space(self):
        """Test case for update_space

        Update some fields of a space  # noqa: E501
        """
        pass

    def test_update_storey(self):
        """Test case for update_storey

        Update some fields of a storey  # noqa: E501
        """
        pass

    def test_update_storey_plan_positioning(self):
        """Test case for update_storey_plan_positioning

        Update the postioning of the plan in the storey  # noqa: E501
        """
        pass

    def test_update_system(self):
        """Test case for update_system

        Update some fields of a system  # noqa: E501
        """
        pass

    def test_update_zone(self):
        """Test case for update_zone

        Update some fields of a zone  # noqa: E501
        """
        pass

    def test_update_zone_space(self):
        """Test case for update_zone_space

        Update some fields of a space  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
