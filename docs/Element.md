# Element

Default behavior: - retrieve kwargs in the route (cloud_pk, project_pk, etc) - trim the _pk (cloud_pk => cloud) - check if the object has a foreign key with the name - if so, set the foreign key to the value in the route Override: If the serializer has a method \"get_parents\", we call it and set the parents The method \"get_parents\" should return an iterable of tuples : (parent_field_name, parent_object)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**uuid** | **str** |  | [optional] 
**type** | **str** | IFC type for the element | 
**attributes** | [**PropertySet**](PropertySet.md) |  | [optional] 
**property_sets** | [**list[PropertySet]**](PropertySet.md) |  | [optional] 
**classifications** | [**list[Classification]**](Classification.md) |  | [optional] 
**material_list** | [**list[MaterialListComponent]**](MaterialListComponent.md) |  | [optional] [readonly] 
**layers** | [**list[LayerElement]**](LayerElement.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


