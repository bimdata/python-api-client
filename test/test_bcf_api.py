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

import bimdata_api_client
from bimdata_api_client.api.bcf_api import BcfApi  # noqa: E501
from bimdata_api_client.rest import ApiException


class TestBcfApi(unittest.TestCase):
    """BcfApi unit test stubs"""

    def setUp(self):
        self.api = bimdata_api_client.api.bcf_api.BcfApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_comment(self):
        """Test case for create_comment

        Create a comment  # noqa: E501
        """
        pass

    def test_create_extension_label(self):
        """Test case for create_extension_label

        Create a Label  # noqa: E501
        """
        pass

    def test_create_extension_priority(self):
        """Test case for create_extension_priority

        Create a Priority  # noqa: E501
        """
        pass

    def test_create_extension_stage(self):
        """Test case for create_extension_stage

        Create a Stage  # noqa: E501
        """
        pass

    def test_create_extension_status(self):
        """Test case for create_extension_status

        Create a TopicStatus  # noqa: E501
        """
        pass

    def test_create_extension_type(self):
        """Test case for create_extension_type

        Create a TopicType  # noqa: E501
        """
        pass

    def test_create_full_topic(self):
        """Test case for create_full_topic

        Create a Topic with viewpoints and comments  # noqa: E501
        """
        pass

    def test_create_topic(self):
        """Test case for create_topic

        Create a topic  # noqa: E501
        """
        pass

    def test_create_viewpoint(self):
        """Test case for create_viewpoint

        Create a Viewpoint  # noqa: E501
        """
        pass

    def test_delete_comment(self):
        """Test case for delete_comment

        Delete a comment  # noqa: E501
        """
        pass

    def test_delete_extension_label(self):
        """Test case for delete_extension_label

        Delete a Label  # noqa: E501
        """
        pass

    def test_delete_extension_priority(self):
        """Test case for delete_extension_priority

        Delete a Priority  # noqa: E501
        """
        pass

    def test_delete_extension_stage(self):
        """Test case for delete_extension_stage

        Delete a Stage  # noqa: E501
        """
        pass

    def test_delete_extension_status(self):
        """Test case for delete_extension_status

        Delete a TopicStatus  # noqa: E501
        """
        pass

    def test_delete_extension_type(self):
        """Test case for delete_extension_type

        Delete a TopicType  # noqa: E501
        """
        pass

    def test_delete_topic(self):
        """Test case for delete_topic

        Delete a topic  # noqa: E501
        """
        pass

    def test_delete_viewpoint(self):
        """Test case for delete_viewpoint

        Delete a Viewpoint  # noqa: E501
        """
        pass

    def test_download_bcf_export(self):
        """Test case for download_bcf_export

        Export project's topics in bcf-xml format  # noqa: E501
        """
        pass

    def test_full_update_bcf_project(self):
        """Test case for full_update_bcf_project

        Update all fields of a BCF project  # noqa: E501
        """
        pass

    def test_full_update_comment(self):
        """Test case for full_update_comment

        Update all fields of a comment  # noqa: E501
        """
        pass

    def test_full_update_full_topic(self):
        """Test case for full_update_full_topic

        Update all fields of a topic  # noqa: E501
        """
        pass

    def test_full_update_topic(self):
        """Test case for full_update_topic

        Update all fields of a topic  # noqa: E501
        """
        pass

    def test_full_update_viewpoint(self):
        """Test case for full_update_viewpoint

        Update all fields of a Viewpoint  # noqa: E501
        """
        pass

    def test_get_bcf_project(self):
        """Test case for get_bcf_project

        Retrieve a BCF project  # noqa: E501
        """
        pass

    def test_get_bcf_projects(self):
        """Test case for get_bcf_projects

        Retrieve all BCF projects  # noqa: E501
        """
        pass

    def test_get_colorings(self):
        """Test case for get_colorings

        Retrieve all colorings of a viewpoint  # noqa: E501
        """
        pass

    def test_get_comment(self):
        """Test case for get_comment

        Retrieve a comment  # noqa: E501
        """
        pass

    def test_get_comments(self):
        """Test case for get_comments

        Retrieve all comments  # noqa: E501
        """
        pass

    def test_get_detailed_extensions(self):
        """Test case for get_detailed_extensions

        Retrieve project detailed extensions  # noqa: E501
        """
        pass

    def test_get_extensions(self):
        """Test case for get_extensions

        Retrieve project extensions  # noqa: E501
        """
        pass

    def test_get_full_topic(self):
        """Test case for get_full_topic

        Retrieve a full topic  # noqa: E501
        """
        pass

    def test_get_full_topics(self):
        """Test case for get_full_topics

        Retrieve all full topics  # noqa: E501
        """
        pass

    def test_get_selections(self):
        """Test case for get_selections

        Retrieve all selections of a viewpoint  # noqa: E501
        """
        pass

    def test_get_snapshot(self):
        """Test case for get_snapshot

        Retrieve the viewpoint' snapshot  # noqa: E501
        """
        pass

    def test_get_topic(self):
        """Test case for get_topic

        Retrieve a topic  # noqa: E501
        """
        pass

    def test_get_topic_viewpoints(self):
        """Test case for get_topic_viewpoints

        Retrieve all viewpoints attached to the topic  # noqa: E501
        """
        pass

    def test_get_topics(self):
        """Test case for get_topics

        Retrieve all topics  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get current user info  # noqa: E501
        """
        pass

    def test_get_viewpoint(self):
        """Test case for get_viewpoint

        Retrieve a Viewpoint  # noqa: E501
        """
        pass

    def test_get_viewpoints(self):
        """Test case for get_viewpoints

        Retrieve all Viewpoints of a topic  # noqa: E501
        """
        pass

    def test_get_visibilities(self):
        """Test case for get_visibilities

        Retrieve all visibilities of a viewpoint  # noqa: E501
        """
        pass

    def test_import_bcf(self):
        """Test case for import_bcf

        Import bcf-xml format into this project  # noqa: E501
        """
        pass

    def test_update_bcf_project(self):
        """Test case for update_bcf_project

        Update some fields of a BCF project  # noqa: E501
        """
        pass

    def test_update_comment(self):
        """Test case for update_comment

        Update some fields of a comment  # noqa: E501
        """
        pass

    def test_update_extension_label(self):
        """Test case for update_extension_label

        Update a Label  # noqa: E501
        """
        pass

    def test_update_extension_priority(self):
        """Test case for update_extension_priority

        Update a Priority  # noqa: E501
        """
        pass

    def test_update_extension_stage(self):
        """Test case for update_extension_stage

        Update a Stage  # noqa: E501
        """
        pass

    def test_update_extension_status(self):
        """Test case for update_extension_status

        Update a TopicStatus  # noqa: E501
        """
        pass

    def test_update_extension_type(self):
        """Test case for update_extension_type

        Update a TopicType  # noqa: E501
        """
        pass

    def test_update_full_topic(self):
        """Test case for update_full_topic

        Update some fields of a topic  # noqa: E501
        """
        pass

    def test_update_topic(self):
        """Test case for update_topic

        Update some fields of a topic  # noqa: E501
        """
        pass

    def test_update_viewpoint(self):
        """Test case for update_viewpoint

        Update some fields of a Viewpoint  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
