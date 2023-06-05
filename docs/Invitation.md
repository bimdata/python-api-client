# Invitation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**client_id** | **int** |  | [readonly] 
**redirect_uri** | **str** | User will be redirected to this uri when they accept the invitation | 
**cloud_name** | **str** |  | 
**cloud_role** | **int** | Role the user will have when they accept the invitation  * &#x60;100&#x60; - admin * &#x60;50&#x60; - user | 
**email** | **str** | email of the user to invite | 
**project_name** | **str** |  | [optional] 
**project_role** | **int, none_type** | Role the user will have when they accept the invitation  * &#x60;100&#x60; - admin * &#x60;50&#x60; - user * &#x60;25&#x60; - guest | [optional] 
**status** | **str** |          A: Accepted         D: Denied         P: Pending           * &#x60;A&#x60; - accepted * &#x60;D&#x60; - denied * &#x60;P&#x60; - pending | [optional] 
**sender_provider_sub** | **str** | OIDC sub of the sender. The original sub from the provider is used instead of the broker sub | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


