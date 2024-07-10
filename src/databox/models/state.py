# coding: utf-8

"""
    Static OpenAPI document of Push API resource

    Push API resources Open API documentation

    The version of the OpenAPI document: 0.3.15-sdk.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class State(str, Enum):
    """
    State
    """

    """
    allowed enum values
    """
    DOWN = 'DOWN'
    UP = 'UP'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of State from a JSON string"""
        return cls(json.loads(json_str))


