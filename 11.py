'''
Write a function called sum2 that takes a number and sums all the numbers
starting from 0 up to that number.
'''

def sum2(num):
    summa=0
    while num >= 0:
        summa=summa+num
        num=num-1
    return summa


print(sum2(3)) #prints: 6
print(sum2(12)) #prints: 78
