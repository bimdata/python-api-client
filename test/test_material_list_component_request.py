"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1 (v1)
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import bimdata_api_client
from bimdata_api_client.model.material_request import MaterialRequest
globals()['MaterialRequest'] = MaterialRequest
from bimdata_api_client.model.material_list_component_request import MaterialListComponentRequest


class TestMaterialListComponentRequest(unittest.TestCase):
    """MaterialListComponentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMaterialListComponentRequest(self):
        """Test MaterialListComponentRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MaterialListComponentRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()