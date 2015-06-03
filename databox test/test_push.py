import unittest
from databox import *

class TestPush(unittest.TestCase):
    def setUp(self):
        self.databox_push_token = "adxg1kq5a4g04k0wk0s4wkssow8osw84"
        self.client = Client(self.databox_push_token)

    def test_setup(self):
        self.client.push("oto", 10.0)
        push("aaa", 22)