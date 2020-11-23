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


class Project(object):
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
        'logo': 'str',
        'name': 'str',
        'cloud': 'Cloud',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'parent_id': 'int',
        'root_folder_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'logo': 'logo',
        'name': 'name',
        'cloud': 'cloud',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'parent_id': 'parent_id',
        'root_folder_id': 'root_folder_id'
    }

    def __init__(self, id=None, logo=None, name=None, cloud=None, status=None, created_at=None, updated_at=None, parent_id=None, root_folder_id=None, local_vars_configuration=None):  # noqa: E501
        """Project - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._logo = None
        self._name = None
        self._cloud = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._parent_id = None
        self._root_folder_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.logo = logo
        self.name = name
        if cloud is not None:
            self.cloud = cloud
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.parent_id = parent_id
        if root_folder_id is not None:
            self.root_folder_id = root_folder_id

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501


        :return: The id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.


        :param id: The id of this Project.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def logo(self):
        """Gets the logo of this Project.  # noqa: E501


        :return: The logo of this Project.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Project.


        :param logo: The logo of this Project.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501

        Name of the project  # noqa: E501

        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.

        Name of the project  # noqa: E501

        :param name: The name of this Project.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 256):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def cloud(self):
        """Gets the cloud of this Project.  # noqa: E501


        :return: The cloud of this Project.  # noqa: E501
        :rtype: Cloud
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this Project.


        :param cloud: The cloud of this Project.  # noqa: E501
        :type: Cloud
        """

        self._cloud = cloud

    @property
    def status(self):
        """Gets the status of this Project.  # noqa: E501


        :return: The status of this Project.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Project.


        :param status: The status of this Project.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "D"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this Project.  # noqa: E501

        Creation date  # noqa: E501

        :return: The created_at of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Project.

        Creation date  # noqa: E501

        :param created_at: The created_at of this Project.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Project.  # noqa: E501

        Date of the last update  # noqa: E501

        :return: The updated_at of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Project.

        Date of the last update  # noqa: E501

        :param updated_at: The updated_at of this Project.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def parent_id(self):
        """Gets the parent_id of this Project.  # noqa: E501


        :return: The parent_id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Project.


        :param parent_id: The parent_id of this Project.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def root_folder_id(self):
        """Gets the root_folder_id of this Project.  # noqa: E501


        :return: The root_folder_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._root_folder_id

    @root_folder_id.setter
    def root_folder_id(self, root_folder_id):
        """Sets the root_folder_id of this Project.


        :param root_folder_id: The root_folder_id of this Project.  # noqa: E501
        :type: str
        """

        self._root_folder_id = root_folder_id

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
        if not isinstance(other, Project):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Project):
            return True

        return self.to_dict() != other.to_dict()
