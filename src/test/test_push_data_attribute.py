# coding: utf-8

"""
    Static OpenAPI document of Push API resource

    Push API resources Open API documentation

    The version of the OpenAPI document: 0.3.15-sdk.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from databox.models.push_data_attribute import PushDataAttribute

class TestPushDataAttribute(unittest.TestCase):
    """PushDataAttribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PushDataAttribute:
        """Test PushDataAttribute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PushDataAttribute`
        """
        model = PushDataAttribute()
        if include_optional:
            return PushDataAttribute(
                key = '',
                value = ''
            )
        else:
            return PushDataAttribute(
        )
        """

    def testPushDataAttribute(self):
        """Test PushDataAttribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
