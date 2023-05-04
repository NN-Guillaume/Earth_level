""" TAILLE D'UNE CHAÎNE """

# Créer un programme qui affiche le nombre de caractères d'une chaîne de caractères passée en argument

import sys
# mettre un compteur et parcourir la string --> une lettre = +1
# plus souvent for que while
try:
    char_to_count = str(sys.argv[1])

    #gives you the length of a string
    def countString():
        print(len(char_to_count))

    countString()
except ValueError:
    print(" Error ")






















# alternative with the "input" statement
"""
#char_to_count = input("enter your chain of characters: ")

def countString():
    print(len(char_to_count))

countString()
"""
