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
from bimdata-api-client.model.zone import Zone
from bimdata-api-client.model.zone_space_request import ZoneSpaceRequest
globals()['Zone'] = Zone
globals()['ZoneSpaceRequest'] = ZoneSpaceRequest
from bimdata-api-client.model.zone_request import ZoneRequest


class TestZoneRequest(unittest.TestCase):
    """ZoneRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testZoneRequest(self):
        """Test ZoneRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ZoneRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
