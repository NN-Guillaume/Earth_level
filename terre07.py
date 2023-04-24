""" TAILLE D'UNE CHAÎNE """

# Créer un programme qui affiche le nombre de caractères d'une chaîne de caractères passée en argument

import sys

char_to_count = str(sys.argv[1])

""" gives you the length of a string"""
def countString():
    print(len(char_to_count))

countString()





# alternative with the "input" statement
"""
#char_to_count = input("enter your chain of characters: ")

def countString():
    print(len(char_to_count))

countString()
"""