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
from bimdata_api_client.models.folder import Folder  # noqa: E501
from bimdata_api_client.rest import ApiException

class TestFolder(unittest.TestCase):
    """Folder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Folder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = bimdata_api_client.models.folder.Folder()  # noqa: E501
        if include_optional :
            return Folder(
                id = 56, 
                parent_id = 56, 
                type = '0', 
                nature = '0', 
                name = '0', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = bimdata_api_client.models.user.User(
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
                    profile_picture = '0', ), 
                groups_permissions = [
                    bimdata_api_client.models.folder_group_permission.FolderGroupPermission(
                        group = bimdata_api_client.models.inline_response_200_1.inline_response_200_1(
                            id = 56, 
                            name = '0', 
                            color = '0', 
                            members = [
                                bimdata_api_client.models.user_project.UserProject(
                                    id = 56, 
                                    user_id = 56, 
                                    invitation_id = 56, 
                                    email = '0', 
                                    firstname = '0', 
                                    lastname = '0', 
                                    profile_picture = '0', 
                                    role = 56, )
                                ], ), 
                        permission = 56, )
                    ], 
                default_permission = 56, 
                user_permission = 56, 
                children = [
                    bimdata_api_client.models.recursive_folder_children.RecursiveFolderChildren(
                        id = 56, 
                        parent_id = 56, 
                        created_by = bimdata_api_client.models.user.User(
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
                            profile_picture = '0', ), 
                        creator = bimdata_api_client.models.user.User(
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
                            profile_picture = '0', ), 
                        type = 'Folder', 
                        nature = 'Folder', 
                        model_type = 'IFC', 
                        name = '0', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        file_name = '0', 
                        description = '0', 
                        size = 56, 
                        model_id = 56, 
                        ifc_id = 56, 
                        file = '0', 
                        groups_permissions = [
                            bimdata_api_client.models.folder_group_permission.FolderGroupPermission(
                                group = bimdata_api_client.models.inline_response_200_1.inline_response_200_1(
                                    id = 56, 
                                    name = '0', 
                                    color = '0', 
                                    members = [
                                        bimdata_api_client.models.user_project.UserProject(
                                            id = 56, 
                                            user_id = 56, 
                                            invitation_id = 56, 
                                            email = '0', 
                                            firstname = '0', 
                                            lastname = '0', 
                                            profile_picture = '0', 
                                            role = 56, )
                                        ], ), 
                                permission = 56, )
                            ], 
                        default_permission = 56, 
                        user_permission = 56, 
                        children = [
                            bimdata_api_client.models.recursive_folder_children.RecursiveFolderChildren(
                                id = 56, 
                                parent_id = 56, 
                                type = 'Folder', 
                                nature = 'Folder', 
                                model_type = 'IFC', 
                                name = '0', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                file_name = '0', 
                                description = '0', 
                                size = 56, 
                                model_id = 56, 
                                ifc_id = 56, 
                                file = '0', 
                                default_permission = 56, 
                                user_permission = 56, )
                            ], )
                    ]
            )
        else :
            return Folder(
                name = '0',
        )

    def testFolder(self):
        """Test Folder"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
