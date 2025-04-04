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
from bimdata-api-client.model.component import Component
from bimdata-api-client.model.view_setup_hints import ViewSetupHints
globals()['Component'] = Component
globals()['ViewSetupHints'] = ViewSetupHints
from bimdata-api-client.model.visibility import Visibility


class TestVisibility(unittest.TestCase):
    """Visibility unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVisibility(self):
        """Test Visibility"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Visibility()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
