""" AFFICHEUR D'ARGUMENT """

import sys

# print(sys.argv) # display the arguments inside a list

arguments = len(sys.argv) - 1

position = 1

while (arguments >= position):
    #print("Parameter %i: %s" % (position, sys.argv[position]))
    print(position, sys.argv[position])
    position = position + 1

# What the fuck is this shit ? ! ! !