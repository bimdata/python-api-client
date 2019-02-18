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


class Folder(object):
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
        'parent_id': 'int',
        'type': 'str',
        'name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'children': 'list[Folder]',
        'created_by': 'User'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parent_id',
        'type': 'type',
        'name': 'name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'children': 'children',
        'created_by': 'created_by'
    }

    def __init__(self, id=None, parent_id=None, type=None, name=None, created_at=None, updated_at=None, children=None, created_by=None):  # noqa: E501
        """Folder - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._parent_id = None
        self._type = None
        self._name = None
        self._created_at = None
        self._updated_at = None
        self._children = None
        self._created_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_id is not None:
            self.parent_id = parent_id
        if type is not None:
            self.type = type
        self.name = name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if children is not None:
            self.children = children
        if created_by is not None:
            self.created_by = created_by

    @property
    def id(self):
        """Gets the id of this Folder.  # noqa: E501


        :return: The id of this Folder.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Folder.


        :param id: The id of this Folder.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this Folder.  # noqa: E501


        :return: The parent_id of this Folder.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Folder.


        :param parent_id: The parent_id of this Folder.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def type(self):
        """Gets the type of this Folder.  # noqa: E501

        Value is \"Folder\". It is usefull to parse the tree and discriminate folders and files  # noqa: E501

        :return: The type of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Folder.

        Value is \"Folder\". It is usefull to parse the tree and discriminate folders and files  # noqa: E501

        :param type: The type of this Folder.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this Folder.  # noqa: E501


        :return: The name of this Folder.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Folder.


        :param name: The name of this Folder.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this Folder.  # noqa: E501


        :return: The created_at of this Folder.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Folder.


        :param created_at: The created_at of this Folder.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Folder.  # noqa: E501


        :return: The updated_at of this Folder.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Folder.


        :param updated_at: The updated_at of this Folder.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def children(self):
        """Gets the children of this Folder.  # noqa: E501


        :return: The children of this Folder.  # noqa: E501
        :rtype: list[Folder]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this Folder.


        :param children: The children of this Folder.  # noqa: E501
        :type: list[Folder]
        """

        self._children = children

    @property
    def created_by(self):
        """Gets the created_by of this Folder.  # noqa: E501


        :return: The created_by of this Folder.  # noqa: E501
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Folder.


        :param created_by: The created_by of this Folder.  # noqa: E501
        :type: User
        """

        self._created_by = created_by

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
        if not isinstance(other, Folder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
