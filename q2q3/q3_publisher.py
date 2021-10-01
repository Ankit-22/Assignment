import redis
import random
import sys
import time

# Create a Redis Connection
r = redis.Redis(host='localhost', port='6379')

# We aren't stopping until we do..
while True:

    # Publish our random number payload to the stream.
    payload = random.randint(0, sys.maxsize)
    r.publish("numberStream", payload)
    print('Sent', payload)

    # Wait for a random interal
    time.sleep(random.randint(1, 5))
