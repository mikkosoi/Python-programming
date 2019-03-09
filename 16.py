import sys

def div(x,y):
    try:
        tulos = x/float(y)
        return tulos
    except:
        print("ZeroDivisionError, cannot divide by 0")
        sys.exit()

try:
    print div(1,3)
    print div(1,3,7)
except TypeError:
    print("Wrong amount of parameters")
