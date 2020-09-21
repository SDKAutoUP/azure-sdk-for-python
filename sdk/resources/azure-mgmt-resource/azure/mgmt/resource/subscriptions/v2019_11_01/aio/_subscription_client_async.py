# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration_async import SubscriptionClientConfiguration
from .operations_async import Operations
from .operations_async import SubscriptionsOperations
from .operations_async import TenantsOperations
from .operations_async import SubscriptionClientOperationsMixin
from .. import models


class SubscriptionClient(SubscriptionClientOperationsMixin):
    """All resource groups and resources exist within subscriptions. These operation enable you get information about your subscriptions and tenants. A tenant is a dedicated instance of Azure Active Directory (Azure AD) for your organization.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.resource.subscriptions.v2019_11_01.aio.operations_async.Operations
    :ivar subscriptions: SubscriptionsOperations operations
    :vartype subscriptions: azure.mgmt.resource.subscriptions.v2019_11_01.aio.operations_async.SubscriptionsOperations
    :ivar tenants: TenantsOperations operations
    :vartype tenants: azure.mgmt.resource.subscriptions.v2019_11_01.aio.operations_async.TenantsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = SubscriptionClientConfiguration(credential, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subscriptions = SubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tenants = TenantsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "SubscriptionClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
