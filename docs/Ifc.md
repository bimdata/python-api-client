# Ifc

Default behavior: - retrieve kwargs in the route (cloud_pk, project_pk, etc) - trim the _pk (cloud_pk => cloud) - check if the object has a foreign key with the name - if so, set the foreign key to the value in the route Override: If the serializer has a method \"get_parents\", we call it and set the parents The method \"get_parents\" should return an iterable of tuples : (parent_field_name, parent_object)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**creator** | [**User**](User.md) |  | [optional] 
**status** | **str** |  | [optional] [readonly] 
**source** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**document_id** | **str** |  | [optional] [readonly] 
**document** | [**Document**](Document.md) |  | [optional] 
**structure_file** | **str** |  | [optional] [readonly] 
**systems_file** | **str** |  | [optional] [readonly] 
**map_file** | **str** |  | [optional] [readonly] 
**gltf_file** | **str** |  | [optional] [readonly] 
**bvh_tree_file** | **str** |  | [optional] [readonly] 
**viewer_360_file** | **str** |  | [optional] [readonly] 
**xkt_file** | **str** |  | [optional] [readonly] 
**project_id** | **str** |  | [optional] [readonly] 
**world_position** | **list[float]** |  | [optional] 
**errors** | **list[str]** |  | [optional] [readonly] 
**warnings** | **list[str]** |  | [optional] [readonly] 
**archived** | **bool** |  | [optional] 
**version** | **str** | This field is only for information. Updating it won&#39;t impact the export. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


