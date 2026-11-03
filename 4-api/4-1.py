import requests
uri = "https://portal.app.cent-su.org/api/funnyname/random?n=3"
response = requests.get(uri)
response.raise_for_status()
names = response.json()
print(names[0]['first'], names[0]['last'])
print(names[1]['first'], names[1]['last'])
print(names[2]['first'], names[2]['last'])