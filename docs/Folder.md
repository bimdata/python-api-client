# Folder

Folder with recursive children field, useful for openapi generator
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**parent_id** | **int** |  | [optional] 
**type** | **str** | Value is \&quot;Folder\&quot;. It is usefull to parse the tree and discriminate folders and files | [optional] [readonly] 
**name** | **str** | Name of the folder | 
**created_at** | **datetime** | Creation date | [optional] [readonly] 
**updated_at** | **datetime** | Date of the last update | [optional] [readonly] 
**created_by** | [**User**](User.md) |  | [optional] 
**children** | [**list[RecursiveFolderChildren]**](RecursiveFolderChildren.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


