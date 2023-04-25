""" DIVISIONS """

# Créer un programme qui affiche le résultat et le reste d'une division entre deux nombres
import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    """ do the division and gives the result """

    def resultat():
        theResult = a / b
        theResult = int(theResult)
        print("result: %d" % theResult)

    """ calculate the modulo of the division and gives it """

    def reste():
        leftover = a % b
        print("leftover: %d" % leftover)

    if a == 0:
        print("error ! you can't divide 0 by a number !")
    elif b == 0:
        print("error ! you can't divide a number by 0 !")
    else:
        resultat()
        reste()
except ValueError:
    print(" Wrong kind of input ")


# alternative with the "input" statement
"""
a = int(input("enter your first number:"))
b = int(input("enter your first number:")) 

def resultat():
    theResult = a / b
    theResult = int(theResult)
    print("result: %d" % theResult)

def reste():
    leftover = a % b
    print("leftover: %d" % leftover)

if a == 0:
    print("error ! you can't divide 0 by a number !")
elif b == 0:
    print("error ! you can't divide a number by 0 !")
else:
    resultat()
    reste()
"""
