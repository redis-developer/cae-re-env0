# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.api.modules_api import ModulesApi


class TestModulesApi(unittest.TestCase):
    """ModulesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ModulesApi()

    def tearDown(self) -> None:
        pass

    def test_modules_get_module_test_run_by_id(self) -> None:
        """Test case for modules_get_module_test_run_by_id

        Get Module Test Run by ID
        """
        pass

    def test_modules_get_module_test_runs(self) -> None:
        """Test case for modules_get_module_test_runs

        List Module Test Runs
        """
        pass

    def test_modules_trigger_module_test_run(self) -> None:
        """Test case for modules_trigger_module_test_run

        Trigger Module Test Run
        """
        pass

    def test_templates_create_module(self) -> None:
        """Test case for templates_create_module

        Create module
        """
        pass

    def test_templates_delete_module_by_id(self) -> None:
        """Test case for templates_delete_module_by_id

        Delete module
        """
        pass

    def test_templates_find_all_modules(self) -> None:
        """Test case for templates_find_all_modules

        List Modules
        """
        pass

    def test_templates_get_module(self) -> None:
        """Test case for templates_get_module

        Get module
        """
        pass

    def test_templates_get_module_readme(self) -> None:
        """Test case for templates_get_module_readme

        Get Module README
        """
        pass

    def test_templates_get_module_versions(self) -> None:
        """Test case for templates_get_module_versions

        List Module Versions
        """
        pass

    def test_templates_update_module(self) -> None:
        """Test case for templates_update_module

        Update module
        """
        pass


if __name__ == '__main__':
    unittest.main()
