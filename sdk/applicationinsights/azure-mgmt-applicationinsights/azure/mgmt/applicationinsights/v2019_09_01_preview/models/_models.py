# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class AzureResourceProperties(Model):
    """An Azure resource QueryPack-Query object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar system_data: Read only system data
    :vartype system_data:
     ~azure.mgmt.applicationinsights.v2019_09_01_preview.models.SystemData
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(self, **kwargs):
        super(AzureResourceProperties, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.system_data = None


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ErrorDetail(Model):
    """Error details.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. The error's code.
    :type code: str
    :param message: Required. A human readable error message.
    :type message: str
    :param target: Indicates which property in the request is responsible for
     the error.
    :type target: str
    :param value: Indicates which value in 'target' is responsible for the
     error.
    :type value: str
    :param resources: Indicates resources which were responsible for the
     error.
    :type resources: list[str]
    :param additional_properties: Additional properties that can be provided
     on the error details object
    :type additional_properties: object
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[str]'},
        'additional_properties': {'key': 'additionalProperties', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.target = kwargs.get('target', None)
        self.value = kwargs.get('value', None)
        self.resources = kwargs.get('resources', None)
        self.additional_properties = kwargs.get('additional_properties', None)


class ErrorInfo(Model):
    """The code and message for an error.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. A machine readable error code.
    :type code: str
    :param message: Required. A human readable error message.
    :type message: str
    :param details: error details.
    :type details:
     list[~azure.mgmt.applicationinsights.v2019_09_01_preview.models.ErrorDetail]
    :param innererror: Inner error details if they exist.
    :type innererror:
     ~azure.mgmt.applicationinsights.v2019_09_01_preview.models.ErrorInfo
    :param additional_properties: Additional properties that can be provided
     on the error info object
    :type additional_properties: object
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'innererror': {'key': 'innererror', 'type': 'ErrorInfo'},
        'additional_properties': {'key': 'additionalProperties', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(ErrorInfo, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.details = kwargs.get('details', None)
        self.innererror = kwargs.get('innererror', None)
        self.additional_properties = kwargs.get('additional_properties', None)


class ErrorResponse(Model):
    """Describe the format of an Error response.

    :param error: The error details.
    :type error:
     ~azure.mgmt.applicationinsights.v2019_09_01_preview.models.ErrorInfo
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorInfo'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class QueryPacksResource(Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(QueryPacksResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)


class LogAnalyticsQueryPack(QueryPacksResource):
    """An Log Analytics QueryPack definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar query_pack_id: The unique ID of your application. This field cannot
     be changed.
    :vartype query_pack_id: str
    :ivar time_created: Creation Date for the Log Analytics QueryPack, in ISO
     8601 format.
    :vartype time_created: datetime
    :ivar time_modified: Last modified date of the Log Analytics QueryPack, in
     ISO 8601 format.
    :vartype time_modified: datetime
    :ivar provisioning_state: Current state of this QueryPack: whether or not
     is has been provisioned within the resource group it is defined. Users
     cannot change this value but are able to read from it. Values will include
     Succeeded, Deploying, Canceled, and Failed.
    :vartype provisioning_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'query_pack_id': {'readonly': True},
        'time_created': {'readonly': True},
        'time_modified': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'query_pack_id': {'key': 'properties.queryPackId', 'type': 'str'},
        'time_created': {'key': 'properties.timeCreated', 'type': 'iso-8601'},
        'time_modified': {'key': 'properties.timeModified', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LogAnalyticsQueryPack, self).__init__(**kwargs)
        self.query_pack_id = None
        self.time_created = None
        self.time_modified = None
        self.provisioning_state = None


class LogAnalyticsQueryPackQuery(AzureResourceProperties):
    """A Log Analytics QueryPack-Query definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar system_data: Read only system data
    :vartype system_data:
     ~azure.mgmt.applicationinsights.v2019_09_01_preview.models.SystemData
    :ivar log_analytics_query_pack_query_id: The unique ID of your
     application. This field cannot be changed.
    :vartype log_analytics_query_pack_query_id: str
    :param display_name: Required. Unique display name for your query within
     the Query Pack.
    :type display_name: str
    :ivar time_created: Creation Date for the Log Analytics Query, in ISO 8601
     format.
    :vartype time_created: datetime
    :ivar time_modified: Last modified date of the Log Analytics Query, in ISO
     8601 format.
    :vartype time_modified: datetime
    :ivar author: Object Id of user creating the query.
    :vartype author: str
    :param description: Description of the query.
    :type description: str
    :param body: Required. Body of the query.
    :type body: str
    :param related: The related metadata items for the function.
    :type related:
     ~azure.mgmt.applicationinsights.v2019_09_01_preview.models.LogAnalyticsQueryPackQueryPropertiesRelated
    :param tags: Tags associated with the query.
    :type tags: dict[str, list[str]]
    :param properties: Additional properties that can be set for the query.
    :type properties: object
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
        'log_analytics_query_pack_query_id': {'readonly': True},
        'display_name': {'required': True},
        'time_created': {'readonly': True},
        'time_modified': {'readonly': True},
        'author': {'readonly': True},
        'body': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'log_analytics_query_pack_query_id': {'key': 'properties.id', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'time_created': {'key': 'properties.timeCreated', 'type': 'iso-8601'},
        'time_modified': {'key': 'properties.timeModified', 'type': 'iso-8601'},
        'author': {'key': 'properties.author', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'body': {'key': 'properties.body', 'type': 'str'},
        'related': {'key': 'properties.related', 'type': 'LogAnalyticsQueryPackQueryPropertiesRelated'},
        'tags': {'key': 'properties.tags', 'type': '{[str]}'},
        'properties': {'key': 'properties.properties', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(LogAnalyticsQueryPackQuery, self).__init__(**kwargs)
        self.log_analytics_query_pack_query_id = None
        self.display_name = kwargs.get('display_name', None)
        self.time_created = None
        self.time_modified = None
        self.author = None
        self.description = kwargs.get('description', None)
        self.body = kwargs.get('body', None)
        self.related = kwargs.get('related', None)
        self.tags = kwargs.get('tags', None)
        self.properties = kwargs.get('properties', None)


class LogAnalyticsQueryPackQueryPropertiesRelated(Model):
    """The related metadata items for the function.

    :param categories: The related categories for the function.
    :type categories: list[str]
    :param resource_types: The related resource types for the function.
    :type resource_types: list[str]
    :param solutions: The related Log Analytics solutions for the function.
    :type solutions: list[str]
    """

    _attribute_map = {
        'categories': {'key': 'categories', 'type': '[str]'},
        'resource_types': {'key': 'resourceTypes', 'type': '[str]'},
        'solutions': {'key': 'solutions', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(LogAnalyticsQueryPackQueryPropertiesRelated, self).__init__(**kwargs)
        self.categories = kwargs.get('categories', None)
        self.resource_types = kwargs.get('resource_types', None)
        self.solutions = kwargs.get('solutions', None)


class LogAnalyticsQueryPackQuerySearchProperties(Model):
    """Properties that define an Log Analytics QueryPack-Query search properties.

    :param related: The related metadata items for the function.
    :type related:
     ~azure.mgmt.applicationinsights.v2019_09_01_preview.models.LogAnalyticsQueryPackQuerySearchPropertiesRelated
    :param tags: Tags associated with the query.
    :type tags: dict[str, list[str]]
    """

    _attribute_map = {
        'related': {'key': 'related', 'type': 'LogAnalyticsQueryPackQuerySearchPropertiesRelated'},
        'tags': {'key': 'tags', 'type': '{[str]}'},
    }

    def __init__(self, **kwargs):
        super(LogAnalyticsQueryPackQuerySearchProperties, self).__init__(**kwargs)
        self.related = kwargs.get('related', None)
        self.tags = kwargs.get('tags', None)


class LogAnalyticsQueryPackQuerySearchPropertiesRelated(Model):
    """The related metadata items for the function.

    :param categories: The related categories for the function.
    :type categories: list[str]
    :param resource_types: The related resource types for the function.
    :type resource_types: list[str]
    :param solutions: The related Log Analytics solutions for the function.
    :type solutions: list[str]
    """

    _attribute_map = {
        'categories': {'key': 'categories', 'type': '[str]'},
        'resource_types': {'key': 'resourceTypes', 'type': '[str]'},
        'solutions': {'key': 'solutions', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(LogAnalyticsQueryPackQuerySearchPropertiesRelated, self).__init__(**kwargs)
        self.categories = kwargs.get('categories', None)
        self.resource_types = kwargs.get('resource_types', None)
        self.solutions = kwargs.get('solutions', None)


class Operation(Model):
    """CDN REST API operation.

    :param name: Operation name: {provider}/{resource}/{operation}
    :type name: str
    :param is_data_action: Indicates whether the operation is a data action
    :type is_data_action: bool
    :param display: Display of the operation
    :type display:
     ~azure.mgmt.applicationinsights.v2019_09_01_preview.models.OperationDisplay
    :param origin: Origin of the operation
    :type origin: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.is_data_action = kwargs.get('is_data_action', None)
        self.display = kwargs.get('display', None)
        self.origin = kwargs.get('origin', None)


class OperationDisplay(Model):
    """Operation display payload.

    :param provider: Resource provider of the operation
    :type provider: str
    :param resource: Resource of the operation
    :type resource: str
    :param operation: Localized friendly name for the operation
    :type operation: str
    :param description: Localized friendly description for the operation
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class SystemData(Model):
    """Read only system data.

    :param created_by: An identifier for the identity that created the
     resource
    :type created_by: str
    :param created_by_type: The type of identity that created the resource.
     Possible values include: 'user', 'application', 'managedIdentity', 'key'
    :type created_by_type: str or
     ~azure.mgmt.applicationinsights.v2019_09_01_preview.models.IdentityType
    :param created_at: The timestamp of resource creation (UTC)
    :type created_at: datetime
    :param last_modified_by: An identifier for the identity that last modified
     the resource
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the
     resource. Possible values include: 'user', 'application',
     'managedIdentity', 'key'
    :type last_modified_by_type: str or
     ~azure.mgmt.applicationinsights.v2019_09_01_preview.models.IdentityType
    :param last_modified_at: The timestamp of resource last modification (UTC)
    :type last_modified_at: datetime
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(SystemData, self).__init__(**kwargs)
        self.created_by = kwargs.get('created_by', None)
        self.created_by_type = kwargs.get('created_by_type', None)
        self.created_at = kwargs.get('created_at', None)
        self.last_modified_by = kwargs.get('last_modified_by', None)
        self.last_modified_by_type = kwargs.get('last_modified_by_type', None)
        self.last_modified_at = kwargs.get('last_modified_at', None)


class TagsResource(Model):
    """A container holding only the Tags for a resource, allowing the user to
    update the tags on a QueryPack instance.

    :param tags: Resource tags
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(TagsResource, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
