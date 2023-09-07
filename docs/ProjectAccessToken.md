# ProjectAccessToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [readonly] 
**scopes** | **[str]** |  | 
**expires_at** | **datetime** |  | [optional] 
**email_impersonation** | **str, none_type** |          If the request is made from an SSO application, you can link the token to a user.         All calls made with the token will populate created_by fields with the user.         If the user don&#39;t have access to some data, the token won&#39;t have access.          | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


