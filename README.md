# Databox bindings for Python

[![Build Status](https://travis-ci.org/databox/databox-python.svg?branch=master)](https://travis-ci.org/databox/databox-python)

## Setup

You can install this package by cloning this directory and running:

```bash
python setup.py install
```

You can also add following line to `requirements.txt` and get latest master:

````
git+https://github.com/databox/databox-python.git
````

And run `pip install --upgrade -r requirements.txt`.

## Getting Databox access tokens

When in Databox Designer go to Account > Access tokens, then either create a new token or get already existing one.

## Using the Databox Python library

To use databox-python libary you have to pass access token to client. You can do this when initialising `Client` or by setting `DATABOX_PUSH_TOKEN` environment variable.

Using `Client` and `push` to push data directly:

```python
from databox import Client

client = Client('<access token>')
client.push('sales.total', 1447.0)
client.push('orders.total', 32, date='2015-01-01 09:00:00')
client.push('orders.total', 34, attributes={
  'something': 1447,
})

```

Inserting multiple matrices with one `insert_all`:

```python
client.insert_all([
    {'key': 'temp.boston', 'value': 51},
    {'key': 'temp.boston', 'value': 49, 'date': '2015-01-01 17:00:00'},
    {'key': 'sales.total', 'value': 3000},
])
```

Retriving information from last push with `last_push`:
```python
print client.last_push()
```

Libary can be used with shorthand methods:


```python
from databox import push, insert_all, last_push

push('sales.total', 1448.9)
print last_push(token)
```

## Development and testing

Using virtualenv:

    mkvirtualenv --no-site-packages databox-python
    workon databox-python
    pip install --upgrade -r requirements.txt

Running test suite with unittest:

    python -munittest discover -p -t . 'test*' -v

You can also check working [example.py](example.py).

## Examples and use-cases
- [Simple Python example](example.py)
- [Advanced Python example with MySQL](https://github.com/databox/databox-python-sql)
- For general documentation and examples check [developers.databox.com](https://developers.databox.com)

## Authors and contributions

- [Vlada Petrović](https://github.com/VladaPetrovic)
- [Oto Brglez](https://github.com/otobrglez)

## Licence

- [MIT](LICENSE.txt)
