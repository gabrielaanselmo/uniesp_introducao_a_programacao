import requests
import json

API_KEY = "63d2f06f0136d4d5e96f7c084f26c529"
LAT = -7.11532
LOG = -34.861
url = (f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LOG}&appid={API_KEY}")

response = requests.request("GET", url)
objects = json.loads(response.text)

print(objects)
print(type(objects))

for i in objects:
    print(f"{i} :: {objects[i]}")