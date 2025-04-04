"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1 (v1)
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import bimdata-api-client
from bimdata-api-client.model.coloring_request import ColoringRequest
from bimdata-api-client.model.component_request import ComponentRequest
from bimdata-api-client.model.visibility_request import VisibilityRequest
globals()['ColoringRequest'] = ColoringRequest
globals()['ComponentRequest'] = ComponentRequest
globals()['VisibilityRequest'] = VisibilityRequest
from bimdata-api-client.model.components_parent_request import ComponentsParentRequest


class TestComponentsParentRequest(unittest.TestCase):
    """ComponentsParentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testComponentsParentRequest(self):
        """Test ComponentsParentRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ComponentsParentRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
