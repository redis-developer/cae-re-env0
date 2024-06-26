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
from env0_client.models.iac_type import IacType
from env0_client.models.workflow_sub_environment_disabled import WorkflowSubEnvironmentDisabled
from typing import Optional, Set
from typing_extensions import Self

class EnvironmentApiWorkflowEnvironmentsWorkflowSubEnvironment(BaseModel):
    """
    EnvironmentApiWorkflowEnvironmentsWorkflowSubEnvironment
    """ # noqa: E501
    environment_id: Optional[StrictStr] = Field(default=None, alias="environmentId")
    to_destroy: Optional[StrictBool] = Field(default=None, alias="toDestroy")
    is_remote_backend: Optional[StrictBool] = Field(default=None, alias="isRemoteBackend")
    k8s_namespace: Optional[StrictStr] = Field(default=None, alias="k8sNamespace")
    name: StrictStr
    template_name: StrictStr = Field(alias="templateName")
    template_id: StrictStr = Field(alias="templateId")
    template_type: IacType = Field(alias="templateType")
    revision: Optional[StrictStr] = None
    workspace: Optional[StrictStr] = None
    needs: Optional[List[StrictStr]] = None
    terragrunt_working_directory: Optional[StrictStr] = Field(default=None, alias="terragruntWorkingDirectory")
    disabled: Optional[WorkflowSubEnvironmentDisabled] = None
    __properties: ClassVar[List[str]] = ["environmentId", "toDestroy", "isRemoteBackend", "k8sNamespace", "name", "templateName", "templateId", "templateType", "revision", "workspace", "needs", "terragruntWorkingDirectory", "disabled"]

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
        """Create an instance of EnvironmentApiWorkflowEnvironmentsWorkflowSubEnvironment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of disabled
        if self.disabled:
            _dict['disabled'] = self.disabled.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EnvironmentApiWorkflowEnvironmentsWorkflowSubEnvironment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "environmentId": obj.get("environmentId"),
            "toDestroy": obj.get("toDestroy"),
            "isRemoteBackend": obj.get("isRemoteBackend"),
            "k8sNamespace": obj.get("k8sNamespace"),
            "name": obj.get("name"),
            "templateName": obj.get("templateName"),
            "templateId": obj.get("templateId"),
            "templateType": obj.get("templateType"),
            "revision": obj.get("revision"),
            "workspace": obj.get("workspace"),
            "needs": obj.get("needs"),
            "terragruntWorkingDirectory": obj.get("terragruntWorkingDirectory"),
            "disabled": WorkflowSubEnvironmentDisabled.from_dict(obj["disabled"]) if obj.get("disabled") is not None else None
        })
        return _obj


