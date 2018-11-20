# coding: utf-8

"""
    BIMData API

    BIMData API documentation  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class IfcCheckerCheckplan(object):
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
        'updated_at': 'datetime',
        'protected': 'bool',
        'name': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'project': 'int',
        'id': 'int'
    }

    attribute_map = {
        'updated_at': 'updated_at',
        'protected': 'protected',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'project': 'project',
        'id': 'id'
    }

    def __init__(self, updated_at=None, protected=None, name=None, description=None, created_at=None, project=None, id=None):  # noqa: E501
        """IfcCheckerCheckplan - a model defined in OpenAPI"""  # noqa: E501

        self._updated_at = None
        self._protected = None
        self._name = None
        self._description = None
        self._created_at = None
        self._project = None
        self._id = None
        self.discriminator = None

        if updated_at is not None:
            self.updated_at = updated_at
        if protected is not None:
            self.protected = protected
        self.name = name
        self.description = description
        if created_at is not None:
            self.created_at = created_at
        self.project = project
        if id is not None:
            self.id = id

    @property
    def updated_at(self):
        """Gets the updated_at of this IfcCheckerCheckplan.  # noqa: E501


        :return: The updated_at of this IfcCheckerCheckplan.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this IfcCheckerCheckplan.


        :param updated_at: The updated_at of this IfcCheckerCheckplan.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def protected(self):
        """Gets the protected of this IfcCheckerCheckplan.  # noqa: E501


        :return: The protected of this IfcCheckerCheckplan.  # noqa: E501
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this IfcCheckerCheckplan.


        :param protected: The protected of this IfcCheckerCheckplan.  # noqa: E501
        :type: bool
        """

        self._protected = protected

    @property
    def name(self):
        """Gets the name of this IfcCheckerCheckplan.  # noqa: E501


        :return: The name of this IfcCheckerCheckplan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IfcCheckerCheckplan.


        :param name: The name of this IfcCheckerCheckplan.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this IfcCheckerCheckplan.  # noqa: E501


        :return: The description of this IfcCheckerCheckplan.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IfcCheckerCheckplan.


        :param description: The description of this IfcCheckerCheckplan.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this IfcCheckerCheckplan.  # noqa: E501


        :return: The created_at of this IfcCheckerCheckplan.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this IfcCheckerCheckplan.


        :param created_at: The created_at of this IfcCheckerCheckplan.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def project(self):
        """Gets the project of this IfcCheckerCheckplan.  # noqa: E501


        :return: The project of this IfcCheckerCheckplan.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this IfcCheckerCheckplan.


        :param project: The project of this IfcCheckerCheckplan.  # noqa: E501
        :type: int
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def id(self):
        """Gets the id of this IfcCheckerCheckplan.  # noqa: E501


        :return: The id of this IfcCheckerCheckplan.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IfcCheckerCheckplan.


        :param id: The id of this IfcCheckerCheckplan.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if not isinstance(other, IfcCheckerCheckplan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
