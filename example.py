#!/usr/bin/env python
from datetime import date, timedelta
from random import randint
from databox import insert_all

"""
This example generates fake temperature KPIs for last 14 days and inserts them.
"""

TOKEN = "adxg1kq5a4g04k0wk0s4wkssow8osw84"

key = 'temp.ljx'
rows = []

for i, day in enumerate([date.today()-timedelta(days=d) for d in range(0, 14)]):
    n = 20 + randint(0, 15)
    rows.append({'key': key, 'value': n, 'date': day.strftime("%Y-%m-%d")})

if insert_all(rows, token=TOKEN):
    print "Inserted", len(rows), "rows."