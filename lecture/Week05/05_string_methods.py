first_name_lower = "jino"
first_name_upper = "JINO"

# str.capitalize() - Capitalizes the first letter and makes the rest lowercase
print(first_name_lower.capitalize())
print(first_name_upper.capitalize())

country_1 = "Slovenia"
country_2 = "LATVIA"
# str.lower() - Converts the entire string to lowercase
print(country_1.lower())
print(country_2.lower())

# str.upper() - Converts the entire string to uppercase
print(country_1.upper())
print(country_2.upper())

sm_mall_prefix = "SM"
mall_1 = "SM - Mall of Asia"
mall_2 = "SM Megamall"
mall_3 = "Robinson's Place Manila"
# str.startswith() - Checks whether the string starts with the specified prefix
print(mall_1.startswith(sm_mall_prefix))
print(mall_2.startswith("SM"))
print(mall_3.startswith(sm_mall_prefix))

country_a = "Yugoslavia"
country_b = "Romania"
country_c = "Bavaria"
country_d = "Hungary"
# str.endswith() - Checks whether the strings ends with the specified suffix
print(country_a.endswith("ia"))
print(country_b.endswith("ia"))
print(country_c.endswith("ia"))
print(country_d.endswith("ia"))

# str.strip() - returns a copy of the string with the leading and trailing whitespaces removed
print("\n\n\n\nNikola Jokic".strip())
print("Luka Doncic\t\t\t".strip())
print(" Peja Stojakovic ".strip())

print("\n\n\n\nNikola Jokic")


campaign_paragraph = """
   Welcome to Resorts World! It is a chain of hotels/casinos in the 
   South East Asia region. Resorts World has locations in Singapore,
   Philippines and Malaysia to name a few
"""

print(campaign_paragraph)
# str.replace() - replaces all occurences of the old substring with the new substring

print(campaign_paragraph.replace("Resorts World", "Newport"))