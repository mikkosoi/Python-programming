# -*- coding: utf-8 -*-
'''
Write a script that reads the animals from the file,
saves them to a list and prints items on alphabetical order.

Example file.txt:
Rabbit
Pig
Dog
Horse
Bird
'''

f = open("animals.txt", "r")

elukat = f.readlines()
elukat.sort()
for i in range(0,len(elukat)):
    elukat[i]=elukat[i].strip()
    print elukat[i]
f.close()
