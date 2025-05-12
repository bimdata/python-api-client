# ModelDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Shown name of the file | 
**file** | **str** |  | 
**size** | **int, none_type** | Size of the file. | [readonly] 
**created_at** | **datetime** | Creation date | [readonly] 
**updated_at** | **datetime** | Date of the last update | [readonly] 
**head_id** | **int, none_type** | Document id of head version | [readonly] 
**is_head_version** | **bool** | Document is a head of version or is owned by another document | [readonly] 
**history_count** | **int, none_type** | Number of previous versions | [readonly] 
**user_permission** | **int** | Aggregate of group user permissions and folder default permission | [readonly] 
**office_preview** | **str, none_type** | Office files will be converted as pdf to provide a web preview. Supported extensions are .ppt, .pptx, .odp, .xls, .xlsx, .ods, .doc, .docx, .odt | [readonly] 
**file_name** | **str** | Full name of the file | [optional] 
**parent_id** | **int, none_type** |  | [optional] 
**description** | **str, none_type** | Description of the file | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


