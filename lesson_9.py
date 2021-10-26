# ------------------------------------------------------------
# Lesson 9: Objects and Class
# ------------------------------------------------------------

# Part 1: What is an object
'''An object is a custom data structure containing both data (variables, called
attributes) and code (functions, called methods). It represents a unique
instance of some concrete thing. Think of objects as nouns and their
methods as verbs. An object represents an individual thing, and its methods
define how it interacts with other things.'''

# Part 2: Class and Objects
# Define class without attributes and methods
class Human():
    pass 

# Create an human object (instance).
human_1 = Human()
human_2 = Human()

# Define a class with attributes and methods
class Human():
    def __init__(self, name, hair, gender):
        self.name = name
        self.hair = hair 
        self.gender = gender

    def talk(self):
        print("My name is", self.name)
        print(f"I have {self.hair} hair.")
        print(f"And I'm a {self.gender}.")

    def do_math(self, a, b):
        print(a + b)

# Create a concrete human name Oanh which have short hair and is a man        
human_1 = Human("Oanh", "short", "male")
human_2 = Human("Andrew", "long", "male")

# Access attributes
print(f'''{human_1.name} is the first man on earth.
He had {human_1.hair} hair.
And he was a {human_1.gender}''')

# Call methods on an object. Tell an object to do something
human_1.talk()
human_2.talk()
human_1.do_math()
Human.talk(human_1)

# Everything in Python are objects
type(12)
type("My name")

# Functions v.s. Methods
print() # is function
"My name".split() # split is method

# Part 3: Inheritance
class Infant(Human):
    
    def cry(self):
        print("oe, oe")

baby_1 = Infant("Lary", "blonde", "female")
print(baby_1.name)
baby_1.cry()





