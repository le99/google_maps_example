## HTTP query

# http://ip-api.com/json/24.48.0.1

import requests

r = requests.get('http://ip-api.com/json/24.48.0.1')

jsonRes = r.json()
print(jsonRes)
