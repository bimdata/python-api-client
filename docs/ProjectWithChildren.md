# ProjectWithChildren

Default behavior: - retrieve kwargs in the route (cloud_pk, project_pk, etc) - trim the _pk (cloud_pk => cloud) - check if the object has a foreign key with the name - if so, set the foreign key to the value in the route Override: If the serializer has a method \"get_parents\", we call it and set the parents The method \"get_parents\" should return an iterable of tuples : (parent_field_name, parent_object)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**logo** | **str** |  | [optional] [readonly] 
**name** | **str** | Name of the project | 
**status** | **str** |  | [optional] 
**created_at** | **datetime** | Creation date | [optional] [readonly] 
**updated_at** | **datetime** | Date of the last update | [optional] [readonly] 
**parent_id** | **int** |  | [optional] 
**children** | [**list[ProjectWithChildren]**](ProjectWithChildren.md) |  | [optional] [readonly] 
**root_folder_id** | **str** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


