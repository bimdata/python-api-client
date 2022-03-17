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
from bimdata_api_client.models.visa import Visa  # noqa: E501
from bimdata_api_client.rest import ApiException

class TestVisa(unittest.TestCase):
    """Visa unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Visa
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = bimdata_api_client.models.visa.Visa()  # noqa: E501
        if include_optional :
            return Visa(
                id = 56, 
                validations = [
                    bimdata_api_client.models.visa_validation.VisaValidation(
                        id = 56, 
                        visa_id = '0', 
                        validator = bimdata_api_client.models.user_project.UserProject(
                            id = 56, 
                            user_id = 56, 
                            invitation_id = 56, 
                            email = '0', 
                            firstname = '0', 
                            lastname = '0', 
                            profile_picture = '0', 
                            role = 56, ), 
                        validator_id = 56, 
                        status = 'P', 
                        has_commented = True, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
                validations_in_error = [
                    56
                    ], 
                creator = bimdata_api_client.models.user_project.UserProject(
                    id = 56, 
                    user_id = 56, 
                    invitation_id = 56, 
                    email = '0', 
                    firstname = '0', 
                    lastname = '0', 
                    profile_picture = '0', 
                    role = 56, ), 
                creator_id = 56, 
                status = 'O', 
                description = '0', 
                document = bimdata_api_client.models.document.Document(
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
                    user_permission = 56, ), 
                comments = [
                    bimdata_api_client.models.visa_comment.VisaComment(
                        id = 56, 
                        author = bimdata_api_client.models.user_project.UserProject(
                            id = 56, 
                            user_id = 56, 
                            invitation_id = 56, 
                            email = '0', 
                            firstname = '0', 
                            lastname = '0', 
                            profile_picture = '0', 
                            role = 56, ), 
                        author_id = 56, 
                        visa_id = '0', 
                        content = '0', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
                deadline = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return Visa(
        )

    def testVisa(self):
        """Test Visa"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
