atrium = {
    "name": "The Atrium @ Benilde",
    "floors": {
        "G": {
            "amenities": [
                "entrance",
                "exit",
                "Vatel Restaurant"
            ],
            "lavatories": "1"
        },
        "M": {},
        "2": {},
        "3": {
            "amenities": [
                "Clinic"
            ],
            "lavatories": "1"
        }
    }
}

print(f"Amenities of the G Floor: {atrium['floors']['G']['amenities']}")

# atrium["floors"].items() 
#  - if atrium["floors"] is a dictionary
#    - returns a tuple
#      - 1st element is the key
#      - 2nd element is the value
for floor in atrium["floors"].items():
    print(floor)

# atrium["floors"] 
#   - if atrium["floors"] is a dictionary
#     - returns a string which is the key
for floor in atrium["floors"]:
    print(floor)

# atrium["floors"].keys()
#  - if atrium["floors"] is a dictionary
#    - return a string which is the key
#    - same with atrium["floors"]
for floor in atrium["floors"].keys():
    print(floor)

# atrium["floors"].values()
#  - if atrium["floors"] is a dictionary
#    - returns the value for each item
for floor in atrium["floors"].values():
    print(floor)

# enumerate(atrium["floors"])
#  - assigns indices for each iterated item
for floor in enumerate(atrium["floors"]):
    print(floor)

for index, floor in enumerate(atrium["floors"]):
    print(f"{index}: {floor}")