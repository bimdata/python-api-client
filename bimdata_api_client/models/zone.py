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


class Zone(object):
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
        'uuid': 'str',
        'zones': 'list[Zone]',
        'parent_id': 'int',
        'spaces': 'list[Space]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'color': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'uuid': 'uuid',
        'zones': 'zones',
        'parent_id': 'parent_id',
        'spaces': 'spaces',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'color': 'color'
    }

    def __init__(self, id=None, name=None, uuid=None, zones=None, parent_id=None, spaces=None, created_at=None, updated_at=None, color=None, local_vars_configuration=None):  # noqa: E501
        """Zone - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._uuid = None
        self._zones = None
        self._parent_id = None
        self._spaces = None
        self._created_at = None
        self._updated_at = None
        self._color = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.uuid = uuid
        if zones is not None:
            self.zones = zones
        if parent_id is not None:
            self.parent_id = parent_id
        if spaces is not None:
            self.spaces = spaces
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.color = color

    @property
    def id(self):
        """Gets the id of this Zone.  # noqa: E501


        :return: The id of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Zone.


        :param id: The id of this Zone.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Zone.  # noqa: E501


        :return: The name of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Zone.


        :param name: The name of this Zone.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this Zone.  # noqa: E501


        :return: The uuid of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Zone.


        :param uuid: The uuid of this Zone.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                uuid is not None and len(uuid) > 255):
            raise ValueError("Invalid value for `uuid`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                uuid is not None and len(uuid) < 1):
            raise ValueError("Invalid value for `uuid`, length must be greater than or equal to `1`")  # noqa: E501

        self._uuid = uuid

    @property
    def zones(self):
        """Gets the zones of this Zone.  # noqa: E501

          # noqa: E501

        :return: The zones of this Zone.  # noqa: E501
        :rtype: list[Zone]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """Sets the zones of this Zone.

          # noqa: E501

        :param zones: The zones of this Zone.  # noqa: E501
        :type: list[Zone]
        """

        self._zones = zones

    @property
    def parent_id(self):
        """Gets the parent_id of this Zone.  # noqa: E501


        :return: The parent_id of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Zone.


        :param parent_id: The parent_id of this Zone.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def spaces(self):
        """Gets the spaces of this Zone.  # noqa: E501

          # noqa: E501

        :return: The spaces of this Zone.  # noqa: E501
        :rtype: list[Space]
        """
        return self._spaces

    @spaces.setter
    def spaces(self, spaces):
        """Sets the spaces of this Zone.

          # noqa: E501

        :param spaces: The spaces of this Zone.  # noqa: E501
        :type: list[Space]
        """

        self._spaces = spaces

    @property
    def created_at(self):
        """Gets the created_at of this Zone.  # noqa: E501


        :return: The created_at of this Zone.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Zone.


        :param created_at: The created_at of this Zone.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Zone.  # noqa: E501


        :return: The updated_at of this Zone.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Zone.


        :param updated_at: The updated_at of this Zone.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def color(self):
        """Gets the color of this Zone.  # noqa: E501


        :return: The color of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Zone.


        :param color: The color of this Zone.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                color is not None and len(color) > 8):
            raise ValueError("Invalid value for `color`, length must be less than or equal to `8`")  # noqa: E501

        self._color = color

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
        if not isinstance(other, Zone):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Zone):
            return True

        return self.to_dict() != other.to_dict()
