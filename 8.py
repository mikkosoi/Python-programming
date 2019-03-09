'''
Create a function, called sum that takes a list of numbers as a parameter and it returns the sum of the numbers in the list.
'''
#example lists:
list1 = [1,2,3,4,5] #the function should return 15
list2 = [1,1,1,1]   #the function should return 4

def sum(lista):
    summa=0
    for item in lista:
        summa+=item
    return summa

print sum(list1)
