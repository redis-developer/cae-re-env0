# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.api.approval_policy_api import ApprovalPolicyApi


class TestApprovalPolicyApi(unittest.TestCase):
    """ApprovalPolicyApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ApprovalPolicyApi()

    def tearDown(self) -> None:
        pass

    def test_templates_assign_approval_policy(self) -> None:
        """Test case for templates_assign_approval_policy

        Assign Approval Policy To Scope
        """
        pass

    def test_templates_create_approval_policy(self) -> None:
        """Test case for templates_create_approval_policy

        Create Approval Policy
        """
        pass

    def test_templates_delete_approval_policy(self) -> None:
        """Test case for templates_delete_approval_policy

        Delete Approval Policy
        """
        pass

    def test_templates_get_approval_policy_by_name(self) -> None:
        """Test case for templates_get_approval_policy_by_name

        Get Approval Policy By Name
        """
        pass

    def test_templates_get_approval_policy_by_scope(self) -> None:
        """Test case for templates_get_approval_policy_by_scope

        Get Approval Policy Assignments By Scope
        """
        pass

    def test_templates_unassign_approval_policy(self) -> None:
        """Test case for templates_unassign_approval_policy

        Unassign Approval Policy From Scope
        """
        pass

    def test_templates_unassign_approval_policy_by_id(self) -> None:
        """Test case for templates_unassign_approval_policy_by_id

        Unassign Approval Policy by assignment id
        """
        pass

    def test_templates_update_approval_policy(self) -> None:
        """Test case for templates_update_approval_policy

        Update Existing Approval Policy
        """
        pass


if __name__ == '__main__':
    unittest.main()
