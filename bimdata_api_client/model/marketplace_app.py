"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1 (v1)
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from bimdata_api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from bimdata_api_client.exceptions import ApiAttributeError


def lazy_import():
    from bimdata_api_client.model.marketplace_app_image import MarketplaceAppImage
    from bimdata_api_client.model.public_organization import PublicOrganization
    from bimdata_api_client.model.user import User
    globals()['MarketplaceAppImage'] = MarketplaceAppImage
    globals()['PublicOrganization'] = PublicOrganization
    globals()['User'] = User


class MarketplaceApp(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('name',): {
            'max_length': 256,
        },
        ('short_description',): {
            'max_length': 130,
        },
        ('activation_webhook_url',): {
            'max_length': 1024,
        },
        ('post_activation_redirect_uri',): {
            'max_length': 1024,
        },
        ('settings_url',): {
            'max_length': 1024,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (int,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'short_description': (str,),  # noqa: E501
            'long_description': (str,),  # noqa: E501
            'creator': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'scopes': ([str],),  # noqa: E501
            'images': ([MarketplaceAppImage],),  # noqa: E501
            'organization': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'activation_webhook_url': (str, none_type,),  # noqa: E501
            'post_activation_redirect_uri': (str, none_type,),  # noqa: E501
            'viewer_plugins_urls': ([str], none_type,),  # noqa: E501
            'settings_url': (str, none_type,),  # noqa: E501
            'is_public': (bool,),  # noqa: E501
            'tags': ([str],),  # noqa: E501
            'logo': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'short_description': 'short_description',  # noqa: E501
        'long_description': 'long_description',  # noqa: E501
        'creator': 'creator',  # noqa: E501
        'scopes': 'scopes',  # noqa: E501
        'images': 'images',  # noqa: E501
        'organization': 'organization',  # noqa: E501
        'activation_webhook_url': 'activation_webhook_url',  # noqa: E501
        'post_activation_redirect_uri': 'post_activation_redirect_uri',  # noqa: E501
        'viewer_plugins_urls': 'viewer_plugins_urls',  # noqa: E501
        'settings_url': 'settings_url',  # noqa: E501
        'is_public': 'is_public',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'logo': 'logo',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'creator',  # noqa: E501
        'scopes',  # noqa: E501
        'images',  # noqa: E501
        'organization',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, name, short_description, long_description, creator, scopes, images, organization, *args, **kwargs):  # noqa: E501
        """MarketplaceApp - a model defined in OpenAPI

        Args:
            id (int):
            name (str):
            short_description (str):
            long_description (str):
            creator (bool, date, datetime, dict, float, int, list, str, none_type):
            scopes ([str]):
            images ([MarketplaceAppImage]):
            organization (bool, date, datetime, dict, float, int, list, str, none_type):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            activation_webhook_url (str, none_type): [optional]  # noqa: E501
            post_activation_redirect_uri (str, none_type): [optional]  # noqa: E501
            viewer_plugins_urls ([str], none_type): [optional]  # noqa: E501
            settings_url (str, none_type): this URL will be called with query params ?cloud_id=. [optional]  # noqa: E501
            is_public (bool): [optional]  # noqa: E501
            tags ([str]): [optional]  # noqa: E501
            logo (str, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.name = name
        self.short_description = short_description
        self.long_description = long_description
        self.creator = creator
        self.scopes = scopes
        self.images = images
        self.organization = organization
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, name, short_description, long_description, *args, **kwargs):  # noqa: E501
        """MarketplaceApp - a model defined in OpenAPI

            name (str):
            short_description (str):
            long_description (str):
        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            activation_webhook_url (str, none_type): [optional]  # noqa: E501
            post_activation_redirect_uri (str, none_type): [optional]  # noqa: E501
            viewer_plugins_urls ([str], none_type): [optional]  # noqa: E501
            settings_url (str, none_type): this URL will be called with query params ?cloud_id=. [optional]  # noqa: E501
            is_public (bool): [optional]  # noqa: E501
            tags ([str]): [optional]  # noqa: E501
            logo (str, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.name = name
        self.short_description = short_description
        self.long_description = long_description
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
