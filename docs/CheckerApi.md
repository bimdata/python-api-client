# bimdata_api_client.CheckerApi

All URIs are relative to *https://api.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_checker**](CheckerApi.md#create_checker) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker | Create a checker to a model
[**create_checker_result**](CheckerApi.md#create_checker_result) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result | Create a CheckerResult
[**create_checkplan**](CheckerApi.md#create_checkplan) | **POST** /cloud/{cloud_pk}/project/{project_pk}/checkplan | Create a Checkplan
[**create_rule**](CheckerApi.md#create_rule) | **POST** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule | Create a Rule
[**create_rule_component**](CheckerApi.md#create_rule_component) | **POST** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent | Create a RuleComponent
[**create_ruleset**](CheckerApi.md#create_ruleset) | **POST** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset | Create a Ruleset
[**delete_checker**](CheckerApi.md#delete_checker) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id} | Delete a checker of a model
[**delete_checker_result**](CheckerApi.md#delete_checker_result) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result/{id} | Delete a CheckerResult
[**delete_checkplan**](CheckerApi.md#delete_checkplan) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{id} | Delete a Checkplan
[**delete_rule**](CheckerApi.md#delete_rule) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{id} | Delete a Rule
[**delete_rule_component**](CheckerApi.md#delete_rule_component) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent/{id} | Delete a RuleComponent
[**delete_ruleset**](CheckerApi.md#delete_ruleset) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{id} | Delete a Ruleset
[**get_checker**](CheckerApi.md#get_checker) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id} | Retrieve a checker of a model
[**get_checker_result**](CheckerApi.md#get_checker_result) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result/{id} | Retrieve one CheckerResult
[**get_checker_results**](CheckerApi.md#get_checker_results) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result | Retrieve all CheckerResults
[**get_checkers**](CheckerApi.md#get_checkers) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker | Retrieve all checkers of a model
[**get_checkplan**](CheckerApi.md#get_checkplan) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{id} | Retrieve one Checkplan
[**get_checkplans**](CheckerApi.md#get_checkplans) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan | Retrieve all Checkplans
[**get_rule**](CheckerApi.md#get_rule) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{id} | Retrieve one Rule
[**get_rule_component**](CheckerApi.md#get_rule_component) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent/{id} | Retrieve one RuleComponent
[**get_rule_components**](CheckerApi.md#get_rule_components) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent | Retrieve all RuleComponents
[**get_rules**](CheckerApi.md#get_rules) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule | Retrieve all Rules
[**get_ruleset**](CheckerApi.md#get_ruleset) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{id} | Retrieve one Ruleset
[**get_rulesets**](CheckerApi.md#get_rulesets) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset | Retrieve all Rulesets
[**launch_new_check**](CheckerApi.md#launch_new_check) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id}/launch-check | Launch a new check on the model
[**update_checker**](CheckerApi.md#update_checker) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id} | Update some fields of a checker of a model
[**update_checker_result**](CheckerApi.md#update_checker_result) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result/{id} | Update some fields of a CheckerResult
[**update_checkplan**](CheckerApi.md#update_checkplan) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{id} | Update some fields of a Checkplan
[**update_rule**](CheckerApi.md#update_rule) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{id} | Update some fields of a Rule
[**update_rule_component**](CheckerApi.md#update_rule_component) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent/{id} | Update some fields of a RuleComponent
[**update_ruleset**](CheckerApi.md#update_ruleset) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{id} | Update some fields of a Ruleset


# **create_checker**
> IfcChecker create_checker(cloud_pk, ifc_pk, project_pk, data)

Create a checker to a model

A checker is a link between a checkplan and a model. A checker can launch a check multiple time and store all the results Required scopes: check:write, ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcChecker() # IfcChecker | 

    try:
        # Create a checker to a model
        api_response = api_instance.create_checker(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_checker: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcChecker() # IfcChecker | 

    try:
        # Create a checker to a model
        api_response = api_instance.create_checker(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_checker: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcChecker() # IfcChecker | 

    try:
        # Create a checker to a model
        api_response = api_instance.create_checker(cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**IfcChecker**](IfcChecker.md)|  | 

### Return type

[**IfcChecker**](IfcChecker.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_checker_result**
> CheckerResult create_checker_result(checker_pk, cloud_pk, ifc_pk, project_pk, data)

Create a CheckerResult

TCreate a CheckerResult Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.CheckerResult() # CheckerResult | 

    try:
        # Create a CheckerResult
        api_response = api_instance.create_checker_result(checker_pk, cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_checker_result: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.CheckerResult() # CheckerResult | 

    try:
        # Create a CheckerResult
        api_response = api_instance.create_checker_result(checker_pk, cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_checker_result: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.CheckerResult() # CheckerResult | 

    try:
        # Create a CheckerResult
        api_response = api_instance.create_checker_result(checker_pk, cloud_pk, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_checker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checker_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**CheckerResult**](CheckerResult.md)|  | 

### Return type

[**CheckerResult**](CheckerResult.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_checkplan**
> CheckPlan create_checkplan(cloud_pk, project_pk, data)

Create a Checkplan

TCreate a Checkplan Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.CheckPlan() # CheckPlan | 

    try:
        # Create a Checkplan
        api_response = api_instance.create_checkplan(cloud_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_checkplan: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.CheckPlan() # CheckPlan | 

    try:
        # Create a Checkplan
        api_response = api_instance.create_checkplan(cloud_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_checkplan: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.CheckPlan() # CheckPlan | 

    try:
        # Create a Checkplan
        api_response = api_instance.create_checkplan(cloud_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_checkplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**CheckPlan**](CheckPlan.md)|  | 

### Return type

[**CheckPlan**](CheckPlan.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rule**
> Rule create_rule(check_plan_pk, cloud_pk, project_pk, ruleset_pk, data)

Create a Rule

TCreate a Rule Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
data = bimdata_api_client.Rule() # Rule | 

    try:
        # Create a Rule
        api_response = api_instance.create_rule(check_plan_pk, cloud_pk, project_pk, ruleset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_rule: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
data = bimdata_api_client.Rule() # Rule | 

    try:
        # Create a Rule
        api_response = api_instance.create_rule(check_plan_pk, cloud_pk, project_pk, ruleset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_rule: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
data = bimdata_api_client.Rule() # Rule | 

    try:
        # Create a Rule
        api_response = api_instance.create_rule(check_plan_pk, cloud_pk, project_pk, ruleset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **data** | [**Rule**](Rule.md)|  | 

### Return type

[**Rule**](Rule.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rule_component**
> RuleComponent create_rule_component(check_plan_pk, cloud_pk, project_pk, rule_pk, ruleset_pk, data)

Create a RuleComponent

TCreate a RuleComponent Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
data = bimdata_api_client.RuleComponent() # RuleComponent | 

    try:
        # Create a RuleComponent
        api_response = api_instance.create_rule_component(check_plan_pk, cloud_pk, project_pk, rule_pk, ruleset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_rule_component: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
data = bimdata_api_client.RuleComponent() # RuleComponent | 

    try:
        # Create a RuleComponent
        api_response = api_instance.create_rule_component(check_plan_pk, cloud_pk, project_pk, rule_pk, ruleset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_rule_component: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
data = bimdata_api_client.RuleComponent() # RuleComponent | 

    try:
        # Create a RuleComponent
        api_response = api_instance.create_rule_component(check_plan_pk, cloud_pk, project_pk, rule_pk, ruleset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_rule_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **data** | [**RuleComponent**](RuleComponent.md)|  | 

### Return type

[**RuleComponent**](RuleComponent.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ruleset**
> Ruleset create_ruleset(check_plan_pk, cloud_pk, project_pk, data)

Create a Ruleset

TCreate a Ruleset Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Ruleset() # Ruleset | 

    try:
        # Create a Ruleset
        api_response = api_instance.create_ruleset(check_plan_pk, cloud_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_ruleset: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Ruleset() # Ruleset | 

    try:
        # Create a Ruleset
        api_response = api_instance.create_ruleset(check_plan_pk, cloud_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_ruleset: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Ruleset() # Ruleset | 

    try:
        # Create a Ruleset
        api_response = api_instance.create_ruleset(check_plan_pk, cloud_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->create_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**Ruleset**](Ruleset.md)|  | 

### Return type

[**Ruleset**](Ruleset.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_checker**
> delete_checker(cloud_pk, id, ifc_pk, project_pk)

Delete a checker of a model

A checker is a link between a checkplan and a model. A checker can launch a check multiple time and store all the results Required scopes: check:write, ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc checker.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a checker of a model
        api_instance.delete_checker(cloud_pk, id, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_checker: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc checker.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a checker of a model
        api_instance.delete_checker(cloud_pk, id, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_checker: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc checker.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a checker of a model
        api_instance.delete_checker(cloud_pk, id, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc checker. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_checker_result**
> delete_checker_result(checker_pk, cloud_pk, id, ifc_pk, project_pk)

Delete a CheckerResult

Delete a CheckerResult Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this checker result.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a CheckerResult
        api_instance.delete_checker_result(checker_pk, cloud_pk, id, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_checker_result: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this checker result.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a CheckerResult
        api_instance.delete_checker_result(checker_pk, cloud_pk, id, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_checker_result: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this checker result.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a CheckerResult
        api_instance.delete_checker_result(checker_pk, cloud_pk, id, ifc_pk, project_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_checker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checker_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this checker result. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_checkplan**
> delete_checkplan(cloud_pk, id, project_pk)

Delete a Checkplan

Delete a Checkplan Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this check plan.
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a Checkplan
        api_instance.delete_checkplan(cloud_pk, id, project_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_checkplan: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this check plan.
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a Checkplan
        api_instance.delete_checkplan(cloud_pk, id, project_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_checkplan: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this check plan.
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a Checkplan
        api_instance.delete_checkplan(cloud_pk, id, project_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_checkplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this check plan. | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule**
> delete_rule(check_plan_pk, cloud_pk, id, project_pk, ruleset_pk)

Delete a Rule

Delete a Rule Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule.
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Delete a Rule
        api_instance.delete_rule(check_plan_pk, cloud_pk, id, project_pk, ruleset_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_rule: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule.
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Delete a Rule
        api_instance.delete_rule(check_plan_pk, cloud_pk, id, project_pk, ruleset_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_rule: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule.
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Delete a Rule
        api_instance.delete_rule(check_plan_pk, cloud_pk, id, project_pk, ruleset_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this rule. | 
 **project_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule_component**
> delete_rule_component(check_plan_pk, cloud_pk, id, project_pk, rule_pk, ruleset_pk)

Delete a RuleComponent

Delete a RuleComponent Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule component.
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Delete a RuleComponent
        api_instance.delete_rule_component(check_plan_pk, cloud_pk, id, project_pk, rule_pk, ruleset_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_rule_component: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule component.
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Delete a RuleComponent
        api_instance.delete_rule_component(check_plan_pk, cloud_pk, id, project_pk, rule_pk, ruleset_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_rule_component: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule component.
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Delete a RuleComponent
        api_instance.delete_rule_component(check_plan_pk, cloud_pk, id, project_pk, rule_pk, ruleset_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_rule_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this rule component. | 
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ruleset**
> delete_ruleset(check_plan_pk, cloud_pk, id, project_pk)

Delete a Ruleset

Delete a Ruleset Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ruleset.
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a Ruleset
        api_instance.delete_ruleset(check_plan_pk, cloud_pk, id, project_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_ruleset: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ruleset.
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a Ruleset
        api_instance.delete_ruleset(check_plan_pk, cloud_pk, id, project_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_ruleset: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ruleset.
project_pk = 'project_pk_example' # str | 

    try:
        # Delete a Ruleset
        api_instance.delete_ruleset(check_plan_pk, cloud_pk, id, project_pk)
    except ApiException as e:
        print("Exception when calling CheckerApi->delete_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ruleset. | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checker**
> IfcChecker get_checker(cloud_pk, id, ifc_pk, project_pk)

Retrieve a checker of a model

A checker is a link between a checkplan and a model. A checker can launch a check multiple time and store all the results Required scopes: check:read, ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc checker.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve a checker of a model
        api_response = api_instance.get_checker(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checker: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc checker.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve a checker of a model
        api_response = api_instance.get_checker(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checker: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc checker.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve a checker of a model
        api_response = api_instance.get_checker(cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc checker. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**IfcChecker**](IfcChecker.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checker_result**
> CheckerResult get_checker_result(checker_pk, cloud_pk, id, ifc_pk, project_pk)

Retrieve one CheckerResult

Retrieve one CheckerResult Required scopes: check:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this checker result.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve one CheckerResult
        api_response = api_instance.get_checker_result(checker_pk, cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checker_result: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this checker result.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve one CheckerResult
        api_response = api_instance.get_checker_result(checker_pk, cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checker_result: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this checker result.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve one CheckerResult
        api_response = api_instance.get_checker_result(checker_pk, cloud_pk, id, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checker_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this checker result. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**CheckerResult**](CheckerResult.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checker_results**
> list[CheckerResult] get_checker_results(checker_pk, cloud_pk, ifc_pk, project_pk)

Retrieve all CheckerResults

Retrieve all CheckerResults Required scopes: check:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all CheckerResults
        api_response = api_instance.get_checker_results(checker_pk, cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checker_results: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all CheckerResults
        api_response = api_instance.get_checker_results(checker_pk, cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checker_results: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all CheckerResults
        api_response = api_instance.get_checker_results(checker_pk, cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checker_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checker_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[CheckerResult]**](CheckerResult.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkers**
> list[IfcChecker] get_checkers(cloud_pk, ifc_pk, project_pk)

Retrieve all checkers of a model

A checker is a link between a checkplan and a model. A checker can launch a check multiple time and store all the results Required scopes: check:read, ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all checkers of a model
        api_response = api_instance.get_checkers(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checkers: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all checkers of a model
        api_response = api_instance.get_checkers(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checkers: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all checkers of a model
        api_response = api_instance.get_checkers(cloud_pk, ifc_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checkers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[IfcChecker]**](IfcChecker.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkplan**
> CheckPlan get_checkplan(cloud_pk, id, project_pk)

Retrieve one Checkplan

Retrieve one Checkplan Required scopes: check:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this check plan.
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve one Checkplan
        api_response = api_instance.get_checkplan(cloud_pk, id, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checkplan: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this check plan.
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve one Checkplan
        api_response = api_instance.get_checkplan(cloud_pk, id, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checkplan: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this check plan.
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve one Checkplan
        api_response = api_instance.get_checkplan(cloud_pk, id, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checkplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this check plan. | 
 **project_pk** | **str**|  | 

### Return type

[**CheckPlan**](CheckPlan.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkplans**
> list[CheckPlan] get_checkplans(cloud_pk, project_pk)

Retrieve all Checkplans

Retrieve all Checkplans Required scopes: check:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all Checkplans
        api_response = api_instance.get_checkplans(cloud_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checkplans: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all Checkplans
        api_response = api_instance.get_checkplans(cloud_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checkplans: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all Checkplans
        api_response = api_instance.get_checkplans(cloud_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_checkplans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[CheckPlan]**](CheckPlan.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule**
> Rule get_rule(check_plan_pk, cloud_pk, id, project_pk, ruleset_pk)

Retrieve one Rule

Retrieve one Rule Required scopes: check:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule.
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Retrieve one Rule
        api_response = api_instance.get_rule(check_plan_pk, cloud_pk, id, project_pk, ruleset_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rule: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule.
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Retrieve one Rule
        api_response = api_instance.get_rule(check_plan_pk, cloud_pk, id, project_pk, ruleset_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rule: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule.
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Retrieve one Rule
        api_response = api_instance.get_rule(check_plan_pk, cloud_pk, id, project_pk, ruleset_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this rule. | 
 **project_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 

### Return type

[**Rule**](Rule.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_component**
> RuleComponent get_rule_component(check_plan_pk, cloud_pk, id, project_pk, rule_pk, ruleset_pk)

Retrieve one RuleComponent

Retrieve one RuleComponent Required scopes: check:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule component.
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Retrieve one RuleComponent
        api_response = api_instance.get_rule_component(check_plan_pk, cloud_pk, id, project_pk, rule_pk, ruleset_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rule_component: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule component.
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Retrieve one RuleComponent
        api_response = api_instance.get_rule_component(check_plan_pk, cloud_pk, id, project_pk, rule_pk, ruleset_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rule_component: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule component.
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Retrieve one RuleComponent
        api_response = api_instance.get_rule_component(check_plan_pk, cloud_pk, id, project_pk, rule_pk, ruleset_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rule_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this rule component. | 
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 

### Return type

[**RuleComponent**](RuleComponent.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_components**
> list[RuleComponent] get_rule_components(check_plan_pk, cloud_pk, project_pk, rule_pk, ruleset_pk)

Retrieve all RuleComponents

Retrieve all RuleComponents Required scopes: check:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Retrieve all RuleComponents
        api_response = api_instance.get_rule_components(check_plan_pk, cloud_pk, project_pk, rule_pk, ruleset_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rule_components: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Retrieve all RuleComponents
        api_response = api_instance.get_rule_components(check_plan_pk, cloud_pk, project_pk, rule_pk, ruleset_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rule_components: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Retrieve all RuleComponents
        api_response = api_instance.get_rule_components(check_plan_pk, cloud_pk, project_pk, rule_pk, ruleset_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rule_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 

### Return type

[**list[RuleComponent]**](RuleComponent.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules**
> list[Rule] get_rules(check_plan_pk, cloud_pk, project_pk, ruleset_pk)

Retrieve all Rules

Retrieve all Rules Required scopes: check:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Retrieve all Rules
        api_response = api_instance.get_rules(check_plan_pk, cloud_pk, project_pk, ruleset_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rules: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Retrieve all Rules
        api_response = api_instance.get_rules(check_plan_pk, cloud_pk, project_pk, ruleset_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rules: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 

    try:
        # Retrieve all Rules
        api_response = api_instance.get_rules(check_plan_pk, cloud_pk, project_pk, ruleset_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 

### Return type

[**list[Rule]**](Rule.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ruleset**
> Ruleset get_ruleset(check_plan_pk, cloud_pk, id, project_pk)

Retrieve one Ruleset

Retrieve one Ruleset Required scopes: check:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ruleset.
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve one Ruleset
        api_response = api_instance.get_ruleset(check_plan_pk, cloud_pk, id, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_ruleset: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ruleset.
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve one Ruleset
        api_response = api_instance.get_ruleset(check_plan_pk, cloud_pk, id, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_ruleset: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ruleset.
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve one Ruleset
        api_response = api_instance.get_ruleset(check_plan_pk, cloud_pk, id, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ruleset. | 
 **project_pk** | **str**|  | 

### Return type

[**Ruleset**](Ruleset.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rulesets**
> list[Ruleset] get_rulesets(check_plan_pk, cloud_pk, project_pk)

Retrieve all Rulesets

Retrieve all Rulesets Required scopes: check:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all Rulesets
        api_response = api_instance.get_rulesets(check_plan_pk, cloud_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rulesets: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all Rulesets
        api_response = api_instance.get_rulesets(check_plan_pk, cloud_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rulesets: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

    try:
        # Retrieve all Rulesets
        api_response = api_instance.get_rulesets(check_plan_pk, cloud_pk, project_pk)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->get_rulesets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[Ruleset]**](Ruleset.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_new_check**
> launch_new_check(cloud_pk, id, ifc_pk, project_pk, data)

Launch a new check on the model

Starts a new check in the checker Required scopes: check:write, ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc checker.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcChecker() # IfcChecker | 

    try:
        # Launch a new check on the model
        api_instance.launch_new_check(cloud_pk, id, ifc_pk, project_pk, data)
    except ApiException as e:
        print("Exception when calling CheckerApi->launch_new_check: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc checker.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcChecker() # IfcChecker | 

    try:
        # Launch a new check on the model
        api_instance.launch_new_check(cloud_pk, id, ifc_pk, project_pk, data)
    except ApiException as e:
        print("Exception when calling CheckerApi->launch_new_check: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc checker.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcChecker() # IfcChecker | 

    try:
        # Launch a new check on the model
        api_instance.launch_new_check(cloud_pk, id, ifc_pk, project_pk, data)
    except ApiException as e:
        print("Exception when calling CheckerApi->launch_new_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc checker. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**IfcChecker**](IfcChecker.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_checker**
> IfcChecker update_checker(cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of a checker of a model

A checker is a link between a checkplan and a model. A checker can launch a check multiple time and store all the results Required scopes: check:write, ifc:read

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc checker.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcChecker() # IfcChecker | 

    try:
        # Update some fields of a checker of a model
        api_response = api_instance.update_checker(cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_checker: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc checker.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcChecker() # IfcChecker | 

    try:
        # Update some fields of a checker of a model
        api_response = api_instance.update_checker(cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_checker: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ifc checker.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.IfcChecker() # IfcChecker | 

    try:
        # Update some fields of a checker of a model
        api_response = api_instance.update_checker(cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ifc checker. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**IfcChecker**](IfcChecker.md)|  | 

### Return type

[**IfcChecker**](IfcChecker.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_checker_result**
> CheckerResult update_checker_result(checker_pk, cloud_pk, id, ifc_pk, project_pk, data)

Update some fields of a CheckerResult

Update some fields of a CheckerResult Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this checker result.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.CheckerResult() # CheckerResult | 

    try:
        # Update some fields of a CheckerResult
        api_response = api_instance.update_checker_result(checker_pk, cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_checker_result: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this checker result.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.CheckerResult() # CheckerResult | 

    try:
        # Update some fields of a CheckerResult
        api_response = api_instance.update_checker_result(checker_pk, cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_checker_result: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this checker result.
ifc_pk = 'ifc_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.CheckerResult() # CheckerResult | 

    try:
        # Update some fields of a CheckerResult
        api_response = api_instance.update_checker_result(checker_pk, cloud_pk, id, ifc_pk, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_checker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checker_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this checker result. | 
 **ifc_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**CheckerResult**](CheckerResult.md)|  | 

### Return type

[**CheckerResult**](CheckerResult.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_checkplan**
> CheckPlan update_checkplan(cloud_pk, id, project_pk, data)

Update some fields of a Checkplan

Update some fields of a Checkplan Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this check plan.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.CheckPlan() # CheckPlan | 

    try:
        # Update some fields of a Checkplan
        api_response = api_instance.update_checkplan(cloud_pk, id, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_checkplan: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this check plan.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.CheckPlan() # CheckPlan | 

    try:
        # Update some fields of a Checkplan
        api_response = api_instance.update_checkplan(cloud_pk, id, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_checkplan: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this check plan.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.CheckPlan() # CheckPlan | 

    try:
        # Update some fields of a Checkplan
        api_response = api_instance.update_checkplan(cloud_pk, id, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_checkplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this check plan. | 
 **project_pk** | **str**|  | 
 **data** | [**CheckPlan**](CheckPlan.md)|  | 

### Return type

[**CheckPlan**](CheckPlan.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule**
> Rule update_rule(check_plan_pk, cloud_pk, id, project_pk, ruleset_pk, data)

Update some fields of a Rule

Update some fields of a Rule Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule.
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
data = bimdata_api_client.Rule() # Rule | 

    try:
        # Update some fields of a Rule
        api_response = api_instance.update_rule(check_plan_pk, cloud_pk, id, project_pk, ruleset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_rule: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule.
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
data = bimdata_api_client.Rule() # Rule | 

    try:
        # Update some fields of a Rule
        api_response = api_instance.update_rule(check_plan_pk, cloud_pk, id, project_pk, ruleset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_rule: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule.
project_pk = 'project_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
data = bimdata_api_client.Rule() # Rule | 

    try:
        # Update some fields of a Rule
        api_response = api_instance.update_rule(check_plan_pk, cloud_pk, id, project_pk, ruleset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this rule. | 
 **project_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **data** | [**Rule**](Rule.md)|  | 

### Return type

[**Rule**](Rule.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule_component**
> RuleComponent update_rule_component(check_plan_pk, cloud_pk, id, project_pk, rule_pk, ruleset_pk, data)

Update some fields of a RuleComponent

Update some fields of a RuleComponent Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule component.
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
data = bimdata_api_client.RuleComponent() # RuleComponent | 

    try:
        # Update some fields of a RuleComponent
        api_response = api_instance.update_rule_component(check_plan_pk, cloud_pk, id, project_pk, rule_pk, ruleset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_rule_component: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule component.
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
data = bimdata_api_client.RuleComponent() # RuleComponent | 

    try:
        # Update some fields of a RuleComponent
        api_response = api_instance.update_rule_component(check_plan_pk, cloud_pk, id, project_pk, rule_pk, ruleset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_rule_component: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this rule component.
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
data = bimdata_api_client.RuleComponent() # RuleComponent | 

    try:
        # Update some fields of a RuleComponent
        api_response = api_instance.update_rule_component(check_plan_pk, cloud_pk, id, project_pk, rule_pk, ruleset_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_rule_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this rule component. | 
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **data** | [**RuleComponent**](RuleComponent.md)|  | 

### Return type

[**RuleComponent**](RuleComponent.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ruleset**
> Ruleset update_ruleset(check_plan_pk, cloud_pk, id, project_pk, data)

Update some fields of a Ruleset

Update some fields of a Ruleset Required scopes: check:write

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ruleset.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Ruleset() # Ruleset | 

    try:
        # Update some fields of a Ruleset
        api_response = api_instance.update_ruleset(check_plan_pk, cloud_pk, id, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_ruleset: %s\n" % e)
```

* OAuth Authentication (bimdata_connect):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ruleset.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Ruleset() # Ruleset | 

    try:
        # Update some fields of a Ruleset
        api_response = api_instance.update_ruleset(check_plan_pk, cloud_pk, id, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_ruleset: %s\n" % e)
```

* OAuth Authentication (client_credentials):
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.bimdata.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure OAuth2 access token for authorization: bimdata_connect
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: client_credentials
configuration = bimdata_api_client.Configuration(
    host = "https://api.bimdata.io"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with bimdata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bimdata_api_client.CheckerApi(api_client)
    check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 56 # int | A unique integer value identifying this ruleset.
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.Ruleset() # Ruleset | 

    try:
        # Update some fields of a Ruleset
        api_response = api_instance.update_ruleset(check_plan_pk, cloud_pk, id, project_pk, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CheckerApi->update_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **int**| A unique integer value identifying this ruleset. | 
 **project_pk** | **str**|  | 
 **data** | [**Ruleset**](Ruleset.md)|  | 

### Return type

[**Ruleset**](Ruleset.md)

### Authorization

[Bearer](../README.md#Bearer), [bimdata_connect](../README.md#bimdata_connect), [client_credentials](../README.md#client_credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | A required field is missing in the body |  -  |
**401** | The authentication failed. Your token may be expired, missing or malformed |  -  |
**403** | You don&#39;t have the authorization to access this resource. Check if the resource is exclusive to users or app (eg: /user is exclusive to users) or if your user has the right to access this resource. |  -  |
**404** | The resource does not exist or you don&#39;t have the right to see if the resource exists |  -  |
**500** | Something really bad happened. Check if your route is correct. By example: /cloud/[object Object]/project may raise a 500. An alert is automatically sent to us, we&#39;ll look at it shortly. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

