# -*- coding: UTF-8 -*.

'''
Update your function so that when the user calls the function with wrong type
as a parameter it says "One or both of your parameters are wrong type!"
(Don't remove the ZeroDivision exception!)
'''
yks = raw_input("Annappa yks: ")
kaks = raw_input("Annappa toenen: ")
def division(x, y):
    try:
        div = x/float(y)
        return div
    except ZeroDivisionError:
        return "ZeroDivisionError, cannot divide by 0"
try:
    print division(int(yks),int(kaks))
except ValueError:
    print "One or both of your parameters are wrong type!"
