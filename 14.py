'''
Write a function called division which takes two parameters and divides the
first parameter with the second.
Write an exception handler and make the program to tell the user if there is a ZeroDivisionError.
Otherwise it should return the division of the parameters.
'''
def division(x, y):
    try:
        div = x/float(y)
        return div
    except ZeroDivisionError:
        return "ZeroDivisionError, cannot divide by 0"

print division(23,6)
print division(1,0)
