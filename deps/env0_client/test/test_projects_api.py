# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.api.projects_api import ProjectsApi


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectsApi()

    def tearDown(self) -> None:
        pass

    def test_environments_get_policies(self) -> None:
        """Test case for environments_get_policies

        Get Policy
        """
        pass

    def test_environments_update_policies(self) -> None:
        """Test case for environments_update_policies

        Update Policy
        """
        pass

    def test_projects_archive(self) -> None:
        """Test case for projects_archive

        Archive a Project
        """
        pass

    def test_projects_create_project(self) -> None:
        """Test case for projects_create_project

        Create a new Project
        """
        pass

    def test_projects_find_by_id(self) -> None:
        """Test case for projects_find_by_id

        Get a Project By ID
        """
        pass

    def test_projects_find_by_organization_id(self) -> None:
        """Test case for projects_find_by_organization_id

        List Projects
        """
        pass

    def test_projects_get_modules_testing_project(self) -> None:
        """Test case for projects_get_modules_testing_project

        Get Modules Testing Project for Organization
        """
        pass

    def test_projects_move_project(self) -> None:
        """Test case for projects_move_project

        Move a project to be a sub-project of another project
        """
        pass

    def test_projects_update(self) -> None:
        """Test case for projects_update

        Update a Project
        """
        pass


if __name__ == '__main__':
    unittest.main()
