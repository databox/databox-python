import databox
from databox.rest import ApiException
from pprint import pprint

configuration = databox.Configuration(
    host = "https://push.databox.com",
    username = "<YOUR-CUSTOM-DATA-TOKEN>",
    password = ""
)

with databox.ApiClient(configuration, "Accept", "application/vnd.databox.v2+json",) as api_client:    
    api_instance = databox.DefaultApi(api_client)    
    push_data = [{"key": "sales2", "value": 100, "unit": "USD", "date": "2021-01-01T00:00:00Z" }]
    try:
        api_instance.data_post(push_data=push_data)        
    except Exception as e:
        print("Exception: %s\n" % e)
    