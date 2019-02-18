# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class IfcFiles(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'structure_file': 'str',
        'systems_file': 'str',
        'map_file': 'str',
        'gltf_file': 'str',
        'bvh_tree_file': 'str',
        'viewer_360_file': 'str'
    }

    attribute_map = {
        'structure_file': 'structure_file',
        'systems_file': 'systems_file',
        'map_file': 'map_file',
        'gltf_file': 'gltf_file',
        'bvh_tree_file': 'bvh_tree_file',
        'viewer_360_file': 'viewer_360_file'
    }

    def __init__(self, structure_file=None, systems_file=None, map_file=None, gltf_file=None, bvh_tree_file=None, viewer_360_file=None):  # noqa: E501
        """IfcFiles - a model defined in OpenAPI"""  # noqa: E501

        self._structure_file = None
        self._systems_file = None
        self._map_file = None
        self._gltf_file = None
        self._bvh_tree_file = None
        self._viewer_360_file = None
        self.discriminator = None

        self.structure_file = structure_file
        self.systems_file = systems_file
        self.map_file = map_file
        self.gltf_file = gltf_file
        self.bvh_tree_file = bvh_tree_file
        self.viewer_360_file = viewer_360_file

    @property
    def structure_file(self):
        """Gets the structure_file of this IfcFiles.  # noqa: E501


        :return: The structure_file of this IfcFiles.  # noqa: E501
        :rtype: str
        """
        return self._structure_file

    @structure_file.setter
    def structure_file(self, structure_file):
        """Sets the structure_file of this IfcFiles.


        :param structure_file: The structure_file of this IfcFiles.  # noqa: E501
        :type: str
        """

        self._structure_file = structure_file

    @property
    def systems_file(self):
        """Gets the systems_file of this IfcFiles.  # noqa: E501


        :return: The systems_file of this IfcFiles.  # noqa: E501
        :rtype: str
        """
        return self._systems_file

    @systems_file.setter
    def systems_file(self, systems_file):
        """Sets the systems_file of this IfcFiles.


        :param systems_file: The systems_file of this IfcFiles.  # noqa: E501
        :type: str
        """

        self._systems_file = systems_file

    @property
    def map_file(self):
        """Gets the map_file of this IfcFiles.  # noqa: E501


        :return: The map_file of this IfcFiles.  # noqa: E501
        :rtype: str
        """
        return self._map_file

    @map_file.setter
    def map_file(self, map_file):
        """Sets the map_file of this IfcFiles.


        :param map_file: The map_file of this IfcFiles.  # noqa: E501
        :type: str
        """

        self._map_file = map_file

    @property
    def gltf_file(self):
        """Gets the gltf_file of this IfcFiles.  # noqa: E501


        :return: The gltf_file of this IfcFiles.  # noqa: E501
        :rtype: str
        """
        return self._gltf_file

    @gltf_file.setter
    def gltf_file(self, gltf_file):
        """Sets the gltf_file of this IfcFiles.


        :param gltf_file: The gltf_file of this IfcFiles.  # noqa: E501
        :type: str
        """

        self._gltf_file = gltf_file

    @property
    def bvh_tree_file(self):
        """Gets the bvh_tree_file of this IfcFiles.  # noqa: E501


        :return: The bvh_tree_file of this IfcFiles.  # noqa: E501
        :rtype: str
        """
        return self._bvh_tree_file

    @bvh_tree_file.setter
    def bvh_tree_file(self, bvh_tree_file):
        """Sets the bvh_tree_file of this IfcFiles.


        :param bvh_tree_file: The bvh_tree_file of this IfcFiles.  # noqa: E501
        :type: str
        """

        self._bvh_tree_file = bvh_tree_file

    @property
    def viewer_360_file(self):
        """Gets the viewer_360_file of this IfcFiles.  # noqa: E501


        :return: The viewer_360_file of this IfcFiles.  # noqa: E501
        :rtype: str
        """
        return self._viewer_360_file

    @viewer_360_file.setter
    def viewer_360_file(self, viewer_360_file):
        """Sets the viewer_360_file of this IfcFiles.


        :param viewer_360_file: The viewer_360_file of this IfcFiles.  # noqa: E501
        :type: str
        """

        self._viewer_360_file = viewer_360_file

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IfcFiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
