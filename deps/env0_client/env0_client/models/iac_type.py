# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class IacType(str, Enum):
    """
    IacType
    """

    """
    allowed enum values
    """
    CLOUDFORMATION = 'cloudformation'
    TERRAFORM = 'terraform'
    OPENTOFU = 'opentofu'
    HELM = 'helm'
    PULUMI = 'pulumi'
    TERRAGRUNT = 'terragrunt'
    K8S = 'k8s'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IacType from a JSON string"""
        return cls(json.loads(json_str))


