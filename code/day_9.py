# Python String

# String literals in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:

# Assign String to a Variable
print("[info]: Basic string")
x = "hello"
print(x)  # should print hello

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
print("[info]: Multiline string")
x = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(x)

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

# Get the character at position 1 (remember that the first character has the position 0):
print("[info]: String as array")
a = "Hello, World!"
print(a[1])  # should print e

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
print("[info]: String as array")
for x in "banana":
    print(x)

for x in "banana":
    print(x, end=" ")  # should print b a n a n a

# String Length
# To get the length of a string, use the len() function.
print("[info]: String length")
a = "Hello, World!"
print(len(a))  # should print 13

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
print("[info]: String check")
txt = "The best things in life are free!"
print("free" in txt)  # should print True

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
print("[info]: String check")
txt = "The best things in life are free!"
print("expensive" not in txt)  # should print True

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
print("[info]: String slicing")
b = "Hello, World!"
print(b[2:5])  # should print llo
# Note: The first character has index 0.
# Note: The last character in the range is NOT included.

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
print("[info]: String slicing")
b = "Hello, World!"
print(b[:5])  # should print Hello

# Slice To the End
# By leaving out the end index, the range will go to the end:
print("[info]: String slicing")
b = "Hello, World!"
print(b[2:])  # should print llo, World!

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
print("[info]: String slicing")
b = "Hello, World!"
print(b[-5:-2])  # should print orl
# -5 is the same as 5 from the end of the string, -2 is the same as 2 from the end of the string.

# Modify Strings
# Python has a set of built-in methods that you can use on strings.
# The strip() method removes any whitespace from the beginning or the end:
print("[info]: String modify")
a = " Hello, World! "
print(a.strip())  # should print Hello, World!

# The lower() method returns the string in lower case:
print("[info]: String modify")
a = "Hello, World!"
print(a.lower())  # should print hello, world!

# The upper() method returns the string in upper case:
print("[info]: String modify")
a = "Hello, World!"
print(a.upper())  # should print HELLO, WORLD!

# The replace() method replaces a string with another string:
print("[info]: String modify")
a = "Hello, World!"
print(a.replace("H", "J"))  # should print Jello, World!

# The split() method splits the string into substrings if it finds instances of the separator:
print("[info]: String modify")
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
print("[info]: String concatenation")
a = "Hello"
b = "World"
c = a + b
print(c)  # should print HelloWorld

# To add a space between them, add a " ":
print("[info]: String concatenation")
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # should print Hello World

# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
print("[info]: String format")
age = 36
# txt = "My name is John, I am " + age
# print(txt)  # should print TypeError: can only concatenate str (not "int") to str
# format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
txt = "My name is John, and I am {}"
print(txt.format(age))  # should print My name is John, and I am 36

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
print("[info]: String format")
quantity = 3
itemno = 567
price = 49.95
txt = "I want {} pieces of item {} for {} dollars."
print(txt.format(quantity, itemno, price))  # should print I want 3 pieces of item 567 for 49.95 dollars.

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
print("[info]: String format")
quantity = 3
itemno = 567
price = 49.95
txt = "I want to pay {2} dollars for {0} pieces of item {1}."
print(txt.format(quantity, itemno, price))  # should print I want to pay 49.95 dollars for 3 pieces of item 567.

# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
print("[info]: Escape character")
# txt = "We are the so-called "Vikings" from the north."
# print(txt)  # should print SyntaxError: invalid syntax
txt = "We are the so-called \"Vikings\" from the north."
print(txt)  # should print We are the so-called "Vikings" from the north.

# Other escape characters used in Python:
# Code	Result	Try it
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value
# String Methods
# Python has a set of built-in methods that you can use on strings.
# Note: All string methods returns new values. They do not change the original string.
