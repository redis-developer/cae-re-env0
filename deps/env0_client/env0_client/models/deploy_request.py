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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from env0_client.models.custom_env0_environment_variables import CustomEnv0EnvironmentVariables
from env0_client.models.environment_api_configuration_changes import EnvironmentApiConfigurationChanges
from env0_client.models.environment_api_ttl_request import EnvironmentApiTTLRequest
from env0_client.models.git_user_data import GitUserData
from env0_client.models.trigger_name import TriggerName
from env0_client.models.workflow_deployment_options import WorkflowDeploymentOptions
from env0_client.models.workflow_sub_environment_request import WorkflowSubEnvironmentRequest
from typing import Optional, Set
from typing_extensions import Self

class DeployRequest(BaseModel):
    """
    DeployRequest
    """ # noqa: E501
    workflow_deployment_id: Optional[StrictStr] = Field(default=None, alias="workflowDeploymentId")
    deployment_type: Optional[StrictStr] = Field(default=None, alias="deploymentType")
    blueprint_id: Optional[StrictStr] = Field(default=None, alias="blueprintId")
    blueprint_revision: Optional[StrictStr] = Field(default=None, alias="blueprintRevision")
    blueprint_repository: Optional[StrictStr] = Field(default=None, alias="blueprintRepository")
    configuration_changes: Optional[EnvironmentApiConfigurationChanges] = Field(default=None, alias="configurationChanges")
    ttl: Optional[EnvironmentApiTTLRequest] = None
    env_name: Optional[StrictStr] = Field(default=None, alias="envName")
    user_requires_approval: Optional[StrictBool] = Field(default=None, alias="userRequiresApproval")
    targets: Optional[List[StrictStr]] = None
    custom_env0_environment_variables: Optional[CustomEnv0EnvironmentVariables] = Field(default=None, alias="customEnv0EnvironmentVariables")
    git_user_data: Optional[GitUserData] = Field(default=None, alias="gitUserData")
    comment: Optional[StrictStr] = None
    trigger_name: Optional[TriggerName] = Field(default=None, alias="triggerName")
    upstream_environment_id: Optional[StrictStr] = Field(default=None, alias="upstreamEnvironmentId")
    task_payload: Optional[StrictStr] = Field(default=None, alias="taskPayload")
    sub_environments: Optional[Dict[str, WorkflowSubEnvironmentRequest]] = Field(default=None, alias="subEnvironments")
    workflow_deployment_options: Optional[WorkflowDeploymentOptions] = Field(default=None, description="[Optional] Only applicable when running a Workflow Environment. Allows to run a partial Workflow, starting from a specific point in the pipeline. Or run a single sub-environment deploy/destroy.", alias="workflowDeploymentOptions")
    __properties: ClassVar[List[str]] = ["workflowDeploymentId", "deploymentType", "blueprintId", "blueprintRevision", "blueprintRepository", "configurationChanges", "ttl", "envName", "userRequiresApproval", "targets", "customEnv0EnvironmentVariables", "gitUserData", "comment", "triggerName", "upstreamEnvironmentId", "taskPayload", "subEnvironments", "workflowDeploymentOptions"]

    @field_validator('deployment_type')
    def deployment_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['remotePlan', 'prPlan', 'deploy', 'moduleTest', 'task', 'driftDetection']):
            raise ValueError("must be one of enum values ('remotePlan', 'prPlan', 'deploy', 'moduleTest', 'task', 'driftDetection')")
        return value

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
        """Create an instance of DeployRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of configuration_changes
        if self.configuration_changes:
            _dict['configurationChanges'] = self.configuration_changes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ttl
        if self.ttl:
            _dict['ttl'] = self.ttl.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_env0_environment_variables
        if self.custom_env0_environment_variables:
            _dict['customEnv0EnvironmentVariables'] = self.custom_env0_environment_variables.to_dict()
        # override the default output from pydantic by calling `to_dict()` of git_user_data
        if self.git_user_data:
            _dict['gitUserData'] = self.git_user_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workflow_deployment_options
        if self.workflow_deployment_options:
            _dict['workflowDeploymentOptions'] = self.workflow_deployment_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeployRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "workflowDeploymentId": obj.get("workflowDeploymentId"),
            "deploymentType": obj.get("deploymentType"),
            "blueprintId": obj.get("blueprintId"),
            "blueprintRevision": obj.get("blueprintRevision"),
            "blueprintRepository": obj.get("blueprintRepository"),
            "configurationChanges": EnvironmentApiConfigurationChanges.from_dict(obj["configurationChanges"]) if obj.get("configurationChanges") is not None else None,
            "ttl": EnvironmentApiTTLRequest.from_dict(obj["ttl"]) if obj.get("ttl") is not None else None,
            "envName": obj.get("envName"),
            "userRequiresApproval": obj.get("userRequiresApproval"),
            "targets": obj.get("targets"),
            "customEnv0EnvironmentVariables": CustomEnv0EnvironmentVariables.from_dict(obj["customEnv0EnvironmentVariables"]) if obj.get("customEnv0EnvironmentVariables") is not None else None,
            "gitUserData": GitUserData.from_dict(obj["gitUserData"]) if obj.get("gitUserData") is not None else None,
            "comment": obj.get("comment"),
            "triggerName": obj.get("triggerName"),
            "upstreamEnvironmentId": obj.get("upstreamEnvironmentId"),
            "taskPayload": obj.get("taskPayload"),
            "workflowDeploymentOptions": WorkflowDeploymentOptions.from_dict(obj["workflowDeploymentOptions"]) if obj.get("workflowDeploymentOptions") is not None else None
        })
        return _obj


