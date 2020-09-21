# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._subscription_client_enums import *


class CheckResourceNameResult(msrest.serialization.Model):
    """Resource Name valid if not a reserved word, does not contain a reserved word and does not start with a reserved word.

    :param name: Name of Resource.
    :type name: str
    :param type: Type of Resource.
    :type type: str
    :param status: Is the resource name Allowed or Reserved. Possible values include: "Allowed",
     "Reserved".
    :type status: str or ~azure.mgmt.resource.subscriptions.v2018_06_01.models.ResourceNameStatus
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        type: Optional[str] = None,
        status: Optional[Union[str, "ResourceNameStatus"]] = None,
        **kwargs
    ):
        super(CheckResourceNameResult, self).__init__(**kwargs)
        self.name = name
        self.type = type
        self.status = status


class ErrorDefinition(msrest.serialization.Model):
    """Error description and code explaining why resource name is invalid.

    :param message: Description of the error.
    :type message: str
    :param code: Code of the error.
    :type code: str
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        message: Optional[str] = None,
        code: Optional[str] = None,
        **kwargs
    ):
        super(ErrorDefinition, self).__init__(**kwargs)
        self.message = message
        self.code = code


class ErrorResponse(msrest.serialization.Model):
    """Error response.

    :param error: The error details.
    :type error: ~azure.mgmt.resource.subscriptions.v2018_06_01.models.ErrorDefinition
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinition'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDefinition"] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class Location(msrest.serialization.Model):
    """Location information.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The fully qualified ID of the location. For example,
     /subscriptions/00000000-0000-0000-0000-000000000000/locations/westus.
    :vartype id: str
    :ivar subscription_id: The subscription ID.
    :vartype subscription_id: str
    :ivar name: The location name.
    :vartype name: str
    :ivar display_name: The display name of the location.
    :vartype display_name: str
    :ivar latitude: The latitude of the location.
    :vartype latitude: str
    :ivar longitude: The longitude of the location.
    :vartype longitude: str
    """

    _validation = {
        'id': {'readonly': True},
        'subscription_id': {'readonly': True},
        'name': {'readonly': True},
        'display_name': {'readonly': True},
        'latitude': {'readonly': True},
        'longitude': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'latitude': {'key': 'latitude', 'type': 'str'},
        'longitude': {'key': 'longitude', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Location, self).__init__(**kwargs)
        self.id = None
        self.subscription_id = None
        self.name = None
        self.display_name = None
        self.latitude = None
        self.longitude = None


class LocationListResult(msrest.serialization.Model):
    """Location list operation response.

    :param value: An array of locations.
    :type value: list[~azure.mgmt.resource.subscriptions.v2018_06_01.models.Location]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Location]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Location"]] = None,
        **kwargs
    ):
        super(LocationListResult, self).__init__(**kwargs)
        self.value = value


class Operation(msrest.serialization.Model):
    """Microsoft.Resources operation.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.resource.subscriptions.v2018_06_01.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["OperationDisplay"] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    :param provider: Service provider: Microsoft.Resources.
    :type provider: str
    :param resource: Resource on which the operation is performed: Profile, endpoint, etc.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    :param description: Description of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationListResult(msrest.serialization.Model):
    """Result of the request to list Microsoft.Resources operations. It contains a list of operations and a URL link to get the next set of results.

    :param value: List of Microsoft.Resources operations.
    :type value: list[~azure.mgmt.resource.subscriptions.v2018_06_01.models.Operation]
    :param next_link: URL to get the next set of operation list results if there are any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Operation"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ResourceName(msrest.serialization.Model):
    """Name and Type of the Resource.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the resource.
    :type name: str
    :param type: Required. The type of the resource.
    :type type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        type: str,
        **kwargs
    ):
        super(ResourceName, self).__init__(**kwargs)
        self.name = name
        self.type = type


class Subscription(msrest.serialization.Model):
    """Subscription information.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The fully qualified ID for the subscription. For example,
     /subscriptions/00000000-0000-0000-0000-000000000000.
    :vartype id: str
    :ivar subscription_id: The subscription ID.
    :vartype subscription_id: str
    :ivar display_name: The subscription display name.
    :vartype display_name: str
    :ivar tenant_id: The subscription tenant ID.
    :vartype tenant_id: str
    :ivar state: The subscription state. Possible values are Enabled, Warned, PastDue, Disabled,
     and Deleted. Possible values include: "Enabled", "Warned", "PastDue", "Disabled", "Deleted".
    :vartype state: str or ~azure.mgmt.resource.subscriptions.v2018_06_01.models.SubscriptionState
    :param subscription_policies: The subscription policies.
    :type subscription_policies:
     ~azure.mgmt.resource.subscriptions.v2018_06_01.models.SubscriptionPolicies
    :param authorization_source: The authorization source of the request. Valid values are one or
     more combinations of Legacy, RoleBased, Bypassed, Direct and Management. For example, 'Legacy,
     RoleBased'.
    :type authorization_source: str
    """

    _validation = {
        'id': {'readonly': True},
        'subscription_id': {'readonly': True},
        'display_name': {'readonly': True},
        'tenant_id': {'readonly': True},
        'state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'subscription_policies': {'key': 'subscriptionPolicies', 'type': 'SubscriptionPolicies'},
        'authorization_source': {'key': 'authorizationSource', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        subscription_policies: Optional["SubscriptionPolicies"] = None,
        authorization_source: Optional[str] = None,
        **kwargs
    ):
        super(Subscription, self).__init__(**kwargs)
        self.id = None
        self.subscription_id = None
        self.display_name = None
        self.tenant_id = None
        self.state = None
        self.subscription_policies = subscription_policies
        self.authorization_source = authorization_source


class SubscriptionListResult(msrest.serialization.Model):
    """Subscription list operation response.

    All required parameters must be populated in order to send to Azure.

    :param value: An array of subscriptions.
    :type value: list[~azure.mgmt.resource.subscriptions.v2018_06_01.models.Subscription]
    :param next_link: Required. The URL to get the next set of results.
    :type next_link: str
    """

    _validation = {
        'next_link': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Subscription]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        next_link: str,
        value: Optional[List["Subscription"]] = None,
        **kwargs
    ):
        super(SubscriptionListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class SubscriptionPolicies(msrest.serialization.Model):
    """Subscription policies.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar location_placement_id: The subscription location placement ID. The ID indicates which
     regions are visible for a subscription. For example, a subscription with a location placement
     Id of Public_2014-09-01 has access to Azure public regions.
    :vartype location_placement_id: str
    :ivar quota_id: The subscription quota ID.
    :vartype quota_id: str
    :ivar spending_limit: The subscription spending limit. Possible values include: "On", "Off",
     "CurrentPeriodOff".
    :vartype spending_limit: str or
     ~azure.mgmt.resource.subscriptions.v2018_06_01.models.SpendingLimit
    """

    _validation = {
        'location_placement_id': {'readonly': True},
        'quota_id': {'readonly': True},
        'spending_limit': {'readonly': True},
    }

    _attribute_map = {
        'location_placement_id': {'key': 'locationPlacementId', 'type': 'str'},
        'quota_id': {'key': 'quotaId', 'type': 'str'},
        'spending_limit': {'key': 'spendingLimit', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SubscriptionPolicies, self).__init__(**kwargs)
        self.location_placement_id = None
        self.quota_id = None
        self.spending_limit = None


class TenantIdDescription(msrest.serialization.Model):
    """Tenant Id information.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The fully qualified ID of the tenant. For example,
     /tenants/00000000-0000-0000-0000-000000000000.
    :vartype id: str
    :ivar tenant_id: The tenant ID. For example, 00000000-0000-0000-0000-000000000000.
    :vartype tenant_id: str
    :ivar country: Country/region name of the address for the tenant.
    :vartype country: str
    :ivar country_code: Country/region abbreviation for the tenant.
    :vartype country_code: str
    :ivar display_name: The display name of the tenant.
    :vartype display_name: str
    :ivar domains: The list of domains for the tenant.
    :vartype domains: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'tenant_id': {'readonly': True},
        'country': {'readonly': True},
        'country_code': {'readonly': True},
        'display_name': {'readonly': True},
        'domains': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'country': {'key': 'country', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'domains': {'key': 'domains', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TenantIdDescription, self).__init__(**kwargs)
        self.id = None
        self.tenant_id = None
        self.country = None
        self.country_code = None
        self.display_name = None
        self.domains = None


class TenantListResult(msrest.serialization.Model):
    """Tenant Ids information.

    All required parameters must be populated in order to send to Azure.

    :param value: An array of tenants.
    :type value: list[~azure.mgmt.resource.subscriptions.v2018_06_01.models.TenantIdDescription]
    :param next_link: Required. The URL to use for getting the next set of results.
    :type next_link: str
    """

    _validation = {
        'next_link': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[TenantIdDescription]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        next_link: str,
        value: Optional[List["TenantIdDescription"]] = None,
        **kwargs
    ):
        super(TenantListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link
