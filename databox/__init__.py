import requests
from os import getenv


class SingleClient(object):
    _token = None

    class MissingToken(Exception):
        pass

    @property
    def token(self):
        if self._token is None:
            self._token = getenv("DATABOX_PUSH_TOKEN", None)

        if self._token is None:
            raise SingleClient.MissingToken("Missing Databox push token")

        return self._token

    def __init__(self, token=None):
        if self._token is None and token is not None:
            self._token = token


    def push(self, key, value, date=None):
        print "--- push --- ", self.token
        pass



class Client(object):
    _instance = None
    client_instance = None

    def __init__(self, token=None):
        self.client_instance = SingleClient(token)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Client, cls). \
                __new__(cls, *args, **kwargs)
        return cls._instance

    @property
    def client(self):
        return self.client_instance

    def push(self, key, value, date=None):
        return self.client.push(key, value, date)


def push(key, value, date=None, token=None):
    return Client().push(key, value, date)