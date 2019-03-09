# -*- coding: utf-8 -*-
import sys
'''
Write a Python script that acts a simple calculator.
The script should present the user with a list of numbered actions to perform (addition, substraction, division or multiplication) and two numbers afer that.

If the user inputs an invalid choice the program should print an error and prompt the user to try again.
If the user inputs anything else than numbers the program should print an error and prompt the user to try again.
If the user attempts to divide by zero the program should print an error message.
Print the result as a float
If the user inputs -1 when choosing the action, the program should terminate.
Try to utilize the fact that Python has functions as first class values! You can for example place anonymous functions inside a variables and call them or use reduce function.

Example execution:

0) add
1) sub
2) multiply
3) divide
-1) quit
choice: 0
number: 1
number: 2
The result is: 3.000000
0) add
1) sub
2) multiply
3) divide
-1) quit
choice: 2
number: 5
number: 5
The result is: 25.000000
0) add
1) sub
2) multiply
3) divide
-1) quit
choice: -1
'''

def add(num1, num2):
    result = num1+float(num2)
    return result

def sub(num1, num2):
    result = num1-float(num2)
    return result

def multiply(num1, num2):
    result = num1*float(num2)
    return result

def divide(num1, num2):
    try:
        result = num1/float(num2)
        return result
    except ZeroDivisionError:
        return "cannot divide by zero!"

def main():
    while True:
        print "0) add"
        print "1) subtract"
        print "2) multiply"
        print "3) divide"
        print "-1) quit"
        choise = raw_input("Choose: ")
        if choise=="0" or choise == "1" or choise == "2" or choise == "3":
            number1 = raw_input("Enter number 1: ")
            number2 = raw_input("Enter number 2: ")
            if choise == "0":
                try:
                    print "result is ", add(int(number1), int(number2))
                except TypeError:
                    print "data type mismatch"
                except:
                    print "Something went wrong"
            elif choise == "1":
                try:
                    print "result is ", sub(int(number1), int(number2))
                except TypeError:
                    print "data type mismatch"
                except:
                    print "Something went wrong"
            elif choise == "2":
                try:
                    print "result is ", multiply(int(number1), int(number2))
                except TypeError:
                    print "data type mismatch"
                except:
                    print "Something went wrong"
            elif choise == "3":
                try:
                    print "result is ", divide(int(number1), int(number2))
                except TypeError:
                    print "data type mismatch"
                except:
                    print "Something went wrong"
        elif choise =="-1":
            sys.exit()
        else:
            print "invalid option"


main()
