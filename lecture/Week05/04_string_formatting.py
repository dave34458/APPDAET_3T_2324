origin = "MNL"
destination = "CEB"

flight = "I'll be departing from {} and arriving at {}"

print(flight)
print(flight.format(origin, destination))
print(flight.format("LAX", "DXB"))
print(flight.format(origin, "HKG"))
print(flight.format("NRT", destination))

# print(flight.format(origin))
print(flight.format(origin, destination, "LAX", "DXB"))