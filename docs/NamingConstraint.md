# NamingConstraint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Name of the naming constraint | 
**rule** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**strict** | **bool** |  When the constraint is strict, documents upload with invalid name and move in a conflict folder will be blocked. If the constraint is non scrict, documents will be flagged on field &#x60;naming_constraint_conflict&#x60;  | 
**conflicting_documents** | [**[LightDocument]**](LightDocument.md) |  | [readonly] 
**creator** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


