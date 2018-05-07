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
> IfcChecker create_checker(project_pk, ifc_pk, cloud_pk, data)





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
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.IfcChecker() # IfcChecker | 

try:
    api_response = api_instance.create_checker(project_pk, ifc_pk, cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->create_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **data** | [**IfcChecker**](IfcChecker.md)|  | 

### Return type

[**IfcChecker**](IfcChecker.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_checker_result**
> CheckerResult create_checker_result(project_pk, checker_pk, ifc_pk, cloud_pk, data)





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
project_pk = 'project_pk_example' # str | 
checker_pk = 'checker_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.CheckerResult() # CheckerResult | 

try:
    api_response = api_instance.create_checker_result(project_pk, checker_pk, ifc_pk, cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->create_checker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **checker_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **data** | [**CheckerResult**](CheckerResult.md)|  | 

### Return type

[**CheckerResult**](CheckerResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_checkplan**
> CheckPlan create_checkplan(project_pk, cloud_pk, data)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
data = bimdata_api_client.CheckPlan() # CheckPlan | 

try:
    api_response = api_instance.create_checkplan(project_pk, cloud_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->create_checkplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **data** | [**CheckPlan**](CheckPlan.md)|  | 

### Return type

[**CheckPlan**](CheckPlan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rule**
> Rule create_rule(project_pk, cloud_pk, ruleset_pk, check_plan_pk, data)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
data = bimdata_api_client.Rule() # Rule | 

try:
    api_response = api_instance.create_rule(project_pk, cloud_pk, ruleset_pk, check_plan_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->create_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **data** | [**Rule**](Rule.md)|  | 

### Return type

[**Rule**](Rule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rule_component**
> RuleComponent create_rule_component(project_pk, rule_pk, cloud_pk, ruleset_pk, check_plan_pk, data)





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
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
data = bimdata_api_client.RuleComponent() # RuleComponent | 

try:
    api_response = api_instance.create_rule_component(project_pk, rule_pk, cloud_pk, ruleset_pk, check_plan_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->create_rule_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **data** | [**RuleComponent**](RuleComponent.md)|  | 

### Return type

[**RuleComponent**](RuleComponent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ruleset**
> Ruleset create_ruleset(project_pk, cloud_pk, check_plan_pk, data)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
data = bimdata_api_client.Ruleset() # Ruleset | 

try:
    api_response = api_instance.create_ruleset(project_pk, cloud_pk, check_plan_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->create_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **data** | [**Ruleset**](Ruleset.md)|  | 

### Return type

[**Ruleset**](Ruleset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_checker**
> delete_checker(project_pk, ifc_pk, cloud_pk, id)





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
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.delete_checker(project_pk, ifc_pk, cloud_pk, id)
except ApiException as e:
    print("Exception when calling CheckplanApi->delete_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_checker_result**
> delete_checker_result(project_pk, checker_pk, cloud_pk, ifc_pk, id)





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
project_pk = 'project_pk_example' # str | 
checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.delete_checker_result(project_pk, checker_pk, cloud_pk, ifc_pk, id)
except ApiException as e:
    print("Exception when calling CheckplanApi->delete_checker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **checker_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_checkplan**
> delete_checkplan(project_pk, cloud_pk, id)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.delete_checkplan(project_pk, cloud_pk, id)
except ApiException as e:
    print("Exception when calling CheckplanApi->delete_checkplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule**
> delete_rule(project_pk, cloud_pk, ruleset_pk, check_plan_pk, id)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.delete_rule(project_pk, cloud_pk, ruleset_pk, check_plan_pk, id)
except ApiException as e:
    print("Exception when calling CheckplanApi->delete_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule_component**
> delete_rule_component(project_pk, rule_pk, cloud_pk, ruleset_pk, check_plan_pk, id)





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
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.delete_rule_component(project_pk, rule_pk, cloud_pk, ruleset_pk, check_plan_pk, id)
except ApiException as e:
    print("Exception when calling CheckplanApi->delete_rule_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ruleset**
> delete_ruleset(project_pk, cloud_pk, check_plan_pk, id)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_instance.delete_ruleset(project_pk, cloud_pk, check_plan_pk, id)
except ApiException as e:
    print("Exception when calling CheckplanApi->delete_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_checker**
> IfcChecker full_update_checker(project_pk, ifc_pk, cloud_pk, id, data)





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
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.IfcChecker() # IfcChecker | 

try:
    api_response = api_instance.full_update_checker(project_pk, ifc_pk, cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->full_update_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**IfcChecker**](IfcChecker.md)|  | 

### Return type

[**IfcChecker**](IfcChecker.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_checker_result**
> CheckerResult full_update_checker_result(project_pk, checker_pk, cloud_pk, ifc_pk, id, data)





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
project_pk = 'project_pk_example' # str | 
checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.CheckerResult() # CheckerResult | 

try:
    api_response = api_instance.full_update_checker_result(project_pk, checker_pk, cloud_pk, ifc_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->full_update_checker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **checker_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**CheckerResult**](CheckerResult.md)|  | 

### Return type

[**CheckerResult**](CheckerResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_checkplan**
> CheckPlan full_update_checkplan(project_pk, cloud_pk, id, data)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.CheckPlan() # CheckPlan | 

try:
    api_response = api_instance.full_update_checkplan(project_pk, cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->full_update_checkplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**CheckPlan**](CheckPlan.md)|  | 

### Return type

[**CheckPlan**](CheckPlan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_rule**
> Rule full_update_rule(project_pk, cloud_pk, ruleset_pk, check_plan_pk, id, data)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.Rule() # Rule | 

try:
    api_response = api_instance.full_update_rule(project_pk, cloud_pk, ruleset_pk, check_plan_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->full_update_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**Rule**](Rule.md)|  | 

### Return type

[**Rule**](Rule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_rule_component**
> RuleComponent full_update_rule_component(project_pk, rule_pk, cloud_pk, ruleset_pk, check_plan_pk, id, data)





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
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.RuleComponent() # RuleComponent | 

try:
    api_response = api_instance.full_update_rule_component(project_pk, rule_pk, cloud_pk, ruleset_pk, check_plan_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->full_update_rule_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**RuleComponent**](RuleComponent.md)|  | 

### Return type

[**RuleComponent**](RuleComponent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **full_update_ruleset**
> Ruleset full_update_ruleset(project_pk, cloud_pk, check_plan_pk, id, data)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.Ruleset() # Ruleset | 

try:
    api_response = api_instance.full_update_ruleset(project_pk, cloud_pk, check_plan_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->full_update_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**Ruleset**](Ruleset.md)|  | 

### Return type

[**Ruleset**](Ruleset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checker**
> IfcChecker get_checker(project_pk, ifc_pk, cloud_pk, id)





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
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_checker(project_pk, ifc_pk, cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**IfcChecker**](IfcChecker.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checker_result**
> CheckerResult get_checker_result(project_pk, checker_pk, cloud_pk, ifc_pk, id)





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
project_pk = 'project_pk_example' # str | 
checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_checker_result(project_pk, checker_pk, cloud_pk, ifc_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_checker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **checker_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**CheckerResult**](CheckerResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checker_results**
> list[CheckerResult] get_checker_results(project_pk, checker_pk, ifc_pk, cloud_pk)





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
project_pk = 'project_pk_example' # str | 
checker_pk = 'checker_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 

try:
    api_response = api_instance.get_checker_results(project_pk, checker_pk, ifc_pk, cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_checker_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **checker_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 

### Return type

[**list[CheckerResult]**](CheckerResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkers**
> list[IfcChecker] get_checkers(project_pk, ifc_pk, cloud_pk)





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
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 

try:
    api_response = api_instance.get_checkers(project_pk, ifc_pk, cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_checkers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 

### Return type

[**list[IfcChecker]**](IfcChecker.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkplan**
> CheckPlan get_checkplan(project_pk, cloud_pk, id)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_checkplan(project_pk, cloud_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_checkplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**CheckPlan**](CheckPlan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkplans**
> list[CheckPlan] get_checkplans(project_pk, cloud_pk)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 

try:
    api_response = api_instance.get_checkplans(project_pk, cloud_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_checkplans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 

### Return type

[**list[CheckPlan]**](CheckPlan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule**
> Rule get_rule(project_pk, cloud_pk, ruleset_pk, check_plan_pk, id)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_rule(project_pk, cloud_pk, ruleset_pk, check_plan_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**Rule**](Rule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_component**
> RuleComponent get_rule_component(project_pk, rule_pk, cloud_pk, ruleset_pk, check_plan_pk, id)





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
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_rule_component(project_pk, rule_pk, cloud_pk, ruleset_pk, check_plan_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_rule_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**RuleComponent**](RuleComponent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_components**
> list[RuleComponent] get_rule_components(project_pk, rule_pk, cloud_pk, ruleset_pk, check_plan_pk)





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
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 

try:
    api_response = api_instance.get_rule_components(project_pk, rule_pk, cloud_pk, ruleset_pk, check_plan_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_rule_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 

### Return type

[**list[RuleComponent]**](RuleComponent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules**
> list[Rule] get_rules(project_pk, cloud_pk, ruleset_pk, check_plan_pk)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 

try:
    api_response = api_instance.get_rules(project_pk, cloud_pk, ruleset_pk, check_plan_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 

### Return type

[**list[Rule]**](Rule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ruleset**
> Ruleset get_ruleset(project_pk, cloud_pk, check_plan_pk, id)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_ruleset(project_pk, cloud_pk, check_plan_pk, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**Ruleset**](Ruleset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rulesets**
> list[Ruleset] get_rulesets(project_pk, cloud_pk, check_plan_pk)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 

try:
    api_response = api_instance.get_rulesets(project_pk, cloud_pk, check_plan_pk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->get_rulesets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 

### Return type

[**list[Ruleset]**](Ruleset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_new_check**
> launch_new_check(project_pk, ifc_pk, cloud_pk, id, data)



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
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.IfcChecker() # IfcChecker | 

try:
    api_instance.launch_new_check(project_pk, ifc_pk, cloud_pk, id, data)
except ApiException as e:
    print("Exception when calling CheckplanApi->launch_new_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**IfcChecker**](IfcChecker.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_checker**
> IfcChecker update_checker(project_pk, ifc_pk, cloud_pk, id, data)





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
project_pk = 'project_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.IfcChecker() # IfcChecker | 

try:
    api_response = api_instance.update_checker(project_pk, ifc_pk, cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->update_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**IfcChecker**](IfcChecker.md)|  | 

### Return type

[**IfcChecker**](IfcChecker.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_checker_result**
> CheckerResult update_checker_result(project_pk, checker_pk, cloud_pk, ifc_pk, id, data)





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
project_pk = 'project_pk_example' # str | 
checker_pk = 'checker_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ifc_pk = 'ifc_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.CheckerResult() # CheckerResult | 

try:
    api_response = api_instance.update_checker_result(project_pk, checker_pk, cloud_pk, ifc_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->update_checker_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **checker_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ifc_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**CheckerResult**](CheckerResult.md)|  | 

### Return type

[**CheckerResult**](CheckerResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_checkplan**
> CheckPlan update_checkplan(project_pk, cloud_pk, id, data)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.CheckPlan() # CheckPlan | 

try:
    api_response = api_instance.update_checkplan(project_pk, cloud_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->update_checkplan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**CheckPlan**](CheckPlan.md)|  | 

### Return type

[**CheckPlan**](CheckPlan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule**
> Rule update_rule(project_pk, cloud_pk, ruleset_pk, check_plan_pk, id, data)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.Rule() # Rule | 

try:
    api_response = api_instance.update_rule(project_pk, cloud_pk, ruleset_pk, check_plan_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->update_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**Rule**](Rule.md)|  | 

### Return type

[**Rule**](Rule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule_component**
> RuleComponent update_rule_component(project_pk, rule_pk, cloud_pk, ruleset_pk, check_plan_pk, id, data)





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
project_pk = 'project_pk_example' # str | 
rule_pk = 'rule_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
ruleset_pk = 'ruleset_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.RuleComponent() # RuleComponent | 

try:
    api_response = api_instance.update_rule_component(project_pk, rule_pk, cloud_pk, ruleset_pk, check_plan_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->update_rule_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **rule_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **ruleset_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**RuleComponent**](RuleComponent.md)|  | 

### Return type

[**RuleComponent**](RuleComponent.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ruleset**
> Ruleset update_ruleset(project_pk, cloud_pk, check_plan_pk, id, data)





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
project_pk = 'project_pk_example' # str | 
cloud_pk = 'cloud_pk_example' # str | 
check_plan_pk = 'check_plan_pk_example' # str | 
id = 'id_example' # str | 
data = bimdata_api_client.Ruleset() # Ruleset | 

try:
    api_response = api_instance.update_ruleset(project_pk, cloud_pk, check_plan_pk, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckplanApi->update_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_pk** | **str**|  | 
 **cloud_pk** | **str**|  | 
 **check_plan_pk** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**Ruleset**](Ruleset.md)|  | 

### Return type

[**Ruleset**](Ruleset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

