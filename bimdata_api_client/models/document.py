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


class Document(object):
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
        'parent': 'int',
        'parent_id': 'int',
        'creator': 'int',
        'project': 'int',
        'name': 'str',
        'file_name': 'str',
        'description': 'str',
        'file': 'str',
        'size': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'ifc_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'parent': 'parent',
        'parent_id': 'parent_id',
        'creator': 'creator',
        'project': 'project',
        'name': 'name',
        'file_name': 'file_name',
        'description': 'description',
        'file': 'file',
        'size': 'size',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'ifc_id': 'ifc_id'
    }

    def __init__(self, id=None, parent=None, parent_id=None, creator=None, project=None, name=None, file_name=None, description=None, file=None, size=None, created_at=None, updated_at=None, ifc_id=None):  # noqa: E501
        """Document - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._parent = None
        self._parent_id = None
        self._creator = None
        self._project = None
        self._name = None
        self._file_name = None
        self._description = None
        self._file = None
        self._size = None
        self._created_at = None
        self._updated_at = None
        self._ifc_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.parent = parent
        if parent_id is not None:
            self.parent_id = parent_id
        self.creator = creator
        self.project = project
        self.name = name
        self.file_name = file_name
        self.description = description
        self.file = file
        self.size = size
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if ifc_id is not None:
            self.ifc_id = ifc_id

    @property
    def id(self):
        """Gets the id of this Document.  # noqa: E501


        :return: The id of this Document.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Document.


        :param id: The id of this Document.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def parent(self):
        """Gets the parent of this Document.  # noqa: E501


        :return: The parent of this Document.  # noqa: E501
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Document.


        :param parent: The parent of this Document.  # noqa: E501
        :type: int
        """

        self._parent = parent

    @property
    def parent_id(self):
        """Gets the parent_id of this Document.  # noqa: E501


        :return: The parent_id of this Document.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Document.


        :param parent_id: The parent_id of this Document.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def creator(self):
        """Gets the creator of this Document.  # noqa: E501


        :return: The creator of this Document.  # noqa: E501
        :rtype: int
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Document.


        :param creator: The creator of this Document.  # noqa: E501
        :type: int
        """

        self._creator = creator

    @property
    def project(self):
        """Gets the project of this Document.  # noqa: E501


        :return: The project of this Document.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Document.


        :param project: The project of this Document.  # noqa: E501
        :type: int
        """

        self._project = project

    @property
    def name(self):
        """Gets the name of this Document.  # noqa: E501


        :return: The name of this Document.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Document.


        :param name: The name of this Document.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 512:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `512`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def file_name(self):
        """Gets the file_name of this Document.  # noqa: E501


        :return: The file_name of this Document.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this Document.


        :param file_name: The file_name of this Document.  # noqa: E501
        :type: str
        """
        if file_name is not None and len(file_name) > 512:
            raise ValueError("Invalid value for `file_name`, length must be less than or equal to `512`")  # noqa: E501

        self._file_name = file_name

    @property
    def description(self):
        """Gets the description of this Document.  # noqa: E501


        :return: The description of this Document.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Document.


        :param description: The description of this Document.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file(self):
        """Gets the file of this Document.  # noqa: E501


        :return: The file of this Document.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Document.


        :param file: The file of this Document.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def size(self):
        """Gets the size of this Document.  # noqa: E501


        :return: The size of this Document.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Document.


        :param size: The size of this Document.  # noqa: E501
        :type: int
        """
        if size is not None and size > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if size is not None and size < 0:  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._size = size

    @property
    def created_at(self):
        """Gets the created_at of this Document.  # noqa: E501


        :return: The created_at of this Document.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Document.


        :param created_at: The created_at of this Document.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Document.  # noqa: E501


        :return: The updated_at of this Document.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Document.


        :param updated_at: The updated_at of this Document.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def ifc_id(self):
        """Gets the ifc_id of this Document.  # noqa: E501


        :return: The ifc_id of this Document.  # noqa: E501
        :rtype: str
        """
        return self._ifc_id

    @ifc_id.setter
    def ifc_id(self, ifc_id):
        """Sets the ifc_id of this Document.


        :param ifc_id: The ifc_id of this Document.  # noqa: E501
        :type: str
        """

        self._ifc_id = ifc_id

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
        if not isinstance(other, Document):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
