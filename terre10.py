""" NOMBRE PREMIER """

# Créer un programme qui affiche si un nombre est premier ou pas

#
# de 0 à 10 ----> 2, 3, 5 et 7 sont des nombres premiers

# selon le Crible d'Eratosthène, de 0 à 100, les chiffres et les nombres finissant par 4, 6, 8 et 0 ne sont PAS des nombres entiers

# divisible par 2 SI dernier chiffre == 0, 2, 4, 6, ou 8
# divisible par 3 SI dernier chiffre == 3, 6 ou 9
# divisible par 5 SI dernier chiffre == 0 ou 5
while 1:
    print("Please, select a number between 0 and 100")
    myNum = int(input("enter your number: "))

    if myNum == 0 or myNum == 1:
        resultat = "%d n'est pas un nombre entier !" % (myNum)
        print(resultat)

    elif myNum == 2 or myNum == 3 or myNum == 5 or myNum == 7:
        resultat = "%d est bien un nombre entier !" % (myNum)
        print(resultat)

    elif (myNum % 2 == 0) or (myNum % 2 == 2) or (myNum % 2 == 4) or (myNum % 2 == 5) or(myNum % 2 == 6) or (myNum % 2 == 8):
        resultat = "%d n'est pas un nombre entier !" % (myNum)
        print(resultat)

    elif (myNum % 3 == 0) or (myNum % 3 == 3) or (myNum % 3 == 6) or (myNum % 3 == 9):
        resultat = "%d n'est pas un nombre entier !" % (myNum)
        print(resultat)

    elif (myNum % 4 == 0) or (myNum % 4 == 2) or (myNum % 4 == 4) or (myNum % 4 == 5) or(myNum % 4 == 6) or (myNum % 4 == 8):
        resultat = "%d n'est pas un nombre entier !" % (myNum)
        print(resultat)

    elif (myNum % 5 == 0) or (myNum % 5 == 5):
        resultat = "%d n'est pas un nombre entier !" % (myNum)
        print(resultat)

    else:
        resultat = " YES ! %d est bien un nombre entier !" % (myNum)
        print(resultat)

# n'oublie pas de gérer les autres exceptions (never trust the user !!!)
# pas de string
# pas de float