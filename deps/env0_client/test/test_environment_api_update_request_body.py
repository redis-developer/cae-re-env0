# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.environment_api_update_request_body import EnvironmentApiUpdateRequestBody

class TestEnvironmentApiUpdateRequestBody(unittest.TestCase):
    """EnvironmentApiUpdateRequestBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnvironmentApiUpdateRequestBody:
        """Test EnvironmentApiUpdateRequestBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnvironmentApiUpdateRequestBody`
        """
        model = EnvironmentApiUpdateRequestBody()
        if include_optional:
            return EnvironmentApiUpdateRequestBody(
                name = '',
                requires_approval = True,
                is_archived = True,
                continuous_deployment = True,
                vcs_commands_alias = '',
                pull_request_plan_deployments = True,
                auto_deploy_on_path_changes_only = True,
                auto_deploy_by_custom_glob = '',
                is_remote_backend = True,
                is_remote_apply_enabled = True
            )
        else:
            return EnvironmentApiUpdateRequestBody(
        )
        """

    def testEnvironmentApiUpdateRequestBody(self):
        """Test EnvironmentApiUpdateRequestBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()