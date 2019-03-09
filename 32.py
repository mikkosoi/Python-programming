# -*- coding: utf-8 -*-
import sys

def printFile(file):
    f = open(file, "r")
    text = f.readlines()
    for i in range(0,len(text)):
        text[i]=text[i].strip()
        print text[i]
    print "\n"
    f.close()

def main():

    try:
        if len(sys.argv) >= 1:
            try:
                filename = sys.argv[1]
                printFile(filename)
            except IOError:
                print "No file %s found!" % filename
    except:
        print "Not enough arguments"
        print "Usage: 32.py <filename>"

main()
