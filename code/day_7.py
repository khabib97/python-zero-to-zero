# Function in Python
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# In Python a function is defined using the def keyword:
# def function_name():
#   statement
#   return something
print("[info]: Basic function")


def basic_function():
    print("Hello from a function")


# call basic_function to execute it
basic_function()  # should print Hello from a function

print("[info]: Basic function with parameter")


def basic_function_with_parameter(name):
    print(f"Hello {name}")


# call basic_function_with_parameter to execute it
basic_function_with_parameter("John Doe")  # pass John Doe as parameter to basic_function_with_parameter

print("[info]: Basic function with parameter and return value")


def basic_function_with_return_value(x):
    return x * 10


invest = 10
evaly_cashback = basic_function_with_return_value(100)
print(f"investment {invest} vs return {evaly_cashback}")  # should print 10 vs return 1000
# disclaimer: evaly is a local e-commerce scammer in Bangladesh, just for fun add this example

# Power of function, by using function you can do complex calculation very easily
# You can call a function from another function
print("[info]: Basic function with another function")
function = basic_function_with_return_value(5)
basic_function_with_parameter(function)  # should print Hello 50


# Homework
# 1. Write a function to print numbers from 1 to 10
# 2. Write a function to print numbers from 10 to 1
# 3. Write a function to print even numbers from 1 to 10
# 4. Write a function to print odd numbers from 1 to 10
# 5. Write a function to print numbers from 1 to 10 except 5
