# Viewpoint

Default behavior: - retrieve kwargs in the route (cloud_pk, project_pk, etc) - trim the _pk (cloud_pk => cloud) - check if the object has a foreign key with the name - if so, set the foreign key to the value in the route Override: If the serializer has a method \"get_parents\", we call it and set the parents The method \"get_parents\" should return an iterable of tuples : (parent_field_name, parent_object)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**guid** | **str** |  | [optional] 
**orthogonal_camera** | [**OrthogonalCamera**](OrthogonalCamera.md) |  | [optional] 
**perspective_camera** | [**PerspectiveCamera**](PerspectiveCamera.md) |  | [optional] 
**lines** | [**list[Line]**](Line.md) |  | [optional] 
**clipping_planes** | [**list[ClippingPlane]**](ClippingPlane.md) |  | [optional] 
**snapshot** | [**Snapshot**](Snapshot.md) |  | [optional] 
**components** | [**ComponentsParent**](ComponentsParent.md) |  | [optional] 
**temp_id** | **int** | Only used when using POST on the full-topic route to bind viewpoint with comment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


