"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1 (v1)
    Contact: support@bimdata.io
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
    from bimdata_api_client.model.tag import Tag
    from bimdata_api_client.model.user import User
    from bimdata_api_client.model.visa import Visa
    globals()['Tag'] = Tag
    globals()['User'] = User
    globals()['Visa'] = Visa


class Document(ModelNormal):
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
        ('model_type',): {
            'None': None,
            'IFC': "IFC",
            'DWG': "DWG",
            'DXF': "DXF",
            'GLTF': "GLTF",
            'PDF': "PDF",
            'JPEG': "JPEG",
            'PNG': "PNG",
            'OBJ': "OBJ",
            'POINT_CLOUD': "POINT_CLOUD",
            'NULL': "null",
        },
        ('user_permission',): {
            '1': 1,
            '50': 50,
            '100': 100,
        },
    }

    validations = {
        ('name',): {
            'max_length': 512,
        },
        ('file_name',): {
            'max_length': 512,
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
            'created_by': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'project': (int,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'file': (str,),  # noqa: E501
            'size': (int, none_type,),  # noqa: E501
            'tags': ([Tag],),  # noqa: E501
            'visas': ([Visa],),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'model_id': (int, none_type,),  # noqa: E501
            'model_type': (str, none_type,),  # noqa: E501
            'ifc_id': (int, none_type,),  # noqa: E501
            'user_permission': (int,),  # noqa: E501
            'is_head_version': (bool,),  # noqa: E501
            'office_preview': (str, none_type,),  # noqa: E501
            'parent_id': (int, none_type,),  # noqa: E501
            'file_name': (str,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'project': 'project',  # noqa: E501
        'name': 'name',  # noqa: E501
        'file': 'file',  # noqa: E501
        'size': 'size',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'visas': 'visas',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'model_id': 'model_id',  # noqa: E501
        'model_type': 'model_type',  # noqa: E501
        'ifc_id': 'ifc_id',  # noqa: E501
        'user_permission': 'user_permission',  # noqa: E501
        'is_head_version': 'is_head_version',  # noqa: E501
        'office_preview': 'office_preview',  # noqa: E501
        'parent_id': 'parent_id',  # noqa: E501
        'file_name': 'file_name',  # noqa: E501
        'description': 'description',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'created_by',  # noqa: E501
        'project',  # noqa: E501
        'size',  # noqa: E501
        'tags',  # noqa: E501
        'visas',  # noqa: E501
        'created_at',  # noqa: E501
        'updated_at',  # noqa: E501
        'model_id',  # noqa: E501
        'model_type',  # noqa: E501
        'ifc_id',  # noqa: E501
        'user_permission',  # noqa: E501
        'is_head_version',  # noqa: E501
        'office_preview',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, created_by, project, name, file, size, tags, visas, created_at, updated_at, model_id, model_type, ifc_id, user_permission, is_head_version, office_preview, *args, **kwargs):  # noqa: E501
        """Document - a model defined in OpenAPI

        Args:
            id (int):
            created_by (bool, date, datetime, dict, float, int, list, str, none_type):
            project (int):
            name (str): Shown name of the file
            file (str):
            size (int, none_type): Size of the file.
            tags ([Tag]):
            visas ([Visa]):
            created_at (datetime): Creation date
            updated_at (datetime): Date of the last update
            model_id (int, none_type):
            model_type (str, none_type): Model's type. Values can be IFC, DWG, DXF, GLTF, PDF, JPEG, PNG, OBJ, POINT_CLOUD
            ifc_id (int, none_type): DEPRECATED: Use 'model_id' instead.
            user_permission (int): Aggregate of group user permissions and folder default permission
            is_head_version (bool): Document is a head of version or is owned by another document
            office_preview (str, none_type): Office files will be converted as pdf to provide a web preview. Supported extensions are .ppt, .pptx, .odp, .xls, .xlsx, .ods, .doc, .docx, .odt

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
            parent_id (int, none_type): [optional]  # noqa: E501
            file_name (str): Full name of the file. [optional]  # noqa: E501
            description (str, none_type): Description of the file. [optional]  # noqa: E501
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
        self.created_by = created_by
        self.project = project
        self.name = name
        self.file = file
        self.size = size
        self.tags = tags
        self.visas = visas
        self.created_at = created_at
        self.updated_at = updated_at
        self.model_id = model_id
        self.model_type = model_type
        self.ifc_id = ifc_id
        self.user_permission = user_permission
        self.is_head_version = is_head_version
        self.office_preview = office_preview
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
    def __init__(self, name, file, *args, **kwargs):  # noqa: E501
        """Document - a model defined in OpenAPI

            name (str): Shown name of the file
            file (str):
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
            parent_id (int, none_type): [optional]  # noqa: E501
            file_name (str): Full name of the file. [optional]  # noqa: E501
            description (str, none_type): Description of the file. [optional]  # noqa: E501
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
        self.file = file
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
