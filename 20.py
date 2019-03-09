# -*- coding: utf-8 -*-
'''
Take values from the previous assignment and write a Python script that does the following:
Iterates the countrycodes list, uses the codemap dict to get the key name for the country in question and
prints the information from the countries dict formatted like this:

finland:
    head honcho: Juha Sipila, who is 54 years old
    population: 5.439000 million
sweden:
    head honcho: Stefan Lofven, who is 58 years old
    population: 9.593000 million
norway:
    head honcho: Erna Solberg, who is 54 years old
    population: 5.084000 million
Use \n and ‘\t’ to format the output.

Note: The printing must be done using iteration (for) and dict lookups(x[y] syntax), manually printing each value will not count as a correct answer!
'''
countrycodes = ["fi", "se", "no"]
codemap = {"fi":"Finland","se":"Sweden","no":"Norway"}
countries = {"Finland" : {"head honcho": ("Juha Sipilä", 54),"population":5.439}, "Sweden" : {"head honcho": ("Steven Löfven", 58), "population":9.593},"Norway" : { "head honcho": ("Erna Solberg",54), "population":5.084}}

for maakoodi in countrycodes:
    print codemap[maakoodi]
    print  "\thead honcho:", countries[codemap[maakoodi]]["head honcho"][0], "who is", countries[codemap[maakoodi]]["head honcho"][1],"years old"
    print  "\tpopulation:", countries[codemap[maakoodi]]["population"], "million\n"
