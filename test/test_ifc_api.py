"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1 (v1)
    Generated by: https://openapi-generator.tech
"""


import unittest

import bimdata_api_client
from bimdata_api_client.api.ifc_api import IfcApi  # noqa: E501


class TestIfcApi(unittest.TestCase):
    """IfcApi unit test stubs"""

    def setUp(self):
        self.api = IfcApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_ifc_errors_deprecated(self):
        """Test case for add_ifc_errors_deprecated

        Add errors to model  # noqa: E501
        """
        pass

    def test_bulk_delete_ifc_classifications_deprecated(self):
        """Test case for bulk_delete_ifc_classifications_deprecated

        Remove all classifications from model's elements  # noqa: E501
        """
        pass

    def test_bulk_delete_ifc_properties_deprecated(self):
        """Test case for bulk_delete_ifc_properties_deprecated

        Delete many Property of a model  # noqa: E501
        """
        pass

    def test_bulk_delete_ifc_property_definitions_deprecated(self):
        """Test case for bulk_delete_ifc_property_definitions_deprecated

        Delete many PropertyDefinitions of a model  # noqa: E501
        """
        pass

    def test_bulk_delete_ifc_units_deprecated(self):
        """Test case for bulk_delete_ifc_units_deprecated

        Delete many Units of a model  # noqa: E501
        """
        pass

    def test_bulk_delete_property_set_deprecated(self):
        """Test case for bulk_delete_property_set_deprecated

        Delete many PropertySet of a model  # noqa: E501
        """
        pass

    def test_bulk_full_update_elements_deprecated(self):
        """Test case for bulk_full_update_elements_deprecated

        Update many elements at once (only changing fields may be defined)  # noqa: E501
        """
        pass

    def test_bulk_full_update_ifc_property_deprecated(self):
        """Test case for bulk_full_update_ifc_property_deprecated

        Update some fields of many properties of a model  # noqa: E501
        """
        pass

    def test_bulk_remove_classifications_of_element_deprecated(self):
        """Test case for bulk_remove_classifications_of_element_deprecated

        Remove many classifications from an element  # noqa: E501
        """
        pass

    def test_bulk_remove_documents_of_element_deprecated(self):
        """Test case for bulk_remove_documents_of_element_deprecated

        Remove many documents from an element  # noqa: E501
        """
        pass

    def test_bulk_remove_elements_from_classification_deprecated(self):
        """Test case for bulk_remove_elements_from_classification_deprecated

        Remove the classifications from all elements  # noqa: E501
        """
        pass

    def test_bulk_update_elements_deprecated(self):
        """Test case for bulk_update_elements_deprecated

        Update many elements at once (all field must be defined)  # noqa: E501
        """
        pass

    def test_bulk_update_ifc_property_deprecated(self):
        """Test case for bulk_update_ifc_property_deprecated

        Update all fields of many properties of a model  # noqa: E501
        """
        pass

    def test_create_access_token_deprecated(self):
        """Test case for create_access_token_deprecated

        Create a token for this model  # noqa: E501
        """
        pass

    def test_create_building_deprecated(self):
        """Test case for create_building_deprecated

        Create a building of a model  # noqa: E501
        """
        pass

    def test_create_building_plan_deprecated(self):
        """Test case for create_building_plan_deprecated

        Create a relation between a 2d model and a building  # noqa: E501
        """
        pass

    def test_create_checker_deprecated(self):
        """Test case for create_checker_deprecated

        Create a checker to a model  # noqa: E501
        """
        pass

    def test_create_checker_result_deprecated(self):
        """Test case for create_checker_result_deprecated

        Create a CheckerResult  # noqa: E501
        """
        pass

    def test_create_classification_element_relations_deprecated(self):
        """Test case for create_classification_element_relations_deprecated

        Create association between existing classification and existing element  # noqa: E501
        """
        pass

    def test_create_classifications_of_element_deprecated(self):
        """Test case for create_classifications_of_element_deprecated

        Create one or many classifications to an element  # noqa: E501
        """
        pass

    def test_create_element_deprecated(self):
        """Test case for create_element_deprecated

        Create an element in the model  # noqa: E501
        """
        pass

    def test_create_element_property_set_deprecated(self):
        """Test case for create_element_property_set_deprecated

        Create a PropertySets to an element  # noqa: E501
        """
        pass

    def test_create_element_property_set_property_definition_deprecated(self):
        """Test case for create_element_property_set_property_definition_deprecated

        Create a Definition to a Property  # noqa: E501
        """
        pass

    def test_create_element_property_set_property_definition_unit_deprecated(self):
        """Test case for create_element_property_set_property_definition_unit_deprecated

        Create a Unit to a Definition  # noqa: E501
        """
        pass

    def test_create_element_property_set_property_deprecated(self):
        """Test case for create_element_property_set_property_deprecated

        Create a property to a PropertySet  # noqa: E501
        """
        pass

    def test_create_ifc_deprecated(self):
        """Test case for create_ifc_deprecated

        Make a PDF or Image file a Model  # noqa: E501
        """
        pass

    def test_create_ifc_property_definition_deprecated(self):
        """Test case for create_ifc_property_definition_deprecated

        Create a PropertyDefinition on the model  # noqa: E501
        """
        pass

    def test_create_ifc_unit_deprecated(self):
        """Test case for create_ifc_unit_deprecated

        Create a Unit on a model  # noqa: E501
        """
        pass

    def test_create_layer_deprecated(self):
        """Test case for create_layer_deprecated

        Create a layer in the model  # noqa: E501
        """
        pass

    def test_create_meta_building_deprecated(self):
        """Test case for create_meta_building_deprecated

        Create an empty 3D Model  # noqa: E501
        """
        pass

    def test_create_property_set_deprecated(self):
        """Test case for create_property_set_deprecated

        Create one or many PropertySet  # noqa: E501
        """
        pass

    def test_create_property_set_element_relations_deprecated(self):
        """Test case for create_property_set_element_relations_deprecated

        Create association between PropertySet and element  # noqa: E501
        """
        pass

    def test_create_raw_elements_deprecated(self):
        """Test case for create_raw_elements_deprecated

        Create elements in an optimized format  # noqa: E501
        """
        pass

    def test_create_space_deprecated(self):
        """Test case for create_space_deprecated

        Create a space in the model  # noqa: E501
        """
        pass

    def test_create_storey_deprecated(self):
        """Test case for create_storey_deprecated

        Create a storey of a model  # noqa: E501
        """
        pass

    def test_create_storey_plan_deprecated(self):
        """Test case for create_storey_plan_deprecated

        Create a relation between a 2d model and a storey  # noqa: E501
        """
        pass

    def test_create_system_deprecated(self):
        """Test case for create_system_deprecated

        Create a system in the model  # noqa: E501
        """
        pass

    def test_create_zone_deprecated(self):
        """Test case for create_zone_deprecated

        Create a zone in the model  # noqa: E501
        """
        pass

    def test_create_zone_space_deprecated(self):
        """Test case for create_zone_space_deprecated

        Create a space in a zone  # noqa: E501
        """
        pass

    def test_delete_access_token_deprecated(self):
        """Test case for delete_access_token_deprecated

        Delete a token  # noqa: E501
        """
        pass

    def test_delete_building_deprecated(self):
        """Test case for delete_building_deprecated

        Delete a building of a model  # noqa: E501
        """
        pass

    def test_delete_building_plan_deprecated(self):
        """Test case for delete_building_plan_deprecated

        Delete the relation between a 2d model and a building  # noqa: E501
        """
        pass

    def test_delete_checker_deprecated(self):
        """Test case for delete_checker_deprecated

        Delete a checker of a model  # noqa: E501
        """
        pass

    def test_delete_checker_result_deprecated(self):
        """Test case for delete_checker_result_deprecated

        Delete a CheckerResult  # noqa: E501
        """
        pass

    def test_delete_element_deprecated(self):
        """Test case for delete_element_deprecated

        Delete an element of a model  # noqa: E501
        """
        pass

    def test_delete_ifc_deprecated(self):
        """Test case for delete_ifc_deprecated

        Delete a model  # noqa: E501
        """
        pass

    def test_delete_ifc_property_definition_deprecated(self):
        """Test case for delete_ifc_property_definition_deprecated

        Delete a PropertyDefinitions of a model  # noqa: E501
        """
        pass

    def test_delete_ifc_property_deprecated(self):
        """Test case for delete_ifc_property_deprecated

        Delete a Property of a model  # noqa: E501
        """
        pass

    def test_delete_ifc_unit_deprecated(self):
        """Test case for delete_ifc_unit_deprecated

        Delete a Unit of a model  # noqa: E501
        """
        pass

    def test_delete_ifc_without_doc_deprecated(self):
        """Test case for delete_ifc_without_doc_deprecated

        Delete the Model without deleting the related document  # noqa: E501
        """
        pass

    def test_delete_layer_deprecated(self):
        """Test case for delete_layer_deprecated

        Delete a layer of a model  # noqa: E501
        """
        pass

    def test_delete_property_set_deprecated(self):
        """Test case for delete_property_set_deprecated

        Delete a PropertySet of a model  # noqa: E501
        """
        pass

    def test_delete_space_deprecated(self):
        """Test case for delete_space_deprecated

        Delete a space  # noqa: E501
        """
        pass

    def test_delete_storey_deprecated(self):
        """Test case for delete_storey_deprecated

        Delete a storey of a model  # noqa: E501
        """
        pass

    def test_delete_storey_plan_deprecated(self):
        """Test case for delete_storey_plan_deprecated

        Delete the relation between a 2d model and a storey  # noqa: E501
        """
        pass

    def test_delete_system_deprecated(self):
        """Test case for delete_system_deprecated

        Delete a system of a model  # noqa: E501
        """
        pass

    def test_delete_zone_deprecated(self):
        """Test case for delete_zone_deprecated

        Delete a zone of a model  # noqa: E501
        """
        pass

    def test_delete_zone_space_deprecated(self):
        """Test case for delete_zone_space_deprecated

        Delete a space of a zone  # noqa: E501
        """
        pass

    def test_export_ifc_deprecated(self):
        """Test case for export_ifc_deprecated

        Export IFC  # noqa: E501
        """
        pass

    def test_full_update_element_deprecated(self):
        """Test case for full_update_element_deprecated

        Update all fields of an element  # noqa: E501
        """
        pass

    def test_get_access_token_deprecated(self):
        """Test case for get_access_token_deprecated

        Retrieve one token created for this model  # noqa: E501
        """
        pass

    def test_get_access_tokens_deprecated(self):
        """Test case for get_access_tokens_deprecated

        Retrieve all tokens created for this model  # noqa: E501
        """
        pass

    def test_get_building_deprecated(self):
        """Test case for get_building_deprecated

        Retrieve a building of a model  # noqa: E501
        """
        pass

    def test_get_building_plan_positioning_deprecated(self):
        """Test case for get_building_plan_positioning_deprecated

        Retrieve the postioning of the plan in the building  # noqa: E501
        """
        pass

    def test_get_buildings_deprecated(self):
        """Test case for get_buildings_deprecated

        Retrieve all buildings of a model  # noqa: E501
        """
        pass

    def test_get_checker_deprecated(self):
        """Test case for get_checker_deprecated

        Retrieve a checker of a model  # noqa: E501
        """
        pass

    def test_get_checker_result_deprecated(self):
        """Test case for get_checker_result_deprecated

        Retrieve one CheckerResult  # noqa: E501
        """
        pass

    def test_get_checker_results_deprecated(self):
        """Test case for get_checker_results_deprecated

        Retrieve all CheckerResults  # noqa: E501
        """
        pass

    def test_get_checkers_deprecated(self):
        """Test case for get_checkers_deprecated

        Retrieve all checkers of a model  # noqa: E501
        """
        pass

    def test_get_classifications_of_element_deprecated(self):
        """Test case for get_classifications_of_element_deprecated

        Retrieve all classifications of an element  # noqa: E501
        """
        pass

    def test_get_documents_of_element_deprecated(self):
        """Test case for get_documents_of_element_deprecated

        Retrieve all documents of an element  # noqa: E501
        """
        pass

    def test_get_element_deprecated(self):
        """Test case for get_element_deprecated

        Retrieve an element of a model  # noqa: E501
        """
        pass

    def test_get_element_linked_documents_deprecated(self):
        """Test case for get_element_linked_documents_deprecated

        Retrieve all documents linked to any element  # noqa: E501
        """
        pass

    def test_get_element_property_set_deprecated(self):
        """Test case for get_element_property_set_deprecated

        Retrieve a PropertySet of an element  # noqa: E501
        """
        pass

    def test_get_element_property_set_properties_deprecated(self):
        """Test case for get_element_property_set_properties_deprecated

        Retrieve all Properties of a PropertySet  # noqa: E501
        """
        pass

    def test_get_element_property_set_property_definition_deprecated(self):
        """Test case for get_element_property_set_property_definition_deprecated

        Retrieve a Definition of a Property  # noqa: E501
        """
        pass

    def test_get_element_property_set_property_definition_unit_deprecated(self):
        """Test case for get_element_property_set_property_definition_unit_deprecated

        Retrieve a Unit of a Definition  # noqa: E501
        """
        pass

    def test_get_element_property_set_property_definition_units_deprecated(self):
        """Test case for get_element_property_set_property_definition_units_deprecated

        Retrieve all Units of a Definition  # noqa: E501
        """
        pass

    def test_get_element_property_set_property_definitions_deprecated(self):
        """Test case for get_element_property_set_property_definitions_deprecated

        Retrieve all Definitions of a PropertySet  # noqa: E501
        """
        pass

    def test_get_element_property_set_property_deprecated(self):
        """Test case for get_element_property_set_property_deprecated

        Retrieve a Property of a PropertySet  # noqa: E501
        """
        pass

    def test_get_element_property_sets_deprecated(self):
        """Test case for get_element_property_sets_deprecated

        Retrieve all PropertySets of an element  # noqa: E501
        """
        pass

    def test_get_elements_deprecated(self):
        """Test case for get_elements_deprecated

        Retrieve all elements of a model  # noqa: E501
        """
        pass

    def test_get_elements_from_classification_deprecated(self):
        """Test case for get_elements_from_classification_deprecated

        Retrieve all elements with the classification  # noqa: E501
        """
        pass

    def test_get_ifc_classifications_deprecated(self):
        """Test case for get_ifc_classifications_deprecated

        Retrieve all classifications in a model  # noqa: E501
        """
        pass

    def test_get_ifc_deprecated(self):
        """Test case for get_ifc_deprecated

        Retrieve one model  # noqa: E501
        """
        pass

    def test_get_ifc_material_deprecated(self):
        """Test case for get_ifc_material_deprecated

        Retrieve a material of a model  # noqa: E501
        """
        pass

    def test_get_ifc_materials_deprecated(self):
        """Test case for get_ifc_materials_deprecated

        Retrieve all materials of a model  # noqa: E501
        """
        pass

    def test_get_ifc_properties_deprecated(self):
        """Test case for get_ifc_properties_deprecated

        Retrieve all Properties of a model  # noqa: E501
        """
        pass

    def test_get_ifc_property_definition_deprecated(self):
        """Test case for get_ifc_property_definition_deprecated

        Retrieve a PropertyDefinition of a model  # noqa: E501
        """
        pass

    def test_get_ifc_property_definitions_deprecated(self):
        """Test case for get_ifc_property_definitions_deprecated

        Retrieve all PropertyDefinitions of a model  # noqa: E501
        """
        pass

    def test_get_ifc_property_deprecated(self):
        """Test case for get_ifc_property_deprecated

        Retrieve a Property of a model  # noqa: E501
        """
        pass

    def test_get_ifc_unit_deprecated(self):
        """Test case for get_ifc_unit_deprecated

        Retrieve a Unit of a model  # noqa: E501
        """
        pass

    def test_get_ifc_units_deprecated(self):
        """Test case for get_ifc_units_deprecated

        Retrieve all Units of a model  # noqa: E501
        """
        pass

    def test_get_ifcs_deprecated(self):
        """Test case for get_ifcs_deprecated

        Retrieve all models  # noqa: E501
        """
        pass

    def test_get_layer_deprecated(self):
        """Test case for get_layer_deprecated

        Retrieve a layer of a model  # noqa: E501
        """
        pass

    def test_get_layers_deprecated(self):
        """Test case for get_layers_deprecated

        Retrieve all layers of a model  # noqa: E501
        """
        pass

    def test_get_material_deprecated(self):
        """Test case for get_material_deprecated

        Retrieve a material of a model  # noqa: E501
        """
        pass

    def test_get_materials_deprecated(self):
        """Test case for get_materials_deprecated

        Retrieve all materials of a model  # noqa: E501
        """
        pass

    def test_get_processor_handler_deprecated(self):
        """Test case for get_processor_handler_deprecated

        Retrieve a processor handler  # noqa: E501
        """
        pass

    def test_get_processor_handlers_deprecated(self):
        """Test case for get_processor_handlers_deprecated

        Get all processor handlers  # noqa: E501
        """
        pass

    def test_get_property_set_deprecated(self):
        """Test case for get_property_set_deprecated

        Retrieve a PropertySet of a model  # noqa: E501
        """
        pass

    def test_get_property_sets_deprecated(self):
        """Test case for get_property_sets_deprecated

        Retrieve all PropertySets of a model  # noqa: E501
        """
        pass

    def test_get_raw_elements_deprecated(self):
        """Test case for get_raw_elements_deprecated

        Retrieve all elements in a optimized format  # noqa: E501
        """
        pass

    def test_get_simple_element_deprecated(self):
        """Test case for get_simple_element_deprecated

        Retrieve an element of a model with a simple value representation  # noqa: E501
        """
        pass

    def test_get_simple_elements_deprecated(self):
        """Test case for get_simple_elements_deprecated

        Retrieve all elements of a model with a simple value representation  # noqa: E501
        """
        pass

    def test_get_space_deprecated(self):
        """Test case for get_space_deprecated

        Retrieve one space of the model  # noqa: E501
        """
        pass

    def test_get_spaces_deprecated(self):
        """Test case for get_spaces_deprecated

        Retrieve all spaces of the model  # noqa: E501
        """
        pass

    def test_get_storey_deprecated(self):
        """Test case for get_storey_deprecated

        Retrieve a storey of a model  # noqa: E501
        """
        pass

    def test_get_storey_plan_positioning_deprecated(self):
        """Test case for get_storey_plan_positioning_deprecated

        Retrieve the postioning of the plan in the storey  # noqa: E501
        """
        pass

    def test_get_storeys_deprecated(self):
        """Test case for get_storeys_deprecated

        Retrieve all storeys of a model  # noqa: E501
        """
        pass

    def test_get_system_deprecated(self):
        """Test case for get_system_deprecated

        Retrieve a system of a model  # noqa: E501
        """
        pass

    def test_get_systems_deprecated(self):
        """Test case for get_systems_deprecated

        Retrieve all systems of a model  # noqa: E501
        """
        pass

    def test_get_zone_deprecated(self):
        """Test case for get_zone_deprecated

        Retrieve one zone of a model  # noqa: E501
        """
        pass

    def test_get_zone_space_deprecated(self):
        """Test case for get_zone_space_deprecated

        Retrieve one space of a zone  # noqa: E501
        """
        pass

    def test_get_zone_spaces_deprecated(self):
        """Test case for get_zone_spaces_deprecated

        Retrieve all spaces of a zone  # noqa: E501
        """
        pass

    def test_get_zones_deprecated(self):
        """Test case for get_zones_deprecated

        Retrieve zones of a model  # noqa: E501
        """
        pass

    def test_launch_new_check_deprecated(self):
        """Test case for launch_new_check_deprecated

        Launch a new check on the model  # noqa: E501
        """
        pass

    def test_link_documents_of_element_deprecated(self):
        """Test case for link_documents_of_element_deprecated

        Link one or many documents to an element  # noqa: E501
        """
        pass

    def test_list_classification_element_relations_deprecated(self):
        """Test case for list_classification_element_relations_deprecated

        List all associations between classifications and elements  # noqa: E501
        """
        pass

    def test_merge_ifcs_deprecated(self):
        """Test case for merge_ifcs_deprecated

        Merge IFC files  # noqa: E501
        """
        pass

    def test_optimize_ifc_deprecated(self):
        """Test case for optimize_ifc_deprecated

        Optimize the IFC  # noqa: E501
        """
        pass

    def test_remove_all_element_property_set_deprecated(self):
        """Test case for remove_all_element_property_set_deprecated

        Remove all property sets from element  # noqa: E501
        """
        pass

    def test_remove_classification_of_element_deprecated(self):
        """Test case for remove_classification_of_element_deprecated

        Remove a classification from an element  # noqa: E501
        """
        pass

    def test_remove_document_of_element_deprecated(self):
        """Test case for remove_document_of_element_deprecated

        Remove a documents from an element  # noqa: E501
        """
        pass

    def test_remove_element_property_set_deprecated(self):
        """Test case for remove_element_property_set_deprecated

        Remove a PropertySet from an element  # noqa: E501
        """
        pass

    def test_remove_element_property_set_property_definition_deprecated(self):
        """Test case for remove_element_property_set_property_definition_deprecated

        Delete a Definition to a Property  # noqa: E501
        """
        pass

    def test_remove_element_property_set_property_definition_unit_deprecated(self):
        """Test case for remove_element_property_set_property_definition_unit_deprecated

        Remove a Unit from a Definition  # noqa: E501
        """
        pass

    def test_remove_element_property_set_property_deprecated(self):
        """Test case for remove_element_property_set_property_deprecated

        Remove a property from a PropertySet  # noqa: E501
        """
        pass

    def test_remove_elements_from_classification_deprecated(self):
        """Test case for remove_elements_from_classification_deprecated

        Remove the classification from all elements  # noqa: E501
        """
        pass

    def test_reprocess_ifc_deprecated(self):
        """Test case for reprocess_ifc_deprecated

        Reprocess Model file  # noqa: E501
        """
        pass

    def test_update_access_token_deprecated(self):
        """Test case for update_access_token_deprecated

        Update some fields of a token  # noqa: E501
        """
        pass

    def test_update_building_deprecated(self):
        """Test case for update_building_deprecated

        Update some fields of a building  # noqa: E501
        """
        pass

    def test_update_building_plan_positioning_deprecated(self):
        """Test case for update_building_plan_positioning_deprecated

        Update the postioning of the plan in the building  # noqa: E501
        """
        pass

    def test_update_checker_deprecated(self):
        """Test case for update_checker_deprecated

        Update some fields of a checker of a model  # noqa: E501
        """
        pass

    def test_update_checker_result_deprecated(self):
        """Test case for update_checker_result_deprecated

        Update some fields of a CheckerResult  # noqa: E501
        """
        pass

    def test_update_element_deprecated(self):
        """Test case for update_element_deprecated

        Update some fields of an element  # noqa: E501
        """
        pass

    def test_update_element_property_set_property_deprecated(self):
        """Test case for update_element_property_set_property_deprecated

        Update a property from an element  # noqa: E501
        """
        pass

    def test_update_ifc_deprecated(self):
        """Test case for update_ifc_deprecated

        Update some fields of a model  # noqa: E501
        """
        pass

    def test_update_ifc_files_deprecated(self):
        """Test case for update_ifc_files_deprecated

        Update models file (gltf, svg, structure, etc)  # noqa: E501
        """
        pass

    def test_update_ifc_property_definition_deprecated(self):
        """Test case for update_ifc_property_definition_deprecated

        Update some fields of many PropertyDefinitions of a model  # noqa: E501
        """
        pass

    def test_update_ifc_property_deprecated(self):
        """Test case for update_ifc_property_deprecated

        Update some fields of a Property  # noqa: E501
        """
        pass

    def test_update_ifc_unit_deprecated(self):
        """Test case for update_ifc_unit_deprecated

        Update some fields of a Unit of a model  # noqa: E501
        """
        pass

    def test_update_layer_deprecated(self):
        """Test case for update_layer_deprecated

        Update some fields of a layer  # noqa: E501
        """
        pass

    def test_update_order_building_plan_deprecated(self):
        """Test case for update_order_building_plan_deprecated

        Update order of all plan of a building  # noqa: E501
        """
        pass

    def test_update_order_storey_plan_deprecated(self):
        """Test case for update_order_storey_plan_deprecated

        Update order of all plan of a storey  # noqa: E501
        """
        pass

    def test_update_order_storeys_deprecated(self):
        """Test case for update_order_storeys_deprecated

        Update order of all storey of a model  # noqa: E501
        """
        pass

    def test_update_processor_handler_deprecated(self):
        """Test case for update_processor_handler_deprecated

        Update the status of a processor handler  # noqa: E501
        """
        pass

    def test_update_property_set_deprecated(self):
        """Test case for update_property_set_deprecated

        Update some fields of a PropertySet  # noqa: E501
        """
        pass

    def test_update_space_deprecated(self):
        """Test case for update_space_deprecated

        Update some fields of a space  # noqa: E501
        """
        pass

    def test_update_storey_deprecated(self):
        """Test case for update_storey_deprecated

        Update some fields of a storey  # noqa: E501
        """
        pass

    def test_update_storey_plan_positioning_deprecated(self):
        """Test case for update_storey_plan_positioning_deprecated

        Update the postioning of the plan in the storey  # noqa: E501
        """
        pass

    def test_update_system_deprecated(self):
        """Test case for update_system_deprecated

        Update some fields of a system  # noqa: E501
        """
        pass

    def test_update_zone_deprecated(self):
        """Test case for update_zone_deprecated

        Update some fields of a zone  # noqa: E501
        """
        pass

    def test_update_zone_space_deprecated(self):
        """Test case for update_zone_space_deprecated

        Update some fields of a space  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
