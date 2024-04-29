# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.api.teams_api import TeamsApi


class TestTeamsApi(unittest.TestCase):
    """TeamsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TeamsApi()

    def tearDown(self) -> None:
        pass

    def test_teams_create_team(self) -> None:
        """Test case for teams_create_team

        Create Team
        """
        pass

    def test_teams_delete_team(self) -> None:
        """Test case for teams_delete_team

        Delete Team
        """
        pass

    def test_teams_deprecated_create_or_update_single_assignment(self) -> None:
        """Test case for teams_deprecated_create_or_update_single_assignment

        Create or Update a single Team to Project Assignment
        """
        pass

    def test_teams_deprecated_delete_single_assignment(self) -> None:
        """Test case for teams_deprecated_delete_single_assignment

        Delete a single Team to Project Assignment
        """
        pass

    def test_teams_deprecated_get_assignments(self) -> None:
        """Test case for teams_deprecated_get_assignments

        List Project Teams Permissions
        """
        pass

    def test_teams_deprecated_update_assignments(self) -> None:
        """Test case for teams_deprecated_update_assignments

        Update Teams Assignments
        """
        pass

    def test_teams_get_team(self) -> None:
        """Test case for teams_get_team

        Get Team
        """
        pass

    def test_teams_get_teams(self) -> None:
        """Test case for teams_get_teams

        List Teams
        """
        pass

    def test_teams_update_team(self) -> None:
        """Test case for teams_update_team

        Update Team
        """
        pass


if __name__ == '__main__':
    unittest.main()