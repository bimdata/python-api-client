# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import bimdata_api_client
from bimdata_api_client.models.material_list_component import MaterialListComponent  # noqa: E501
from bimdata_api_client.rest import ApiException

class TestMaterialListComponent(unittest.TestCase):
    """MaterialListComponent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MaterialListComponent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = bimdata_api_client.models.material_list_component.MaterialListComponent()  # noqa: E501
        if include_optional :
            return MaterialListComponent(
                material = bimdata_api_client.models.material.Material(
                    id = 56, 
                    name = '0', 
                    category = '0', 
                    description = '0', 
                    property_sets = [
                        bimdata_api_client.models.property_set.PropertySet(
                            id = 56, 
                            name = '0', 
                            description = '0', 
                            type = '0', 
                            properties = [
                                bimdata_api_client.models.property.Property(
                                    id = 56, 
                                    definition = bimdata_api_client.models.property_definition.PropertyDefinition(
                                        id = 56, 
                                        unit = bimdata_api_client.models.unit.Unit(
                                            id = 56, 
                                            type = '0', 
                                            name = '0', 
                                            unit_type = '0', 
                                            prefix = '0', 
                                            dimensions = [
                                                1.337
                                                ], 
                                            conversion_factor = 1.337, 
                                            conversion_baseunit = bimdata_api_client.models.unit.Unit(
                                                id = 56, 
                                                type = '0', 
                                                name = '0', 
                                                unit_type = '0', 
                                                prefix = '0', 
                                                conversion_factor = 1.337, 
                                                elements = bimdata_api_client.models.elements.Elements(), 
                                                is_default = True, ), 
                                            elements = bimdata_api_client.models.elements.Elements(), 
                                            is_default = True, ), 
                                        name = '0', 
                                        description = '0', 
                                        type = '0', 
                                        value_type = '0', ), 
                                    value = bimdata_api_client.models.value.Value(), 
                                    property_set_id = '0', 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], ), 
                option = bimdata_api_client.models.material_option.MaterialOption(
                    id = 56, 
                    thickness = 1.337, 
                    list_components = [
                        {
                            'key' : '0'
                            }
                        ], )
            )
        else :
            return MaterialListComponent(
                option = bimdata_api_client.models.material_option.MaterialOption(
                    id = 56, 
                    thickness = 1.337, 
                    list_components = [
                        {
                            'key' : '0'
                            }
                        ], ),
        )

    def testMaterialListComponent(self):
        """Test MaterialListComponent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
