""" PUISSANCE D'UN NOMBRE """

# Créer un programme qui affiche le résultat d'une puissance

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