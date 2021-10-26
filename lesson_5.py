# ------------------------------------------------------------
# Lesson 5: Repetitive task with Loops
# ------------------------------------------------------------

# --- Part 1: What is a loop? ---
# print number from one to 5
print(1)
print(2)
print(3)
print(4)
print(5)

# repeat the print function 5 times with loops

# --- Part 2: While loop ---
# while True:
    # do something
    # increment till while False

# Infinite loop:
while True:     
    print("I'm looping forever")
    # Ctrl + C to stop infinite loop

number = 1 
while number <= 5: # True untill number's value > 5
    print(number)
    number += 1  # number = number + 1

# Cancel with break
# Loop until something occurs but don't know when that might happen
command = input()
if command == "iPython" or "ipython":
    while True:
        command = input("Enter words: ")
        if command == "exit":
            break
        elif command == "quit":
            print("Did you mean exit?")

# Skip a block of code wit continue
# Adding one to positive integer, if user inputs negative, don't print the result.
while True:
    value = input("Adding 1 to an positive integer: ")
    if value == 'exit':
        break
    number = int(value)
    if number < 0:
        continue
    print(number, "+ 1 = ", number + 1)

 # --- Part 3: For loop ---   
 # for something in iterators:
    # do something

# iterators: something that is iterable (have next item)
# print all character in a String (string is iterable)
text = "This is a string"
for letter in text:
    print(letter)

# int, float are not iterable (no next item)
for i in 12:
    print(i) 

# but list of int, float is iterable
numbers = [12, 13, 14, 15]
for number in numbers:
    print(number)

# print from 1 to 5 by range() function 
for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

# cancel with break
text = "This is a string"
for letter in text:
    if letter == "a":
        break 
    print(letter)
    
# skip with continue
for letter in text:
    if letter == "a":
        continue
    else:
        print(letter)

# Exercise: read document of range() function
# Automation example: we use FOR to call keywords (click button) many time ---> Consider this with stress test



