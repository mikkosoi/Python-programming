# -*- coding: UTF-8 -*-
'''
Write a function called vowels that is a given a string and it
returns the number of vowels in that string.
To keep things simple, do not include ö, ä and å.
'''
def vowels(word):
    vokaalit=["a","e","i","o","u"]
    num=0
    for x in word:
        for item in vokaalit:
            if item == x:
                num+=1
    return num

print(vowels("aaa")) # prints: 3
print(vowels("aba")) # prints: 2
print(vowels("bca")) # prints: 1
