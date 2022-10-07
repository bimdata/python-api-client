# UserInvitation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**redirect_uri** | **str** | User will be redirected to this uri when they accept the invitation | 
**cloud_id** | **int** |  | [readonly] 
**cloud_name** | **str** |  | 
**project_id** | **int, none_type** |  | [readonly] 
**sender** | [**User**](User.md) |  | 
**project_name** | **str** |  | [optional] 
**status** | **str** |          A: Accepted         D: Denied         P: Pending          | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


