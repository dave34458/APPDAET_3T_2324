import csv

axis = []
allies = []

with open("ww2_countries.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row[2] == "Allies":
            allies.append(row)
        elif row[2] == "Axis":
            axis.append(row)

print("Axis: ")
print("-" * 30)
# print("\n".join([country[1] for country in axis]))
for country in axis:
    print(country[1])

print()

print("Allies: ")
print("-" * 30)
# print("\n".join([country[1] for country in allies]))
for country in allies:
    print(country[1])