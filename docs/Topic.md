# Topic


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**modified_date** | **datetime, none_type** |  | [readonly] 
**guid** | **str** |  | [optional] 
**topic_type** | **str, none_type** |  | [optional] 
**topic_status** | **str, none_type** |  | [optional] 
**priority** | **str, none_type** |  | [optional] 
**labels** | **[str, none_type]** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**creation_author** | **str, none_type** |  | [optional] 
**modified_author** | **str, none_type** |  | [optional] 
**assigned_to** | **str, none_type** |  | [optional] 
**reference_links** | **[str], none_type** |  | [optional] 
**stage** | **str, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**due_date** | **datetime, none_type** |  | [optional] 
**ifcs** | **[int]** | DEPRECATED: Use &#39;models&#39; instead | [optional] 
**models** | **[int]** |  | [optional] 
**format** | **str** |          The BCF data structure may be used for other purposes than BCF Topics. (Storing coordinates, a viewpoint, a list of objecs, etc)         The default value is \&quot;standard\&quot;.         If you want to use the BCF routes to store custom data not related to a BCF Topic, you must set this value to something else.         You must add a query string filter if you want to fetch topics with a non \&quot;standard\&quot; format.          | [optional] 
**index** | **int, none_type** |  | [optional] 
**bimdata_viewer_layout** | **bool, date, datetime, dict, float, int, list, str, none_type** | Non standard field. JSON describing bimdataViewerLayout. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


