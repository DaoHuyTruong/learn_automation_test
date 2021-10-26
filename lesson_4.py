# ------------------------------------------------------------
# Lesson 4: Text Strings
# ------------------------------------------------------------

# Part 1: Manipulate Strings
# How to get the discount percentage in the text "This product is 50% off"

# Multi-lines string with '''
multi_lines_string = '''Line 1
Line 2
Line 3'''
print(multi_lines_string)

# Multi-lines string with \n (newline character)
one_line_string = "Line 1\nLine 2\nLine 3"
print(one_line_string)

# String with quotes
single_quotes = "He said to me 'I will go outside tonight'"
print(single_quotes)

double_quotes = 'He said to me "I will go outside tonight"'
print(double_quotes)

# Combine strings by + (concatenation)
first_name = "Oanh"
last_name = "Nguyen"
full_name = first_name + last_name  # first_name + " " + last_name 
name = "Nguyen" + " Trong" + " Oanh"
print(name)
print(full_name)

# Get a character with []
letters = 'ABCD'
letters[0] # index 0
letters[1] # index 1
letters[2] # index 2
letters[3] # index 3
# Note: in programming the first index is 0 not 1
#letters[4] ---> error string index out of range 

# Get a substring with [start:end]
letters_and_numbers = 'ABCD1234'
letters_only = letters_and_numbers[0:4]  # exclude character at index 4
numbers_only = letters_and_numbers[4:8]  # exclude character at index 8 ---> will not show out of range error 
print(letters_only)
print(letters_and_numbers[4:8])

# length of a string
len(letters_and_numbers)
len("")
len(" ")

# split string 
# syntax of a function that specify to string data types: string.function(arguments).
text = "This is a string"
text.split() # = 

student_names = "Andrew, Mathew, Gherkin"
student_names.split(",")
student_names = "Andrew; Mathew; Gherkin"
student_names.split(";")

# strip string
text_with_space = "      The price is 1000       "
text_with_space.strip()

# letter in string
text = "This product is on sale!"
"sale!" in text
"sale!" not in text

# format string
a = 12 
b = 30
print(f"The result of {a} + {b} is {a + b}") # String interpolation

# Part 2: Exercise
# Read about escape character in Python
# Extract the discount percentage in the text below
discount = "This product is 50% of"