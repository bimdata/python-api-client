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
from bimdata_api_client.models.document import Document  # noqa: E501
from bimdata_api_client.rest import ApiException

class TestDocument(unittest.TestCase):
    """Document unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Document
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = bimdata_api_client.models.document.Document()  # noqa: E501
        if include_optional :
            return Document(
                id = 56, 
                parent = 56, 
                parent_id = 56, 
                creator = 56, 
                project = 56, 
                name = '0', 
                file_name = '0', 
                description = '0', 
                file = '0', 
                size = 0, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                model_source = 'UPLOAD', 
                model_id = '0', 
                ifc_source = 'UPLOAD', 
                ifc_id = '0', 
                user_permission = 56
            )
        else :
            return Document(
                name = '0',
        )

    def testDocument(self):
        """Test Document"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
