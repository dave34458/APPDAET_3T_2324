fruits = [
    "apple",
    "pomegranate",
    "kiwi",
    "salak",
    "blackberry"
]

# problem:
# how would you check if "kiwi" is in fruits?
# 1. via for loop
fruit_to_find = "kiwi"

for fruit in fruits:
    if fruit_to_find == fruit:
        print(f"{fruit_to_find} is in {fruits}")

#2 "in" operator
print(f"is {fruit_to_find} in {fruits}? {fruit_to_find in fruits}")
print(f"{fruit_to_find in fruits}")

superstars = [77, 15, 2, 34, 0]
print(23 in superstars)
print(35 in superstars)
print(77 in superstars)