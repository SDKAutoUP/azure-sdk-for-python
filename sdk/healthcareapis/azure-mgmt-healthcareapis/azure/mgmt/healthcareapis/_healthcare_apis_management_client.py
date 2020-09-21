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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import HealthcareApisManagementClientConfiguration
from .operations import ServicesOperations
from .operations import Operations
from .operations import OperationResultsOperations
from . import models


class HealthcareApisManagementClient(SDKClient):
    """Azure Healthcare APIs Client

    :ivar config: Configuration for client.
    :vartype config: HealthcareApisManagementClientConfiguration

    :ivar services: Services operations
    :vartype services: azure.mgmt.healthcareapis.operations.ServicesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.healthcareapis.operations.Operations
    :ivar operation_results: OperationResults operations
    :vartype operation_results: azure.mgmt.healthcareapis.operations.OperationResultsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = HealthcareApisManagementClientConfiguration(credentials, subscription_id, base_url)
        super(HealthcareApisManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2020-03-15'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.services = ServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operation_results = OperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
