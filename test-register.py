import requests
import json

url = "http://127.0.0.1:5000/register"

payload = {"username": "marc", "password": "marc"}

resp = requests.post(url, data=json.dumps(payload))

print(resp.text)