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


class DocumentWithElementList(object):
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
        'document': 'Document',
        'element_ids': 'list[int]'
    }

    attribute_map = {
        'document': 'document',
        'element_ids': 'element_ids'
    }

    def __init__(self, document=None, element_ids=None, local_vars_configuration=None):  # noqa: E501
        """DocumentWithElementList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._document = None
        self._element_ids = None
        self.discriminator = None

        if document is not None:
            self.document = document
        if element_ids is not None:
            self.element_ids = element_ids

    @property
    def document(self):
        """Gets the document of this DocumentWithElementList.  # noqa: E501


        :return: The document of this DocumentWithElementList.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this DocumentWithElementList.


        :param document: The document of this DocumentWithElementList.  # noqa: E501
        :type: Document
        """

        self._document = document

    @property
    def element_ids(self):
        """Gets the element_ids of this DocumentWithElementList.  # noqa: E501


        :return: The element_ids of this DocumentWithElementList.  # noqa: E501
        :rtype: list[int]
        """
        return self._element_ids

    @element_ids.setter
    def element_ids(self, element_ids):
        """Sets the element_ids of this DocumentWithElementList.


        :param element_ids: The element_ids of this DocumentWithElementList.  # noqa: E501
        :type: list[int]
        """

        self._element_ids = element_ids

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
        if not isinstance(other, DocumentWithElementList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentWithElementList):
            return True

        return self.to_dict() != other.to_dict()
