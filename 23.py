#-*- coding: UTF-8 -*-
'''
Write a function called calculator that takes 3 parameters:

A string which can be either “add”, “sub” or “multiply”
A number
Another number

When the string is:
add, the two numbers are added together and the result is returned from the function.
sub, the two numbers are subtracted and the result is returned from the function
multiply, the two numbers are multiplied and the result is returned from the function.

In other words, the function should work like this:

print(calculator("add", 1, 2)) #should print 3
print(calculator("sub", 1, 2)) #should print -1
print(calculator("multiply", 1, 2)) #should print 2
'''

def calculator(cmd, num1, num2):

    if cmd =="add":
        return num1+num2
    elif cmd =="sub":
        return num1-num2
    elif cmd == "multiply":
        return num1*num2
    else:
        return ("invalid function")

print(calculator("add", 1, 2)) #should print 3
print(calculator("sub", 1, 2)) #should print -1
print(calculator("multiply", 1, 2)) #should print 2
print(calculator("div", 1, 2)) #should print 2
