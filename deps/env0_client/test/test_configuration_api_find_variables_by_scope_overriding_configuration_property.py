# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.configuration_api_find_variables_by_scope_overriding_configuration_property import ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty

class TestConfigurationApiFindVariablesByScopeOverridingConfigurationProperty(unittest.TestCase):
    """ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty:
        """Test ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty`
        """
        model = ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty()
        if include_optional:
            return ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty(
                overwrites = None,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                value = '',
                id = None,
                user_id = '',
                is_sensitive = True,
                is_readonly = True,
                is_required = True,
                regex = '',
                scope_id = None,
                scope = 'WORKFLOW',
                type = 0,
                to_delete = True,
                project_id = '',
                organization_id = '',
                var_schema = env0_client.models.partial_json_schema7.PartialJSONSchema7(
                    type = '', 
                    enum = [
                        ''
                        ], 
                    format = 'JSON', ),
                description = ''
            )
        else:
            return ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty(
                overwrites = None,
                name = '',
                scope = 'WORKFLOW',
                type = 0,
                organization_id = '',
        )
        """

    def testConfigurationApiFindVariablesByScopeOverridingConfigurationProperty(self):
        """Test ConfigurationApiFindVariablesByScopeOverridingConfigurationProperty"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
