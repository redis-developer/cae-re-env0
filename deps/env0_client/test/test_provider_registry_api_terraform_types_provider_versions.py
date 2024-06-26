# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.provider_registry_api_terraform_types_provider_versions import ProviderRegistryApiTerraformTypesProviderVersions

class TestProviderRegistryApiTerraformTypesProviderVersions(unittest.TestCase):
    """ProviderRegistryApiTerraformTypesProviderVersions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProviderRegistryApiTerraformTypesProviderVersions:
        """Test ProviderRegistryApiTerraformTypesProviderVersions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProviderRegistryApiTerraformTypesProviderVersions`
        """
        model = ProviderRegistryApiTerraformTypesProviderVersions()
        if include_optional:
            return ProviderRegistryApiTerraformTypesProviderVersions(
                versions = [
                    env0_client.models.provider_registry_api/terraform_types/version.ProviderRegistryApi.TerraformTypes.Version(
                        version = '', 
                        platforms = [
                            env0_client.models.provider_registry_api/terraform_types/platform.ProviderRegistryApi.TerraformTypes.Platform(
                                os = '', 
                                arch = '', )
                            ], )
                    ]
            )
        else:
            return ProviderRegistryApiTerraformTypesProviderVersions(
                versions = [
                    env0_client.models.provider_registry_api/terraform_types/version.ProviderRegistryApi.TerraformTypes.Version(
                        version = '', 
                        platforms = [
                            env0_client.models.provider_registry_api/terraform_types/platform.ProviderRegistryApi.TerraformTypes.Platform(
                                os = '', 
                                arch = '', )
                            ], )
                    ],
        )
        """

    def testProviderRegistryApiTerraformTypesProviderVersions(self):
        """Test ProviderRegistryApiTerraformTypesProviderVersions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
