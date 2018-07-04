# coding: utf-8

"""
    BIMData API

    BIMData API documentation  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RawUnit(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'type': 'str',
        'unit_type': 'str',
        'prefix': 'str',
        'elements': 'str',
        'conversion_factor': 'float',
        'dimensions': 'list[float]',
        'conversion_baseunit_index': 'int'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'unit_type': 'unit_type',
        'prefix': 'prefix',
        'elements': 'elements',
        'conversion_factor': 'conversion_factor',
        'dimensions': 'dimensions',
        'conversion_baseunit_index': 'conversion_baseunit_index'
    }

    def __init__(self, name=None, type=None, unit_type=None, prefix=None, elements=None, conversion_factor=None, dimensions=None, conversion_baseunit_index=None):  # noqa: E501
        """RawUnit - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._type = None
        self._unit_type = None
        self._prefix = None
        self._elements = None
        self._conversion_factor = None
        self._dimensions = None
        self._conversion_baseunit_index = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.type = type
        if unit_type is not None:
            self.unit_type = unit_type
        if prefix is not None:
            self.prefix = prefix
        if elements is not None:
            self.elements = elements
        if conversion_factor is not None:
            self.conversion_factor = conversion_factor
        if dimensions is not None:
            self.dimensions = dimensions
        if conversion_baseunit_index is not None:
            self.conversion_baseunit_index = conversion_baseunit_index

    @property
    def name(self):
        """Gets the name of this RawUnit.  # noqa: E501


        :return: The name of this RawUnit.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RawUnit.


        :param name: The name of this RawUnit.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this RawUnit.  # noqa: E501


        :return: The type of this RawUnit.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RawUnit.


        :param type: The type of this RawUnit.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if type is not None and len(type) < 1:
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def unit_type(self):
        """Gets the unit_type of this RawUnit.  # noqa: E501


        :return: The unit_type of this RawUnit.  # noqa: E501
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """Sets the unit_type of this RawUnit.


        :param unit_type: The unit_type of this RawUnit.  # noqa: E501
        :type: str
        """

        self._unit_type = unit_type

    @property
    def prefix(self):
        """Gets the prefix of this RawUnit.  # noqa: E501


        :return: The prefix of this RawUnit.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this RawUnit.


        :param prefix: The prefix of this RawUnit.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def elements(self):
        """Gets the elements of this RawUnit.  # noqa: E501


        :return: The elements of this RawUnit.  # noqa: E501
        :rtype: str
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this RawUnit.


        :param elements: The elements of this RawUnit.  # noqa: E501
        :type: str
        """

        self._elements = elements

    @property
    def conversion_factor(self):
        """Gets the conversion_factor of this RawUnit.  # noqa: E501


        :return: The conversion_factor of this RawUnit.  # noqa: E501
        :rtype: float
        """
        return self._conversion_factor

    @conversion_factor.setter
    def conversion_factor(self, conversion_factor):
        """Sets the conversion_factor of this RawUnit.


        :param conversion_factor: The conversion_factor of this RawUnit.  # noqa: E501
        :type: float
        """

        self._conversion_factor = conversion_factor

    @property
    def dimensions(self):
        """Gets the dimensions of this RawUnit.  # noqa: E501


        :return: The dimensions of this RawUnit.  # noqa: E501
        :rtype: list[float]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this RawUnit.


        :param dimensions: The dimensions of this RawUnit.  # noqa: E501
        :type: list[float]
        """

        self._dimensions = dimensions

    @property
    def conversion_baseunit_index(self):
        """Gets the conversion_baseunit_index of this RawUnit.  # noqa: E501


        :return: The conversion_baseunit_index of this RawUnit.  # noqa: E501
        :rtype: int
        """
        return self._conversion_baseunit_index

    @conversion_baseunit_index.setter
    def conversion_baseunit_index(self, conversion_baseunit_index):
        """Sets the conversion_baseunit_index of this RawUnit.


        :param conversion_baseunit_index: The conversion_baseunit_index of this RawUnit.  # noqa: E501
        :type: int
        """

        self._conversion_baseunit_index = conversion_baseunit_index

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, RawUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
