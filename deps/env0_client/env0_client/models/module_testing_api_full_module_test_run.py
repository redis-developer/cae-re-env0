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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from env0_client.models.custom_env0_environment_variables import CustomEnv0EnvironmentVariables
from env0_client.models.environment_api_deployment_log_status import EnvironmentApiDeploymentLogStatus
from env0_client.models.module_testing_api_test_file_result import ModuleTestingApiTestFileResult
from env0_client.models.module_testing_api_test_file_summary import ModuleTestingApiTestFileSummary
from env0_client.models.trigger_name import TriggerName
from env0_client.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class ModuleTestingApiFullModuleTestRun(BaseModel):
    """
    ModuleTestingApiFullModuleTestRun
    """ # noqa: E501
    status: Optional[EnvironmentApiDeploymentLogStatus] = None
    blueprint_revision: Optional[StrictStr] = Field(default=None, alias="blueprintRevision")
    pr_number: Optional[StrictStr] = Field(default=None, alias="prNumber")
    started_by: Optional[StrictStr] = Field(default=None, alias="startedBy")
    started_by_user: Optional[User] = Field(default=None, alias="startedByUser")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    queued_at: Optional[datetime] = Field(default=None, alias="queuedAt")
    started_at: Optional[datetime] = Field(default=None, alias="startedAt")
    finished_at: Optional[datetime] = Field(default=None, alias="finishedAt")
    error: Optional[Dict[str, Any]] = None
    custom_env0_environment_variables: Optional[CustomEnv0EnvironmentVariables] = Field(default=None, alias="customEnv0EnvironmentVariables")
    git_avatar_url: Optional[StrictStr] = Field(default=None, alias="gitAvatarUrl")
    git_user: Optional[StrictStr] = Field(default=None, alias="gitUser")
    blueprint_repository: Optional[StrictStr] = Field(default=None, alias="blueprintRepository")
    id: Optional[StrictStr] = None
    deployment_log_id: StrictStr = Field(alias="deploymentLogId")
    environment_id: StrictStr = Field(alias="environmentId")
    organization_id: StrictStr = Field(alias="organizationId")
    trigger_name: Optional[TriggerName] = Field(default=None, alias="triggerName")
    test_summary: Optional[ModuleTestingApiTestFileSummary] = Field(default=None, alias="testSummary")
    test_files_results: Optional[Dict[str, ModuleTestingApiTestFileResult]] = Field(default=None, alias="testFilesResults")
    module_id: Optional[StrictStr] = Field(default=None, alias="moduleId")
    __properties: ClassVar[List[str]] = ["status", "blueprintRevision", "prNumber", "startedBy", "startedByUser", "createdAt", "queuedAt", "startedAt", "finishedAt", "error", "customEnv0EnvironmentVariables", "gitAvatarUrl", "gitUser", "blueprintRepository", "id", "deploymentLogId", "environmentId", "organizationId", "triggerName", "testSummary", "testFilesResults", "moduleId"]

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
        """Create an instance of ModuleTestingApiFullModuleTestRun from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of started_by_user
        if self.started_by_user:
            _dict['startedByUser'] = self.started_by_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_env0_environment_variables
        if self.custom_env0_environment_variables:
            _dict['customEnv0EnvironmentVariables'] = self.custom_env0_environment_variables.to_dict()
        # override the default output from pydantic by calling `to_dict()` of test_summary
        if self.test_summary:
            _dict['testSummary'] = self.test_summary.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModuleTestingApiFullModuleTestRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "blueprintRevision": obj.get("blueprintRevision"),
            "prNumber": obj.get("prNumber"),
            "startedBy": obj.get("startedBy"),
            "startedByUser": User.from_dict(obj["startedByUser"]) if obj.get("startedByUser") is not None else None,
            "createdAt": obj.get("createdAt"),
            "queuedAt": obj.get("queuedAt"),
            "startedAt": obj.get("startedAt"),
            "finishedAt": obj.get("finishedAt"),
            "error": obj.get("error"),
            "customEnv0EnvironmentVariables": CustomEnv0EnvironmentVariables.from_dict(obj["customEnv0EnvironmentVariables"]) if obj.get("customEnv0EnvironmentVariables") is not None else None,
            "gitAvatarUrl": obj.get("gitAvatarUrl"),
            "gitUser": obj.get("gitUser"),
            "blueprintRepository": obj.get("blueprintRepository"),
            "id": obj.get("id"),
            "deploymentLogId": obj.get("deploymentLogId"),
            "environmentId": obj.get("environmentId"),
            "organizationId": obj.get("organizationId"),
            "triggerName": obj.get("triggerName"),
            "testSummary": ModuleTestingApiTestFileSummary.from_dict(obj["testSummary"]) if obj.get("testSummary") is not None else None,
            "moduleId": obj.get("moduleId")
        })
        return _obj


