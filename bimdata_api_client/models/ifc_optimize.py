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


class IfcOptimize(object):
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
        'floating_point_reduction': 'int'
    }

    attribute_map = {
        'floating_point_reduction': 'floating_point_reduction'
    }

    def __init__(self, floating_point_reduction=None, local_vars_configuration=None):  # noqa: E501
        """IfcOptimize - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._floating_point_reduction = None
        self.discriminator = None

        if floating_point_reduction is not None:
            self.floating_point_reduction = floating_point_reduction

    @property
    def floating_point_reduction(self):
        """Gets the floating_point_reduction of this IfcOptimize.  # noqa: E501

        Precision of geometries. 6 is micrometre, 9 is nanometre, ect...  # noqa: E501

        :return: The floating_point_reduction of this IfcOptimize.  # noqa: E501
        :rtype: int
        """
        return self._floating_point_reduction

    @floating_point_reduction.setter
    def floating_point_reduction(self, floating_point_reduction):
        """Sets the floating_point_reduction of this IfcOptimize.

        Precision of geometries. 6 is micrometre, 9 is nanometre, ect...  # noqa: E501

        :param floating_point_reduction: The floating_point_reduction of this IfcOptimize.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                floating_point_reduction is not None and floating_point_reduction > 15):  # noqa: E501
            raise ValueError("Invalid value for `floating_point_reduction`, must be a value less than or equal to `15`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                floating_point_reduction is not None and floating_point_reduction < 6):  # noqa: E501
            raise ValueError("Invalid value for `floating_point_reduction`, must be a value greater than or equal to `6`")  # noqa: E501

        self._floating_point_reduction = floating_point_reduction

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
        if not isinstance(other, IfcOptimize):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IfcOptimize):
            return True

        return self.to_dict() != other.to_dict()
