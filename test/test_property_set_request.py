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
from bimdata-api-client.model.property_request import PropertyRequest
globals()['PropertyRequest'] = PropertyRequest
from bimdata-api-client.model.property_set_request import PropertySetRequest


class TestPropertySetRequest(unittest.TestCase):
    """PropertySetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPropertySetRequest(self):
        """Test PropertySetRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PropertySetRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
