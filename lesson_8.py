# ------------------------------------------------------------
# Lesson 8: Function
# ------------------------------------------------------------

# ---- Part 1: Define a function ----
def do_nothing():
    pass   # Use pass if you just want to create ideas for functions. 

# Call a function
do_nothing()

# Define a function that add two number
def add_two_number():
    a = 10
    b = 20
    c = a + b

print(add_two_number()) 

# Get a value back from function with return
def add_two_number():
    a = 10
    b = 20
    return a + b

print(add_two_number()) 

# Use return value in if else
if add_two_number() == 30:
    print("You can do math")
else:
    print("You cannot do math")

# Use return value in loops
count = 0
while count <= add_two_number():  # count <= 30
    print(count)
    count += 5

for i in range(20, add_two_number()):   # range(20, 30)
    print(i)

# Return is optional
def greeting():
    print("Hello!")
    print("Hola")
    
# ---- Part 2: Arguments and Parameters ----
# Parameters
def add_two_number(number_1, number_2):
    a = number_1    # a copy value of number_1
    b = number_2    # b copy value of number_2
    return a + b    # return number_1 + number_2

print(add_two_number(100, 200))

### Note: 
# Arguments = the values you pass into the function when you call it (100, 100)
# Parameters = the variables in () when you define a function (number_1, number_2)

# Parameters can take any types: int, float, string, list, dictionary.etc.
def get_product_list(product_list):
    return product_list

print(get_product_list(["iphone", "ipad", "ipython"]))

# Multiple returns in a function
def age_validation(age):
    if age > 18: 
        return "You are an adult"
    elif 16 < age < 18:
        return "You are not old enough"
    else:
        return "You are a child"

age_checking = age_validation(30)
print(age_checking)

# Positional Arguments
def get_full_name(first_name, last_name):
    return first_name + " " + last_name

get_full_name("Oanh", "Nguyen")
get_full_name("Nguyen", "Oanh")  # change order of arguments

# Keyword Arguments
def get_full_name(first_name, last_name)
    return first_name + " " + last_name

get_full_name(last_name="Nguyen", first_name="Oanh")  


# Default Parameter Values
def get_breakfast(dish_1, dish_2, drink="Coffee"):
    return f"I eat {dish_1}, {dish_2} and drink {drink} in the morning"

print(get_breakfast("Phở", "Bánh mì"))
print(get_breakfast("Phở", "Bánh mì", "Milk"))

# None as Default Parameters
def get_breakfast(dish_1, dish_2, drink=None):
    if drink is not None:
        return f"I eat {dish_1}, {dish_2} and drink {drink} in the morning"
    elif drink is None:
        return f"I eat {dish_1}, {dish_2} in the morning"


# *args, **kwargs
def count_total(*args):
    print(args)     
    return sum(args)

count_total(1, 99, 100)
# Explore print()

def get_full_name(**kwargs):
    print(kwargs)
    full_name = ""
    for name in kwargs.values():
        full_name += name + " "  # full_name = full_name + name
    return full_name

print(get_full_name(first_name="Oanh", last_name="Nguyen", middle_name="Trong"))
print(get_full_name(first_name="Oanh", last_name="Nguyen"))

# Argument order: required positional arguments > default keyword arguments > *args > **kwargs 
def foo(a, b, c=0, *args, **kwargs):
    pass 

foo(c=10, 10, 20)

# Exercise: practice with the code again to make sure you really understand the concepts
            # Try to think about your own function that make use of positional arguments, keyword arguments, *args, and **kwargs   

# Install plugin for python
