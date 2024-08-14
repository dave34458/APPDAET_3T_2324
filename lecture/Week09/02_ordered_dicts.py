dictionary_a = {}
dictionary_a["delta"] = "delta"
dictionary_a["foxtrot"] = "foxtrot"
dictionary_a["bravo"] = "bravo"

print(dictionary_a)

from collections import OrderedDict
dictionary_b = OrderedDict(
    uniform="uniform",
    golf="golf",
    echo="echo"
)
print(dictionary_b)
print(dict(dictionary_b))