# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.configuration_api_update_configuration_set_request_path_params import ConfigurationApiUpdateConfigurationSetRequestPathParams

class TestConfigurationApiUpdateConfigurationSetRequestPathParams(unittest.TestCase):
    """ConfigurationApiUpdateConfigurationSetRequestPathParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigurationApiUpdateConfigurationSetRequestPathParams:
        """Test ConfigurationApiUpdateConfigurationSetRequestPathParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigurationApiUpdateConfigurationSetRequestPathParams`
        """
        model = ConfigurationApiUpdateConfigurationSetRequestPathParams()
        if include_optional:
            return ConfigurationApiUpdateConfigurationSetRequestPathParams(
                id = ''
            )
        else:
            return ConfigurationApiUpdateConfigurationSetRequestPathParams(
                id = '',
        )
        """

    def testConfigurationApiUpdateConfigurationSetRequestPathParams(self):
        """Test ConfigurationApiUpdateConfigurationSetRequestPathParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
