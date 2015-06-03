# Databox bindings for Python

## Setup

You can install this package by cloning this directory and running:

   ```$ python setup.py install```

## Getting Databox access tokens

When in Databox Designer go to Account > Access tokens, then either create a new token or get already existing one.

## Using the Databox Python library

    from databox import PushClient
    
    # instantiate PushClient
    client = PushClient('<access token>')
    
    # push metric "answer1" with value 42 for today
    client.add(42, "answer1")
    
    # push metric "answer1" with value 42 for any other day
    client.add(42, "answer1", "2015-05-01 10:10:10")
    
    # send to Databox
    print client.send()
    
    # get last push
    print client.lastPush()


Check working sample in [sample1.py](/sample1.py) file.

## Development

    mkvirtualenv --no-site-packages databox-python
    workon databox-python
    pip install --upgrade -r requirements.txt

## Authors and contributions

- [Vlada Petrović](https://github.com/VladaPetrovic)
- [Oto Brglez](https://github.com/otobrglez)

## Licence

- [MIT](LICENSE.txt)