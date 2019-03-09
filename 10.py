'''
Write a function called reverse that is given a list and it returns the list in reverse order.
(Using reverse from the standard library is not allowed) Hint: pop
'''
def reverse(lista):
    revved = []
    while lista:
        revved.append(lista.pop())
    return revved


print(reverse([1,2,3,4])) #prints [4,3,2,1]
print(reverse(["aa", "bb", "cc"])) #prints ["cc", "bb", "aa"]
print(reverse([1,2,3,4,5])) #prints [4,3,2,1]
