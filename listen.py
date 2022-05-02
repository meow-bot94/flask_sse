import sseclient
import requests

url = 'http://localhost:5000/subscribe'
# response = requests.get(url, stream=True)
messages = sseclient.SSEClient(url)

print('start')
for msg in messages:
    print(msg)
