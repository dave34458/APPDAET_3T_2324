import csv

axis = []
allies = []

with open("ww2_countries_headers.csv") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        if row["Affiliation"] == "Axis":
            axis.append(row)
        elif row["Affiliation"] == "Allies":
            allies.append(row)

print("Axis Leaders: ")
print("-" * 50)
for country in axis:
    print(country["Leader"])

print("Allies Leaders: ")
print("-" * 50)
for country in allies:
    print(country["Leader"])