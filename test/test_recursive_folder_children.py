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
from bimdata-api-client.model.short_user import ShortUser
from bimdata-api-client.model.tag import Tag
globals()['ShortUser'] = ShortUser
globals()['Tag'] = Tag
from bimdata-api-client.model.recursive_folder_children import RecursiveFolderChildren


class TestRecursiveFolderChildren(unittest.TestCase):
    """RecursiveFolderChildren unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRecursiveFolderChildren(self):
        """Test RecursiveFolderChildren"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RecursiveFolderChildren()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
