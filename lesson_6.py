# ------------------------------------------------------------
# Lesson 6: List and Tuple
# ------------------------------------------------------------

# --- Part 1: Tuple ---
# Create a tuple
empty_tuple = ()
# Create a tuple with one item
one_tuple = 'Orange',  # if don't have comma, this will be a string assignment
one_tuple = ('Orange',)
# Create a tuple with multiple items
number_tuple = 12, 13, "Apple", "88.0"  # Mix types

# Tuple unpacking
a, b, c, d = number_tuple
x, y, z = number_tuple

# Exchange value with tuple
x, y = 12,99  # x = 12, y = 99
x, y = y, x   # x = 99, y = 12

# Convert list to tuple
list_num = [12, 13, 14]
list_tuple = tuple(list_num)

# Convert string to tuple
my_name = "Oanh"
characters = tuple(my_name)

# Combine tuple
('Eric',) + ('Duc Phuc', 'Hoa Minz') # create a new tuple from 2 tuple

# Get an item from a tuple with [index]
# Slicing tuple with [start:end]

# count number of items in tuple with len
names = ("Eric", "Duc Phuc", "Hoa Minzy", "Oanh")
len(names)

# check if an item is in a tuple
"Oanh" in names
"a" not in names

# Compare tuple
a = (200, 100 )
b = (99, 100)
a == b

# for loop in tuple, tuple is an iterator
for number in (1, 2, 3, 4, 5):
    print(number)

# Modify tuple ---> Cannot modify tuple. Tuple is immutable
a[0] = 2000 # ---> Error

# --- Part 2: List ---
# Create list
empty_list = []
mix_list = ['1.0', 1.0, 1, (1, 2, 3, 4)]
split_string = "This is a list of word".split()

# Convert string, tuple to list 
characters = list("Hello")
numbers = list((1, 2, 3))  # Pay attention to the ()

# Get an item from a list with [index]
# Slicing list with [start index:end index]

# Add an item to the end of the list with append()
names = ["Eric", "Duc Phuc"]
names.append("Hoa Minzy")

# Add in item to a specific index with insert()
names.insert(1, "Oanh")

# Combine list with extend()
number = [1, 2, 3]
letter = ["one", "two", "three"]
number.extend(letter)

# Combine list with +
number = [1, 2, 3]
letter = ["one", "two", "three"]
number += letter # number = number + letter 

# change item in list
number = [1, 2, 3] 
number[1] = 99

# delete with index and del 
names = ["Eric", "Duc Phuc", "Hoa Minzy", "Oanh"]
del names[3]  

# remove item with value
names = ["Eric", "Duc Phuc", "Hoa Minzy", "Oanh"]
names.remove("Oanh")

# clear a list
names.clear()

# count number of items in list with len
names = ["Eric", "Duc Phuc", "Hoa Minzy", "Oanh"]
len(names)

# for loop in list, list is an iterator
for name in names():
    print(name)

# check if an item is in a list 
"Oanh" in names

# ----- Conclusion ---------
# List is mutable, tuple is immutable
# Tuple is use a lot in arguments of function definition
