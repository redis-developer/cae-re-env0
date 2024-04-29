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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from env0_client.models.configuration_set_assignment_scope import ConfigurationSetAssignmentScope
from env0_client.models.set_creation_scope import SetCreationScope
from env0_client.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class ConfigurationSet(BaseModel):
    """
    ConfigurationSet
    """ # noqa: E501
    id: Optional[StrictStr] = None
    name: StrictStr
    description: Optional[StrictStr] = None
    assignment_scope_id: StrictStr = Field(alias="assignmentScopeId")
    assignment_scope: Optional[ConfigurationSetAssignmentScope] = Field(default=None, alias="assignmentScope")
    creation_scope_id: StrictStr = Field(alias="creationScopeId")
    creation_scope: SetCreationScope = Field(alias="creationScope")
    organization_id: StrictStr = Field(alias="organizationId")
    created_by: StrictStr = Field(alias="createdBy")
    created_by_user: Optional[User] = Field(default=None, alias="createdByUser")
    to_delete: Optional[StrictBool] = Field(default=None, alias="toDelete")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "name", "description", "assignmentScopeId", "assignmentScope", "creationScopeId", "creationScope", "organizationId", "createdBy", "createdByUser", "toDelete", "createdAt", "updatedAt"]

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
        """Create an instance of ConfigurationSet from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by_user
        if self.created_by_user:
            _dict['createdByUser'] = self.created_by_user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "assignmentScopeId": obj.get("assignmentScopeId"),
            "assignmentScope": obj.get("assignmentScope"),
            "creationScopeId": obj.get("creationScopeId"),
            "creationScope": obj.get("creationScope"),
            "organizationId": obj.get("organizationId"),
            "createdBy": obj.get("createdBy"),
            "createdByUser": User.from_dict(obj["createdByUser"]) if obj.get("createdByUser") is not None else None,
            "toDelete": obj.get("toDelete"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


