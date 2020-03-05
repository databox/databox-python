import unittest
from databox import Client
from os import getenv

RESPONSE_ID = '2837643'


def mock_push_json(data=None, path='/'):
    return {'id': RESPONSE_ID}


class TestPush(unittest.TestCase):
    def setUp(self):
        # Configuration of tokens in real world - use your own!
        self.databox_push_token = getenv("DATABOX_PUSH_TOKEN") or "your_token"
        self.client = Client(self.databox_push_token)

        # Mocking the original methods with fake ones
        self.original_push_json = self.client._push_json
        self.client._push_json = mock_push_json

    def test_push(self):
        assert self.client.push("temp", 10.0) is RESPONSE_ID
        assert self.client.push("temp", 12.0, date="2015-01-01 09:00:00") is RESPONSE_ID

    def test_push_with_attributes(self):
        assert self.client.push("meta", 100, attributes={'n': 100}) is RESPONSE_ID

    def test_push_validation(self):
        self.assertRaises(
            Client.KPIValidationException,
            lambda: self.client.push(None, None)
        )

    def test_insert_all(self):
        assert self.client.insert_all([
            {'key': 'temp', 'value': 83.3},
            {'key': 'temp', 'value': 83.3, 'date': "2015-01-01 09:00:00"},
            {'key': 'temp', 'value': 12.3},
        ]) is RESPONSE_ID

        values = [{'value': 83.3},
                  {'key': 'temp', 'value': 83.3, 'date': "2015-01-01 09:00:00"},
                  {'key': 'temp', 'value': 12.3}]

        self.assertRaises(Client.KPIValidationException, lambda: self.client.insert_all(values))

    def test_last_push(self):
        self.client._get_json = lambda path='/': {
            'err': [],
            'no_err': 0}

        assert self.client.last_push()['err'] == []

    def test_last_push_with_number(self):
        self.client._get_json = lambda data=None, path='/': path
        assert self.client.last_push(3) == '/lastpushes?limit=3'
