import json
from databox.client import PushClient

# Create Push object
pc = PushClient("339fb7fcxssg0sk48wocogo8wsck8408")

# Add metrics
pc.add(576.45, "sales.total", "2015-05-10 09:00:00")
pc.add(42, "orders.total", "2015-05-10 09:00:00")

# Send to Databox
response = pc.send()

if response["status"] == "ok":
    print "Successfully pushed metrics to Databox!"
else:
    # get error info
    lastPush = pc.lastPush()
    print json.dumps(lastPush, indent=4)
