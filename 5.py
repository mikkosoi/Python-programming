lista = []
while True:
    feed = raw_input("VALITSE: (L)isaa arvo, (P)oista arvo tai (T)ulosta lista ja lopeta): ")
    if (feed == "T"):
            for item in lista:
                print item
            break
    elif (feed == "L"):
        value = raw_input("Anna lisattava arvo: ")
        lista.append(value)
    elif (feed == "P"):
        value = raw_input("Anna poistettava arvo: ")
        lista.remove(value)
