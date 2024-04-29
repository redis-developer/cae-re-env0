# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.configuration_api_create_configuration_set_request_body import ConfigurationApiCreateConfigurationSetRequestBody

class TestConfigurationApiCreateConfigurationSetRequestBody(unittest.TestCase):
    """ConfigurationApiCreateConfigurationSetRequestBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigurationApiCreateConfigurationSetRequestBody:
        """Test ConfigurationApiCreateConfigurationSetRequestBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigurationApiCreateConfigurationSetRequestBody`
        """
        model = ConfigurationApiCreateConfigurationSetRequestBody()
        if include_optional:
            return ConfigurationApiCreateConfigurationSetRequestBody(
                scope = 'project',
                scope_id = '',
                configuration_properties = [
                    env0_client.models.configuration_property_request.ConfigurationPropertyRequest(
                        name = '', 
                        value = '', 
                        id = '', 
                        is_sensitive = True, 
                        is_readonly = True, 
                        is_required = True, 
                        regex = '', 
                        scope_id = '', 
                        scope = 'WORKFLOW', 
                        type = 0, 
                        to_delete = True, 
                        project_id = '', 
                        organization_id = '', 
                        schema = env0_client.models.partial_json_schema7.PartialJSONSchema7(
                            enum = [
                                ''
                                ], 
                            format = 'JSON', ), 
                        description = '', )
                    ],
                name = '',
                description = ''
            )
        else:
            return ConfigurationApiCreateConfigurationSetRequestBody(
                scope = 'project',
                scope_id = '',
                name = '',
        )
        """

    def testConfigurationApiCreateConfigurationSetRequestBody(self):
        """Test ConfigurationApiCreateConfigurationSetRequestBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
