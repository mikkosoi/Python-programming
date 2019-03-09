#-*- coding: UTF-8 -*-
'''
Add a divide operation to your calculator from the previous assignment and make sure it can handle division by zero(use try and except). If a division by zero occurs return None.

Note: Returning None like this is usually not the correct choice, but in this case it is done for simplicity.
'''


def calculator(cmd, num1, num2):

    if cmd == "add":
        return num1+num2
    elif cmd == "sub":
        return num1-num2
    elif cmd == "multiply":
        return num1*num2
    elif cmd == "divide":
        try:
            return num1/float(num2)
        except ZeroDivisionError:
            return None
    #else:
    #    return ("invalid function")

print(calculator("add", 1, 2)) #should print 3
print(calculator("sub", 1, 2)) #should print -1
print(calculator("multiply", 1, 2)) #should print 2
print(calculator("divide", 1, 2)) #should print 0.5
print(calculator("divide", 1, 0)) #should print 0.5
