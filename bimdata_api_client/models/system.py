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


class System(object):
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
        'uuid': 'str',
        'name': 'str',
        'object_type': 'str',
        'description': 'str',
        'elements': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'uuid': 'uuid',
        'name': 'name',
        'object_type': 'object_type',
        'description': 'description',
        'elements': 'elements'
    }

    def __init__(self, id=None, uuid=None, name=None, object_type=None, description=None, elements=None, local_vars_configuration=None):  # noqa: E501
        """System - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._uuid = None
        self._name = None
        self._object_type = None
        self._description = None
        self._elements = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid
        self.name = name
        self.object_type = object_type
        self.description = description
        self.elements = elements

    @property
    def id(self):
        """Gets the id of this System.  # noqa: E501


        :return: The id of this System.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this System.


        :param id: The id of this System.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this System.  # noqa: E501


        :return: The uuid of this System.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this System.


        :param uuid: The uuid of this System.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                uuid is not None and len(uuid) > 22):
            raise ValueError("Invalid value for `uuid`, length must be less than or equal to `22`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                uuid is not None and len(uuid) < 22):
            raise ValueError("Invalid value for `uuid`, length must be greater than or equal to `22`")  # noqa: E501

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this System.  # noqa: E501

        Name of the system  # noqa: E501

        :return: The name of this System.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this System.

        Name of the system  # noqa: E501

        :param name: The name of this System.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def object_type(self):
        """Gets the object_type of this System.  # noqa: E501


        :return: The object_type of this System.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this System.


        :param object_type: The object_type of this System.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                object_type is not None and len(object_type) > 255):
            raise ValueError("Invalid value for `object_type`, length must be less than or equal to `255`")  # noqa: E501

        self._object_type = object_type

    @property
    def description(self):
        """Gets the description of this System.  # noqa: E501


        :return: The description of this System.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this System.


        :param description: The description of this System.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def elements(self):
        """Gets the elements of this System.  # noqa: E501


        :return: The elements of this System.  # noqa: E501
        :rtype: list[str]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this System.


        :param elements: The elements of this System.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and elements is None:  # noqa: E501
            raise ValueError("Invalid value for `elements`, must not be `None`")  # noqa: E501

        self._elements = elements

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
        if not isinstance(other, System):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, System):
            return True

        return self.to_dict() != other.to_dict()
