def my_function(x, y, z=None):
    if z:
        return (x + y + z)
    else:
        return (x + y)

print(my_function(1, 1, 1))
print(my_function(1, 1))