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


class ElementPropertySetRelation(object):
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
        'element_uuid': 'str',
        'property_set_id': 'int'
    }

    attribute_map = {
        'element_uuid': 'element_uuid',
        'property_set_id': 'property_set_id'
    }

    def __init__(self, element_uuid=None, property_set_id=None, local_vars_configuration=None):  # noqa: E501
        """ElementPropertySetRelation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._element_uuid = None
        self._property_set_id = None
        self.discriminator = None

        self.element_uuid = element_uuid
        self.property_set_id = property_set_id

    @property
    def element_uuid(self):
        """Gets the element_uuid of this ElementPropertySetRelation.  # noqa: E501


        :return: The element_uuid of this ElementPropertySetRelation.  # noqa: E501
        :rtype: str
        """
        return self._element_uuid

    @element_uuid.setter
    def element_uuid(self, element_uuid):
        """Sets the element_uuid of this ElementPropertySetRelation.


        :param element_uuid: The element_uuid of this ElementPropertySetRelation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and element_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `element_uuid`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                element_uuid is not None and len(element_uuid) < 1):
            raise ValueError("Invalid value for `element_uuid`, length must be greater than or equal to `1`")  # noqa: E501

        self._element_uuid = element_uuid

    @property
    def property_set_id(self):
        """Gets the property_set_id of this ElementPropertySetRelation.  # noqa: E501


        :return: The property_set_id of this ElementPropertySetRelation.  # noqa: E501
        :rtype: int
        """
        return self._property_set_id

    @property_set_id.setter
    def property_set_id(self, property_set_id):
        """Sets the property_set_id of this ElementPropertySetRelation.


        :param property_set_id: The property_set_id of this ElementPropertySetRelation.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and property_set_id is None:  # noqa: E501
            raise ValueError("Invalid value for `property_set_id`, must not be `None`")  # noqa: E501

        self._property_set_id = property_set_id

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
        if not isinstance(other, ElementPropertySetRelation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElementPropertySetRelation):
            return True

        return self.to_dict() != other.to_dict()
