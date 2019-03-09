#-*- coding: UTF-8 -*-
'''
Extend the function in the previous assignment to handle TypeError which is caused when you try to divide a number with a non-number (e.g. character).
'''


def calculator(cmd, num1, num2):
    try:
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
    except TypeError:
        return "Non numeral value"
    #else:
    #    return ("invalid function")

print(calculator("add", 1, 2)) #should print 3
print(calculator("sub", 1, 2)) #should print -1
print(calculator("multiply", 1, 2)) #should print 2
print(calculator("divide", 1, 2)) #should print 0.5
print(calculator("divide", 1, 0)) #should print 0.5
print(calculator("add", "x", 2)) #should print error
