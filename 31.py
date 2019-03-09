# -*- coding: utf-8 -*-
'''
Append functionality to a assignment 30.
Add user a possibility to delete existing items from the file.
'''
import sys

def printFile():
    f = open("animals.txt", "r")
    elukat = f.readlines()
    elukat.sort()
    for i in range(0,len(elukat)):
        elukat[i]=elukat[i].strip()
        print elukat[i]
    print "\n"
    f.close()


def addStuff():
    f = open("animals.txt", "a")
    add = raw_input("Anna lisättävä eläin: ")
    f.write(add+"\r\n")
    f.close()

def deleteStuff():
    print "Eläimet listassa: \n"
    printFile()
    option = raw_input("Anna poistettava tieto: ")
    f = open("animals.txt","r")
    elukat = f.readlines()
    for i in range(0, len(elukat)):
        elukat[i]=elukat[i].strip()
    f.close()

    elukat.remove(option)

    with open("animals.txt", "w") as f:
        for item in elukat:
            f.write("{}\n".format(item))



def main():
    while True:
        print "Valitse toiminto: "
        print "(T)ulosta aakkostettuna"
        print "(L)isää listaan"
        print "(P)oista tieto"
        print "Lopeta (Q)"
        option = raw_input("Valintasi: ")


        if option == "T" or option  == "t":
            printFile()
        elif option == "L" or option == "l":
            addStuff()
        elif option == "Q" or option == "q":
            sys.exit()
        elif option == "P" or option == "p":
            deleteStuff()
        else:
            print "Ei toimintoa käskyllä %s" % option

main()
