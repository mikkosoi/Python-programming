'''
Write multiple functions that print the following information when called:
'''

def dog_sleeps(name, time): #prints: X sleeps Y hours
    print name, " sleeps ", time, " hours"
def dog_walks(name, speed): #prints: X walks Y speed
    print name, " walks ", speed, " speed"
def dog_runs(name, speed):  #prints: X runs Y speed
    print name, " runs ", speed, " speed"
def dog_barks(name, sound): #prints: X barks with a sound Y
    print name, " barks with a sound ", sound
#For example:
name = "Musti"
dog_walks(name, 10) #Musti walks 10.00km/h speed
dog_barks(name,"wuf wuf") # Musti barks with a sound "wuf wuf"
