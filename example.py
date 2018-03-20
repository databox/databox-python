#!/usr/bin/env python
from datetime import date, timedelta
from random import randint
from os import getenv

"""
This example generates fake temperature KPIs for last 14 days and inserts them.
"""

TOKEN = getenv("DATABOX_PUSH_TOKEN") or "your_token_1234321"

from databox import Client

client = Client(TOKEN)

push = client.push('transaction', 1447.4)

pushId = client.insert_all([
    {'key': 'temp.boston', 'value': 51},
    {'key': 'temp.boston', 'value': 49, 'date': '2015-01-01 17:00:00'},
    {'key': 'sales.total', 'value': 3000, 'attributes': {
        'name': "Oto",
        'price': 199
    }},
    {'key': 'transaction', 'value': 45.6, 'unit': 'USD'}
])

print ("Push id: ", pushId)

# lastPushes = client.last_push(3)
# print lastPushes

print (client.get_push(pushId))
print (client.metrics())
print (client.purge())
