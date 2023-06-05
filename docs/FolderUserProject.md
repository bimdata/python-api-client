# FolderUserProject

This is a flattened nested represetation of FosUser and Invitation models in this serializer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**user_id** | **int, none_type** |  | [readonly] 
**invitation_id** | **int, none_type** |  | [readonly] 
**email** | **str** |  | [readonly] 
**firstname** | **str, none_type** |  | [readonly] 
**lastname** | **str, none_type** |  | [readonly] 
**profile_picture** | **str, none_type** |  | [readonly] 
**sub** | **str, none_type** |  | [readonly] 
**role** | **int** | * &#x60;100&#x60; - admin * &#x60;50&#x60; - user * &#x60;25&#x60; - guest | [readonly] 
**permission** | **int** | * &#x60;1&#x60; - denied * &#x60;50&#x60; - read_only * &#x60;100&#x60; - read_write | [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


