""" TERRE: OK !!! """

# Créer un programme qui célébre ta victoire.

# Exemple: " Jai terminé l'épreuve de la Terre et c'était [insert whatever the fuck you want here]"

import random

complain1 = " si CA s'était facile, et ben bordel j'imagine pas la suite ! "
complain2 = " je ne suis quand même pas rassurer ! "
complain3 = " on a tous un côté maso et le code est le meilleur moyen de le faire ressortir !  ;-p "

randomChoice = random.randint(1, 3)
if randomChoice == 1:
    randomChoice = complain1
    print(complain1)
elif randomChoice == 2:
    randomChoice = complain2
    print(complain2)
elif randomChoice == 3:
    randomChoice = complain3
    print(complain3)
else:
    print(" si cette phrase s'affiche, alors j'ai foiré mon programme  :^) ")

print(" Le soleil chante, les oiseaux brillent (et parfois l'inverse aussi) et... ")
print(
    " ... après avoir fait la nique à ces FDP (Faux Doctorants en Programmation) d'OpenClassRooms ..."
)
print("... je me sens un peu fier et heureux d'avoir terminer l'épreuve de la Terre...")
print("... même s' il faut bien dire que %s " % (randomChoice))
