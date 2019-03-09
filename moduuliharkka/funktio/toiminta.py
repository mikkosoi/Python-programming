def tulosta(countrycodes,codemap,countries):
    for maakoodi in countrycodes:
        print codemap[maakoodi]
        print  "\thead honcho:", countries[codemap[maakoodi]]["head honcho"][0], "who is", countries[codemap[maakoodi]]["head honcho"][1],"years old"
        print  "\tpopulation:", countries[codemap[maakoodi]]["population"], "million\n"
