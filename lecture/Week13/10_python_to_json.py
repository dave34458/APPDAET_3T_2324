import json

cat_data = {
  "name": "Miming",
  "isCat": True,
  "miceCaught": 15,
  "felineIQ": None,
}

json_data = json.dumps(cat_data)

with open("cat.json", "w") as jsonfile:
  jsonfile.write(json_data)