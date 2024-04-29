# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.api_key_user import ApiKeyUser

class TestApiKeyUser(unittest.TestCase):
    """ApiKeyUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiKeyUser:
        """Test ApiKeyUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiKeyUser`
        """
        model = ApiKeyUser()
        if include_optional:
            return ApiKeyUser(
                user_id = '',
                username = '',
                created_at = '',
                app_metadata = env0_client.models.app_metadata.app_metadata(),
                name = '',
                nickname = '',
                last_login = '',
                blocked = True,
                identities = [
                    env0_client.models.api_key_user_identity.ApiKeyUserIdentity(
                        user_id = '', 
                        profile_data = env0_client.models.api_key_user_identity_profile_data.ApiKeyUserIdentity_profileData(
                            username = '', 
                            nickname = '', 
                            email = '', ), 
                        blocked = True, )
                    ]
            )
        else:
            return ApiKeyUser(
        )
        """

    def testApiKeyUser(self):
        """Test ApiKeyUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
