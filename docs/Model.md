# Model


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**type** | **str** | * &#x60;IFC&#x60; - IFC * &#x60;DWG&#x60; - DWG * &#x60;DXF&#x60; - DXF * &#x60;GLTF&#x60; - GLTF * &#x60;PDF&#x60; - PDF * &#x60;JPEG&#x60; - JPEG * &#x60;PNG&#x60; - PNG * &#x60;OBJ&#x60; - OBJ * &#x60;POINT_CLOUD&#x60; - POINT_CLOUD * &#x60;METABUILDING&#x60; - METABUILDING * &#x60;PHOTOSPHERE&#x60; - PHOTOSPHERE * &#x60;PHOTOSPHERE_BUILDING&#x60; - PHOTOSPHERE_BUILDING | [readonly] 
**creator** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [readonly] 
**status** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**document_id** | **int, none_type** |  | [readonly] 
**document** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [readonly] 
**structure_file** | **str, none_type** |  | [readonly] 
**systems_file** | **str, none_type** |  | [readonly] 
**map_file** | **str, none_type** |  | [readonly] 
**gltf_file** | **str, none_type** |  | [readonly] 
**preview_file** | **str, none_type** |  | [readonly] 
**viewer_360_file** | **str, none_type** | DEPRECATED: Use &#39;preview_file&#39; instead. | [readonly] 
**xkt_file** | **str, none_type** | DEPRECATED: Use &#39;xkt_files&#39; instead. This field only respond with xkt v6 files | [readonly] 
**xkt_files** | [**[XktFile]**](XktFile.md) |  | [readonly] 
**binary_2d_file** | **str, none_type** |  | [readonly] 
**project_id** | **int, none_type** |  | [readonly] 
**errors** | **[str], none_type** | List of errors that happened during IFC processing | [readonly] 
**warnings** | **[str], none_type** | List of warnings that happened during IFC processing | [readonly] 
**parent_id** | **int, none_type** | The first page of the pdf | [readonly] 
**page_number** | **int, none_type** | The page number of the related pdf | [readonly] 
**mask_2d** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [readonly] 
**children** | [**[ModelSerializerWithoutChildren]**](ModelSerializerWithoutChildren.md) | Contains additional pages of a pdf | [readonly] 
**name** | **str, none_type** |  | [optional] 
**source** | **str** | * &#x60;UPLOAD&#x60; - UPLOAD * &#x60;SPLIT&#x60; - SPLIT * &#x60;MERGE&#x60; - MERGE * &#x60;EXPORT&#x60; - EXPORT * &#x60;OPTIMIZED&#x60; - OPTIMIZED | [optional] 
**world_position** | **[float], none_type** | [x,y,z] array of the position of the local_placement in world coordinates | [optional] 
**size_ratio** | **float, none_type** | How many meters a unit represents | [optional] 
**archived** | **bool** |  | [optional] 
**version** | **str, none_type** | This field is only for information. Updating it won&#39;t impact the export. | [optional] 
**north_vector** | **[[float]], none_type** | This field is only for information. Updating it won&#39;t impact the export. | [optional] 
**recommanded_2d_angle** | **float, none_type** | This is the angle in clockwise degree to apply on the 2D to optimise the horizontality of objects. This field is only for information. Updating it won&#39;t impact the export. | [optional] 
**layout_name** | **str, none_type** | The name of the DWG layout (only set when type&#x3D;&#x3D;DWG) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


