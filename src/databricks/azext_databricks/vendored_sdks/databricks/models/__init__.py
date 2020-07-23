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

try:
    from ._models_py3 import AddressSpace
    from ._models_py3 import CreatedBy
    from ._models_py3 import Encryption
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorInfo
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import ManagedIdentityConfiguration
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import Resource
    from ._models_py3 import Sku
    from ._models_py3 import TrackedResource
    from ._models_py3 import VirtualNetworkPeering
    from ._models_py3 import VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetwork
    from ._models_py3 import VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetwork
    from ._models_py3 import Workspace
    from ._models_py3 import WorkspaceCustomBooleanParameter
    from ._models_py3 import WorkspaceCustomObjectParameter
    from ._models_py3 import WorkspaceCustomParameters
    from ._models_py3 import WorkspaceCustomStringParameter
    from ._models_py3 import WorkspaceEncryptionParameter
    from ._models_py3 import WorkspaceProviderAuthorization
    from ._models_py3 import WorkspaceUpdate
except (SyntaxError, ImportError):
    from ._models import AddressSpace
    from ._models import CreatedBy
    from ._models import Encryption
    from ._models import ErrorDetail
    from ._models import ErrorInfo
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import ManagedIdentityConfiguration
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import Resource
    from ._models import Sku
    from ._models import TrackedResource
    from ._models import VirtualNetworkPeering
    from ._models import VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetwork
    from ._models import VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetwork
    from ._models import Workspace
    from ._models import WorkspaceCustomBooleanParameter
    from ._models import WorkspaceCustomObjectParameter
    from ._models import WorkspaceCustomParameters
    from ._models import WorkspaceCustomStringParameter
    from ._models import WorkspaceEncryptionParameter
    from ._models import WorkspaceProviderAuthorization
    from ._models import WorkspaceUpdate
from ._paged_models import OperationPaged
from ._paged_models import VirtualNetworkPeeringPaged
from ._paged_models import WorkspacePaged
from ._databricks_client_enums import (
    CustomParameterType,
    KeySource,
    ProvisioningState,
    PeeringProvisioningState,
    PeeringState,
)

__all__ = [
    'AddressSpace',
    'CreatedBy',
    'Encryption',
    'ErrorDetail',
    'ErrorInfo',
    'ErrorResponse', 'ErrorResponseException',
    'ManagedIdentityConfiguration',
    'Operation',
    'OperationDisplay',
    'Resource',
    'Sku',
    'TrackedResource',
    'VirtualNetworkPeering',
    'VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetwork',
    'VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetwork',
    'Workspace',
    'WorkspaceCustomBooleanParameter',
    'WorkspaceCustomObjectParameter',
    'WorkspaceCustomParameters',
    'WorkspaceCustomStringParameter',
    'WorkspaceEncryptionParameter',
    'WorkspaceProviderAuthorization',
    'WorkspaceUpdate',
    'WorkspacePaged',
    'VirtualNetworkPeeringPaged',
    'OperationPaged',
    'CustomParameterType',
    'KeySource',
    'ProvisioningState',
    'PeeringProvisioningState',
    'PeeringState',
]
