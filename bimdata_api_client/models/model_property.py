# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: contact@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ModelProperty(object):
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
        'definition': 'PropertyDefinition',
        'value': 'object'
    }

    attribute_map = {
        'id': 'id',
        'definition': 'definition',
        'value': 'value'
    }

    def __init__(self, id=None, definition=None, value=None):  # noqa: E501
        """ModelProperty - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._definition = None
        self._value = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.definition = definition
        self.value = value

    @property
    def id(self):
        """Gets the id of this ModelProperty.  # noqa: E501


        :return: The id of this ModelProperty.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelProperty.


        :param id: The id of this ModelProperty.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def definition(self):
        """Gets the definition of this ModelProperty.  # noqa: E501


        :return: The definition of this ModelProperty.  # noqa: E501
        :rtype: PropertyDefinition
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this ModelProperty.


        :param definition: The definition of this ModelProperty.  # noqa: E501
        :type: PropertyDefinition
        """
        if definition is None:
            raise ValueError("Invalid value for `definition`, must not be `None`")  # noqa: E501

        self._definition = definition

    @property
    def value(self):
        """Gets the value of this ModelProperty.  # noqa: E501


        :return: The value of this ModelProperty.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ModelProperty.


        :param value: The value of this ModelProperty.  # noqa: E501
        :type: object
        """

        self._value = value

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
        if not isinstance(other, ModelProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
