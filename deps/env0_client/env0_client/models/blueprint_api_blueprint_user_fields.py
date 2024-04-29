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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from env0_client.models.blueprint_api_retry import BlueprintApiRetry
from env0_client.models.blueprint_api_ssh_key import BlueprintApiSshKey
from env0_client.models.blueprint_api_terraform_version import BlueprintApiTerraformVersion
from env0_client.models.blueprint_api_terragrunt_tf_binary import BlueprintApiTerragruntTfBinary
from env0_client.models.blueprint_type import BlueprintType
from typing import Optional, Set
from typing_extensions import Self

class BlueprintApiBlueprintUserFields(BaseModel):
    """
    BlueprintApiBlueprintUserFields
    """ # noqa: E501
    name: StrictStr
    description: Optional[StrictStr] = None
    retry: Optional[BlueprintApiRetry] = None
    run_tests_on_pull_request: Optional[StrictBool] = Field(default=None, alias="runTestsOnPullRequest")
    is_terragrunt_run_all: Optional[StrictBool] = Field(default=None, alias="isTerragruntRunAll")
    project_ids: Optional[List[StrictStr]] = Field(default=None, alias="projectIds")
    tag_prefix: Optional[StrictStr] = Field(default=None, alias="tagPrefix")
    repository: StrictStr
    revision: Optional[StrictStr] = None
    path: Optional[StrictStr] = None
    file_name: Optional[StrictStr] = Field(default=None, alias="fileName")
    helm_chart_name: Optional[StrictStr] = Field(default=None, alias="helmChartName")
    terraform_version: Optional[BlueprintApiTerraformVersion] = Field(default=None, description="A string representing semantic version of Terraform. If set to \"RESOLVE_FROM_TERRAFORM_CODE\", the version will be determined by using tfenv's 'min-required'. When set to \"latest\", the version used will be the most recent one available for Terraform.", alias="terraformVersion")
    opentofu_version: Optional[StrictStr] = Field(default=None, alias="opentofuVersion")
    terragrunt_version: Optional[StrictStr] = Field(default=None, alias="terragruntVersion")
    terragrunt_tf_binary: Optional[BlueprintApiTerragruntTfBinary] = Field(default=None, alias="terragruntTfBinary")
    pulumi_version: Optional[StrictStr] = Field(default=None, alias="pulumiVersion")
    type: BlueprintType
    gitlab_project_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gitlabProjectId")
    token_name: Optional[StrictStr] = Field(default=None, alias="tokenName")
    token_id: Optional[StrictStr] = Field(default=None, alias="tokenId")
    ssh_keys: Optional[List[BlueprintApiSshKey]] = Field(default=None, alias="sshKeys")
    github_installation_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="githubInstallationId")
    bitbucket_client_key: Optional[StrictStr] = Field(default=None, alias="bitbucketClientKey")
    is_bitbucket_server: Optional[StrictBool] = Field(default=None, alias="isBitbucketServer")
    is_git_lab_enterprise: Optional[StrictBool] = Field(default=None, alias="isGitLabEnterprise")
    is_git_hub_enterprise: Optional[StrictBool] = Field(default=None, alias="isGitHubEnterprise")
    is_git_lab: Optional[StrictBool] = Field(default=None, alias="isGitLab")
    is_azure_dev_ops: Optional[StrictBool] = Field(default=None, alias="isAzureDevOps")
    is_helm_repository: Optional[StrictBool] = Field(default=None, alias="isHelmRepository")
    __properties: ClassVar[List[str]] = ["name", "description", "retry", "runTestsOnPullRequest", "isTerragruntRunAll", "projectIds", "tagPrefix", "repository", "revision", "path", "fileName", "helmChartName", "terraformVersion", "opentofuVersion", "terragruntVersion", "terragruntTfBinary", "pulumiVersion", "type", "gitlabProjectId", "tokenName", "tokenId", "sshKeys", "githubInstallationId", "bitbucketClientKey", "isBitbucketServer", "isGitLabEnterprise", "isGitHubEnterprise", "isGitLab", "isAzureDevOps", "isHelmRepository"]

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
        """Create an instance of BlueprintApiBlueprintUserFields from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of retry
        if self.retry:
            _dict['retry'] = self.retry.to_dict()
        # override the default output from pydantic by calling `to_dict()` of terraform_version
        if self.terraform_version:
            _dict['terraformVersion'] = self.terraform_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ssh_keys (list)
        _items = []
        if self.ssh_keys:
            for _item in self.ssh_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sshKeys'] = _items
        # set to None if gitlab_project_id (nullable) is None
        # and model_fields_set contains the field
        if self.gitlab_project_id is None and "gitlab_project_id" in self.model_fields_set:
            _dict['gitlabProjectId'] = None

        # set to None if github_installation_id (nullable) is None
        # and model_fields_set contains the field
        if self.github_installation_id is None and "github_installation_id" in self.model_fields_set:
            _dict['githubInstallationId'] = None

        # set to None if bitbucket_client_key (nullable) is None
        # and model_fields_set contains the field
        if self.bitbucket_client_key is None and "bitbucket_client_key" in self.model_fields_set:
            _dict['bitbucketClientKey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BlueprintApiBlueprintUserFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "retry": BlueprintApiRetry.from_dict(obj["retry"]) if obj.get("retry") is not None else None,
            "runTestsOnPullRequest": obj.get("runTestsOnPullRequest"),
            "isTerragruntRunAll": obj.get("isTerragruntRunAll"),
            "projectIds": obj.get("projectIds"),
            "tagPrefix": obj.get("tagPrefix"),
            "repository": obj.get("repository"),
            "revision": obj.get("revision"),
            "path": obj.get("path"),
            "fileName": obj.get("fileName"),
            "helmChartName": obj.get("helmChartName"),
            "terraformVersion": BlueprintApiTerraformVersion.from_dict(obj["terraformVersion"]) if obj.get("terraformVersion") is not None else None,
            "opentofuVersion": obj.get("opentofuVersion"),
            "terragruntVersion": obj.get("terragruntVersion"),
            "terragruntTfBinary": obj.get("terragruntTfBinary"),
            "pulumiVersion": obj.get("pulumiVersion"),
            "type": obj.get("type"),
            "gitlabProjectId": obj.get("gitlabProjectId"),
            "tokenName": obj.get("tokenName"),
            "tokenId": obj.get("tokenId"),
            "sshKeys": [BlueprintApiSshKey.from_dict(_item) for _item in obj["sshKeys"]] if obj.get("sshKeys") is not None else None,
            "githubInstallationId": obj.get("githubInstallationId"),
            "bitbucketClientKey": obj.get("bitbucketClientKey"),
            "isBitbucketServer": obj.get("isBitbucketServer"),
            "isGitLabEnterprise": obj.get("isGitLabEnterprise"),
            "isGitHubEnterprise": obj.get("isGitHubEnterprise"),
            "isGitLab": obj.get("isGitLab"),
            "isAzureDevOps": obj.get("isAzureDevOps"),
            "isHelmRepository": obj.get("isHelmRepository")
        })
        return _obj


