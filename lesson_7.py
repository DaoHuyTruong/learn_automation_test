# ------------------------------------------------------------
# Lesson 7: Dictionary
# ------------------------------------------------------------

# Create a dictionnary with {}
empty_dictionary = {}

# Dictionary is key:value pairs
products = {"iphone 12": 100, "Note 9": 200, "Galaxy": 200}
# Dictionary values can be anything, int, float, string, list, dictionary, tuple
products = {"iphone 12": {"new": 100, "old": 100},"Note 9": [100, 200], "Galaxy": 200}

# Convert to dict 
product_list = [["iphone 12", 100], ["Note 9", 200], ["Galaxy", 200]]
dict(product_list)

product_list_tuple = [("iphone 12", 100), ("Note 9", 200), ("Galaxy", 200)]
dict(product_list_tuple)

letters = ['aab', 'cd', 'ef']
dict(letters)

# Get a value by key
products = {"iphone 12": {"new": 100, "old": 100},"Note 9": 200, "Galaxy": 200}
products["iphone 12"]

# Change value by key
products = {"iphone 12": 100,"Note 9": 200, "Galaxy": 200}
products["iphone 12"] = 200

# Add new key-value
products["Vsmart"] = 200
### Note: dictionary keys must be unique

# Get all keys with keys() 
products = {"iphone 12": 100,"Note 9": 200, "Galaxy": 200}
products.keys()

# Get all values with values() 
products.values()

# Get all key-values pairs with items()
products.items()
### Note: the return type of those methods above are dict_item not a list, dict_item can be convert to list with list()
type(products.items())

# Get the number of key-value pairs with len()
len(products)

# Delete item by key with del
products = {"iphone 12": 100,"Note 9": 200, "Galaxy": 200}
del products["iphone 12"]

# Clear all items with clear
products.clear()

# For loop in dictionary
products = {"iphone 12": 100,"Note 9": 200, "Galaxy": 200}
for product in products.keys():
    print(product)

for amount in products.values():
    print(amount)

for product, amount in products.items():
    print(f"{product}, {amount}")

# check if a key is in a dictionary 
products = {"iphone 12": 100,"Note 9": 200, "Galaxy": 200}
"Galaxy" in products