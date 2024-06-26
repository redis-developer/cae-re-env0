# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.custom_env0_environment_variables import CustomEnv0EnvironmentVariables

class TestCustomEnv0EnvironmentVariables(unittest.TestCase):
    """CustomEnv0EnvironmentVariables unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomEnv0EnvironmentVariables:
        """Test CustomEnv0EnvironmentVariables
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomEnv0EnvironmentVariables`
        """
        model = CustomEnv0EnvironmentVariables()
        if include_optional:
            return CustomEnv0EnvironmentVariables(
                environment_id = '',
                project_id = '',
                project_name = '',
                deployment_log_id = '',
                deployment_type = 'prPlan',
                deployment_revision = '',
                workspace_name = '',
                root_dir = '',
                organization_id = '',
                template_id = '',
                template_dir = '',
                template_name = '',
                environment_name = '',
                environment_creator_name = '',
                environment_creator_email = '',
                deployer_name = '',
                deployer_email = '',
                reviewer_name = '',
                reviewer_email = '',
                pr_author = '',
                pr_source_branch = '',
                pr_target_branch = '',
                commit_hash = '',
                commit_url = '',
                oidc_token = '',
                vcs_access_token = '',
                tf_plan_json = '',
                cli_args_plan = '',
                cli_args_apply = ''
            )
        else:
            return CustomEnv0EnvironmentVariables(
        )
        """

    def testCustomEnv0EnvironmentVariables(self):
        """Test CustomEnv0EnvironmentVariables"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
