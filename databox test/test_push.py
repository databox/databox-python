import unittest
from databox import *
from pprint import pprint as pp
from os import getenv

RESPONSE_ID = '2837643'

def mock_push_json(data=None, path='/'):
    return {'id': RESPONSE_ID}


class TestPush(unittest.TestCase):
    def setUp(self):
        self.databox_push_token = getenv("DATABOX_PUSH_TOKEN") or "your_token_1234321"
        self.client = Client(self.databox_push_token)

        self.original_push_json = self.client._push_json
        self.client._push_json = mock_push_json


    def test_push(self):
        assert self.client.push("templj", 10.0) is RESPONSE_ID
        assert self.client.push("templj", 12.0, date="2015-01-01 09:00:00") is RESPONSE_ID


    def test_push_with_attributes(self):
        assert self.client.push("meta", 100, attributes={
            'n': 100
        }) is RESPONSE_ID


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
        ]) is RESPONSE_ID

        self.assertRaises(
            Client.KPIValidationException,
            lambda: self.client.insert_all([
                {'value': 83.3},
                {'key': 'templj', 'value': 83.3, 'date': "2015-01-01 09:00:00"},
                {'key': 'templj', 'value': 12.3},
            ])
        )


    def test_last_push(self):
        self.client._get_json = lambda path='/': {
            'err': [],
            'no_err': 0
        }

        assert self.client.last_push()['err'] == []


    def test_last_push_with_number(self):
        self.client._get_json = lambda data=None, path='/': path
        assert self.client.last_push(3) == '/lastpushes?limit=3'
