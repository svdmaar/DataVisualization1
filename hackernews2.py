import requests

url = "https://hacker-news.firebaseio.com/v0/item/9884165.json"

r = requests.get(url)

print("Status code: " + str(r.status_code))

json1 = r.json()
print(json1)