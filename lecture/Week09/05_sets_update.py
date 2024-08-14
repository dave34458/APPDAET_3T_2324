cat_breeds = {
    "Siamese",
    "Persian",
    "Maine Coon",
}

print(f"Original cat_breeds set: {cat_breeds}")
cat_breeds.update(["British Shorthair", "Persian"])
cat_breeds.update(["Maine Coon", "Russian Blue", "Bombay"])
print(f"cat_breeds set after 2 update() calls: {cat_breeds}")