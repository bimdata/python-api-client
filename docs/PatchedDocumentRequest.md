# PatchedDocumentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **int, none_type** |  | [optional] 
**name** | **str** | Shown name of the file | [optional] 
**file_name** | **str** | Full name of the file | [optional] 
**description** | **str, none_type** | Description of the file | [optional] 
**file** | **file_type** |  | [optional] 
**model_source** | **str** | Define the model.source field if the upload is a Model (IFC, PDF, DWG...)  * &#x60;UPLOAD&#x60; - UPLOAD * &#x60;SPLIT&#x60; - SPLIT * &#x60;MERGE&#x60; - MERGE * &#x60;EXPORT&#x60; - EXPORT * &#x60;OPTIMIZED&#x60; - OPTIMIZED | [optional] 
**ifc_source** | **str** | DEPRECATED: Use &#39;model_source&#39; instead. Define the model.source field if the upload is a Model (IFC, PDF, DWG...)  * &#x60;UPLOAD&#x60; - UPLOAD * &#x60;SPLIT&#x60; - SPLIT * &#x60;MERGE&#x60; - MERGE * &#x60;EXPORT&#x60; - EXPORT * &#x60;OPTIMIZED&#x60; - OPTIMIZED | [optional] 
**successor_of** | **int** | Old document version to replace. Only for create | [optional] 
**process_hint** | **str** | Provide a info about the document in order to customize the way it is processed.  * &#x60;PHOTOSPHERE&#x60; - PHOTOSPHERE | [optional]  if omitted the server will use the default value of "PHOTOSPHERE"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


