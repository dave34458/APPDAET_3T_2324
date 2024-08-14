raptor = {
    "brand": "Ford",
    "name": "Raptor",
    "type": "Pickup",
}

print(raptor)
raptor.update({"engine_displacement": "3.0L"})  # add a new key: value
print(raptor)
raptor.update({"brand": "Chevrolet"})  # update an existing key: value
print(raptor)