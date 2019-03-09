x=1

try:
    print "NameError testi:\n"
    print "Tulostetaan x: "
    print x
    print "\nTulostetaan y: "
    print y
except NameError:
    print "NameError! \n"

list=["sika","possu","kissa","apina","kimalainen"]
try:
    print "Listatesti indeksille:\n"
    print list
    print "Tulostetaan apina[3]: "
    print list[3]
    print "Tulostetaan kahdeksas indeksi: "
    print list[6]
except IndexError:
    print "IndexError! \n"

dict = {"A":1,"B":2}
try:
    print "Avainarvoparitesti: "
    print "Dictionary:  %s \n" % dict
    print "Tulostetaan avain[B]: "
    print dict["B\n"]
    print "Tulostetaan avain[C]: "
    print dict["C"]
except KeyError:
    print "KeyError!\n"
