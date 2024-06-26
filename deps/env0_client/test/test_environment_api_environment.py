# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.environment_api_environment import EnvironmentApiEnvironment

class TestEnvironmentApiEnvironment(unittest.TestCase):
    """EnvironmentApiEnvironment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnvironmentApiEnvironment:
        """Test EnvironmentApiEnvironment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnvironmentApiEnvironment`
        """
        model = EnvironmentApiEnvironment()
        if include_optional:
            return EnvironmentApiEnvironment(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                organization_id = '',
                project_id = '',
                user_id = '',
                workspace_name = '',
                user = env0_client.models.user.User(
                    email = '', 
                    user_id = '', 
                    created_at = '', 
                    app_metadata = env0_client.models.app_metadata.app_metadata(), 
                    picture = '', 
                    name = '', 
                    last_login = '', 
                    given_name = '', 
                    family_name = '', ),
                requires_approval = True,
                status = 'ABORTING',
                latest_deployment_log_id = '',
                latest_deployment_log = env0_client.models.environment_api/deployment_log.EnvironmentApi.DeploymentLog(
                    id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    type = 'remotePlan', 
                    started_by = '', 
                    queued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    output = null, 
                    error = env0_client.models.error.error(), 
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
                    cost_estimation = env0_client.models.infracost/total_output.Infracost.TotalOutput(
                        version = '', 
                        projects = [
                            env0_client.models.infracost_total_output_projects_inner.Infracost_TotalOutput_projects_inner(
                                path = '', 
                                metadata = null, 
                                past_breakdown = env0_client.models.infracost/output.Infracost.Output(
                                    resources = [
                                        null
                                        ], 
                                    total_hourly_cost = '', 
                                    total_monthly_cost = '', ), 
                                breakdown = env0_client.models.infracost/output.Infracost.Output(
                                    total_hourly_cost = '', 
                                    total_monthly_cost = '', ), 
                                diff = , )
                            ], 
                        time_generated = '', 
                        summary = env0_client.models.infracost_total_output_summary.Infracost_TotalOutput_summary(
                            unsupported_resource_counts = null, ), 
                        resources = [
                            null
                            ], 
                        total_hourly_cost = '', 
                        total_monthly_cost = '', ), 
                    status = 'QUEUED', 
                    blueprint_id = '', 
                    blueprint_name = '', 
                    blueprint_repository = '', 
                    blueprint_revision = '', 
                    blueprint_path = '', 
                    blueprint_type = 'cloudformation', 
                    comment = '', 
                    environment_id = '', 
                    resource_count = 1.337, 
                    resources = [
                        env0_client.models.environment_api/environment_resource.EnvironmentApi.EnvironmentResource(
                            provider = '', 
                            type = '', 
                            name = '', 
                            module_name = '', )
                        ], 
                    started_by_user = env0_client.models.user.User(
                        email = '', 
                        user_id = '', 
                        created_at = '', 
                        app_metadata = env0_client.models.app_metadata.app_metadata(), 
                        picture = '', 
                        name = '', 
                        last_login = '', 
                        given_name = '', 
                        family_name = '', ), 
                    is_scheduled_run = True, 
                    aborted_by = '', 
                    aborted_by_user = env0_client.models.user.User(
                        email = '', 
                        user_id = '', 
                        created_at = '', 
                        app_metadata = env0_client.models.app_metadata.app_metadata(), 
                        picture = '', 
                        name = '', 
                        last_login = '', 
                        given_name = '', 
                        family_name = '', ), 
                    git_user = '', 
                    git_avatar_url = '', 
                    pr_number = '', 
                    trigger_name = 'scheduled', 
                    drift_detected = True, 
                    plan = env0_client.models.environment_api_deployment_log_plan.EnvironmentApi_DeploymentLog_plan(
                        resource_changes = [
                            env0_client.models.deployment_api/plan/plan_resource_change.DeploymentApi.Plan.PlanResourceChange(
                                name = '', 
                                provider_name = '', 
                                type = '', 
                                path = '', 
                                action = 'create', 
                                attributes = [
                                    env0_client.models.deployment_api/plan/attribute_change.DeploymentApi.Plan.AttributeChange(
                                        name = '', 
                                        before = null, 
                                        after = null, )
                                    ], 
                                importing = env0_client.models.deployment_api/plan/resource_import_data.DeploymentApi.Plan.ResourceImportData(
                                    id = '', ), 
                                previous_address = '', )
                            ], 
                        output_changes = [
                            env0_client.models.deployment_api/plan/plan_output_change.DeploymentApi.Plan.PlanOutputChange(
                                name = '', 
                                action = 'create', 
                                attributes = [
                                    env0_client.models.deployment_api/plan/attribute_change.DeploymentApi.Plan.AttributeChange(
                                        name = '', 
                                        before = null, 
                                        after = null, )
                                    ], )
                            ], ), 
                    plan_summary = env0_client.models.deployment_api/plan/plan_summary.DeploymentApi.Plan.PlanSummary(
                        added = 1.337, 
                        changed = 1.337, 
                        destroyed = 1.337, 
                        imported = 1.337, ), 
                    is_skipped_apply = True, 
                    workflow_deployment_id = '', 
                    workflow_file = env0_client.models.environment_api/workflow_environments/workflow_file.EnvironmentApi.WorkflowEnvironments.WorkflowFile(
                        settings = env0_client.models.workflow_file_settings.WorkflowFile_settings(
                            environment_removal_strategy = destroy, ), 
                        environments = {
                            'key' : env0_client.models.environment_api/workflow_environments/workflow_sub_environment.EnvironmentApi.WorkflowEnvironments.WorkflowSubEnvironment(
                                environment_id = '', 
                                to_destroy = True, 
                                is_remote_backend = True, 
                                k8s_namespace = '', 
                                name = '', 
                                template_name = '', 
                                template_id = '', 
                                template_type = 'cloudformation', 
                                revision = '', 
                                workspace = '', 
                                needs = [
                                    ''
                                    ], 
                                terragrunt_working_directory = '', 
                                disabled = null, )
                            }, ), 
                    workflow_deployment_options = env0_client.models.workflow_deployment_options.WorkflowDeploymentOptions(
                        node = '', 
                        operation = 'single-node-deploy', ), 
                    state_version_id = '', 
                    reviewers_users = [
                        env0_client.models.environment_api/reviewer_user.EnvironmentApi.ReviewerUser(
                            user = , 
                            action = 'cancelled', )
                        ], 
                    reviewers = [
                        env0_client.models.environment_api/reviewer.EnvironmentApi.Reviewer(
                            user_id = '', 
                            action = 'cancelled', )
                        ], 
                    reviewed_by = '', 
                    reviewed_by_user = , 
                    targets = [
                        ''
                        ], ),
                lifespan_end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                marked_for_auto_destroy = 0,
                is_archived = True,
                next_scheduled_dates = env0_client.models.environment_api/environment_next_scheduled_dates.EnvironmentApi.EnvironmentNextScheduledDates(
                    deploy = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    destroy = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                vcs_commands_alias = '',
                continuous_deployment = True,
                pull_request_plan_deployments = True,
                auto_deploy_on_path_changes_only = True,
                auto_deploy_by_custom_glob = '',
                terragrunt_working_directory = '',
                is_single_use_blueprint = True,
                workflow_environment_id = '',
                is_remote_backend = True,
                is_locked = True,
                lock_status = env0_client.models.environment_api/environment_lock_status.EnvironmentApi.EnvironmentLockStatus(
                    reason = '', 
                    updated_by = '', 
                    updated_by_user = env0_client.models.user.User(
                        email = '', 
                        user_id = '', 
                        created_at = '', 
                        app_metadata = env0_client.models.app_metadata.app_metadata(), 
                        picture = '', 
                        name = '', 
                        last_login = '', 
                        given_name = '', 
                        family_name = '', ), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                k8s_namespace = '',
                is_remote_apply_enabled = True,
                drift_status = 'NEVER_RUN'
            )
        else:
            return EnvironmentApiEnvironment(
                name = '',
                organization_id = '',
                project_id = '',
                user_id = '',
                workspace_name = '',
                requires_approval = True,
                status = 'ABORTING',
                latest_deployment_log_id = '',
                latest_deployment_log = env0_client.models.environment_api/deployment_log.EnvironmentApi.DeploymentLog(
                    id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    type = 'remotePlan', 
                    started_by = '', 
                    queued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    output = null, 
                    error = env0_client.models.error.error(), 
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
                    cost_estimation = env0_client.models.infracost/total_output.Infracost.TotalOutput(
                        version = '', 
                        projects = [
                            env0_client.models.infracost_total_output_projects_inner.Infracost_TotalOutput_projects_inner(
                                path = '', 
                                metadata = null, 
                                past_breakdown = env0_client.models.infracost/output.Infracost.Output(
                                    resources = [
                                        null
                                        ], 
                                    total_hourly_cost = '', 
                                    total_monthly_cost = '', ), 
                                breakdown = env0_client.models.infracost/output.Infracost.Output(
                                    total_hourly_cost = '', 
                                    total_monthly_cost = '', ), 
                                diff = , )
                            ], 
                        time_generated = '', 
                        summary = env0_client.models.infracost_total_output_summary.Infracost_TotalOutput_summary(
                            unsupported_resource_counts = null, ), 
                        resources = [
                            null
                            ], 
                        total_hourly_cost = '', 
                        total_monthly_cost = '', ), 
                    status = 'QUEUED', 
                    blueprint_id = '', 
                    blueprint_name = '', 
                    blueprint_repository = '', 
                    blueprint_revision = '', 
                    blueprint_path = '', 
                    blueprint_type = 'cloudformation', 
                    comment = '', 
                    environment_id = '', 
                    resource_count = 1.337, 
                    resources = [
                        env0_client.models.environment_api/environment_resource.EnvironmentApi.EnvironmentResource(
                            provider = '', 
                            type = '', 
                            name = '', 
                            module_name = '', )
                        ], 
                    started_by_user = env0_client.models.user.User(
                        email = '', 
                        user_id = '', 
                        created_at = '', 
                        app_metadata = env0_client.models.app_metadata.app_metadata(), 
                        picture = '', 
                        name = '', 
                        last_login = '', 
                        given_name = '', 
                        family_name = '', ), 
                    is_scheduled_run = True, 
                    aborted_by = '', 
                    aborted_by_user = env0_client.models.user.User(
                        email = '', 
                        user_id = '', 
                        created_at = '', 
                        app_metadata = env0_client.models.app_metadata.app_metadata(), 
                        picture = '', 
                        name = '', 
                        last_login = '', 
                        given_name = '', 
                        family_name = '', ), 
                    git_user = '', 
                    git_avatar_url = '', 
                    pr_number = '', 
                    trigger_name = 'scheduled', 
                    drift_detected = True, 
                    plan = env0_client.models.environment_api_deployment_log_plan.EnvironmentApi_DeploymentLog_plan(
                        resource_changes = [
                            env0_client.models.deployment_api/plan/plan_resource_change.DeploymentApi.Plan.PlanResourceChange(
                                name = '', 
                                provider_name = '', 
                                type = '', 
                                path = '', 
                                action = 'create', 
                                attributes = [
                                    env0_client.models.deployment_api/plan/attribute_change.DeploymentApi.Plan.AttributeChange(
                                        name = '', 
                                        before = null, 
                                        after = null, )
                                    ], 
                                importing = env0_client.models.deployment_api/plan/resource_import_data.DeploymentApi.Plan.ResourceImportData(
                                    id = '', ), 
                                previous_address = '', )
                            ], 
                        output_changes = [
                            env0_client.models.deployment_api/plan/plan_output_change.DeploymentApi.Plan.PlanOutputChange(
                                name = '', 
                                action = 'create', 
                                attributes = [
                                    env0_client.models.deployment_api/plan/attribute_change.DeploymentApi.Plan.AttributeChange(
                                        name = '', 
                                        before = null, 
                                        after = null, )
                                    ], )
                            ], ), 
                    plan_summary = env0_client.models.deployment_api/plan/plan_summary.DeploymentApi.Plan.PlanSummary(
                        added = 1.337, 
                        changed = 1.337, 
                        destroyed = 1.337, 
                        imported = 1.337, ), 
                    is_skipped_apply = True, 
                    workflow_deployment_id = '', 
                    workflow_file = env0_client.models.environment_api/workflow_environments/workflow_file.EnvironmentApi.WorkflowEnvironments.WorkflowFile(
                        settings = env0_client.models.workflow_file_settings.WorkflowFile_settings(
                            environment_removal_strategy = destroy, ), 
                        environments = {
                            'key' : env0_client.models.environment_api/workflow_environments/workflow_sub_environment.EnvironmentApi.WorkflowEnvironments.WorkflowSubEnvironment(
                                environment_id = '', 
                                to_destroy = True, 
                                is_remote_backend = True, 
                                k8s_namespace = '', 
                                name = '', 
                                template_name = '', 
                                template_id = '', 
                                template_type = 'cloudformation', 
                                revision = '', 
                                workspace = '', 
                                needs = [
                                    ''
                                    ], 
                                terragrunt_working_directory = '', 
                                disabled = null, )
                            }, ), 
                    workflow_deployment_options = env0_client.models.workflow_deployment_options.WorkflowDeploymentOptions(
                        node = '', 
                        operation = 'single-node-deploy', ), 
                    state_version_id = '', 
                    reviewers_users = [
                        env0_client.models.environment_api/reviewer_user.EnvironmentApi.ReviewerUser(
                            user = , 
                            action = 'cancelled', )
                        ], 
                    reviewers = [
                        env0_client.models.environment_api/reviewer.EnvironmentApi.Reviewer(
                            user_id = '', 
                            action = 'cancelled', )
                        ], 
                    reviewed_by = '', 
                    reviewed_by_user = , 
                    targets = [
                        ''
                        ], ),
                lifespan_end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                marked_for_auto_destroy = 0,
                is_archived = True,
                continuous_deployment = True,
                pull_request_plan_deployments = True,
                auto_deploy_on_path_changes_only = True,
                is_remote_backend = True,
                is_locked = True,
                drift_status = 'NEVER_RUN',
        )
        """

    def testEnvironmentApiEnvironment(self):
        """Test EnvironmentApiEnvironment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
