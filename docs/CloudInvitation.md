# CloudInvitation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**email** | **str** | email of the user to invite | 
**redirect_uri** | **str** | User will be redirected to this uri when they accept the invitation | 
**role** | **int** | * &#x60;100&#x60; - admin * &#x60;50&#x60; - user | [optional]  if omitted the server will use the default value of 100
**project_role** | **int** | * &#x60;100&#x60; - admin * &#x60;50&#x60; - user * &#x60;25&#x60; - guest | [optional] 
**in_all_projects** | **bool** | When inviting non-admin cloud user, specify if the user will be invited in all existing projects. project_role needs to be specified. | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


