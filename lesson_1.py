# ------------------------------------------------------------
# Lesson 1: Data Types, Variable, Values and Name
# ------------------------------------------------------------

##### Part 1: Python's basic data types

# Integer 
47, 12, 13, -15

# Float 
47.0, 12.5, 13.88, -15.31

# String (text) is wrapped around "" or ''. There's no character type in Python. One single character is a String.
"This is a paragraph"
'This is a paragraph'
"a"
'a'

# List - A list of items
["Orange", "Apple", "Grape"]

# Tuple
(2, 4, 8)

# Dictionary - A list of key-value pairs
{"Orange": 2, "Apple": 4, "Grape": 10}

# Boolean - True or False
True 
False 

# You can create your own data types known as custom class and object which will introduce in OOP (Object Oriented Programming) video

##### Part 2: Values and Variables
# There are two ways to define a value in Python: Literal and Variable
# Way 1: Literal  
"Literal String"
12
14 

# Way 2: Variable 
x = 12 
my_string = "Literal String"
y = 14.0 
boolean = True
fruits_list = ["Orange", "Apple", "Grape"]
fruits_dict = {"Orange": 2, "Apple": 4, "Grape": 10}

# Declare a varibale: variable name + assignment operator + values
var = "Values"
empty_list = []
empty_string = ""

# Invalid variable declaration:
# empty_var

# Reassigning a variable
c = 17
c = 20 # the value of c is now 20

# Copy a variable:
a = 15
b = a # the value of b is 15

# Assigning to Multiple Names
var_1, var_2, var_3 = 55, 56, 57 # var_1 = 55, var_2 = 56, var_3 = 57

# print() function is used for showing the values on the screen.
# Print literal values
print("Literal String")
print(12)
print(["Orange", "Apple", "Grape"])
print() # print a new line

# Print variable's values
print(x)
print(my_string)
print(fruits_dict)
print(fruits_list)
print() # print a new line

print(var_1, var_2, var_3)
### Note: Naming convention of variable
# 1. They can contain only these characters:
    # Lowercase letters (a through z)
    # Uppercase letters (A through Z)
    # Digits (0 through 9)
    # Underscore (_)
# 2. Case-sensitive: var, Var and VAR are different names
# 3. Must begin with a letter or an underscore, not a digit
# 4. Cannot be Python's reserved words (keywords): if, else, list, dict..etc
# 5. Styling: camelCase or camel_case
# 6. Constant variable should be in uppercase

### Exercise: search and read document of print() function, try some printing option.



