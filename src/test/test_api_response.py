# coding: utf-8

"""
    Static OpenAPI document of Push API resource

    Push API resources Open API documentation asdas

    The version of the OpenAPI document: 0.4.4-alpha.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from databox.models.api_response import ApiResponse

class TestApiResponse(unittest.TestCase):
    """ApiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiResponse:
        """Test ApiResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiResponse`
        """
        model = ApiResponse()
        if include_optional:
            return ApiResponse(
                status = '',
                message = ''
            )
        else:
            return ApiResponse(
        )
        """

    def testApiResponse(self):
        """Test ApiResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
