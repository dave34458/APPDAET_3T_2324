campus = ["Main"]
print(campus)

# append(item) - adds an item at the end of the list
campus.append("Hotel Benilde")
print(campus)

# extend(iterable) - adds another list at the end
campus.extend(["DA+C", "Atrium"])
print(campus)

# insert(item, index) - adds an item at the specified index
campus.insert(3, "MCAD")
print(campus)

# remove(item) - removes an item
campus.remove("MCAD")
print(campus)

# pop([index]) - w/o index parameter = removes the last item
#              - w/ index parameter = removes the item from that index
campus.pop()
print(campus)

campus.pop(1)
print(campus)

# clear - removes all items in the list
campus.clear()
print(campus)

campus.extend(["Main", "Hotel Benilde", "DA+C", "Atrium"])

# count - counts the occurrences in the list with the given item
print(campus.count("Main"))

# sort - sorts a list alphabetically
#      w/ kw reverse=True, sorts a list alphabetically in reverse
campus.sort()
print(campus)

campus.sort(reverse=True)
print(campus)
