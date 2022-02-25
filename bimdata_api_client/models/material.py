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


class Material(object):
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
        'category': 'str',
        'description': 'str',
        'property_sets': 'list[PropertySet]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'category': 'category',
        'description': 'description',
        'property_sets': 'property_sets'
    }

    def __init__(self, id=None, name=None, category=None, description=None, property_sets=None, local_vars_configuration=None):  # noqa: E501
        """Material - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._category = None
        self._description = None
        self._property_sets = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        self.category = category
        self.description = description
        self.property_sets = property_sets

    @property
    def id(self):
        """Gets the id of this Material.  # noqa: E501


        :return: The id of this Material.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Material.


        :param id: The id of this Material.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Material.  # noqa: E501


        :return: The name of this Material.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Material.


        :param name: The name of this Material.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def category(self):
        """Gets the category of this Material.  # noqa: E501


        :return: The category of this Material.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Material.


        :param category: The category of this Material.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                category is not None and len(category) < 1):
            raise ValueError("Invalid value for `category`, length must be greater than or equal to `1`")  # noqa: E501

        self._category = category

    @property
    def description(self):
        """Gets the description of this Material.  # noqa: E501


        :return: The description of this Material.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Material.


        :param description: The description of this Material.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def property_sets(self):
        """Gets the property_sets of this Material.  # noqa: E501


        :return: The property_sets of this Material.  # noqa: E501
        :rtype: list[PropertySet]
        """
        return self._property_sets

    @property_sets.setter
    def property_sets(self, property_sets):
        """Sets the property_sets of this Material.


        :param property_sets: The property_sets of this Material.  # noqa: E501
        :type: list[PropertySet]
        """
        if self.local_vars_configuration.client_side_validation and property_sets is None:  # noqa: E501
            raise ValueError("Invalid value for `property_sets`, must not be `None`")  # noqa: E501

        self._property_sets = property_sets

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
        if not isinstance(other, Material):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Material):
            return True

        return self.to_dict() != other.to_dict()
