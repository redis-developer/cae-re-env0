# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.scheduling_api_scheduled_action import SchedulingApiScheduledAction

class TestSchedulingApiScheduledAction(unittest.TestCase):
    """SchedulingApiScheduledAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SchedulingApiScheduledAction:
        """Test SchedulingApiScheduledAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SchedulingApiScheduledAction`
        """
        model = SchedulingApiScheduledAction()
        if include_optional:
            return SchedulingApiScheduledAction(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                environment_id = '',
                project_id = '',
                organization_id = '',
                cron = '',
                next_schedule = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                enabled = True
            )
        else:
            return SchedulingApiScheduledAction(
                environment_id = '',
                project_id = '',
                organization_id = '',
                cron = '',
                enabled = True,
        )
        """

    def testSchedulingApiScheduledAction(self):
        """Test SchedulingApiScheduledAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()