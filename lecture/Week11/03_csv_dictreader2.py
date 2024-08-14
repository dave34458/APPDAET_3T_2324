import csv

with open("browsers.csv") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        browser_name = row["Browser"]
        browser_platforms = row["Platforms"].split(",")
        browser_market_share = float(row["MarketShare"])

        print(f"Browser Name: {browser_name}")
        print(f"Browser Platforms: {browser_platforms}")
        print(f"Browser Market Share: {browser_market_share}")
        print("-" * 50)

        # add code here

        # end add code here

# 1 - Print all browsers that run on Windows
print("These browsers can be installed on Windows machines:")
# add print statement here


# 2 - Print all browsers that can only be ran on exactly one platform
print("These browsers can only be installed on one platform")
# add print statement here

# 3 - Print the browser with the highest MarketShare
print("This browser has the most MarketShare")
# add print statement here