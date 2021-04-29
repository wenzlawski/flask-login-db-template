import requests, pickle

# TODO Test persistant session and store cookie

cookie = pickle.load(open("cookie.txt", "rb"))

url = "http://127.0.0.1:5000/protected"

response = requests.get(url, cookies=cookie)

print(response.text)