# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from bimdata_api_client.configuration import Configuration


class RawMaterialList(object):
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
        'materials_data': 'list[RawMaterial]',
        'list_components': 'list[RawMaterialListComponents]',
        'options': 'list[RawMaterialOptions]'
    }

    attribute_map = {
        'materials_data': 'materials_data',
        'list_components': 'list_components',
        'options': 'options'
    }

    def __init__(self, materials_data=None, list_components=None, options=None, local_vars_configuration=None):  # noqa: E501
        """RawMaterialList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._materials_data = None
        self._list_components = None
        self._options = None
        self.discriminator = None

        self.materials_data = materials_data
        self.list_components = list_components
        self.options = options

    @property
    def materials_data(self):
        """Gets the materials_data of this RawMaterialList.  # noqa: E501

          # noqa: E501

        :return: The materials_data of this RawMaterialList.  # noqa: E501
        :rtype: list[RawMaterial]
        """
        return self._materials_data

    @materials_data.setter
    def materials_data(self, materials_data):
        """Sets the materials_data of this RawMaterialList.

          # noqa: E501

        :param materials_data: The materials_data of this RawMaterialList.  # noqa: E501
        :type: list[RawMaterial]
        """

        self._materials_data = materials_data

    @property
    def list_components(self):
        """Gets the list_components of this RawMaterialList.  # noqa: E501

          # noqa: E501

        :return: The list_components of this RawMaterialList.  # noqa: E501
        :rtype: list[RawMaterialListComponents]
        """
        return self._list_components

    @list_components.setter
    def list_components(self, list_components):
        """Sets the list_components of this RawMaterialList.

          # noqa: E501

        :param list_components: The list_components of this RawMaterialList.  # noqa: E501
        :type: list[RawMaterialListComponents]
        """

        self._list_components = list_components

    @property
    def options(self):
        """Gets the options of this RawMaterialList.  # noqa: E501

          # noqa: E501

        :return: The options of this RawMaterialList.  # noqa: E501
        :rtype: list[RawMaterialOptions]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this RawMaterialList.

          # noqa: E501

        :param options: The options of this RawMaterialList.  # noqa: E501
        :type: list[RawMaterialOptions]
        """

        self._options = options

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
        if not isinstance(other, RawMaterialList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RawMaterialList):
            return True

        return self.to_dict() != other.to_dict()