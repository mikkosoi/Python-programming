'''
Write a function called largest that is given a list of numbers and the function returns the largest number in the list.
'''
list1 = [10,2,99,4,11] #the function should return 15

def largest(lista):
    max=0
    for item in lista:
        if item > max:
            max=item
    return max

print largest(list1)
