import requests as req

res = req.get("http://api.open-notify.org/astros.json")
data = res.json()
print(data["people"][4]["name"])
print(data)