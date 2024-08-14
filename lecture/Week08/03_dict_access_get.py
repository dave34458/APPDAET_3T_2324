fortuner = {
  "name": "Fortuner",
  "brand": "Toyota",
  "fuel_type": "Diesel",
  "type": "Mid-size SUV",
}

print(f"Car type is: {fortuner['type']}")
print(f"Car fuel_type is: {fortuner['fuel_type']}")
print(f"Car fuel_type is: {fortuner.get('fuel_type')}")

print(f"Car variant is: {fortuner.get('variant')}")
print(f"Car variant is: {fortuner.get('variant', 'G')}")