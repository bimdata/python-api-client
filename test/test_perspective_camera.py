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
from bimdata_api_client.models.perspective_camera import PerspectiveCamera  # noqa: E501
from bimdata_api_client.rest import ApiException

class TestPerspectiveCamera(unittest.TestCase):
    """PerspectiveCamera unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PerspectiveCamera
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = bimdata_api_client.models.perspective_camera.PerspectiveCamera()  # noqa: E501
        if include_optional :
            return PerspectiveCamera(
                field_of_view = 1.337, 
                camera_direction = bimdata_api_client.models.direction.Direction(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ), 
                camera_up_vector = bimdata_api_client.models.direction.Direction(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ), 
                camera_view_point = bimdata_api_client.models.point.Point(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ), 
                bimdata_camera_direction = bimdata_api_client.models.direction.Direction(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, )
            )
        else :
            return PerspectiveCamera(
                field_of_view = 1.337,
                camera_direction = bimdata_api_client.models.direction.Direction(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
                camera_up_vector = bimdata_api_client.models.direction.Direction(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
                camera_view_point = bimdata_api_client.models.point.Point(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
        )

    def testPerspectiveCamera(self):
        """Test PerspectiveCamera"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
