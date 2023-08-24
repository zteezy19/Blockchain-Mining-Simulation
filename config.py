from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconfig = PNConfiguration()
pnconfig.publish_key = 'pub-c-ab8c9942-8f70-4b75-bef7-50aefc226142'
pnconfig.subscribe_key = 'sub-c-d53102f0-0bb3-4329-a2a7-79d97501e42e'
pnconfig.ssl = True

# Dynamic UUID assignment based on the script
import sys
if 'alice.py' in sys.argv[0]:
    pnconfig.uuid = "Alice's UUID"
elif 'bob.py' in sys.argv[0]:
    pnconfig.uuid = "Bob's UUID"
else:
    pnconfig.uuid = "Unknown UUID"

pubnub = PubNub(pnconfig)
