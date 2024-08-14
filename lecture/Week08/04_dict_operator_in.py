model_s = {
  "brand": "Tesla",
  "name": "Model S",
  "range": "400mi"
}

print("fuel_type" in model_s)
print("range" in model_s)

print(model_s.keys())

# if fuel_type is in this dictionary's keys
is_electric = True
for key in model_s.keys():
    if key == "fuel_type":
        is_electric = False

print(f"The car is electric: {is_electric}")