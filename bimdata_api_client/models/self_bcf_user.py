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


class SelfBcfUser(object):
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
        'id': 'str',
        'name': 'str',
        'email': 'str',
        'is_client': 'bool',
        'is_project_token': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'email': 'email',
        'is_client': 'is_client',
        'is_project_token': 'is_project_token'
    }

    def __init__(self, id=None, name=None, email=None, is_client=None, is_project_token=None, local_vars_configuration=None):  # noqa: E501
        """SelfBcfUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._email = None
        self._is_client = None
        self._is_project_token = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        self.email = email
        if is_client is not None:
            self.is_client = is_client
        if is_project_token is not None:
            self.is_project_token = is_project_token

    @property
    def id(self):
        """Gets the id of this SelfBcfUser.  # noqa: E501


        :return: The id of this SelfBcfUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SelfBcfUser.


        :param id: The id of this SelfBcfUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this SelfBcfUser.  # noqa: E501


        :return: The name of this SelfBcfUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SelfBcfUser.


        :param name: The name of this SelfBcfUser.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this SelfBcfUser.  # noqa: E501


        :return: The email of this SelfBcfUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SelfBcfUser.


        :param email: The email of this SelfBcfUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 254):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `254`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def is_client(self):
        """Gets the is_client of this SelfBcfUser.  # noqa: E501


        :return: The is_client of this SelfBcfUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_client

    @is_client.setter
    def is_client(self, is_client):
        """Sets the is_client of this SelfBcfUser.


        :param is_client: The is_client of this SelfBcfUser.  # noqa: E501
        :type: bool
        """

        self._is_client = is_client

    @property
    def is_project_token(self):
        """Gets the is_project_token of this SelfBcfUser.  # noqa: E501


        :return: The is_project_token of this SelfBcfUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_project_token

    @is_project_token.setter
    def is_project_token(self, is_project_token):
        """Sets the is_project_token of this SelfBcfUser.


        :param is_project_token: The is_project_token of this SelfBcfUser.  # noqa: E501
        :type: bool
        """

        self._is_project_token = is_project_token

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
        if not isinstance(other, SelfBcfUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SelfBcfUser):
            return True

        return self.to_dict() != other.to_dict()
