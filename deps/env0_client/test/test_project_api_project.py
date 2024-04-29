# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.project_api_project import ProjectApiProject

class TestProjectApiProject(unittest.TestCase):
    """ProjectApiProject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectApiProject:
        """Test ProjectApiProject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectApiProject`
        """
        model = ProjectApiProject()
        if include_optional:
            return ProjectApiProject(
                name = '',
                description = '',
                organization_id = '',
                parent_project_id = '',
                id = '',
                created_by = '',
                created_by_user = env0_client.models.user.User(
                    email = '', 
                    user_id = '', 
                    created_at = '', 
                    app_metadata = env0_client.models.app_metadata.app_metadata(), 
                    picture = '', 
                    name = '', 
                    last_login = '', 
                    given_name = '', 
                    family_name = '', ),
                is_archived = True,
                hierarchy = ''
            )
        else:
            return ProjectApiProject(
                name = '',
                organization_id = '',
                created_by = '',
                hierarchy = '',
        )
        """

    def testProjectApiProject(self):
        """Test ProjectApiProject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
