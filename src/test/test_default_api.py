# coding: utf-8

"""
    Static OpenAPI document of Push API resource

    Push API resources Open API documentation

    The version of the OpenAPI document: 0.4.4-alpha.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from databox.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_data_delete(self) -> None:
        """Test case for data_delete

        """
        pass

    def test_data_metric_key_delete(self) -> None:
        """Test case for data_metric_key_delete

        """
        pass

    def test_data_post(self) -> None:
        """Test case for data_post

        """
        pass

    def test_metrickeys_get(self) -> None:
        """Test case for metrickeys_get

        """
        pass

    def test_metrickeys_post(self) -> None:
        """Test case for metrickeys_post

        """
        pass

    def test_ping_get(self) -> None:
        """Test case for ping_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
