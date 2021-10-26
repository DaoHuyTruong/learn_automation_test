# ------------------------------------------------------------
# Lesson 10: Variable scope
# ------------------------------------------------------------

# Local and global variable

food = "Hambuger"
# food is in global scope
def global_food():
    print(food)

# viet_food is in local scope
def local_food():
    viet_food = "Banh mi"

print(viet_food)

print(viet_food)

# Other scopes are class variable and instance (object) variable

