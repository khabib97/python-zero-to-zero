# Python loops
# Python has two primitive loop commands:
#   while loops
#   for loops

# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.
# while condition:
#   statement
print("[info]: Basic while loop")
i = 1
while i < 6:
    print(i)  # should print 1 2 3 4 5
    i += 1

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
# while condition:
#   statement
#   if condition:
#     break
print("[info]: Basic while loop with break statement")
i = 1
while i < 6:
    print(i)  # should print 1 2 3
    if i == 3:
        break
    i += 1

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
# while condition:
#   statement
#   if condition:
#     continue
print("[info]: Basic while loop with continue statement")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)  # should print 1 2 4 5 6

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:
# while condition:
#   statement
# else:
#   statement
print("[info]: Basic while loop with else statement")
i = 1
while i < 6:
    print(i)  # should print 1 2 3 4 5
    i += 1
else:
    print("i is no longer less than 6")

# The for Loop A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set,
# or a string).
# Advance Note:This is less like the for keyword in other programming languages, and works more like an
# iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
# for item in sequence:
#   statement
print("[info]: Basic for loop")
list_of_names = ['John Doe', 'Jane Doe', 'John Smith']
for name in list_of_names:
    print(name)  # should print John Doe Jane Doe John Smith

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:
# for item in sequence:
#   statement
print("[info]: Basic for loop")
name = 'John Doe'
for character in name:
    print(character)  # should print J o h n   D o e

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
# for item in sequence:
#   statement
#   if condition:
#     break
print("[info]: Basic for loop with break statement")
list_of_names = ['John Doe', 'Jane Doe', 'John Smith']
for name in list_of_names:
    print(name)  # should print John Doe Jane Doe
    if name == 'John Smith':
        break

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
# for item in sequence:
#   statement
#   if condition:
#     continue
print("[info]: Basic for loop with continue statement")
list_of_names = ['John Doe', 'Jane Doe', 'John Smith']
for name in list_of_names:
    if name == 'Jane Doe':
        continue
    print(name)  # should print John Doe John Smith

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and ends at a specified number.
# range(number)
# range(start_number, end_number)
# range(start_number, end_number, step_number)
print("[info]: Basic for loop with range function")
for x in range(6):
    print(x)  # should print 0 1 2 3 4 5

print("[info]: Basic for loop with range function")
for x in range(2, 6):
    print(x)  # should print 2 3 4 5

print("[info]: Basic for loop with range function")
for x in range(2, 30, 3):
    print(x)  # should print 2 5 8 11 14 17 20 23 26 29

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# for item in sequence:
#   statement
# else:
#   statement
print("[info]: Basic for loop with else statement")
list_of_names = ['John Doe', 'Jane Doe', 'John Smith']
for name in list_of_names:
    print(name)  # should print John Doe Jane Doe John Smith
else:
    print("All names are printed")

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# for item in sequence:
#   statement
#   for item in sequence:
#     statement
print("[info]: Basic nested for loop")
list_of_names = ['John Doe', 'Jane Doe', 'John Smith']
list_of_numbers = [1, 2, 3]
for name in list_of_names:
    for number in list_of_numbers:
        print(name, number)  # should print John Doe 1 John Doe 2 John Doe 3 Jane Doe 1 Jane Doe 2 Jane Doe 3 John Smith 1 John Smith 2 John Smith 3

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to
# avoid getting an error.
# for item in sequence:
#   pass
print("[info]: Basic for loop with pass statement")
list_of_names = ['John Doe', 'Jane Doe', 'John Smith']
for name in list_of_names:
    pass

# Difference between while loop and for loop
# while loop: use when you don't know how many times you want to loop
# for loop: use when you know how many times you want to loop

# Homework
# 1. Write a program to print numbers from 1 to 10
# 2. Write a program to print numbers from 10 to 1
# 3. Write a program to print even numbers from 1 to 10
# 4. Write a program to print odd numbers from 1 to 10
# 5. Write a program to print numbers from 1 to 10 except 5
# 6. Write a program to print numbers from 1 to 10 except 5 and 7
# 7. Write a program to print numbers from 1 to 10 except 5 and 7 using continue statement
# 8. Write a program to print numbers from 1 to 10 except 5 and 7 using break statement
# 9. Write a program to print numbers from 1 to 10 except 5 and 7 using pass statement
# 10. Write a program to print numbers from 1 to 10 except 5 and 7 using while loop
# 11. Write a program to print numbers from 1 to 10 except 5 and 7 using for loop
# 12. Write a program to print numbers from 1 to 10 except 5 and 7 using for loop and range function
# 13. Write a program to print numbers from 1 to 10 except 5 and 7 using for loop and range function and else statement
# 14. Write a program to print numbers from 1 to 10 except 5 and 7 using for loop and range function and else statement and break statement
# 15. Write a program to print numbers from 1 to 10 except 5 and 7 using for loop and range function and else statement and continue statement
# 16. Write a program to print numbers from 1 to 10 except 5 and 7 using for loop and range function and else statement and pass statement
# 17. Write a program to print numbers from 1 to 10 except 5 and 7 using for loop and range function and else statement and pass statement and break statement
# 18. Write a program to print numbers from 1 to 10 except 5 and 7 using for loop and range function and else statement and pass statement and continue statement
# 19. Write a program to print numbers from 1 to 10 except 5 and 7 using for loop and range function and else statement and pass statement and continue statement and break statement
# 20. Write a program to print numbers from 1 to 10 except 5 and 7 using for loop and range function and else statement and pass statement and continue statement and break statement and nested for loop