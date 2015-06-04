import unittest
from databox import *
from pprint import pprint as pp


def mock_push_json(data={}):
    return True


class TestPush(unittest.TestCase):
    def setUp(self):
        self.databox_push_token = "adxg1kq5a4g04k0wk0s4wkssow8osw84"
        self.client = Client(self.databox_push_token)
        self.client._push_json = mock_push_json

    def test_push(self):
        assert self.client.push("templj", 10.0) is True
        assert self.client.push("templj", 12.0, date="2015-01-01 09:00:00") is True

    def test_push_validation(self):
        self.assertRaises(
            Client.KPIValidationException,
            lambda: self.client.push(None, None)
        )

    def test_insert_all(self):
        assert self.client.insert_all([
            {'key': 'templj', 'value': 83.3},
            {'key': 'templj', 'value': 83.3, 'date': "2015-01-01 09:00:00"},
            {'key': 'templj', 'value': 12.3},
        ]) is True

        self.assertRaises(
            Client.KPIValidationException,
            lambda: self.client.insert_all([
                {'value': 83.3},
                {'key': 'templj', 'value': 83.3, 'date': "2015-01-01 09:00:00"},
                {'key': 'templj', 'value': 12.3},
            ])
        )

    def test_short(self):
        assert push("templj", 22, token=self.databox_push_token) is True

        assert insert_all([
            {'key': 'templj', 'value': 83.3},
        ], token=self.databox_push_token) is True