import json
import requests
from requests.auth import HTTPBasicAuth

class PushClient(object):
    metrics = {"data": []}

    def __init__(self, api_key):
        self.api_key = api_key
        self.host = "https://push2new.databox.com"

    def add(self, value, metric_key, date=None):
        item = {}

        # Add date if provided
        if date is not None:
            item["date"] = date

        # Add value
        item["$" + metric_key] = value

        # Add to metrics
        self.metrics["data"].append(item)

    def addWithAttribute(self, value, metric_key, attribute_value, attribute_name, date=None):
        item = {}

        # Add date if provided
        if date is not None:
            item["date"] = date

        # Add value
        item["$" + metric_key] = value

        # Add attribute
        item[attribute_name] = attribute_value

        # Add to metrics
        self.metrics["data"].append(item)

    def send(self):
        payload = json.dumps(self.metrics)
        response = requests.post(
            self.host,
            auth = HTTPBasicAuth(self.api_key, ""),
            headers = {"Content-Type": "application/json"},
            data = payload
        )

        return response.json()

    def lastPush(self):
        response = requests.post(
            self.host + "/lastpushes/1",
            auth = HTTPBasicAuth(self.api_key, ""),
            headers = {"Content-Type": "application/json"}
        )

        return response.json()
