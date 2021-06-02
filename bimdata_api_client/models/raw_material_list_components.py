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


class RawMaterialListComponents(object):
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
        'id': 'int',
        'material': 'int',
        'material_option': 'int'
    }

    attribute_map = {
        'id': 'id',
        'material': 'material',
        'material_option': 'material_option'
    }

    def __init__(self, id=None, material=None, material_option=None, local_vars_configuration=None):  # noqa: E501
        """RawMaterialListComponents - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._material = None
        self._material_option = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.material = material
        self.material_option = material_option

    @property
    def id(self):
        """Gets the id of this RawMaterialListComponents.  # noqa: E501


        :return: The id of this RawMaterialListComponents.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RawMaterialListComponents.


        :param id: The id of this RawMaterialListComponents.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def material(self):
        """Gets the material of this RawMaterialListComponents.  # noqa: E501


        :return: The material of this RawMaterialListComponents.  # noqa: E501
        :rtype: int
        """
        return self._material

    @material.setter
    def material(self, material):
        """Sets the material of this RawMaterialListComponents.


        :param material: The material of this RawMaterialListComponents.  # noqa: E501
        :type: int
        """

        self._material = material

    @property
    def material_option(self):
        """Gets the material_option of this RawMaterialListComponents.  # noqa: E501


        :return: The material_option of this RawMaterialListComponents.  # noqa: E501
        :rtype: int
        """
        return self._material_option

    @material_option.setter
    def material_option(self, material_option):
        """Sets the material_option of this RawMaterialListComponents.


        :param material_option: The material_option of this RawMaterialListComponents.  # noqa: E501
        :type: int
        """

        self._material_option = material_option

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
        if not isinstance(other, RawMaterialListComponents):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RawMaterialListComponents):
            return True

        return self.to_dict() != other.to_dict()
