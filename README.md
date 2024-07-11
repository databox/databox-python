# databox
Push API resources Open API documentation

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.4.0
- Package version: 2.3.0
- Generator version: 7.6.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import databox
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import databox
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import databox
from databox.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://push.databox.com
# See configuration.py for a list of all supported configuration parameters.
configuration = databox.Configuration(
    host = "https://push.databox.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = databox.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)


# Enter a context with an instance of the API client
with databox.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databox.DefaultApi(api_client)

    try:
        api_instance.data_delete()
    except ApiException as e:
        print("Exception when calling DefaultApi->data_delete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://push.databox.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**data_delete**](docs/DefaultApi.md#data_delete) | **DELETE** /data | 
*DefaultApi* | [**data_metric_key_delete**](docs/DefaultApi.md#data_metric_key_delete) | **DELETE** /data/{metricKey} | 
*DefaultApi* | [**data_post**](docs/DefaultApi.md#data_post) | **POST** /data | 
*DefaultApi* | [**metrickeys_get**](docs/DefaultApi.md#metrickeys_get) | **GET** /metrickeys | 
*DefaultApi* | [**metrickeys_post**](docs/DefaultApi.md#metrickeys_post) | **POST** /metrickeys | 
*DefaultApi* | [**ping_get**](docs/DefaultApi.md#ping_get) | **GET** /ping | 


## Documentation For Models

 - [ApiResponse](docs/ApiResponse.md)
 - [PushData](docs/PushData.md)
 - [PushDataAttribute](docs/PushDataAttribute.md)
 - [State](docs/State.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="basicAuth"></a>
### basicAuth

- **Type**: HTTP basic authentication


## Author




