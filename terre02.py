""" AFFICHEUR D'ARGUMENT """

import sys

print(sys.argv) # dois-je utiliser ce truc ?

# Créer un programme qui affiche les arguments qu'il reçoit ligne par ligne, peu importe le nombre d'arguments.
""""
def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

foo(1, 2, 3, 4, 5)
"""
# First: 1
# Second: 2
# Third: 3
# And all the rest... [4, 5]

"""
def display_args():
    arguments = input("enter your arguments:")
    print("your input is:" + arguments)
    for charac in arguments:
        charac = arguments.splitlines()
    print(charac)

display_args()
"""