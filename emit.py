import time
import datetime
import requests
import numpy as np
import json

while True:
    msg_data = {'datetime': f'{datetime.datetime.now()}', 'message': f'{np.random.rand():.2f}'}
    # msg_data = f'{datetime.datetime.now()}'
    # new_message = json.dumps(msg_data)
    try:
        requests.post('http://localhost:5000/publish', json=msg_data, timeout=0.2)
        # requests.post('http://localhost:5000/publish', data=msg_data, timeout=0.2)
    except requests.exceptions.ConnectionError as e:
        # print('No connection found. Continue')
        pass
    except Exception as e:
        print(e)
    time.sleep(1)
