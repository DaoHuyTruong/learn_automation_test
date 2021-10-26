# ------------------------------------------------------------
# Lesson 2: Basic Math with Python
# ------------------------------------------------------------

# Part 1: Math operators
# Multiply
2 * 3
a = 2
b = 3
c = a * b  # the result is 6

print(a * b)

# Divide
13 / 10  # The result is always an float, result = 1.3
13 // 10  # The result is an integer, result = 1
13 % 10  # Modulus, the result is the remainder, result = 3

# Add numbers
2 + 3
a + b  # The result is

# Subtract numbers
2 - 3
a - b  # The result is -1

# Exponent
2 ** 3
a ** b  # The result is 8

# Operators precedence as in math
2 + 3 * 3  # The result is 11

# Grouping operation with ()
(3 - 2) * 3  # The result is 3


# Part 2: Type Conversion
# Convert from int to float
float(10)  # The result is 10.0

# Convert from float to int
int(10.6)  # The result is 10

# Convert from string to int
int("10")  # try with int("10.0")

# Convert from int to string
str(10)

# Convert from string to float
float("10.3")

# Convert from float to string
str("10.444")

# Part 3: Real life automation example
# Calculate the product's price after discount
discount = 0.5
old_price = 100

# hard code
new_price = 100 - (100 * 0.5)
new_price_again = 100 - (100 * 0.5)

# parameterize
new_price_ = old_price - (old_price * discount)
new_price_ = old_price - (old_price * discount)

# Exercise:
# Experiment with interactive shell (iPython), types conversion, grouping operations and division.
# Try to think about a test case that you need to do calculation
