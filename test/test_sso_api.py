"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1 (v1)
    Generated by: https://openapi-generator.tech
"""


import unittest

import bimdata_api_client
from bimdata_api_client.api.sso_api import SsoApi  # noqa: E501


class TestSsoApi(unittest.TestCase):
    """SsoApi unit test stubs"""

    def setUp(self):
        self.api = SsoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accept_invitation(self):
        """Test case for accept_invitation

        Accept an invitation  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete user from BIMData  # noqa: E501
        """
        pass

    def test_deny_invitation(self):
        """Test case for deny_invitation

        Deny an invitation  # noqa: E501
        """
        pass

    def test_get_invitation(self):
        """Test case for get_invitation

        Retrieve an invitation  # noqa: E501
        """
        pass

    def test_get_invitations(self):
        """Test case for get_invitations

        Retrieve all invitations  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
