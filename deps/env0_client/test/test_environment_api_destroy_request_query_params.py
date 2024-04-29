# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.environment_api_destroy_request_query_params import EnvironmentApiDestroyRequestQueryParams

class TestEnvironmentApiDestroyRequestQueryParams(unittest.TestCase):
    """EnvironmentApiDestroyRequestQueryParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnvironmentApiDestroyRequestQueryParams:
        """Test EnvironmentApiDestroyRequestQueryParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnvironmentApiDestroyRequestQueryParams`
        """
        model = EnvironmentApiDestroyRequestQueryParams()
        if include_optional:
            return EnvironmentApiDestroyRequestQueryParams(
                checkout_updated_code = 'false',
                is_scheduled_run = 'false',
                skip_state_refresh = 'false',
                revision = '',
                requires_approval = 'false'
            )
        else:
            return EnvironmentApiDestroyRequestQueryParams(
        )
        """

    def testEnvironmentApiDestroyRequestQueryParams(self):
        """Test EnvironmentApiDestroyRequestQueryParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
