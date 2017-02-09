import requests
from requests.auth import HTTPBasicAuth
from os import getenv
from json import dumps as json_dumps

__version__ = "2.1.0"


class Client(object):
    push_token = None
    push_host = 'https://push.databox.com'
    last_push_content = None

    class MissingToken(Exception):
        pass

    class KPIValidationException(Exception):
        pass

    def __init__(self, token=None):
        self.push_token = token
        if self.push_token is None:
            self.push_token = getenv('DATABOX_PUSH_TOKEN', None)

        if self.push_token is None:
            raise self.MissingToken('Push token is missing!')

    def process_kpi(self, **args):
        key = args.get('key', None)
        if key is None:
            raise self.KPIValidationException('Missing "key"')

        value = args.get('value', None)
        if value is None:
            raise self.KPIValidationException('Missing "value"')

        item = {("$%s" % args['key']): args['value']}

        date = args.get('date', None)
        if date is not None:
            item['date'] = date

        unit = args.get('unit', None)
        if unit is not None:
            item['unit'] = unit

        attributes = args.get('attributes', None)
        if attributes is not None:
            item.update(attributes)

        return item

    def _push_json(self, data=None, path="/"):
        if data is not None:
            data = json_dumps(data)

        response = requests.post(
                self.push_host + path,
                auth=HTTPBasicAuth(self.push_token, ''),
                headers={
                    'Content-Type': 'application/json',
                    'User-Agent': 'databox-python/' + __version__,
                    'Accept': 'application/vnd.databox.v' + __version__.split('.')[0] + '+json'
                },
                data=data
        )

        return response.json()

    def _get_json(self, path):
        response = requests.get(
                self.push_host + path,
                auth=HTTPBasicAuth(self.push_token, ''),
                headers={
                    'Content-Type': 'application/json',
                    'User-Agent': 'databox-python/' + __version__,
                    'Accept': 'application/vnd.databox.v' + __version__.split('.')[0] + '+json'
                }
        )

        return response.json()

    def _delete_json(self, path):
        response = requests.delete(
                self.push_host + path,
                auth=HTTPBasicAuth(self.push_token, ''),
                headers={
                    'Content-Type': 'application/json',
                    'User-Agent': 'databox-python/' + __version__,
                    'Accept': 'application/vnd.databox.v' + __version__.split('.')[0] + '+json'
                }
        )

        return response.json()

    def push(self, key, value, date=None, attributes=None, unit=None):
        self.last_push_content = self._push_json({
            'data': [self.process_kpi(
                    key=key,
                    value=value,
                    date=date,
                    unit=unit,
                    attributes=attributes
            )]
        })

        return self.last_push_content['id']

    def insert_all(self, rows):
        self.last_push_content = self._push_json({
            'data': [self.process_kpi(**row) for row in rows]
        })
        return self.last_push_content['id']

    def last_push(self, number=1):
        return self._get_json(path='/lastpushes?limit={n}'.format(**{'n': number}))

    def get_push(self, sha):
        return self._get_json(path='/lastpushes?id=' + sha)

    def metrics(self):
        return self._get_json(path='/metrickeys')

    def purge(self):
        return self._delete_json(path='/data')


def push(key, value, date=None, attributes=None, unit=None, token=None):
    return Client(token).push(key, value, date, attributes, unit)


def insert_all(rows=[], token=None):
    return Client(token).insert_all(rows)


def last_push(token=None):
    return Client(token).last_push()
