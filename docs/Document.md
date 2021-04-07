# Document

Default behavior: - retrieve kwargs in the route (cloud_pk, project_pk, etc) - trim the _pk (cloud_pk => cloud) - check if the object has a foreign key with the name - if so, set the foreign key to the value in the route Override: If the serializer has a method \"get_parents\", we call it and set the parents The method \"get_parents\" should return an iterable of tuples : (parent_field_name, parent_object)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**parent** | **int** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**creator** | **int** |  | [optional] 
**project** | **int** |  | [optional] [readonly] 
**name** | **str** | Shown name of the file | 
**file_name** | **str** | Full name of the file | [optional] 
**description** | **str** | Description of the file | [optional] 
**file** | **str** |  | [optional] [readonly] 
**size** | **int** | Size of the file. | [optional] 
**created_at** | **datetime** | Creation date | [optional] [readonly] 
**updated_at** | **datetime** | Date of the last update | [optional] [readonly] 
**ifc_source** | **str** | Define the ifc.source field if the upload is an IFC | [optional] 
**ifc_id** | **str** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


