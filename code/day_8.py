# Python List
#  is a collection which is ordered and changeable. Allows duplicate members.

# Why list is so important when you are learning programming?
# Because list is the most used data structure in programming.
# You can store anything in a list, even another list.

# How to create a list?
# my_list = ["apple", "banana", "cherry"]
# print(my_list)  # should print ['apple', 'banana', 'cherry']
print("[info]: Basic list")
my_list = ["apple", "banana", "cherry"]
print(my_list)  # should print ['apple', 'banana', 'cherry']

# How to access list items?
# my_list = ["apple", "banana", "cherry"]
# print(my_list[0])  # should print apple
# print(my_list[1])  # should print banana
# print(my_list[2])  # should print cherry
print("[info]: Basic list access")
my_list = ["apple", "banana", "cherry"]
print(my_list[0])  # should print apple
# Important Note: In programming, counting starts from 0, not 1

# How to change the value of a specific item in a list?
# my_list = ["apple", "banana", "cherry"]
# my_list[0] = "orange"
# print(my_list)  # should print ['orange', 'banana', 'cherry']
print("[info]: Basic list change value")
my_list = ["apple", "banana", "cherry"]
my_list[0] = "orange"
print(my_list)  # should print ['orange', 'banana', 'cherry']

# How to loop through a list?
# my_list = ["apple", "banana", "cherry"]
# for item in my_list:
#     print(item)  # should print apple banana cherry
print("[info]: Basic list loop")
my_list = ["apple", "banana", "cherry"]
for item in my_list:
    print(item)  # should print apple banana cherry

# How to check if an item exists in a list?
# my_list = ["apple", "banana", "cherry"]
# if "apple" in my_list:
#     print("Yes, 'apple' is in the fruits list")  # should print Yes, 'apple' is in the fruits list
print("[info]: Basic list check item")
my_list = ["apple", "banana", "cherry"]
if "apple" in my_list:
    print("Yes, 'apple' is in the fruits list")  # should print Yes, 'apple' is in the fruits list

# How to get the length of a list?
# my_list = ["apple", "banana", "cherry"]
# print(len(my_list))  # should print 3
print("[info]: Basic list length")
my_list = ["apple", "banana", "cherry"]
print(len(my_list))  # should print 3

# How to add an item to the end of a list?
# my_list = ["apple", "banana", "cherry"]
# my_list.append("orange")
# print(my_list)  # should print ['apple', 'banana', 'cherry', 'orange']
print("[info]: Basic list add item")
my_list = ["apple", "banana", "cherry"]
my_list.append("orange")
print(my_list)  # should print ['apple', 'banana', 'cherry', 'orange']

# How to add an item at the specified index?
# my_list = ["apple", "banana", "cherry"]
# my_list.insert(1, "orange")
# print(my_list)  # should print ['apple', 'orange', 'banana', 'cherry']
print("[info]: Basic list add item at specified index")
my_list = ["apple", "banana", "cherry"]
my_list.insert(1, "orange")

# How to remove an item?
# my_list = ["apple", "banana", "cherry"]
# my_list.remove("banana")
# print(my_list)  # should print ['apple', 'cherry']
print("[info]: Basic list remove item")
my_list = ["apple", "banana", "cherry"]
my_list.remove("banana")
print(my_list)  # should print ['apple', 'cherry']

# How to remove the last item?
# my_list = ["apple", "banana", "cherry"]
# my_list.pop()
# print(my_list)  # should print ['apple', 'banana']
print("[info]: Basic list remove last item")
my_list = ["apple", "banana", "cherry"]
my_list.pop()
print(my_list)  # should print ['apple', 'banana']

# How to remove an item at the specified index?
# my_list = ["apple", "banana", "cherry"]
# my_list.pop(1)
# print(my_list)  # should print ['apple', 'cherry']
print("[info]: Basic list remove item at specified index")
my_list = ["apple", "banana", "cherry"]
my_list.pop(1)
print(my_list)  # should print ['apple', 'cherry']

# How to empty a list?
# my_list = ["apple", "banana", "cherry"]
# my_list.clear()
# print(my_list)  # should print []
print("[info]: Basic list empty")
my_list = ["apple", "banana", "cherry"]
my_list.clear()
print(my_list)  # should print []

# How to copy a list?
# my_list = ["apple", "banana", "cherry"]
# new_list = my_list.copy()
# print(new_list)  # should print ['apple', 'banana', 'cherry']
print("[info]: Basic list copy")
my_list = ["apple", "banana", "cherry"]
new_list = my_list.copy()
print(new_list)  # should print ['apple', 'banana', 'cherry']

# How to join two lists?
# list_one = ["a", "b", "c"]
# list_two = [1, 2, 3]
# list_three = list_one + list_two
# print(list_three)  # should print ['a', 'b', 'c', 1, 2, 3]
print("[info]: Basic list join")
list_one = ["a", "b", "c"]
list_two = [1, 2, 3]
list_three = list_one + list_two
print(list_three)  # should print ['a', 'b', 'c', 1, 2, 3]

# How to create a list using list constructor?
# my_list = list(("apple", "banana", "cherry"))
# print(my_list)  # should print ['apple', 'banana', 'cherry']

print("[info]: Basic list constructor")
my_list = list(("apple", "banana", "cherry"))
print(my_list)  # should print ['apple', 'banana', 'cherry']
# What is constructor?
# A constructor is a special kind of method that Python calls when it instantiates an object using the definitions found

# How to sort a list?
# my_list = [100, 50, 65, 82, 23]
# my_list.sort()
# print(my_list)  # should print [23, 50, 65, 82, 100]
print("[info]: Basic list sort")
my_list = [100, 50, 65, 82, 23]
my_list.sort()
print(my_list)  # should print [23, 50, 65, 82, 100]
# What is sorting?
# Sorting means putting elements in a ordered sequence.
# Sorting can be done in ascending or descending order.
# python sort() method sorts the list ascending by default.

# How to sort a list in descending order?
# my_list = [100, 50, 65, 82, 23]
# my_list.sort(reverse=True)
# print(my_list)  # should print [100, 82, 65, 50, 23]
print("[info]: Basic list sort in descending order")
my_list = [100, 50, 65, 82, 23]
my_list.sort(reverse=True)
print(my_list)  # should print [100, 82, 65, 50, 23]

# How to reverse a list?
# my_list = ["apple", "banana", "cherry"]
# my_list.reverse()
# print(my_list)  # should print ['cherry', 'banana', 'apple']
print("[info]: Basic list reverse")
my_list = ["apple", "banana", "cherry"]
my_list.reverse()
print(my_list)  # should print ['cherry', 'banana', 'apple']

# How to loop through the index numbers?
# my_list = ["apple", "banana", "cherry"]
# for index in range(len(my_list)):
#     print(my_list[index])  # should print apple banana cherry
print("[info]: Basic list loop through index numbers")
my_list = ["apple", "banana", "cherry"]
for index in range(len(my_list)):
    print(my_list[index])  # should print apple banana cherry

# How to loop using while loop?
# my_list = ["apple", "banana", "cherry"]
# i = 0
# while i < len(my_list):
#     print(my_list[i])  # should print apple banana cherry
#     i += 1
print("[info]: Basic list loop using while loop")
my_list = ["apple", "banana", "cherry"]
i = 0
while i < len(my_list):
    print(my_list[i])  # should print apple banana cherry
    i += 1









