# Topic

Default behavior: - retrieve kwargs in the route (cloud_pk, project_pk, etc) - trim the _pk (cloud_pk => cloud) - check if the object has a foreign key with the name - if so, set the foreign key to the value in the route Override: If the serializer has a method \"get_parents\", we call it and set the parents The method \"get_parents\" should return an iterable of tuples : (parent_field_name, parent_object)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional] 
**topic_type** | **str** |  | [optional] 
**topic_status** | **str** |  | [optional] 
**title** | **str** |  | 
**priority** | **str** |  | [optional] 
**labels** | **list[str]** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**creation_author** | **str** |  | [optional] 
**modified_date** | **datetime** |  | [optional] [readonly] 
**modified_author** | **str** |  | [optional] 
**assigned_to** | **str** |  | [optional] 
**reference_links** | **list[str]** |  | [optional] 
**stage** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**ifcs** | **list[int]** |  | [optional] 
**format** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**project** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


