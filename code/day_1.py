# Before running the code, read every comment carefully and try to understand what is going on in the code

print("[info] Basic print ")
# Write a program that print 0
print(0)  # should print 0

print("[info] Basic print, old school way")
# Write a program that print 0 t 10
print(0)  # should print 0
print(1)  # should print 1
print(2)  # should print 2
print(3)  # should print 3
print(4)  # should print 4
print(5)  # should print 5
print(6)  # should print 6
print(7)  # should print 7
print(8)  # should print 8
print(9)  # should print 9
print(10)  # should print 10

print("[info] Basic print, computer write on behalf of you, smart way")
# Write a program that print 1 to 10
for i in range(1, 11, 1):
    print(i)  # should print 1 2 3 4 5 6 7 8 9 10

print("[info] Basic print, computer reverse and print on behalf of you, smart way")
# Write a program that print 1 to 10 in reverse order
# print in the same line
for i in range(10, 0, -1):
    print(i, end=' ')  # should print 10 9 8 7 6 5 4 3 2 1

# TODO: Write a program that print 0 to 100 in reverse order, in the same line
