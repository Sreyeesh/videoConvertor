"""This file contains exceptions related to services.

This file doesn't contain any service."""


class InvalidPath(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
