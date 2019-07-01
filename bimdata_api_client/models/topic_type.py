# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: contact@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class TopicType(object):
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
        'topic_type': 'str'
    }

    attribute_map = {
        'topic_type': 'topic_type'
    }

    def __init__(self, topic_type=None):  # noqa: E501
        """TopicType - a model defined in OpenAPI"""  # noqa: E501

        self._topic_type = None
        self.discriminator = None

        self.topic_type = topic_type

    @property
    def topic_type(self):
        """Gets the topic_type of this TopicType.  # noqa: E501


        :return: The topic_type of this TopicType.  # noqa: E501
        :rtype: str
        """
        return self._topic_type

    @topic_type.setter
    def topic_type(self, topic_type):
        """Sets the topic_type of this TopicType.


        :param topic_type: The topic_type of this TopicType.  # noqa: E501
        :type: str
        """
        if topic_type is None:
            raise ValueError("Invalid value for `topic_type`, must not be `None`")  # noqa: E501
        if topic_type is not None and len(topic_type) > 255:
            raise ValueError("Invalid value for `topic_type`, length must be less than or equal to `255`")  # noqa: E501
        if topic_type is not None and len(topic_type) < 1:
            raise ValueError("Invalid value for `topic_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._topic_type = topic_type

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
        if not isinstance(other, TopicType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
