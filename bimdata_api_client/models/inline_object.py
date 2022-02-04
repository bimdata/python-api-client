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


class InlineObject(object):
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
        'nature': 'str',
        'name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'created_by': 'User',
        'groups_permissions': 'list[FolderGroupPermission]',
        'default_permission': 'int',
        'user_permission': 'int'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parent_id',
        'type': 'type',
        'nature': 'nature',
        'name': 'name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'created_by': 'created_by',
        'groups_permissions': 'groups_permissions',
        'default_permission': 'default_permission',
        'user_permission': 'user_permission'
    }

    def __init__(self, id=None, parent_id=None, type=None, nature=None, name=None, created_at=None, updated_at=None, created_by=None, groups_permissions=None, default_permission=None, user_permission=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._parent_id = None
        self._type = None
        self._nature = None
        self._name = None
        self._created_at = None
        self._updated_at = None
        self._created_by = None
        self._groups_permissions = None
        self._default_permission = None
        self._user_permission = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.parent_id = parent_id
        if type is not None:
            self.type = type
        if nature is not None:
            self.nature = nature
        self.name = name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if created_by is not None:
            self.created_by = created_by
        if groups_permissions is not None:
            self.groups_permissions = groups_permissions
        if default_permission is not None:
            self.default_permission = default_permission
        if user_permission is not None:
            self.user_permission = user_permission

    @property
    def id(self):
        """Gets the id of this InlineObject.  # noqa: E501


        :return: The id of this InlineObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineObject.


        :param id: The id of this InlineObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this InlineObject.  # noqa: E501


        :return: The parent_id of this InlineObject.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this InlineObject.


        :param parent_id: The parent_id of this InlineObject.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def type(self):
        """Gets the type of this InlineObject.  # noqa: E501

        DEPRECATED: Use 'nature' instead. Value is \"Folder\". It is usefull to parse the tree and discriminate folders and files  # noqa: E501

        :return: The type of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineObject.

        DEPRECATED: Use 'nature' instead. Value is \"Folder\". It is usefull to parse the tree and discriminate folders and files  # noqa: E501

        :param type: The type of this InlineObject.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def nature(self):
        """Gets the nature of this InlineObject.  # noqa: E501

        Value is \"Folder\". It is usefull to parse the tree and discriminate folders and files  # noqa: E501

        :return: The nature of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._nature

    @nature.setter
    def nature(self, nature):
        """Sets the nature of this InlineObject.

        Value is \"Folder\". It is usefull to parse the tree and discriminate folders and files  # noqa: E501

        :param nature: The nature of this InlineObject.  # noqa: E501
        :type: str
        """

        self._nature = nature

    @property
    def name(self):
        """Gets the name of this InlineObject.  # noqa: E501

        Name of the folder  # noqa: E501

        :return: The name of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject.

        Name of the folder  # noqa: E501

        :param name: The name of this InlineObject.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this InlineObject.  # noqa: E501

        Creation date  # noqa: E501

        :return: The created_at of this InlineObject.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineObject.

        Creation date  # noqa: E501

        :param created_at: The created_at of this InlineObject.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this InlineObject.  # noqa: E501

        Date of the last update  # noqa: E501

        :return: The updated_at of this InlineObject.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InlineObject.

        Date of the last update  # noqa: E501

        :param updated_at: The updated_at of this InlineObject.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def created_by(self):
        """Gets the created_by of this InlineObject.  # noqa: E501


        :return: The created_by of this InlineObject.  # noqa: E501
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this InlineObject.


        :param created_by: The created_by of this InlineObject.  # noqa: E501
        :type: User
        """

        self._created_by = created_by

    @property
    def groups_permissions(self):
        """Gets the groups_permissions of this InlineObject.  # noqa: E501


        :return: The groups_permissions of this InlineObject.  # noqa: E501
        :rtype: list[FolderGroupPermission]
        """
        return self._groups_permissions

    @groups_permissions.setter
    def groups_permissions(self, groups_permissions):
        """Sets the groups_permissions of this InlineObject.


        :param groups_permissions: The groups_permissions of this InlineObject.  # noqa: E501
        :type: list[FolderGroupPermission]
        """

        self._groups_permissions = groups_permissions

    @property
    def default_permission(self):
        """Gets the default_permission of this InlineObject.  # noqa: E501

        Permission for a Folder  # noqa: E501

        :return: The default_permission of this InlineObject.  # noqa: E501
        :rtype: int
        """
        return self._default_permission

    @default_permission.setter
    def default_permission(self, default_permission):
        """Sets the default_permission of this InlineObject.

        Permission for a Folder  # noqa: E501

        :param default_permission: The default_permission of this InlineObject.  # noqa: E501
        :type: int
        """

        self._default_permission = default_permission

    @property
    def user_permission(self):
        """Gets the user_permission of this InlineObject.  # noqa: E501

        Aggregate of group user permissions and folder default permission  # noqa: E501

        :return: The user_permission of this InlineObject.  # noqa: E501
        :rtype: int
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this InlineObject.

        Aggregate of group user permissions and folder default permission  # noqa: E501

        :param user_permission: The user_permission of this InlineObject.  # noqa: E501
        :type: int
        """

        self._user_permission = user_permission

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
        if not isinstance(other, InlineObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject):
            return True

        return self.to_dict() != other.to_dict()
