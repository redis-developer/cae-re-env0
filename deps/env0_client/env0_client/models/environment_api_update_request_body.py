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
from typing import Optional, Set
from typing_extensions import Self

class EnvironmentApiUpdateRequestBody(BaseModel):
    """
    EnvironmentApiUpdateRequestBody
    """ # noqa: E501
    name: Optional[StrictStr] = None
    requires_approval: Optional[StrictBool] = Field(default=None, alias="requiresApproval")
    is_archived: Optional[StrictBool] = Field(default=None, description="Mark the environment as inactive", alias="isArchived")
    continuous_deployment: Optional[StrictBool] = Field(default=None, alias="continuousDeployment")
    vcs_commands_alias: Optional[StrictStr] = Field(default=None, alias="vcsCommandsAlias")
    pull_request_plan_deployments: Optional[StrictBool] = Field(default=None, alias="pullRequestPlanDeployments")
    auto_deploy_on_path_changes_only: Optional[StrictBool] = Field(default=None, alias="autoDeployOnPathChangesOnly")
    auto_deploy_by_custom_glob: Optional[StrictStr] = Field(default=None, alias="autoDeployByCustomGlob")
    is_remote_backend: Optional[StrictBool] = Field(default=None, alias="isRemoteBackend")
    is_remote_apply_enabled: Optional[StrictBool] = Field(default=None, alias="isRemoteApplyEnabled")
    __properties: ClassVar[List[str]] = ["name", "requiresApproval", "isArchived", "continuousDeployment", "vcsCommandsAlias", "pullRequestPlanDeployments", "autoDeployOnPathChangesOnly", "autoDeployByCustomGlob", "isRemoteBackend", "isRemoteApplyEnabled"]

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
        """Create an instance of EnvironmentApiUpdateRequestBody from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EnvironmentApiUpdateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "requiresApproval": obj.get("requiresApproval"),
            "isArchived": obj.get("isArchived"),
            "continuousDeployment": obj.get("continuousDeployment"),
            "vcsCommandsAlias": obj.get("vcsCommandsAlias"),
            "pullRequestPlanDeployments": obj.get("pullRequestPlanDeployments"),
            "autoDeployOnPathChangesOnly": obj.get("autoDeployOnPathChangesOnly"),
            "autoDeployByCustomGlob": obj.get("autoDeployByCustomGlob"),
            "isRemoteBackend": obj.get("isRemoteBackend"),
            "isRemoteApplyEnabled": obj.get("isRemoteApplyEnabled")
        })
        return _obj


