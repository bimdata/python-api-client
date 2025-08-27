# WriteFolder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **datetime** | Date of the last update | [readonly] 
**groups_permissions** | [**[GroupFolderRead]**](GroupFolderRead.md) | List of group permissions | [readonly] 
**name** | **str** | Name of the folder | 
**id** | **int** |  | [readonly] 
**created_by** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [readonly] 
**user_permission** | **int** | Aggregate of group user permissions and folder default permission | [readonly] 
**nature** | **str** | Value is \&quot;Folder\&quot;. It is usefull to parse the tree and discriminate folders and files | [readonly] 
**created_at** | **datetime** | Creation date | [readonly] 
**type** | **str** | DEPRECATED: Use &#39;nature&#39; instead. Value is \&quot;Folder\&quot;. It is usefull to parse the tree and discriminate folders and files | [readonly] 
**parent_id** | **int, none_type** |  | [optional] 
**default_permission** | **int** | Permission for a Folder  * &#x60;1&#x60; - denied * &#x60;50&#x60; - read_only * &#x60;100&#x60; - read_write | [optional] 
**children** | [**[WriteFolder], none_type**](WriteFolder.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


