import requests, pickle, json

url = "http://127.0.0.1:5000/login"

data = {"username": "marc", "password": "marc"}

response = requests.post(url, data=json.dumps(data))

print(response.text)
cookie = response.cookies

with open("cookie.txt", mode="wb") as f:
    pickle.dump(cookie, f)