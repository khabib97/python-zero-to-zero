# Python conditions and If statements

# Python conditions are a fundamental part of the language, allowing for decision-making in the code.
# They are used to execute a specific block of code if a certain condition or set of conditions is met.
# Python uses boolean logic to evaluate these conditions, resulting in either True or False.
# Based on this evaluation, Python decides which code blocks to execute.

# There are several types of conditions in Python:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
print("[info]: Basic conditions")
x = 5
y = 3
print(x == y)  # should print False

# Python also has a set of logical operators that can be used to combine conditional statements:
# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
print("[info]: Basic logical operators")
x = 5
print(x < 5 and x < 10)  # should print False
print(x < 5 or x < 4)  # should print False
print(x == 5)  # should print True

# These conditions can be used in several ways, most commonly in "if statements" and loops.
# An "if statement" is written by using the if keyword.
# if condition:
#   statement
print("[info]: Basic if statement")
x = 5
if x == 5:
    print("x is equal to 5")  # should print x is equal to 5

# If statement with else:
# if condition:
#   statement
# else:
#   statement
print("[info]: Basic if statement with else")
x = 5
if x == 5:
    print("x is equal to 5")  # should print x is equal to 5
else:
    print("x is not equal to 5")

# If statement with elif without else:
# if condition:
#   statement
# elif condition:
#   statement
# else:
#   statement
print("[info]: Basic if statement with elif without else")
x = 6
if x == 5:
    print("x is equal to 5")  # should print x is equal to 5
elif x == 6:
    print("x is equal to 6")  # should not print

# If statement with elif and else:
# if condition:
#   statement
# elif condition:
#   statement
# else:
#   statement
print("[info]: Basic if statement with elif and else")
x = 7
if x == 5:
    print("x is equal to 5")  # should print x is equal to 5
elif x == 6:
    print("x is equal to 6")  # should not print
elif 6 < x < 8:
    print("x is greater than 6 and less than 8")
else:
    print("x is not equal to 5 or 6 or 7")

# If statement with nested if:
# if condition:
#   statement
#   if condition:
#     statement
#   else:
#     statement
# else:
#   statement
print("[info]: Basic if statement with nested if")
x = 7
if x > 5:
    print("x is greater than 5")  # should print x is greater than 5
    if x == 7:
        print("x is equal to 7")  # should not print
    else:
        print("x is not equal to 7")  # should print x is not equal to 7
else:
    print("x is not greater than 5")  # should not print


# use if statement to check if a number is even or odd
# if the number is even, print "even"
# if the number is odd, print "odd"
# hint: use % operator
print("[info]: Basic if statement")
x = 5
if x % 2 == 0:
    print("even")  # should not print
else:
    print("odd")

# use if statement to check if a number is positive or negative
# if the number is positive, print "positive"
# if the number is negative, print "negative"
# hint: use > operator
print("[info]: Basic if statement")
x = -10
if x > 0:
    print("positive")  # should print positive
else:
    print("negative")

# use string comparison to check if a string is equal to "hello"
# if the string is equal to "hello", print "hello"
# if the string is not equal to "hello", print "not hello"
# hint: use == operator
print("[info]: Basic if statement")
x = "hello"
if x == "hello":
    print("hello")  # should print hello
else:
    print("not hello")


# using if statement you can check if a key is present in a dictionary
# if the key is present, print the value of the key
# if the key is not present, print "key not present"
# hint: use in operator
print("[info]: Basic if statement")
x = {"name": "John Doe", "age": 25}
if "name" in x:
    print(x["name"])  # should print John Doe
else:
    print("key not present")


# There are tons of other things you can do with if statement
# But for now, we will stop here
