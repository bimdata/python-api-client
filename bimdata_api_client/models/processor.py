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


class Processor(object):
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
        'name': 'str',
        'parent_processors': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'parent_processors': 'parent_processors'
    }

    def __init__(self, id=None, name=None, parent_processors=None):  # noqa: E501
        """Processor - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._parent_processors = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if parent_processors is not None:
            self.parent_processors = parent_processors

    @property
    def id(self):
        """Gets the id of this Processor.  # noqa: E501


        :return: The id of this Processor.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Processor.


        :param id: The id of this Processor.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Processor.  # noqa: E501


        :return: The name of this Processor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Processor.


        :param name: The name of this Processor.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def parent_processors(self):
        """Gets the parent_processors of this Processor.  # noqa: E501


        :return: The parent_processors of this Processor.  # noqa: E501
        :rtype: list[int]
        """
        return self._parent_processors

    @parent_processors.setter
    def parent_processors(self, parent_processors):
        """Sets the parent_processors of this Processor.


        :param parent_processors: The parent_processors of this Processor.  # noqa: E501
        :type: list[int]
        """

        self._parent_processors = parent_processors

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
        if not isinstance(other, Processor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
