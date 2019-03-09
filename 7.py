def compare(x,y):
    '''
    Make a function which takes two parameters, sums them up and checks if the sum is divisible by 2.
    If it is print "Yes it is!" and if not "Nope." (tip: %)
    '''
    sum = x+y
    if sum % 2 == 0:
        print "Yes it is!"
    else:
        print "Nope"
compare(2,9)
