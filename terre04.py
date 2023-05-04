""" PAIR OU IMPAIR """

# Créer un programme qui de déterminer si l'argument donné est un entier pair ou impair.

import sys

while True:
    try:
        # input
        userNber = int(sys.argv[1])
        print("you have chose %d as number" % (userNber))

        if type(userNber) != int:
            print("Nope, you must choose a number")
        elif type(userNber) == str:
            print("no entry")
        elif userNber == 0:
            print(" That is a good question  :-)")
        elif userNber <= 0:
            print("negative input")
        else:
            pass

        if (userNber % 2) == 1: # vérif toujours point positif
            print("Impair")
        else:
            print("Pair")

    except ValueError:
        print(" NOPE ! That is not an INT !!!")
    break











# alternative with the "input" statement
"""
while True:
    try:
        user_number = int(input("enter your number:"))
        #user_number = sys.argv[1]
        
        if type(user_number) != int:
            print("NOPE !")
        else:
            pass

        if (user_number % 2) == 1: 
            print("impair")
        else:
            print("pair")
        break
    
    except ValueError:
        print(" NOPE ! That is not an INT !!!")
"""
