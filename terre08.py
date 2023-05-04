""" PUISSANCE D'UN NOMBRE """

# Créer un programme qui affiche le résultat d'une puissance

import sys

try:
    while True:
        baseNumber = int(sys.argv[1])
        powerNumber = int(sys.argv[2])
        break

    def powerMath():
        powerResult = baseNumber ** powerNumber
        print(powerResult)

    if powerNumber <= 0:
        print("negative value are forbiden for the power number")
    else:
        powerMath()

except ValueError:
    print(" Wrong input ! ")
















# alternative with the "input" statement
"""
while True:
    try:
        baseNumber = int(input("Enter your base number: "))
        powerNumber = int(input("Enter your power number: "))
        break
    except ValueError:
        print(" NOPE ! That is NOT an \"int\" !!!")

def powerMath():
    powerResult = baseNumber ** powerNumber
    print(powerResult)

if powerNumber <= 0:
    print("negative value are forbiden for the power number")
else:
    powerMath()
"""
