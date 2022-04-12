# IfcExportRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | The name of the exported IFC file. It MUST end with .ifc or the exported file won&#39;t be processed by BIMData | 
**classifications** | **bool, date, datetime, dict, float, int, list, str, none_type** | Exported IFC will include classifications from original IFC file (ORIGINAL), from latest API updates (UPDATED), or won&#39;t include classifications(NONE) | [optional] 
**zones** | **bool, date, datetime, dict, float, int, list, str, none_type** | Exported IFC will include zones from original IFC file (ORIGINAL), from latest API updates (UPDATED), or won&#39;t include zones(NONE) | [optional] 
**properties** | **bool, date, datetime, dict, float, int, list, str, none_type** | Exported IFC will include properties from original IFC file (ORIGINAL), from latest API updates (UPDATED), or won&#39;t include properties(NONE) | [optional] 
**systems** | **bool, date, datetime, dict, float, int, list, str, none_type** | Exported IFC will include systems from original IFC file (ORIGINAL), from latest API updates (UPDATED), or won&#39;t include systems(NONE) | [optional] 
**layers** | **bool, date, datetime, dict, float, int, list, str, none_type** | Exported IFC will include layers from original IFC file (ORIGINAL), from latest API updates (UPDATED), or won&#39;t include layers(NONE) | [optional] 
**materials** | **bool, date, datetime, dict, float, int, list, str, none_type** | Exported IFC will include materials from original IFC file (ORIGINAL), from latest API updates (UPDATED), or won&#39;t include materials(NONE) | [optional] 
**attributes** | **bool, date, datetime, dict, float, int, list, str, none_type** | Exported IFC will include attributes from original IFC file (ORIGINAL), from latest API updates (UPDATED), or won&#39;t include attributes(NONE) | [optional] 
**structure** | **bool, date, datetime, dict, float, int, list, str, none_type** | Exported IFC will include the structure from original IFC file (ORIGINAL), from latest API updates (UPDATED), or won&#39;t include structure(NONE) | [optional] 
**uuids** | **[str]** | Exported IFC will only have those elements. If omitted, all elements will be exported | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


