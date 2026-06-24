# FolderNamingConstraint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**applied_on_folder_id** | **int** | The folder owning the constraint. May be a parent folder of the current folder if the constraint is recursive. | [readonly] 
**constraint** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [readonly] 
**recursive** | **bool** |  | 
**conflicting_documents** | [**[LightDocument]**](LightDocument.md) |  | [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


