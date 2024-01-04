# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.

# To program Python, we don't need to declare the type of variable.
# But we need to know what type of data we are storing in a variable.
# For better understanding, let's see an example:

# Python has the following data types built-in by default, in these categories:
# Text Type: str
# Numeric Types: int, float, complex
# Boolean Type:	bool

# Advance Types:
# Mapping Type:	dict
# Sequence Types: list, tuple, range
# Set Types: set, frozenset
# Binary Types:	bytes, bytearray, memoryview

# Getting the Data Type
# You can get the data type of any object by using the type() function:

# From day_2.py file, we know that we can store different types of data in a variable

# Let's see what is the type of those data
x = 5
print(f"Type of `x` is: {type(x)}")

a = 'A'
print(f"Type of `a` is: {type(a)}")

name = 'John Doe'
print(f"Type of `name` is: {type(name)}")
# In python, string and character are same
# String with length 1 is character in python

is_active = True
print(f"Type of `is_active` is: {type(is_active)}")

list_of_names = ['John Doe', 'Jane Doe', 'John Smith']
print(f"Type of `list_of_names` is: {type(list_of_names)}")

person = {'name': 'John Doe', 'age': 25, 'is_active': True}
print(f"Type of `person` is: {type(person)}")

# Ignore other types for now
