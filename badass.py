import requests
import os
import random
import string
import json
import matplotlib


chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'urlplacehere'

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice())
