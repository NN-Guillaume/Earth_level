""" Trouver la Suisse (?) """

# Créer un programme qui prend en paramètre trois entiers et affiche la valeur du milieu

# exemples:
# 11  40  34  --->    le programme doit retourner 34
#  2   1   3  --->    le programme doit retourner 2
# 20  20  20  --->    le programme doit retourner une erreur

import sys

try:
    #Input the 3 values
    val1 = int(sys.argv[1])
    val2 = int(sys.argv[2])
    val3 = int(sys.argv[3])

    #Condition to determine which value is in the MIDDLE
    # if the 3 values are the same, gives a error message:
    if val1 == val2 and val2 == val3:
        print("you have put the same number 3 times.")

    # if same value --- DOESN'T WORKS !
    elif val1 == val2 or val2 == val3 or val1 == val3:
        print("2 options ar the same, can't give the middle number")

    # if val1 have the middle value --- WORKS !
    elif val1 >= val2 and val1 <= val3:
        print(val1)
    elif val1 <= val2 and val1 >= val3:
        print(val1)

    # if val2 have the middle value --- WORKS !
    elif val2 >= val3 and val2 <= val1:
        print(val2)
    elif val2 <= val3 and val2 >= val1:
        print(val2)

    # if val3 have the middle value --- WORKS !
    elif val3 >= val1 and val3 <= val2:
        print(val3)
    elif val3 <= val1 and val3 >= val2:
        print(val3)

    else:
        print("oops ! something wet wrong !")

except ValueError:
    print(" Wrong input ! ")





# alternative with the "input" statement
"""
###Input the 3 values 
val1 = int(input("valeur 1 = "))
val2 = int(input("valeur 2 = "))
val3 = int(input("valeur 3 = "))

###Condition to determine which value is in the MIDDLE
# if the 3 values are the same, gives a error message:
if val1 == val2 and val2 == val3 :
    print("you have put the same number 3 times.")

# ???
elif val1 == val2 or val2 == val3 or val1 == val3:
    print("2 options ar the same, can't give the middle number")

# if val1 have the middle value --- WORKS !
elif val1 >= val2 and val1 <= val3:
    print(val1)
elif val1 <= val2 and val1 >= val3:
    print(val1)


# if val2 have the middle value --- DOESN'T WORKS !
elif val2 >= val3 and val2 <= val1:
    print(val2)
elif val2 <= val3 and val2 >= val1:
    print(val2)

# if val3 have the middle value --- DOESN'T WORKS !
elif val3 >= val1 and val3 <= val2:
    print(val3)
elif val3 <= val1 and val3 >= val2:
    print(val3)

else:
    print("oops ! something wet wrong !")
"""
