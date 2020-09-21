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

from enum import Enum


class Error(str, Enum):

    invalid_request = "invalid_request"
    unauthorized_client = "unauthorized_client"
    access_denied = "access_denied"
    unsupported_response_type = "unsupported_response_type"
    invalid_scope = "invalid_scope"
    server_error = "server_error"
    service_unavailable = "service_unavailable"
    bad_request = "bad_request"
    forbidden = "forbidden"
    not_found = "not_found"
    method_not_allowed = "method_not_allowed"
    too_many_requests = "too_many_requests"


class BypassCache(str, Enum):

    true = "true"
