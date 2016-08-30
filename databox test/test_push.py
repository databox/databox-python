import unittest
from databox import *
from pprint import pprint as pp
from os import getenv


def mock_push_json(data=None, path='/'):
    return {'id': '2837643'}


class TestPush(unittest.TestCase):
    def setUp(self):
        self.databox_push_token = getenv("DATABOX_PUSH_TOKEN") or "adxg1kq5a4g04k0wk0s4wkssow8osw84"
        self.client = Client(self.databox_push_token)

        self.original_push_json = self.client._push_json
        self.client._push_json = mock_push_json

    def test_push(self):
        assert self.client.push("templj", 10.0) is True
        assert self.client.push("templj", 12.0, date="2015-01-01 09:00:00") is True

    def test_push_with_attributes(self):
        self.client._push_json = lambda data=None, path='/': dict({
                                                                      'status': 'ok',
                                                                  }.items() + data.items())

        push = self.client.push("meta", 100, attributes={
            'n': 100
        })

        assert self.client.last_push_content['data'][0]['$meta'] == 100
        assert self.client.last_push_content['data'][0]['n'] == 100


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


    def test_last_push(self):
        self.client._get_json = lambda path='/': {
            'err': [],
            'no_err': 0
        }

        assert self.client.last_push()['err'] == []


    def test_last_push_with_number(self):
        self.client._get_json = lambda data=None, path='/': path
        assert self.client.last_push(3) == '/lastpushes?limit=3'


    def test_short(self):
        Client._push_json = mock_push_json

        assert push("templj", 22, token=self.databox_push_token) is True

        assert insert_all([
                              {
                                  'key': 'templj',
                                  'value': 83.3
                              },
                          ], token=self.databox_push_token) is True

        Client._get_json = lambda number=None, path='/': {
            'err': [],
            'no_err': 0
        }

        assert last_push(token=self.databox_push_token)['err'] == []
