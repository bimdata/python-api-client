# coding: utf-8

"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@bimdata.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from bimdata_api_client.api_client import ApiClient


class ApplicationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_web_hook(self, cloud_pk, web_hook, **kwargs):  # noqa: E501
        """Create a new Webhook  # noqa: E501

        Create a new Webhook Required scopes: webhook:manage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_web_hook(cloud_pk, web_hook, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_pk: (required)
        :param WebHook web_hook: (required)
        :return: WebHook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_web_hook_with_http_info(cloud_pk, web_hook, **kwargs)  # noqa: E501
        else:
            (data) = self.create_web_hook_with_http_info(cloud_pk, web_hook, **kwargs)  # noqa: E501
            return data

    def create_web_hook_with_http_info(self, cloud_pk, web_hook, **kwargs):  # noqa: E501
        """Create a new Webhook  # noqa: E501

        Create a new Webhook Required scopes: webhook:manage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_web_hook_with_http_info(cloud_pk, web_hook, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_pk: (required)
        :param WebHook web_hook: (required)
        :return: WebHook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['cloud_pk', 'web_hook']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_web_hook" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cloud_pk' is set
        if ('cloud_pk' not in local_var_params or
                local_var_params['cloud_pk'] is None):
            raise ValueError("Missing the required parameter `cloud_pk` when calling `create_web_hook`")  # noqa: E501
        # verify the required parameter 'web_hook' is set
        if ('web_hook' not in local_var_params or
                local_var_params['web_hook'] is None):
            raise ValueError("Missing the required parameter `web_hook` when calling `create_web_hook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_pk' in local_var_params:
            path_params['cloud_pk'] = local_var_params['cloud_pk']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'web_hook' in local_var_params:
            body_params = local_var_params['web_hook']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{cloud_pk}/webhook', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebHook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_web_hook(self, cloud_pk, id, **kwargs):  # noqa: E501
        """Delete a webhook  # noqa: E501

        Delete a webhook Required scopes: webhook:manage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_web_hook(cloud_pk, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_pk: (required)
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_web_hook_with_http_info(cloud_pk, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_web_hook_with_http_info(cloud_pk, id, **kwargs)  # noqa: E501
            return data

    def delete_web_hook_with_http_info(self, cloud_pk, id, **kwargs):  # noqa: E501
        """Delete a webhook  # noqa: E501

        Delete a webhook Required scopes: webhook:manage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_web_hook_with_http_info(cloud_pk, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_pk: (required)
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['cloud_pk', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_web_hook" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cloud_pk' is set
        if ('cloud_pk' not in local_var_params or
                local_var_params['cloud_pk'] is None):
            raise ValueError("Missing the required parameter `cloud_pk` when calling `delete_web_hook`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_web_hook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_pk' in local_var_params:
            path_params['cloud_pk'] = local_var_params['cloud_pk']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{cloud_pk}/webhook/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def full_update_web_hook(self, cloud_pk, id, web_hook, **kwargs):  # noqa: E501
        """Update all field of a webhook  # noqa: E501

        Update all field of a webhook Required scopes: webhook:manage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.full_update_web_hook(cloud_pk, id, web_hook, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_pk: (required)
        :param str id: (required)
        :param WebHook web_hook: (required)
        :return: WebHook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.full_update_web_hook_with_http_info(cloud_pk, id, web_hook, **kwargs)  # noqa: E501
        else:
            (data) = self.full_update_web_hook_with_http_info(cloud_pk, id, web_hook, **kwargs)  # noqa: E501
            return data

    def full_update_web_hook_with_http_info(self, cloud_pk, id, web_hook, **kwargs):  # noqa: E501
        """Update all field of a webhook  # noqa: E501

        Update all field of a webhook Required scopes: webhook:manage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.full_update_web_hook_with_http_info(cloud_pk, id, web_hook, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_pk: (required)
        :param str id: (required)
        :param WebHook web_hook: (required)
        :return: WebHook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['cloud_pk', 'id', 'web_hook']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method full_update_web_hook" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cloud_pk' is set
        if ('cloud_pk' not in local_var_params or
                local_var_params['cloud_pk'] is None):
            raise ValueError("Missing the required parameter `cloud_pk` when calling `full_update_web_hook`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `full_update_web_hook`")  # noqa: E501
        # verify the required parameter 'web_hook' is set
        if ('web_hook' not in local_var_params or
                local_var_params['web_hook'] is None):
            raise ValueError("Missing the required parameter `web_hook` when calling `full_update_web_hook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_pk' in local_var_params:
            path_params['cloud_pk'] = local_var_params['cloud_pk']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'web_hook' in local_var_params:
            body_params = local_var_params['web_hook']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{cloud_pk}/webhook/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebHook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_web_hook(self, cloud_pk, id, **kwargs):  # noqa: E501
        """Retrieve one configured webhook  # noqa: E501

        Retrieve one configured webhook Required scopes: webhook:manage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_web_hook(cloud_pk, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_pk: (required)
        :param str id: (required)
        :return: WebHook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_web_hook_with_http_info(cloud_pk, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_web_hook_with_http_info(cloud_pk, id, **kwargs)  # noqa: E501
            return data

    def get_web_hook_with_http_info(self, cloud_pk, id, **kwargs):  # noqa: E501
        """Retrieve one configured webhook  # noqa: E501

        Retrieve one configured webhook Required scopes: webhook:manage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_web_hook_with_http_info(cloud_pk, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_pk: (required)
        :param str id: (required)
        :return: WebHook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['cloud_pk', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_web_hook" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cloud_pk' is set
        if ('cloud_pk' not in local_var_params or
                local_var_params['cloud_pk'] is None):
            raise ValueError("Missing the required parameter `cloud_pk` when calling `get_web_hook`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_web_hook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_pk' in local_var_params:
            path_params['cloud_pk'] = local_var_params['cloud_pk']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{cloud_pk}/webhook/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebHook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_web_hooks(self, cloud_pk, **kwargs):  # noqa: E501
        """Retrieve all configured webhooks  # noqa: E501

        Retrieve all configured webhooks Required scopes: webhook:manage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_web_hooks(cloud_pk, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_pk: (required)
        :return: list[WebHook]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_web_hooks_with_http_info(cloud_pk, **kwargs)  # noqa: E501
        else:
            (data) = self.get_web_hooks_with_http_info(cloud_pk, **kwargs)  # noqa: E501
            return data

    def get_web_hooks_with_http_info(self, cloud_pk, **kwargs):  # noqa: E501
        """Retrieve all configured webhooks  # noqa: E501

        Retrieve all configured webhooks Required scopes: webhook:manage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_web_hooks_with_http_info(cloud_pk, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_pk: (required)
        :return: list[WebHook]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['cloud_pk']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_web_hooks" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cloud_pk' is set
        if ('cloud_pk' not in local_var_params or
                local_var_params['cloud_pk'] is None):
            raise ValueError("Missing the required parameter `cloud_pk` when calling `get_web_hooks`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_pk' in local_var_params:
            path_params['cloud_pk'] = local_var_params['cloud_pk']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{cloud_pk}/webhook', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[WebHook]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ping_web_hook(self, cloud_pk, id, web_hook, **kwargs):  # noqa: E501
        """Test a webhook  # noqa: E501

        Trigger a Ping Event sending {\"ok\": true} to the webhook URL. Useful to test your app Required scopes: webhook:manage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ping_web_hook(cloud_pk, id, web_hook, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_pk: (required)
        :param str id: (required)
        :param WebHook web_hook: (required)
        :return: WebHook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ping_web_hook_with_http_info(cloud_pk, id, web_hook, **kwargs)  # noqa: E501
        else:
            (data) = self.ping_web_hook_with_http_info(cloud_pk, id, web_hook, **kwargs)  # noqa: E501
            return data

    def ping_web_hook_with_http_info(self, cloud_pk, id, web_hook, **kwargs):  # noqa: E501
        """Test a webhook  # noqa: E501

        Trigger a Ping Event sending {\"ok\": true} to the webhook URL. Useful to test your app Required scopes: webhook:manage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ping_web_hook_with_http_info(cloud_pk, id, web_hook, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_pk: (required)
        :param str id: (required)
        :param WebHook web_hook: (required)
        :return: WebHook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['cloud_pk', 'id', 'web_hook']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ping_web_hook" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cloud_pk' is set
        if ('cloud_pk' not in local_var_params or
                local_var_params['cloud_pk'] is None):
            raise ValueError("Missing the required parameter `cloud_pk` when calling `ping_web_hook`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `ping_web_hook`")  # noqa: E501
        # verify the required parameter 'web_hook' is set
        if ('web_hook' not in local_var_params or
                local_var_params['web_hook'] is None):
            raise ValueError("Missing the required parameter `web_hook` when calling `ping_web_hook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_pk' in local_var_params:
            path_params['cloud_pk'] = local_var_params['cloud_pk']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'web_hook' in local_var_params:
            body_params = local_var_params['web_hook']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{cloud_pk}/webhook/{id}/ping', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebHook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_web_hook(self, cloud_pk, id, web_hook, **kwargs):  # noqa: E501
        """Update some field of a webhook  # noqa: E501

        Update some field of a webhook Required scopes: webhook:manage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_web_hook(cloud_pk, id, web_hook, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_pk: (required)
        :param str id: (required)
        :param WebHook web_hook: (required)
        :return: WebHook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_web_hook_with_http_info(cloud_pk, id, web_hook, **kwargs)  # noqa: E501
        else:
            (data) = self.update_web_hook_with_http_info(cloud_pk, id, web_hook, **kwargs)  # noqa: E501
            return data

    def update_web_hook_with_http_info(self, cloud_pk, id, web_hook, **kwargs):  # noqa: E501
        """Update some field of a webhook  # noqa: E501

        Update some field of a webhook Required scopes: webhook:manage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_web_hook_with_http_info(cloud_pk, id, web_hook, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_pk: (required)
        :param str id: (required)
        :param WebHook web_hook: (required)
        :return: WebHook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['cloud_pk', 'id', 'web_hook']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_web_hook" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cloud_pk' is set
        if ('cloud_pk' not in local_var_params or
                local_var_params['cloud_pk'] is None):
            raise ValueError("Missing the required parameter `cloud_pk` when calling `update_web_hook`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_web_hook`")  # noqa: E501
        # verify the required parameter 'web_hook' is set
        if ('web_hook' not in local_var_params or
                local_var_params['web_hook'] is None):
            raise ValueError("Missing the required parameter `web_hook` when calling `update_web_hook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_pk' in local_var_params:
            path_params['cloud_pk'] = local_var_params['cloud_pk']  # noqa: E501
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'web_hook' in local_var_params:
            body_params = local_var_params['web_hook']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/cloud/{cloud_pk}/webhook/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebHook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
