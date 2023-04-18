""" PAIR OU IMPAIR """

# Créer un programme qui de déterminer si l'argument donné un entier  pair ou impair.

# Attention aux entiers négatifs !
while True:
    try:
        user_number = int(input("enter your number:"))
        
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
