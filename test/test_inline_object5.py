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
from bimdata_api_client.models.inline_object5 import InlineObject5  # noqa: E501
from bimdata_api_client.rest import ApiException

class TestInlineObject5(unittest.TestCase):
    """InlineObject5 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject5
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = bimdata_api_client.models.inline_object5.InlineObject5()  # noqa: E501
        if include_optional :
            return InlineObject5(
                id = 56, 
                name = '0', 
                color = '0', 
                members = [
                    bimdata_api_client.models.user.User(
                        id = 56, 
                        email = '0', 
                        firstname = '0', 
                        lastname = '0', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        cloud_role = 56, 
                        project_role = 56, 
                        provider = '0', 
                        sub = '0', 
                        profile_picture = '0', )
                    ]
            )
        else :
            return InlineObject5(
                name = '0',
        )

    def testInlineObject5(self):
        """Test InlineObject5"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
