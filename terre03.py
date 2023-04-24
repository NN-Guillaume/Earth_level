""" L' ALPHABET A PARTIR DE """

# Créer un programme qui affiche l'alphabet à partir de la lettre donnée en argument, en lettre minuscule, suivi d'un retour à la ligne.

""" display the alphabet from a given letter """
def alphabet_from():
    #youn need to enter a letter to display the alphabet from this letter
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    listAlpha = alphabet.rsplit(" ")
    #print(listAlpha)
    myLetter = input()
    
    startingPoint = listAlpha.index(myLetter)    # put the starting letter (corresponding index) into a value
    resultat = listAlpha[startingPoint:]              # resultat = in listAlpha, from my input, print the remaining elements of the list.
    
    print(resultat)

alphabet_from()