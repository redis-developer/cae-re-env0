# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from env0_client.models.provider_registry_api_terraform_types_gpg_public_keys import ProviderRegistryApiTerraformTypesGpgPublicKeys
from typing import Optional, Set
from typing_extensions import Self

class ProviderRegistryApiTerraformTypesSigningKeys(BaseModel):
    """
    ProviderRegistryApiTerraformTypesSigningKeys
    """ # noqa: E501
    gpg_public_keys: List[ProviderRegistryApiTerraformTypesGpgPublicKeys]
    __properties: ClassVar[List[str]] = ["gpg_public_keys"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ProviderRegistryApiTerraformTypesSigningKeys from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in gpg_public_keys (list)
        _items = []
        if self.gpg_public_keys:
            for _item in self.gpg_public_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['gpg_public_keys'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProviderRegistryApiTerraformTypesSigningKeys from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gpg_public_keys": [ProviderRegistryApiTerraformTypesGpgPublicKeys.from_dict(_item) for _item in obj["gpg_public_keys"]] if obj.get("gpg_public_keys") is not None else None
        })
        return _obj

