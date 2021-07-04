import requests
import json
from PIL import Image
import pickle

r = requests.get('http://127.0.0.1:5000') # make a get request to the local host (look in your hosts file)

print(r.__dir__()) # 
print(r.json()) # get the bytes back