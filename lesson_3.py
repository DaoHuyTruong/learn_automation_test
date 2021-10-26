# ------------------------------------------------------------
# Lesson 3: Conditional Statements
# ------------------------------------------------------------

### Part 1: Comparision Operators
# The result of comparision operation is a Boolean value True or False
a = 3
b = 4

# Greater than
2 > 3
a > b 

# Less than
2 < 3
a < b

# Greater than or equal to
2 >= 3
a >= b 

# Less than or equal to
2 <= 3
a <= b

# not equal to
(2 + 1) != 3
a != b

# equal to
2 == 3
"my string" == "my string"
"my string" == "My String"

### Part 2: Conditional Statements
# if
rain = True 
if rain:        
    print("Stay home")  # I will stay home

# if else
have_money = False
if have_money:   # if I don't have money 
    print("I will cook myself")
else:            # if I have money, I will order food           
    print("I will order food")

# if elif else
color = "red"
if color == "red": 
    print("Haverst tomatos")
elif color == "greeen": 
    print("It's not time yet")
elif color == "black": 
    print("It's rotted")
else:
    print("No cà chua to thu hoạch") 

### Part 3: Nested Statement
car = "BMW"
year = 2020
if car == "BMW":
    if year == 2020:
        print("You are rich kid")
    elif year < 2020:
        print("You are not a rich kid")
elif car == "Toyota":
    print("You are normal")
else:
    print("You don't have a real car")

# Note: don't nest to deep, 2 or 3 is enough. 

### Part 4: Combine conditions
rain = True 
have_money = False

if rain and have_money :
    print("Stay home")

if rain or have_money:
    print("I will go outside")
 
 # Grouping conditions with (): if ((a == b) and ((a != c)) or (a >= d))
 # Note: 
 # True and False = False
 # False and True = False
 # True or False = True
 # False or True = True

### Part 5: Do Multiple Comparision with in
name = "Oanh"
celebs = ["Eric", "Hoa Minzy", "Duc Phuc"]


# using or
if name == "Eric" or name == "Hoa Minzy" or name == "Duc Phuc":
    print("You are famous")
else:
    print("You are not famous")

# Using in
if name in celebs:
    print("You are famous")
elif name not in celebs:
    print("You are not famous")

### Part 6: Real life automation example
# Different messages for different number of remaining products.
product = 1

if product == 1:
    # check page contain message: "Only 1 products left"
    pass
elif product == 0:
    # check page contain message: "Out of stock"
    pass 
else:
    # check page not contain message: "Only 1 products left" and ""Out of stock"
    pass
