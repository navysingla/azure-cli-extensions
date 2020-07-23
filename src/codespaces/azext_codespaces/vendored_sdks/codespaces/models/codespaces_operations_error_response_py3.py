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


class CodespacesOperationsErrorResponse(Model):
    """Error response indicates that the service is not able to process the
    incoming request.

    :param error: The error details.
    :type error: ~microsoft.codespaces.models.ErrorDefinition
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinition'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(CodespacesOperationsErrorResponse, self).__init__(**kwargs)
        self.error = error


class CodespacesOperationsErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'CodespacesOperationsErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(CodespacesOperationsErrorResponseException, self).__init__(deserialize, response, 'CodespacesOperationsErrorResponse', *args)
