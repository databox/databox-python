import databox
from databox.rest import ApiException
from pprint import pprint

# Configuration setup for the Databox API client
# The API token is used as the username for authentication
# It's recommended to store your API token securely, e.g., in an environment variable
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
    except ApiException as e:
        # Handle exceptions that occur during the API call, such as invalid data or authentication issues
        pprint("API Exception occurred: %s\n" % e)
    except Exception as e:
        # Handle any other unexpected exceptions
        pprint("An unexpected error occurred: %s\n" % e)
    