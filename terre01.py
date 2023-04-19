""" NOM DU PROGRAMME """

import os

# Créer un programme qui affiche son nom de fichier
file_name = os.path.basename('C:/Users/guill/Desktop/GALAXY/ENTREPRENEUR/Coding Accelerator/02_Epreuves/00_TERRE/Earth_Level/terre01.py')
print(file_name)


# alternative 01
"""
def file_name():
    path = 'C:/Users/guill/Desktop/GALAXY/ENTREPRENEUR/Coding Accelerator/02_Epreuves/00_TERRE/Earth_Level/terre01.py'
    print(os.path.basename(path).split('/')[-1])

file_name()
"""

# alternative 02
"""
file_path = 'C:/Users/guill/Desktop/GALAXY/ENTREPRENEUR/Coding Accelerator/02_Epreuves/00_TERRE/Earth_Level/terre01.py' # file path

# using basename function from os
# module to print file name
file_name = os.path.basename(file_path)

print(file_name)
"""

# alternative 03
"""
file_path = 'C:/Users/guill/Desktop/GALAXY/ENTREPRENEUR/Coding Accelerator/02_Epreuves/00_TERRE/Earth_Level/terre01.py'

file_name = os.path.basename(file_path)
file = os.path.splitext(file_name)

print(file)  # returns tuple of string

print(file[0] + file[1])
"""

# l'alternative aussi intelligente que cet exercice à la con (niveau débutant, il faut pondre ça tout seul ?!)
"""
def display_file_name():
    file_name = "terre01.py"
    print(file_name)

display_file_name()
"""