#-*- coding:UTF-8 -*-

'''
++ Guessing Game ++
Guess a number between 0 and 20 !
Guess 1/5: a
Not a number, try again
Guess 1/5: 999
The guess should be between 0 and 20, try again
Guess 1/5: -1000
The guess should be between 0 and 20, try again
Guess 1/5: 10
sorry, try again!
Guess 2/5: 5
sorry, try again!
Guess 3/5: 4
sorry, try again!
Guess 4/5: 11
sorry, try again!
Guess 5/5: 12
sorry, try again!
game over, you lost! the correct number was 9
'''
import random
import sys


print "++ Guessing Game ++"
print "Guess a number between 0 and 20 !"
rnd = random.randint(0,20)

for i in range(1,6):
    x = raw_input("Guess %s/5: " % i)

    try:
        guess = int(x)
        if guess == rnd:
            print "Correct!"
            sys.exit()
        elif guess not in range(0,20):
            print "The guess should be between 0 and 20, try again"
        else:
            print "Wrong, try again!"

        if i==5:
            print "game over, you lost! the correct number was", rnd
    except ValueError:
        print "Not a number, try again"
        if i==5:
            print "game over, you lost! the correct number was", rnd
