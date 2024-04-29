# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.bulk_operations_api_base_payload import BulkOperationsApiBasePayload

class TestBulkOperationsApiBasePayload(unittest.TestCase):
    """BulkOperationsApiBasePayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BulkOperationsApiBasePayload:
        """Test BulkOperationsApiBasePayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BulkOperationsApiBasePayload`
        """
        model = BulkOperationsApiBasePayload()
        if include_optional:
            return BulkOperationsApiBasePayload(
                environment_ids = [
                    ''
                    ],
                organization_id = ''
            )
        else:
            return BulkOperationsApiBasePayload(
                environment_ids = [
                    ''
                    ],
                organization_id = '',
        )
        """

    def testBulkOperationsApiBasePayload(self):
        """Test BulkOperationsApiBasePayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
