import json, requests, sys

APPID = "6fc7ffa0081ea1be74aa936f7fdd4a69"

# TODO: Download the JSON data from OpenWeatherMap.org's API\
latitude = 14.56217
longitude = 121.0220638

url = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={APPID}&units=metric"
print(url)
response = requests.get(url)
response.raise_for_status

json_data = response.json()

with open("weather_data.json", "w") as jsonfile:
  jsonfile.write(json.dumps(json_data))

# TODO: Load JSON data into a Python variable.
print("weather today: ")
print(f'{json_data["list"][0]["weather"][0]["main"]} - {json_data["list"][0]["weather"][0]["description"]}')

print("weather tomorrow: ")
print(f'{json_data["list"][1]["weather"][0]["main"]} - {json_data["list"][1]["weather"][0]["description"]}')

print("weather day after tomorrow: ")
print(f'{json_data["list"][2]["weather"][0]["main"]} - {json_data["list"][2]["weather"][0]["description"]}')