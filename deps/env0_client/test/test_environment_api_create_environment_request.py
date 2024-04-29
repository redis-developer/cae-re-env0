# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.environment_api_create_environment_request import EnvironmentApiCreateEnvironmentRequest

class TestEnvironmentApiCreateEnvironmentRequest(unittest.TestCase):
    """EnvironmentApiCreateEnvironmentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnvironmentApiCreateEnvironmentRequest:
        """Test EnvironmentApiCreateEnvironmentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnvironmentApiCreateEnvironmentRequest`
        """
        model = EnvironmentApiCreateEnvironmentRequest()
        if include_optional:
            return EnvironmentApiCreateEnvironmentRequest(
                name = '',
                project_id = '0',
                workspace_name = '',
                requires_approval = True,
                ttl = env0_client.models.environment_api/ttl_request.EnvironmentApi.TTLRequest(
                    type = 'DATE', 
                    value = '', ),
                configuration_changes = None,
                vcs_commands_alias = '',
                deploy_request = env0_client.models.deploy_request.DeployRequest(
                    workflow_deployment_id = '', 
                    deployment_type = 'remotePlan', 
                    blueprint_id = '', 
                    blueprint_revision = '', 
                    blueprint_repository = '', 
                    configuration_changes = null, 
                    ttl = env0_client.models.environment_api/ttl_request.EnvironmentApi.TTLRequest(
                        type = 'DATE', 
                        value = '', ), 
                    env_name = '', 
                    user_requires_approval = True, 
                    targets = [
                        ''
                        ], 
                    custom_env0_environment_variables = env0_client.models.custom_env0_environment_variables.CustomEnv0EnvironmentVariables(
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
                        cli_args_apply = '', ), 
                    git_user_data = env0_client.models.git_user_data.GitUserData(
                        git_user = '', 
                        git_avatar_url = '', 
                        pr_number = '', ), 
                    comment = '', 
                    trigger_name = 'scheduled', 
                    upstream_environment_id = '', 
                    task_payload = '', 
                    sub_environments = {
                        'key' : env0_client.models.workflow_sub_environment_request.WorkflowSubEnvironmentRequest(
                            revision = '', 
                            workspace_name = '', 
                            k8s_namespace = '', 
                            terragrunt_working_directory = '', 
                            is_remote_backend = True, )
                        }, 
                    workflow_deployment_options = env0_client.models.workflow_deployment_options.WorkflowDeploymentOptions(
                        node = '', 
                        operation = 'single-node-deploy', ), ),
                continuous_deployment = True,
                pull_request_plan_deployments = True,
                drift_detection_request = env0_client.models.environment_api/drift_detection_request.EnvironmentApi.DriftDetectionRequest(
                    enabled = True, 
                    cron = '', ),
                auto_deploy_on_path_changes_only = True,
                auto_deploy_by_custom_glob = '',
                terragrunt_working_directory = '',
                is_remote_backend = True,
                k8s_namespace = '',
                prevent_auto_deploy = True
            )
        else:
            return EnvironmentApiCreateEnvironmentRequest(
                name = '',
                project_id = '0',
                deploy_request = env0_client.models.deploy_request.DeployRequest(
                    workflow_deployment_id = '', 
                    deployment_type = 'remotePlan', 
                    blueprint_id = '', 
                    blueprint_revision = '', 
                    blueprint_repository = '', 
                    configuration_changes = null, 
                    ttl = env0_client.models.environment_api/ttl_request.EnvironmentApi.TTLRequest(
                        type = 'DATE', 
                        value = '', ), 
                    env_name = '', 
                    user_requires_approval = True, 
                    targets = [
                        ''
                        ], 
                    custom_env0_environment_variables = env0_client.models.custom_env0_environment_variables.CustomEnv0EnvironmentVariables(
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
                        cli_args_apply = '', ), 
                    git_user_data = env0_client.models.git_user_data.GitUserData(
                        git_user = '', 
                        git_avatar_url = '', 
                        pr_number = '', ), 
                    comment = '', 
                    trigger_name = 'scheduled', 
                    upstream_environment_id = '', 
                    task_payload = '', 
                    sub_environments = {
                        'key' : env0_client.models.workflow_sub_environment_request.WorkflowSubEnvironmentRequest(
                            revision = '', 
                            workspace_name = '', 
                            k8s_namespace = '', 
                            terragrunt_working_directory = '', 
                            is_remote_backend = True, )
                        }, 
                    workflow_deployment_options = env0_client.models.workflow_deployment_options.WorkflowDeploymentOptions(
                        node = '', 
                        operation = 'single-node-deploy', ), ),
        )
        """

    def testEnvironmentApiCreateEnvironmentRequest(self):
        """Test EnvironmentApiCreateEnvironmentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
