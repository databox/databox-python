# coding: utf-8

"""
    Static OpenAPI document of Push API resource

    Push API resources Open API documentation asdas

    The version of the OpenAPI document: 0.4.4-alpha.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from databox.models.push_data import PushData

class TestPushData(unittest.TestCase):
    """PushData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PushData:
        """Test PushData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PushData`
        """
        model = PushData()
        if include_optional:
            return PushData(
                attributes = [
                    databox.models.push_data_attribute.PushDataAttribute(
                        key = '', 
                        value = '', )
                    ],
                var_date = '',
                key = '',
                period_from = '',
                period_to = '',
                unit = '',
                value = 1.337
            )
        else:
            return PushData(
        )
        """

    def testPushData(self):
        """Test PushData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
