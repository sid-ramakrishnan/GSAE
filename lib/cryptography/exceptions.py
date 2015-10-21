# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

from enum import Enum

from cryptography import utils
from cryptography.hazmat.primitives import twofactor


class _Reasons(Enum):
    BACKEND_MISSING_INTERFACE = 0
    UNSUPPORTED_HASH = 1
    UNSUPPORTED_CIPHER = 2
    UNSUPPORTED_PADDING = 3
    UNSUPPORTED_MGF = 4
    UNSUPPORTED_PUBLIC_KEY_ALGORITHM = 5
    UNSUPPORTED_ELLIPTIC_CURVE = 6
    UNSUPPORTED_SERIALIZATION = 7
    UNSUPPORTED_X509 = 8


class UnsupportedAlgorithm(Exception):
    def __init__(self, message, reason=None):
        super(UnsupportedAlgorithm, self).__init__(message)
        self._reason = reason


class AlreadyFinalized(Exception):
    pass


class AlreadyUpdated(Exception):
    pass


class NotYetFinalized(Exception):
    pass


class InvalidTag(Exception):
    pass


class InvalidSignature(Exception):
    pass


class InternalError(Exception):
    def __init__(self, msg, err_code):
        super(InternalError, self).__init__(msg)
        self.err_code = err_code


class InvalidKey(Exception):
    pass


InvalidToken = utils.deprecated(
    twofactor.InvalidToken,
    __name__,
    (
        "The InvalidToken exception has moved to the "
        "cryptography.hazmat.primitives.twofactor module"
    ),
    utils.DeprecatedIn09
)