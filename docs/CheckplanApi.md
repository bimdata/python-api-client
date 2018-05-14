# bimdata_api_client.CheckplanApi

All URIs are relative to *https://api-staging.bimdata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_checker**](CheckplanApi.md#create_checker) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker | 
[**create_checker_result**](CheckplanApi.md#create_checker_result) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result | 
[**create_checkplan**](CheckplanApi.md#create_checkplan) | **POST** /cloud/{cloud_pk}/project/{project_pk}/checkplan | 
[**create_rule**](CheckplanApi.md#create_rule) | **POST** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule | 
[**create_rule_component**](CheckplanApi.md#create_rule_component) | **POST** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent | 
[**create_ruleset**](CheckplanApi.md#create_ruleset) | **POST** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset | 
[**delete_checker**](CheckplanApi.md#delete_checker) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id} | 
[**delete_checker_result**](CheckplanApi.md#delete_checker_result) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result/{id} | 
[**delete_checkplan**](CheckplanApi.md#delete_checkplan) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{id} | 
[**delete_rule**](CheckplanApi.md#delete_rule) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{id} | 
[**delete_rule_component**](CheckplanApi.md#delete_rule_component) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent/{id} | 
[**delete_ruleset**](CheckplanApi.md#delete_ruleset) | **DELETE** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{id} | 
[**full_update_checker**](CheckplanApi.md#full_update_checker) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id} | 
[**full_update_checker_result**](CheckplanApi.md#full_update_checker_result) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result/{id} | 
[**full_update_checkplan**](CheckplanApi.md#full_update_checkplan) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{id} | 
[**full_update_rule**](CheckplanApi.md#full_update_rule) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{id} | 
[**full_update_rule_component**](CheckplanApi.md#full_update_rule_component) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent/{id} | 
[**full_update_ruleset**](CheckplanApi.md#full_update_ruleset) | **PUT** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{id} | 
[**get_checker**](CheckplanApi.md#get_checker) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id} | 
[**get_checker_result**](CheckplanApi.md#get_checker_result) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result/{id} | 
[**get_checker_results**](CheckplanApi.md#get_checker_results) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result | 
[**get_checkers**](CheckplanApi.md#get_checkers) | **GET** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker | 
[**get_checkplan**](CheckplanApi.md#get_checkplan) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{id} | 
[**get_checkplans**](CheckplanApi.md#get_checkplans) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan | 
[**get_rule**](CheckplanApi.md#get_rule) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{id} | 
[**get_rule_component**](CheckplanApi.md#get_rule_component) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent/{id} | 
[**get_rule_components**](CheckplanApi.md#get_rule_components) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent | 
[**get_rules**](CheckplanApi.md#get_rules) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule | 
[**get_ruleset**](CheckplanApi.md#get_ruleset) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{id} | 
[**get_rulesets**](CheckplanApi.md#get_rulesets) | **GET** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset | 
[**launch_new_check**](CheckplanApi.md#launch_new_check) | **POST** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id}/launch-check | 
[**update_checker**](CheckplanApi.md#update_checker) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{id} | 
[**update_checker_result**](CheckplanApi.md#update_checker_result) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/ifc/{ifc_pk}/checker/{checker_pk}/result/{id} | 
[**update_checkplan**](CheckplanApi.md#update_checkplan) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{id} | 
[**update_rule**](CheckplanApi.md#update_rule) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{id} | 
[**update_rule_component**](CheckplanApi.md#update_rule_component) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{ruleset_pk}/rule/{rule_pk}/rulecomponent/{id} | 
[**update_ruleset**](CheckplanApi.md#update_ruleset) | **PATCH** /cloud/{cloud_pk}/project/{project_pk}/checkplan/{check_plan_pk}/ruleset/{id} | 


# **create_checker**
> WrappedClass create_checker(cloud_pk, project_pk, ifc_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.create_checker(cloud_pk, project_pk, ifc_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->create_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_checker_result**
> WrappedClass create_checker_result(checker_pk, cloud_pk, project_pk, ifc_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.create_checker_result(checker_pk, cloud_pk, project_pk, ifc_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->create_checker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checker_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_checkplan**
> WrappedClass create_checkplan(cloud_pk, project_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.create_checkplan(cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->create_checkplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rule**
> WrappedClass create_rule(ruleset_pk, check_plan_pk, cloud_pk, project_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.create_rule(ruleset_pk, check_plan_pk, cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->create_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rule_component**
> WrappedClass create_rule_component(cloud_pk, ruleset_pk, check_plan_pk, project_pk, rule_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.create_rule_component(cloud_pk, ruleset_pk, check_plan_pk, project_pk, rule_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->create_rule_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ruleset**
> WrappedClass create_ruleset(check_plan_pk, cloud_pk, project_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.create_ruleset(check_plan_pk, cloud_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->create_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_checker**
> delete_checker(cloud_pk, id, project_pk, ifc_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 

try:
    api_instance.delete_checker(cloud_pk, id, project_pk, ifc_pk)
except ApiException as e:
    print("Exception when calling CheckplanApi->delete_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_checker_result**
> delete_checker_result(cloud_pk, id, checker_pk, project_pk, ifc_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
checker_pk = 'checker_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 

try:
    api_instance.delete_checker_result(cloud_pk, id, checker_pk, project_pk, ifc_pk)
except ApiException as e:
    print("Exception when calling CheckplanApi->delete_checker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **checker_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_checkplan**
> delete_checkplan(cloud_pk, id, project_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.delete_checkplan(cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CheckplanApi->delete_checkplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule**
> delete_rule(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.delete_rule(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk)
except ApiException as e:
    print("Exception when calling CheckplanApi->delete_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule_component**
> delete_rule_component(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk, rule_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 

try:
    api_instance.delete_rule_component(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk, rule_pk)
except ApiException as e:
    print("Exception when calling CheckplanApi->delete_rule_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ruleset**
> delete_ruleset(check_plan_pk, cloud_pk, id, project_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_instance.delete_ruleset(check_plan_pk, cloud_pk, id, project_pk)
except ApiException as e:
    print("Exception when calling CheckplanApi->delete_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_checker**
> WrappedClass full_update_checker(cloud_pk, id, project_pk, ifc_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.full_update_checker(cloud_pk, id, project_pk, ifc_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->full_update_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_checker_result**
> WrappedClass full_update_checker_result(cloud_pk, id, checker_pk, project_pk, ifc_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
checker_pk = 'checker_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.full_update_checker_result(cloud_pk, id, checker_pk, project_pk, ifc_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->full_update_checker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **checker_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_checkplan**
> WrappedClass full_update_checkplan(cloud_pk, id, project_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.full_update_checkplan(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->full_update_checkplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_rule**
> WrappedClass full_update_rule(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.full_update_rule(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->full_update_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_rule_component**
> WrappedClass full_update_rule_component(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk, rule_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.full_update_rule_component(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk, rule_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->full_update_rule_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_ruleset**
> WrappedClass full_update_ruleset(check_plan_pk, cloud_pk, id, project_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.full_update_ruleset(check_plan_pk, cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->full_update_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checker**
> WrappedClass get_checker(cloud_pk, id, project_pk, ifc_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 

try:
    api_response = api_instance.get_checker(cloud_pk, id, project_pk, ifc_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checker_result**
> WrappedClass get_checker_result(cloud_pk, id, checker_pk, project_pk, ifc_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
checker_pk = 'checker_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 

try:
    api_response = api_instance.get_checker_result(cloud_pk, id, checker_pk, project_pk, ifc_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_checker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **checker_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checker_results**
> list[WrappedClass] get_checker_results(checker_pk, cloud_pk, project_pk, ifc_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 

try:
    api_response = api_instance.get_checker_results(checker_pk, cloud_pk, project_pk, ifc_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_checker_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checker_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 

### Return type

[**list[WrappedClass]**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkers**
> list[WrappedClass] get_checkers(cloud_pk, project_pk, ifc_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 

try:
    api_response = api_instance.get_checkers(cloud_pk, project_pk, ifc_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_checkers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 

### Return type

[**list[WrappedClass]**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkplan**
> WrappedClass get_checkplan(cloud_pk, id, project_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_checkplan(cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_checkplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkplans**
> list[WrappedClass] get_checkplans(cloud_pk, project_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_checkplans(cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_checkplans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[WrappedClass]**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule**
> WrappedClass get_rule(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_rule(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_component**
> WrappedClass get_rule_component(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk, rule_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 

try:
    api_response = api_instance.get_rule_component(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk, rule_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_rule_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_components**
> list[WrappedClass] get_rule_components(cloud_pk, ruleset_pk, check_plan_pk, project_pk, rule_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 

try:
    api_response = api_instance.get_rule_components(cloud_pk, ruleset_pk, check_plan_pk, project_pk, rule_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_rule_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 

### Return type

[**list[WrappedClass]**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules**
> list[WrappedClass] get_rules(ruleset_pk, check_plan_pk, cloud_pk, project_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_rules(ruleset_pk, check_plan_pk, cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[WrappedClass]**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ruleset**
> WrappedClass get_ruleset(check_plan_pk, cloud_pk, id, project_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_ruleset(check_plan_pk, cloud_pk, id, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rulesets**
> list[WrappedClass] get_rulesets(check_plan_pk, cloud_pk, project_pk)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
project_pk = 'project_pk_example' # str | 

try:
    api_response = api_instance.get_rulesets(check_plan_pk, cloud_pk, project_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_rulesets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **project_pk** | **str**|  | 

### Return type

[**list[WrappedClass]**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_new_check**
> launch_new_check(cloud_pk, id, project_pk, ifc_pk, data)



Starts a new check in the checker

### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_instance.launch_new_check(cloud_pk, id, project_pk, ifc_pk, data)
except ApiException as e:
    print("Exception when calling CheckplanApi->launch_new_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_checker**
> WrappedClass update_checker(cloud_pk, id, project_pk, ifc_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.update_checker(cloud_pk, id, project_pk, ifc_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->update_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_checker_result**
> WrappedClass update_checker_result(cloud_pk, id, checker_pk, project_pk, ifc_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
checker_pk = 'checker_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.update_checker_result(cloud_pk, id, checker_pk, project_pk, ifc_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->update_checker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **checker_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_checkplan**
> WrappedClass update_checkplan(cloud_pk, id, project_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.update_checkplan(cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->update_checkplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule**
> WrappedClass update_rule(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.update_rule(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->update_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule_component**
> WrappedClass update_rule_component(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk, rule_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.update_rule_component(cloud_pk, id, ruleset_pk, check_plan_pk, project_pk, rule_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->update_rule_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ruleset**
> WrappedClass update_ruleset(check_plan_pk, cloud_pk, id, project_pk, data)





### Example
```python
from __future__ import print_function
import time
import bimdata_api_client
from bimdata_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = bimdata_api_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = bimdata_api_client.CheckplanApi(bimdata_api_client.ApiClient(configuration))
check_plan_pk = 'check_plan_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
project_pk = 'project_pk_example' # str | 
data = bimdata_api_client.WrappedClass() # WrappedClass | 

try:
    api_response = api_instance.update_ruleset(check_plan_pk, cloud_pk, id, project_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->update_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_plan_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **project_pk** | **str**|  | 
 **data** | [**WrappedClass**](WrappedClass.md)|  | 

### Return type

[**WrappedClass**](WrappedClass.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

