# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.cost_api_project_costs_credentials import CostApiProjectCostsCredentials

class TestCostApiProjectCostsCredentials(unittest.TestCase):
    """CostApiProjectCostsCredentials unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CostApiProjectCostsCredentials:
        """Test CostApiProjectCostsCredentials
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CostApiProjectCostsCredentials`
        """
        model = CostApiProjectCostsCredentials()
        if include_optional:
            return CostApiProjectCostsCredentials(
                project_id = '',
                credentials_id = '',
                credentials_type = 'GCP_SERVICE_ACCOUNT_FOR_DEPLOYMENT'
            )
        else:
            return CostApiProjectCostsCredentials(
                project_id = '',
                credentials_id = '',
        )
        """

    def testCostApiProjectCostsCredentials(self):
        """Test CostApiProjectCostsCredentials"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
