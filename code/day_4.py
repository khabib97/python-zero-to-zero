# Basic operators in Python
# Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups:
# 1. Arithmetic operators
# 2. Assignment operators
# 3. Comparison operators
# 4. Logical operators
# 5. Identity operators
# 6. Membership operators
# 7. Bitwise operators

# Why we need operators?
# Let's say we have two variables x and y
# x = 5
# y = 3
# Now we want to add x and y
# print(x + y)  # should print 8


# Arithmetic operators are used with numeric values to perform common mathematical operations:
# Operator	Name	Example	Try it
# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y
print("[info]: Basic arithmetic operators")
x = 2
y = 3
print(x + y)  # should print 5
print(x - y)  # should print -1
print(x * y)  # should print 6
print(x / y)  # should print 0.6666666666666666
print(x % y)  # should print 2
print(x ** y)  # should print 8, means 2 * 2 * 2
print(x // y)  # should print 0, meaning 0.6666666666666666 is rounded to 0

# Assignment operators are used to assign values to variables:
# Operator	Example	Same As	Try it
# =	x = 5	x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# %=	x %= 3	x = x % 3
# skip difficult ones
print("[info]: Basic assignment operators")
x = 5
print(x)  # should print 5
x += 3  # same as x = x + 3
print(x)  # should print 8
x -= 3  # same as x = x - 3
print(x)  # should print 5
x *= 3  # same as x = x * 3
print(x)  # should print 15
x /= 3  # same as x = x / 3,
print(x)  # should print 5
x %= 3  # same as x = x % 3
print(x)  # should print 2

# Comparison operators are used to compare two values:
# Operator	Name	Example	Try it
# ==	Equal	x == y
# !=	Not equal	x != y
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y
print("[info]: Basic comparison operators")
x = 5
y = 3
print(x == y)  # should print False
print(x != y)  # should print True
print(x > y)  # should print True
print(x < y)  # should print False
print(x >= y)  # should print True
print(x <= y)  # should print False

# Logical operators are used to combine conditional statements:
# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
print("[info]: Basic logical operators")
x = 5
print(x < 5 and x < 10)  # should print False
print(x < 5 or x < 4)  # should print False
print(not (x < 5 and x < 10))  # should print True

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object,
# with the same memory location: Operator	Description	Example	Try it is 	Returns true if both variables are the
# same object	x is y is not	Returns true if both variables are not the same object	x is not y
print("[info]: Basic identity operators")
x = 5
y = 3
print(x is y)  # should print False
print(x is not y)  # should print True

# Membership operators are used to test if a sequence is presented in an object:
# Operator	Description	Example	Try it
# in 	Returns True if a sequence with the specified value is present in the object	x in y
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y
print("[info]: Basic membership operators")
x = 5
y = 3
list_of_numbers = [1, 2, 3, 4, 5]
print(x in list_of_numbers)  # should print True
print(y in list_of_numbers)  # should print True
print(x not in list_of_numbers)  # should print False

# Advanced topic, ignore for now
# Bitwise operators are used to compare (binary) numbers:
# Operator	Name	Description
# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
# ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print("[info]: Basic bitwise operators")
x = 5
y = 3
print(x & y)  # should print 1
print(x | y)  # should print 7
print(x ^ y)  # should print 6
print(~x)  # should print -6
print(x << y)  # should print 40
print(x >> y)  # should print 0
