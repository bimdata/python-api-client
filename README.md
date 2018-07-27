# bimdata-api-client
BIMData API documentation

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import bimdata_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import bimdata_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ifc_checker = bimdata_api_client.IfcChecker() # IfcChecker | 

try:
    api_response = api_instance.create_checker(cloud_pk, ifc_pk, project_pk, ifc_checker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->create_checker: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api-beta.bimdata.io/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CheckplanApi* | [**create_checker**](docs/CheckplanApi.md#create_checker) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker | 
*CheckplanApi* | [**create_checker_result**](docs/CheckplanApi.md#create_checker_result) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result | 
*CheckplanApi* | [**create_checkplan**](docs/CheckplanApi.md#create_checkplan) | **POST** /cloud/{cloud_pk}/project/{project_pk}/checkplan | 
*CheckplanApi* | [**create_rule**](docs/CheckplanApi.md#create_rule) | **POST** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule | 
*CheckplanApi* | [**create_rule_component**](docs/CheckplanApi.md#create_rule_component) | **POST** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent | 
*CheckplanApi* | [**create_ruleset**](docs/CheckplanApi.md#create_ruleset) | **POST** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset | 
*CheckplanApi* | [**delete_checker**](docs/CheckplanApi.md#delete_checker) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id} | 
*CheckplanApi* | [**delete_checker_result**](docs/CheckplanApi.md#delete_checker_result) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result/{id} | 
*CheckplanApi* | [**delete_checkplan**](docs/CheckplanApi.md#delete_checkplan) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{id} | 
*CheckplanApi* | [**delete_rule**](docs/CheckplanApi.md#delete_rule) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{id} | 
*CheckplanApi* | [**delete_rule_component**](docs/CheckplanApi.md#delete_rule_component) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent/{id} | 
*CheckplanApi* | [**delete_ruleset**](docs/CheckplanApi.md#delete_ruleset) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{id} | 
*CheckplanApi* | [**full_update_checker**](docs/CheckplanApi.md#full_update_checker) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id} | 
*CheckplanApi* | [**full_update_checker_result**](docs/CheckplanApi.md#full_update_checker_result) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result/{id} | 
*CheckplanApi* | [**full_update_checkplan**](docs/CheckplanApi.md#full_update_checkplan) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{id} | 
*CheckplanApi* | [**full_update_rule**](docs/CheckplanApi.md#full_update_rule) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{id} | 
*CheckplanApi* | [**full_update_rule_component**](docs/CheckplanApi.md#full_update_rule_component) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent/{id} | 
*CheckplanApi* | [**full_update_ruleset**](docs/CheckplanApi.md#full_update_ruleset) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{id} | 
*CheckplanApi* | [**get_checker**](docs/CheckplanApi.md#get_checker) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id} | 
*CheckplanApi* | [**get_checker_result**](docs/CheckplanApi.md#get_checker_result) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result/{id} | 
*CheckplanApi* | [**get_checker_results**](docs/CheckplanApi.md#get_checker_results) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result | 
*CheckplanApi* | [**get_checkers**](docs/CheckplanApi.md#get_checkers) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker | 
*CheckplanApi* | [**get_checkplan**](docs/CheckplanApi.md#get_checkplan) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{id} | 
*CheckplanApi* | [**get_checkplans**](docs/CheckplanApi.md#get_checkplans) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan | 
*CheckplanApi* | [**get_rule**](docs/CheckplanApi.md#get_rule) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{id} | 
*CheckplanApi* | [**get_rule_component**](docs/CheckplanApi.md#get_rule_component) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent/{id} | 
*CheckplanApi* | [**get_rule_components**](docs/CheckplanApi.md#get_rule_components) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent | 
*CheckplanApi* | [**get_rules**](docs/CheckplanApi.md#get_rules) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule | 
*CheckplanApi* | [**get_ruleset**](docs/CheckplanApi.md#get_ruleset) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{id} | 
*CheckplanApi* | [**get_rulesets**](docs/CheckplanApi.md#get_rulesets) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset | 
*CheckplanApi* | [**launch_new_check**](docs/CheckplanApi.md#launch_new_check) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id}/launch-check | 
*CheckplanApi* | [**update_checker**](docs/CheckplanApi.md#update_checker) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id} | 
*CheckplanApi* | [**update_checker_result**](docs/CheckplanApi.md#update_checker_result) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result/{id} | 
*CheckplanApi* | [**update_checkplan**](docs/CheckplanApi.md#update_checkplan) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{id} | 
*CheckplanApi* | [**update_rule**](docs/CheckplanApi.md#update_rule) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{id} | 
*CheckplanApi* | [**update_rule_component**](docs/CheckplanApi.md#update_rule_component) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent/{id} | 
*CheckplanApi* | [**update_ruleset**](docs/CheckplanApi.md#update_ruleset) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{id} | 
*CloudApi* | [**create_cloud**](docs/CloudApi.md#create_cloud) | **POST** /cloud | 
*CloudApi* | [**create_cloud_user**](docs/CloudApi.md#create_cloud_user) | **POST** /cloud/{cloud_pk}/user | 
*CloudApi* | [**delete_cloud_user**](docs/CloudApi.md#delete_cloud_user) | **DELETE** /cloud/{cloud_pk}/user/{id} | 
*CloudApi* | [**full_update_cloud**](docs/CloudApi.md#full_update_cloud) | **PUT** /cloud/{id} | 
*CloudApi* | [**full_update_cloud_user**](docs/CloudApi.md#full_update_cloud_user) | **PUT** /cloud/{cloud_pk}/user/{id} | 
*CloudApi* | [**get_cloud**](docs/CloudApi.md#get_cloud) | **GET** /cloud/{id} | 
*CloudApi* | [**get_cloud_size**](docs/CloudApi.md#get_cloud_size) | **GET** /cloud/{id}/size | 
*CloudApi* | [**get_cloud_user**](docs/CloudApi.md#get_cloud_user) | **GET** /cloud/{cloud_pk}/user/{id} | 
*CloudApi* | [**get_cloud_users**](docs/CloudApi.md#get_cloud_users) | **GET** /cloud/{cloud_pk}/user | 
*CloudApi* | [**get_clouds**](docs/CloudApi.md#get_clouds) | **GET** /cloud | 
*CloudApi* | [**update_cloud**](docs/CloudApi.md#update_cloud) | **PATCH** /cloud/{id} | 
*CloudApi* | [**update_cloud_user**](docs/CloudApi.md#update_cloud_user) | **PATCH** /cloud/{cloud_pk}/user/{id} | 
*IfcApi* | [**bulk_delete_ifc_classifications**](docs/IfcApi.md#bulk_delete_ifc_classifications) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/list_destroy | 
*IfcApi* | [**bulk_delete_ifc_properties**](docs/IfcApi.md#bulk_delete_ifc_properties) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/bulk_destroy | 
*IfcApi* | [**bulk_delete_ifc_property_definitions**](docs/IfcApi.md#bulk_delete_ifc_property_definitions) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/bulk_destroy | 
*IfcApi* | [**bulk_delete_ifc_units**](docs/IfcApi.md#bulk_delete_ifc_units) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/bulk_destroy | 
*IfcApi* | [**bulk_delete_property_set**](docs/IfcApi.md#bulk_delete_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/bulk_destroy | 
*IfcApi* | [**bulk_full_update_elements**](docs/IfcApi.md#bulk_full_update_elements) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/bulk_update | 
*IfcApi* | [**bulk_full_update_ifc_property**](docs/IfcApi.md#bulk_full_update_ifc_property) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/bulk_update | 
*IfcApi* | [**bulk_remove_classifications_of_element**](docs/IfcApi.md#bulk_remove_classifications_of_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification/bulk_destroy | 
*IfcApi* | [**bulk_remove_elements_from_classification**](docs/IfcApi.md#bulk_remove_elements_from_classification) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/{ifc_classification_pk}/element/bulk_destroy | 
*IfcApi* | [**bulk_update_elements**](docs/IfcApi.md#bulk_update_elements) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/bulk_update | 
*IfcApi* | [**bulk_update_ifc_property**](docs/IfcApi.md#bulk_update_ifc_property) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/bulk_update | 
*IfcApi* | [**create_classification_element_relations**](docs/IfcApi.md#create_classification_element_relations) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification-element | 
*IfcApi* | [**create_classifications_of_element**](docs/IfcApi.md#create_classifications_of_element) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification | 
*IfcApi* | [**create_element**](docs/IfcApi.md#create_element) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element | 
*IfcApi* | [**create_element_property_set**](docs/IfcApi.md#create_element_property_set) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset | 
*IfcApi* | [**create_element_property_set_property**](docs/IfcApi.md#create_element_property_set_property) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property | 
*IfcApi* | [**create_element_property_set_property_definition**](docs/IfcApi.md#create_element_property_set_property_definition) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition | 
*IfcApi* | [**create_element_property_set_property_definition_unit**](docs/IfcApi.md#create_element_property_set_property_definition_unit) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit | 
*IfcApi* | [**create_ifc_property_definition**](docs/IfcApi.md#create_ifc_property_definition) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition | 
*IfcApi* | [**create_ifc_unit**](docs/IfcApi.md#create_ifc_unit) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit | 
*IfcApi* | [**create_property_set**](docs/IfcApi.md#create_property_set) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset | 
*IfcApi* | [**create_property_set_element_relations**](docs/IfcApi.md#create_property_set_element_relations) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset-element | 
*IfcApi* | [**create_raw_elements**](docs/IfcApi.md#create_raw_elements) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/raw | 
*IfcApi* | [**create_space**](docs/IfcApi.md#create_space) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space | 
*IfcApi* | [**create_zone**](docs/IfcApi.md#create_zone) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone | 
*IfcApi* | [**create_zone_space**](docs/IfcApi.md#create_zone_space) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space | 
*IfcApi* | [**delete_element**](docs/IfcApi.md#delete_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | 
*IfcApi* | [**delete_ifc**](docs/IfcApi.md#delete_ifc) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | 
*IfcApi* | [**delete_ifc_property**](docs/IfcApi.md#delete_ifc_property) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | 
*IfcApi* | [**delete_ifc_property_definition**](docs/IfcApi.md#delete_ifc_property_definition) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | 
*IfcApi* | [**delete_ifc_unit**](docs/IfcApi.md#delete_ifc_unit) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | 
*IfcApi* | [**delete_property_set**](docs/IfcApi.md#delete_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | 
*IfcApi* | [**delete_space**](docs/IfcApi.md#delete_space) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | 
*IfcApi* | [**delete_zone**](docs/IfcApi.md#delete_zone) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | 
*IfcApi* | [**delete_zone_space**](docs/IfcApi.md#delete_zone_space) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | 
*IfcApi* | [**full_update_element**](docs/IfcApi.md#full_update_element) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | 
*IfcApi* | [**full_update_ifc**](docs/IfcApi.md#full_update_ifc) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | 
*IfcApi* | [**full_update_ifc_property**](docs/IfcApi.md#full_update_ifc_property) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | 
*IfcApi* | [**full_update_ifc_property_definition**](docs/IfcApi.md#full_update_ifc_property_definition) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | 
*IfcApi* | [**full_update_ifc_unit**](docs/IfcApi.md#full_update_ifc_unit) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | 
*IfcApi* | [**full_update_property_set**](docs/IfcApi.md#full_update_property_set) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | 
*IfcApi* | [**full_update_space**](docs/IfcApi.md#full_update_space) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | 
*IfcApi* | [**full_update_zone**](docs/IfcApi.md#full_update_zone) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | 
*IfcApi* | [**full_update_zone_space**](docs/IfcApi.md#full_update_zone_space) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | 
*IfcApi* | [**get_classifications_of_element**](docs/IfcApi.md#get_classifications_of_element) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification | 
*IfcApi* | [**get_element**](docs/IfcApi.md#get_element) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | 
*IfcApi* | [**get_element_property_set**](docs/IfcApi.md#get_element_property_set) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{id} | 
*IfcApi* | [**get_element_property_set_properties**](docs/IfcApi.md#get_element_property_set_properties) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property | 
*IfcApi* | [**get_element_property_set_property**](docs/IfcApi.md#get_element_property_set_property) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{id} | 
*IfcApi* | [**get_element_property_set_property_definition**](docs/IfcApi.md#get_element_property_set_property_definition) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{id} | 
*IfcApi* | [**get_element_property_set_property_definition_unit**](docs/IfcApi.md#get_element_property_set_property_definition_unit) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit/{id} | 
*IfcApi* | [**get_element_property_set_property_definition_units**](docs/IfcApi.md#get_element_property_set_property_definition_units) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit | 
*IfcApi* | [**get_element_property_set_property_definitions**](docs/IfcApi.md#get_element_property_set_property_definitions) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition | 
*IfcApi* | [**get_element_property_sets**](docs/IfcApi.md#get_element_property_sets) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset | 
*IfcApi* | [**get_elements**](docs/IfcApi.md#get_elements) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element | 
*IfcApi* | [**get_elements_from_classification**](docs/IfcApi.md#get_elements_from_classification) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/{ifc_classification_pk}/element | 
*IfcApi* | [**get_ifc**](docs/IfcApi.md#get_ifc) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | 
*IfcApi* | [**get_ifc_bvh**](docs/IfcApi.md#get_ifc_bvh) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/bvh | 
*IfcApi* | [**get_ifc_classifications**](docs/IfcApi.md#get_ifc_classifications) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification | 
*IfcApi* | [**get_ifc_gltf**](docs/IfcApi.md#get_ifc_gltf) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/gltf | 
*IfcApi* | [**get_ifc_map**](docs/IfcApi.md#get_ifc_map) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/map | 
*IfcApi* | [**get_ifc_properties**](docs/IfcApi.md#get_ifc_properties) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property | 
*IfcApi* | [**get_ifc_property**](docs/IfcApi.md#get_ifc_property) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | 
*IfcApi* | [**get_ifc_property_definition**](docs/IfcApi.md#get_ifc_property_definition) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | 
*IfcApi* | [**get_ifc_property_definitions**](docs/IfcApi.md#get_ifc_property_definitions) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition | 
*IfcApi* | [**get_ifc_structure**](docs/IfcApi.md#get_ifc_structure) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/structure | 
*IfcApi* | [**get_ifc_systems**](docs/IfcApi.md#get_ifc_systems) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/systems | 
*IfcApi* | [**get_ifc_unit**](docs/IfcApi.md#get_ifc_unit) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | 
*IfcApi* | [**get_ifc_units**](docs/IfcApi.md#get_ifc_units) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit | 
*IfcApi* | [**get_ifcs**](docs/IfcApi.md#get_ifcs) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc | 
*IfcApi* | [**get_property_set**](docs/IfcApi.md#get_property_set) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | 
*IfcApi* | [**get_property_sets**](docs/IfcApi.md#get_property_sets) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset | 
*IfcApi* | [**get_raw_elements**](docs/IfcApi.md#get_raw_elements) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/raw | 
*IfcApi* | [**get_space**](docs/IfcApi.md#get_space) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | 
*IfcApi* | [**get_spaces**](docs/IfcApi.md#get_spaces) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space | 
*IfcApi* | [**get_zone**](docs/IfcApi.md#get_zone) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | 
*IfcApi* | [**get_zone_space**](docs/IfcApi.md#get_zone_space) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | 
*IfcApi* | [**get_zone_spaces**](docs/IfcApi.md#get_zone_spaces) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space | 
*IfcApi* | [**get_zones**](docs/IfcApi.md#get_zones) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone | 
*IfcApi* | [**list_classification_element_relations**](docs/IfcApi.md#list_classification_element_relations) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification-element | 
*IfcApi* | [**remove_classification_of_element**](docs/IfcApi.md#remove_classification_of_element) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/classification/{id} | 
*IfcApi* | [**remove_element_property_set**](docs/IfcApi.md#remove_element_property_set) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{id} | 
*IfcApi* | [**remove_element_property_set_property**](docs/IfcApi.md#remove_element_property_set_property) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{id} | 
*IfcApi* | [**remove_element_property_set_property_definition**](docs/IfcApi.md#remove_element_property_set_property_definition) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{id} | 
*IfcApi* | [**remove_element_property_set_property_definition_unit**](docs/IfcApi.md#remove_element_property_set_property_definition_unit) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{element_uuid}/propertyset/{propertyset_pk}/property/{property_pk}/propertydefinition/{propertydefinition_pk}/unit/{id} | 
*IfcApi* | [**remove_elements_from_classification**](docs/IfcApi.md#remove_elements_from_classification) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/classification/{ifc_classification_pk}/element/{uuid} | 
*IfcApi* | [**update_element**](docs/IfcApi.md#update_element) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/element/{uuid} | 
*IfcApi* | [**update_ifc**](docs/IfcApi.md#update_ifc) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id} | 
*IfcApi* | [**update_ifc_files**](docs/IfcApi.md#update_ifc_files) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{id}/files | 
*IfcApi* | [**update_ifc_property**](docs/IfcApi.md#update_ifc_property) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/property/{id} | 
*IfcApi* | [**update_ifc_property_definition**](docs/IfcApi.md#update_ifc_property_definition) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertydefinition/{id} | 
*IfcApi* | [**update_ifc_unit**](docs/IfcApi.md#update_ifc_unit) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/unit/{id} | 
*IfcApi* | [**update_property_set**](docs/IfcApi.md#update_property_set) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/propertyset/{id} | 
*IfcApi* | [**update_space**](docs/IfcApi.md#update_space) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/space/{id} | 
*IfcApi* | [**update_zone**](docs/IfcApi.md#update_zone) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{id} | 
*IfcApi* | [**update_zone_space**](docs/IfcApi.md#update_zone_space) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/zone/{zone_pk}/space/{id} | 
*ProjectApi* | [**create_classification**](docs/ProjectApi.md#create_classification) | **POST** /cloud/{cloud_pk}/project/{project_pk}/classification | 
*ProjectApi* | [**create_document**](docs/ProjectApi.md#create_document) | **POST** /cloud/{cloud_pk}/project/{project_pk}/document | 
*ProjectApi* | [**create_folder**](docs/ProjectApi.md#create_folder) | **POST** /cloud/{cloud_pk}/project/{project_pk}/folder | 
*ProjectApi* | [**create_project**](docs/ProjectApi.md#create_project) | **POST** /cloud/{cloud_pk}/project | 
*ProjectApi* | [**create_project_user**](docs/ProjectApi.md#create_project_user) | **POST** /cloud/{cloud_pk}/project/{project_pk}/user | 
*ProjectApi* | [**delete_classification**](docs/ProjectApi.md#delete_classification) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | 
*ProjectApi* | [**delete_document**](docs/ProjectApi.md#delete_document) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | 
*ProjectApi* | [**delete_folder**](docs/ProjectApi.md#delete_folder) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | 
*ProjectApi* | [**delete_project**](docs/ProjectApi.md#delete_project) | **DELETE** /cloud/{cloud_pk}/project/{id} | 
*ProjectApi* | [**delete_project_user**](docs/ProjectApi.md#delete_project_user) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | 
*ProjectApi* | [**full_update_classification**](docs/ProjectApi.md#full_update_classification) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | 
*ProjectApi* | [**full_update_document**](docs/ProjectApi.md#full_update_document) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | 
*ProjectApi* | [**full_update_folder**](docs/ProjectApi.md#full_update_folder) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | 
*ProjectApi* | [**full_update_project**](docs/ProjectApi.md#full_update_project) | **PUT** /cloud/{cloud_pk}/project/{id} | 
*ProjectApi* | [**full_update_project_user**](docs/ProjectApi.md#full_update_project_user) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | 
*ProjectApi* | [**get_classification**](docs/ProjectApi.md#get_classification) | **GET** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | 
*ProjectApi* | [**get_classifications**](docs/ProjectApi.md#get_classifications) | **GET** /cloud/{cloud_pk}/project/{project_pk}/classification | 
*ProjectApi* | [**get_document**](docs/ProjectApi.md#get_document) | **GET** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | 
*ProjectApi* | [**get_documents**](docs/ProjectApi.md#get_documents) | **GET** /cloud/{cloud_pk}/project/{project_pk}/document | 
*ProjectApi* | [**get_folder**](docs/ProjectApi.md#get_folder) | **GET** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | 
*ProjectApi* | [**get_folders**](docs/ProjectApi.md#get_folders) | **GET** /cloud/{cloud_pk}/project/{project_pk}/folder | 
*ProjectApi* | [**get_project**](docs/ProjectApi.md#get_project) | **GET** /cloud/{cloud_pk}/project/{id} | 
*ProjectApi* | [**get_project_tree**](docs/ProjectApi.md#get_project_tree) | **GET** /cloud/{cloud_pk}/project/{id}/tree | 
*ProjectApi* | [**get_project_user**](docs/ProjectApi.md#get_project_user) | **GET** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | 
*ProjectApi* | [**get_project_users**](docs/ProjectApi.md#get_project_users) | **GET** /cloud/{cloud_pk}/project/{project_pk}/user | 
*ProjectApi* | [**get_projects**](docs/ProjectApi.md#get_projects) | **GET** /cloud/{cloud_pk}/project | 
*ProjectApi* | [**update_classification**](docs/ProjectApi.md#update_classification) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/classification/{id} | 
*ProjectApi* | [**update_document**](docs/ProjectApi.md#update_document) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/document/{id} | 
*ProjectApi* | [**update_folder**](docs/ProjectApi.md#update_folder) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/folder/{id} | 
*ProjectApi* | [**update_project**](docs/ProjectApi.md#update_project) | **PATCH** /cloud/{cloud_pk}/project/{id} | 
*ProjectApi* | [**update_project_user**](docs/ProjectApi.md#update_project_user) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/user/{id} | 
*UserApi* | [**ask_reset_password_token**](docs/UserApi.md#ask_reset_password_token) | **POST** /user/forgot-password | 
*UserApi* | [**full_update_notification**](docs/UserApi.md#full_update_notification) | **PUT** /user/notification/{id} | 
*UserApi* | [**get_notification**](docs/UserApi.md#get_notification) | **GET** /user/notification/{id} | 
*UserApi* | [**get_self_notifications**](docs/UserApi.md#get_self_notifications) | **GET** /user/notification | 
*UserApi* | [**get_self_projects**](docs/UserApi.md#get_self_projects) | **GET** /user/projects | 
*UserApi* | [**get_self_user**](docs/UserApi.md#get_self_user) | **GET** /user | 
*UserApi* | [**reset_password**](docs/UserApi.md#reset_password) | **POST** /user/reset-password | 
*UserApi* | [**sign_up**](docs/UserApi.md#sign_up) | **POST** /user/signup | 
*UserApi* | [**sign_up_with_invitation_token**](docs/UserApi.md#sign_up_with_invitation_token) | **POST** /user/invited-signup | 
*UserApi* | [**update_notification**](docs/UserApi.md#update_notification) | **PATCH** /user/notification/{id} | 
*UserApi* | [**update_self_user**](docs/UserApi.md#update_self_user) | **PATCH** /user | 


## Documentation For Models

 - [CheckPlan](docs/CheckPlan.md)
 - [CheckerResult](docs/CheckerResult.md)
 - [Classification](docs/Classification.md)
 - [Cloud](docs/Cloud.md)
 - [CloudRole](docs/CloudRole.md)
 - [Document](docs/Document.md)
 - [Element](docs/Element.md)
 - [ElementClassificationRelation](docs/ElementClassificationRelation.md)
 - [ElementPropertySetRelation](docs/ElementPropertySetRelation.md)
 - [Feature](docs/Feature.md)
 - [Folder](docs/Folder.md)
 - [ForgotPassword](docs/ForgotPassword.md)
 - [Ifc](docs/Ifc.md)
 - [IfcChecker](docs/IfcChecker.md)
 - [IfcFiles](docs/IfcFiles.md)
 - [InviteUser](docs/InviteUser.md)
 - [InvitedSignUpUser](docs/InvitedSignUpUser.md)
 - [ModelProperty](docs/ModelProperty.md)
 - [Notification](docs/Notification.md)
 - [Project](docs/Project.md)
 - [ProjectRole](docs/ProjectRole.md)
 - [PropertyDefinition](docs/PropertyDefinition.md)
 - [PropertySet](docs/PropertySet.md)
 - [RawDefinition](docs/RawDefinition.md)
 - [RawElement](docs/RawElement.md)
 - [RawElements](docs/RawElements.md)
 - [RawProperty](docs/RawProperty.md)
 - [RawPropertySet](docs/RawPropertySet.md)
 - [RawUnit](docs/RawUnit.md)
 - [ResetPassword](docs/ResetPassword.md)
 - [Rule](docs/Rule.md)
 - [RuleComponent](docs/RuleComponent.md)
 - [Ruleset](docs/Ruleset.md)
 - [SelfUser](docs/SelfUser.md)
 - [SignUpUser](docs/SignUpUser.md)
 - [Space](docs/Space.md)
 - [Unit](docs/Unit.md)
 - [User](docs/User.md)
 - [Zone](docs/Zone.md)
 - [ZoneSpace](docs/ZoneSpace.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

contact@bimdata.io


