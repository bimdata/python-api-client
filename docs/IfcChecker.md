# IfcChecker

Default behavior: - retrieve kwargs in the route (cloud_pk, project_pk, etc) - trim the _pk (cloud_pk => cloud) - check if the object has a foreign key with the name - if so, set the foreign key to the value in the route Override: If the serializer has a method \"get_parents\", we call it and set the parents The method \"get_parents\" should return an iterable of tuples : (parent_field_name, parent_object)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**ifc** | [**Ifc**](Ifc.md) |  | [optional] 
**creator** | [**User**](User.md) |  | [optional] 
**name** | **str** |  | [optional] 
**checkplan_id** | **int** |  | [optional] 
**results** | [**list[IfcCheckerResults]**](IfcCheckerResults.md) |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**checkplan** | [**IfcCheckerCheckplan**](IfcCheckerCheckplan.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


