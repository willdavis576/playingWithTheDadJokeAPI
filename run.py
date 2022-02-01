import requests

url = 'https://icanhazdadjoke.com/'
headers = {"Accept" : "application/json"}
r = requests.get(url, headers=headers)
r = r.json()

joke = r["joke"]

print(joke)