dog_breeds = {
    "Chihuahua",
    "Lhasa Apso",
    "Poodle",
    "German Shepherd"
}

print(f"Original Set: {dog_breeds}")
dog_breeds.add("German Shepherd")
dog_breeds.add("Golden Retriever")
print(f"Set after two add() calls: {dog_breeds}")