""" INVERSER UNE CHAÎNE """

# Créer un programme qui affiche l'inverse de la chaîne de caractères donnée en argument

str_to_reverse = input("enter your chain of characters: ")

def reverseString():
    print(str_to_reverse[::-1])


if len(str_to_reverse) <= 1:
    print("Can't reverse this. You must use 2 characters at least")
else:
    reverseString()