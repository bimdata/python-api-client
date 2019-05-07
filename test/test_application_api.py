# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import bimdata_api_client
from bimdata_api_client.api.application_api import ApplicationApi  # noqa: E501
from bimdata_api_client.rest import ApiException


class TestApplicationApi(unittest.TestCase):
    """ApplicationApi unit test stubs"""

    def setUp(self):
        self.api = bimdata_api_client.api.application_api.ApplicationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_web_hook(self):
        """Test case for create_web_hook

        Create a new Webhook  # noqa: E501
        """
        pass

    def test_delete_web_hook(self):
        """Test case for delete_web_hook

        Delete a webhook  # noqa: E501
        """
        pass

    def test_full_update_web_hook(self):
        """Test case for full_update_web_hook

        Update all field of a webhook  # noqa: E501
        """
        pass

    def test_get_web_hook(self):
        """Test case for get_web_hook

        Retrieve one configured webhook  # noqa: E501
        """
        pass

    def test_get_web_hooks(self):
        """Test case for get_web_hooks

        Retrieve all configured webhooks  # noqa: E501
        """
        pass

    def test_ping_web_hook(self):
        """Test case for ping_web_hook

        Test a webhook  # noqa: E501
        """
        pass

    def test_update_web_hook(self):
        """Test case for update_web_hook

        Update some field of a webhook  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
