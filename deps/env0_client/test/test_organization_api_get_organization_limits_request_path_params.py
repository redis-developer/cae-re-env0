# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.organization_api_get_organization_limits_request_path_params import OrganizationApiGetOrganizationLimitsRequestPathParams

class TestOrganizationApiGetOrganizationLimitsRequestPathParams(unittest.TestCase):
    """OrganizationApiGetOrganizationLimitsRequestPathParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationApiGetOrganizationLimitsRequestPathParams:
        """Test OrganizationApiGetOrganizationLimitsRequestPathParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationApiGetOrganizationLimitsRequestPathParams`
        """
        model = OrganizationApiGetOrganizationLimitsRequestPathParams()
        if include_optional:
            return OrganizationApiGetOrganizationLimitsRequestPathParams(
                id = ''
            )
        else:
            return OrganizationApiGetOrganizationLimitsRequestPathParams(
                id = '',
        )
        """

    def testOrganizationApiGetOrganizationLimitsRequestPathParams(self):
        """Test OrganizationApiGetOrganizationLimitsRequestPathParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
