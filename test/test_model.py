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
from bimdata_api_client.model.mask2_d import Mask2D
from bimdata_api_client.model.model_document import ModelDocument
from bimdata_api_client.model.model_serializer_without_children import ModelSerializerWithoutChildren
from bimdata_api_client.model.transform import Transform
from bimdata_api_client.model.user import User
from bimdata_api_client.model.xkt_file import XktFile
globals()['Mask2D'] = Mask2D
globals()['ModelDocument'] = ModelDocument
globals()['ModelSerializerWithoutChildren'] = ModelSerializerWithoutChildren
globals()['Transform'] = Transform
globals()['User'] = User
globals()['XktFile'] = XktFile
from bimdata_api_client.model.model import Model


class TestModel(unittest.TestCase):
    """Model unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testModel(self):
        """Test Model"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Model()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
