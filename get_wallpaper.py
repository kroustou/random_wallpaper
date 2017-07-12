#!/usr/bin/env python3
import os
import requests
api_key = os.environ.get('UNSPLASH_CLIENT_ID')
url = 'https://api.unsplash.com/photos/random/?client_id=%s' % (api_key)
response = requests.get(url).json()
print(response['urls']['full'])
