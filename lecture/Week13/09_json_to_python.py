import json

json_data = '{"name": "Zophie", "isCat": true, "miceCaught": "0", "felineIQ": null}'
print(json_data)

python_dict = json.loads(json_data)

print(f"Name: {python_dict["name"]}")
print(f"is Cat?: {python_dict["isCat"]}")
print(f"Mice Caught: {python_dict["miceCaught"]}")
print(f"Feline IQ: {python_dict["felineIQ"]}")