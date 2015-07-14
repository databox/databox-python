#!/usr/bin/env python
from datetime import date, timedelta
from random import randint
from databox import insert_all

"""
This example generates fake temperature KPIs for last 14 days and inserts them.
"""

TOKEN = "adxg1kq5a4g04k0wk0s4wkssow8osw84"

from databox import Client

client = Client(TOKEN)
# client.push('sales.total', 1447.0)
#client.push('orders.total', 32, date='2015-01-01 09:00:00')

# key = 'temp.ljx'
# rows = []
#
# for i, day in enumerate([date.today()-timedelta(days=d) for d in range(0, 14)]):
#     n = 20 + randint(0, 15)
#     rows.append({'key': key, 'value': n, 'date': day.strftime("%Y-%m-%d")})
#
# if insert_all(rows, token=TOKEN):
#     print "Inserted", len(rows), "rows."
#
#


print client.insert_all([
    {'key': 'temp.boston', 'value': 51},
    {'key': 'temp.boston', 'value': 49, 'date': '2015-01-01 17:00:00'},
    {'key': 'sales.total', 'value': 3000, 'attributes': {
        'name': "Oto",
        'price': 199
    }},
])

print client.last_push(3)

