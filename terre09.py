""" RACINE CARREE D'UN NOMBRE """

# Créer un programme qui affiche la racine carrée d'un entier positif

# ATTENTION ! la méthode  math.sqrt(\"nombre de base à convertir\") est ici interdite TT__TT


#-------------------------------------------------------------------------------------------------------------------------------------

print("please, use a number between 0 and 100.")
randomNumber = int(input("enter your number: "))

for x in range (100):
    square = x**2
    
    if square == randomNumber:
        result = "%d is the square root of %d" % (x, randomNumber)
        print (result)
        break
    
    if randomNumber <= 0:
        print ("you can't go under 0")
        break

    if randomNumber >= 100:
        print ("you can't go beyond 100")
        break



#-------------------------------------------------------------------------------------------------------------------------------------

""" POUR RAPPEL   --->  la méthode  math.sqrt(\"nombre de base à convertir\")   s'occupe de calculée les racines carrées  ;-) """

"""
import math

# print the square root of 81
print(math.sqrt(81))
#resultat =  9
"""