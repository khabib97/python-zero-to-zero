# Q: what is variable?
# A: variable is a container for a value, which can be of various types
# Example:  x = 5

# keep in mind that variable name can be anything, but it should be meaningful
# put 5 in x and print it
print("[info]: Basic variable")
x = 5
print(x)  # should print 5

# put 10 in y and print it
y = 10
print(y)  # should print 10

print("[info]: Basic variable, computer do some calculation on behalf of you")
# you can use this and do some calculation
print(x + y)  # should print 15
print(y - x)  # should print 5
print(x * y)  # should print 50
print(y / x)  # should print 2.0
print(x * 2)  # should print 10

print("[info]: Store different types of data in a variable")
# Even you can store Character in a variable
a = 'A'
print(a)  # should print A

# Even you can store String in a variable
name = 'John Doe'
print(name)  # should print John Doe

# Even you can store Boolean in a variable
is_active = True
print(is_active)  # should print True

# You can ignore this for now. We will cover this later
# Advance type of variable
print("[info]: Store list, dictionary, range... in a variable")

# Even you can store List in a variable
print("[info]: List is a collection which is ordered and changeable. Allows duplicate members.")
list_of_names = ['John Doe', 'Jane Doe', 'John Smith']
print(list_of_names)  # should print ['John Doe', 'Jane Doe', 'John Smith']

# Even you can store Dictionary in a variable
print("[info]: Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.")
person = {'name': 'John Doe', 'age': 25, 'is_active': True}
print(person)  # should print {'name': 'John Doe', 'age': 25, 'is_active': True}
print(person['name'])  # should print John Doe
print(person['age'])  # should print 25
print(person['is_active'])  # should print True