"""This file contains exceptions related to services.

This file doesn't contain any service."""


class InvalidPath(Exception):
    """Supposed to be raised when expected Path argument is invalid."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ArgumentError(Exception):
    """Supposed to be raised when arguments are in some way invalid."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
