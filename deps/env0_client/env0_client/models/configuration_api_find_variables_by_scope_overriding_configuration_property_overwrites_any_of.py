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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from env0_client.models.configuration_scope import ConfigurationScope
from env0_client.models.partial_json_schema7 import PartialJSONSchema7
from typing import Optional, Set
from typing_extensions import Self

class ConfigurationApiFindVariablesByScopeOverridingConfigurationPropertyOverwritesAnyOf(BaseModel):
    """
    ConfigurationApiFindVariablesByScopeOverridingConfigurationPropertyOverwritesAnyOf
    """ # noqa: E501
    scope: ConfigurationScope
    scope_id: Optional[Any] = Field(default=None, description="The ID of the entity of the provided `scope`. e.g. a project's ID when the provided `scope` is `PROJECT`. Inapplicable for `GLOBAL` scope, as it has no specific entity.", alias="scopeId")
    value: Optional[StrictStr] = None
    var_schema: Optional[PartialJSONSchema7] = Field(default=None, description="If none passed, JSON and HCL values will be considered to be of string type. Make sure you specify the correct variable type. ENVIRONMENT_OUTPUT is a special type that is used to indicate that the value is an output from the environment. Its is of format ${env0:<environmentId>:<outputName>}", alias="schema")
    is_readonly: Optional[StrictBool] = Field(default=None, alias="isReadonly")
    is_required: Optional[StrictBool] = Field(default=None, alias="isRequired")
    is_sensitive: Optional[StrictBool] = Field(default=None, alias="isSensitive")
    regex: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["scope", "scopeId", "value", "schema", "isReadonly", "isRequired", "isSensitive", "regex"]

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
        """Create an instance of ConfigurationApiFindVariablesByScopeOverridingConfigurationPropertyOverwritesAnyOf from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # set to None if scope_id (nullable) is None
        # and model_fields_set contains the field
        if self.scope_id is None and "scope_id" in self.model_fields_set:
            _dict['scopeId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationApiFindVariablesByScopeOverridingConfigurationPropertyOverwritesAnyOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "scope": obj.get("scope"),
            "scopeId": obj.get("scopeId"),
            "value": obj.get("value"),
            "schema": PartialJSONSchema7.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "isReadonly": obj.get("isReadonly"),
            "isRequired": obj.get("isRequired"),
            "isSensitive": obj.get("isSensitive"),
            "regex": obj.get("regex")
        })
        return _obj


