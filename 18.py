#-*- coding:UTF-8 -*-

thedict = {
    "List1": ["Bob","Comes","After","You"],
    "List2": [100,"Hello"]
}

# function takes a dict, a list name and the element
def add_to_list_in_dict(thedict, listname, element):
    try:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))
    except KeyError:
        print("The dict don't have a following key %s" % (listname))
    else:
        print "Jotain muuta tapahtui"
    finally:
        print "Dictionary after function call ", thedict

add_to_list_in_dict(thedict, "List1", "Hellou")
add_to_list_in_dict(thedict, "Book", "Page1")
add_to_list_in_dict(thedict, "List2", "randomrandom")
