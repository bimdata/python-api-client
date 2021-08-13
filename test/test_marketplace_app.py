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
from bimdata_api_client.models.marketplace_app import MarketplaceApp  # noqa: E501
from bimdata_api_client.rest import ApiException

class TestMarketplaceApp(unittest.TestCase):
    """MarketplaceApp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MarketplaceApp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = bimdata_api_client.models.marketplace_app.MarketplaceApp()  # noqa: E501
        if include_optional :
            return MarketplaceApp(
                id = 56, 
                name = '0', 
                short_description = '0', 
                long_description = '0', 
                activation_webhook_url = '0', 
                post_activation_redirect_uri = '0', 
                viewer_plugins_urls = [
                    '0'
                    ], 
                webhook_secret = '0', 
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
                scopes = [
                    '0'
                    ], 
                settings_url = '0', 
                is_public = True, 
                tags = [
                    '0'
                    ], 
                logo = '0', 
                images = [
                    bimdata_api_client.models.marketplace_app_image.MarketplaceAppImage(
                        id = 56, 
                        image = '0', 
                        order = 56, )
                    ], 
                organization_id = '0'
            )
        else :
            return MarketplaceApp(
                name = '0',
                short_description = '0',
                long_description = '0',
        )

    def testMarketplaceApp(self):
        """Test MarketplaceApp"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
