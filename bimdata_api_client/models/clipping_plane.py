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


class ClippingPlane(object):
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
        'location': 'Point',
        'direction': 'Direction'
    }

    attribute_map = {
        'location': 'location',
        'direction': 'direction'
    }

    def __init__(self, location=None, direction=None, local_vars_configuration=None):  # noqa: E501
        """ClippingPlane - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._location = None
        self._direction = None
        self.discriminator = None

        self.location = location
        self.direction = direction

    @property
    def location(self):
        """Gets the location of this ClippingPlane.  # noqa: E501


        :return: The location of this ClippingPlane.  # noqa: E501
        :rtype: Point
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ClippingPlane.


        :param location: The location of this ClippingPlane.  # noqa: E501
        :type: Point
        """
        if self.local_vars_configuration.client_side_validation and location is None:  # noqa: E501
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def direction(self):
        """Gets the direction of this ClippingPlane.  # noqa: E501


        :return: The direction of this ClippingPlane.  # noqa: E501
        :rtype: Direction
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this ClippingPlane.


        :param direction: The direction of this ClippingPlane.  # noqa: E501
        :type: Direction
        """
        if self.local_vars_configuration.client_side_validation and direction is None:  # noqa: E501
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501

        self._direction = direction

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
        if not isinstance(other, ClippingPlane):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClippingPlane):
            return True

        return self.to_dict() != other.to_dict()
