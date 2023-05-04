""" AFFICHEUR D'ARGUMENT """

# display the arguments inside a list

import sys

arguments = len(sys.argv) - 1

position = 1

while arguments >= position:
    print(position, sys.argv[position])
    position = position + 1

