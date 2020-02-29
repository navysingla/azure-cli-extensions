# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6219, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from msrest.service_client import ServiceClient
from msrest import Deserializer, Serializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations import SubscriptionOperations
from .operations import SubscriptionOperationOperations
from .operations import Operations
from . import models

class SubscriptionClientConfiguration(AzureConfiguration):
    """Configuration for SubscriptionClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(SubscriptionClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-subscription/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials

class SubscriptionClient(object):
    """The subscription client

    :ivar subscription: SubscriptionOperations operations
    :vartype subscription: subscription_client.operations.SubscriptionOperations
    :ivar subscription_operation: SubscriptionOperationOperations operations
    :vartype subscription_operation: subscription_client.operations.SubscriptionOperationOperations
    :ivar operations: Operations operations
    :vartype operations: subscription_client.operations.Operations
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = SubscriptionClientConfiguration(credentials, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.subscription_operations = SubscriptionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.subscription_factory = SubscriptionFactoryOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.subscriptions = SubscriptionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.tenants = TenantsOperations(
            self._client, self.config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> SubscriptionClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
