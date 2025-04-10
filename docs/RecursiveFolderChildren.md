# RecursiveFolderChildren


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**parent_id** | **int, none_type** |  | [readonly] 
**type** | **str** | DEPRECATED: Use &#39;nature&#39; instead. Values can be &#39;Folder&#39;, &#39;Document&#39; or &#39;Ifc&#39;. It is usefull to parse the tree and discriminate folders and files | [readonly] 
**nature** | **str** | Values can be &#39;Folder&#39;, &#39;Document&#39; or &#39;Model&#39;. It is usefull to parse the tree and discriminate folders and files | [readonly] 
**model_type** | **str, none_type** | Model&#39;s type. Values can be IFC, DWG, DXF, GLTF, PDF, JPEG, PNG, OBJ, POINT_CLOUD | [readonly] 
**name** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**model_id** | **int, none_type** |  | [readonly] 
**ifc_id** | **int, none_type** | DEPRECATED: Use &#39;model_id&#39; instead | [readonly] 
**groups_permissions** | **bool, none_type** | DEPRECATED: This field must be present because of legacy constraints but will always be empty. If you want to see group permissions of a folder, see &#x60;getFolder&#x60; | [readonly] 
**default_permission** | **int** | Default permissions of folder | [readonly] 
**user_permission** | **int** | Aggregate of group user permissions and folder default permission | [readonly] 
**history_count** | **int, none_type** | Number of previous versions | [readonly] 
**tags** | [**[Tag], none_type**](Tag.md) | Tags of a document | [readonly] 
**children** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [readonly] 
**created_by** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**file_name** | **str, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**size** | **int, none_type** |  | [optional] 
**file** | **str, none_type** |  | [optional] 
**office_preview** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


