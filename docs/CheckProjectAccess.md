# CheckProjectAccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_read_permission** | **bool** |  | 
**has_write_permission** | **bool** |  | 
**has_admin_permission** | **bool** |  | 
**token_scopes** | **[str]** |  | 
**usable_scopes** | **[str]** | Some tokens may have write scopes (eg: model:write) but the user of the token is a guest in the project so they can&#39;t use the scopes. | 
**user_role** | **int** | * &#x60;100&#x60; - admin * &#x60;50&#x60; - user * &#x60;25&#x60; - guest | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


