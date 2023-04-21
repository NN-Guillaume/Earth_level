""" Trier, ou pas ! """

# Créer un programme qui détermine si une liste d'entiers est triée ou non.

#exemples:   
#  9   8   3        --->    pas triée !
#  3   8   9  12    --->    triée !
# Yolooo            --->    nope, erreur !

# Recursive approach to check if an array is sorted or not
""" NORMALY SORTED LIST - Function return 0 is a pair is found unsorted """
def sortedOrNot(intList):
    
    # get the length
    lenList =len(intList)

    # Array has one or no element OR the rest is already checked and approved
    if lenList == 1 or lenList == 0:
        return True

    # Recursion (the fuck is this ?) applied till last element
    return intList[0] <= intList[1] and sortedOrNot(intList[1:])

""" REVERSE SORTED LIST - Function return 0 is a pair is found unsorted """
def revSortedOrNot(intList):
    
    # get the length
    lenList =len(intList)

    # Array has one or no element OR the rest is already checked and approved
    if lenList == 1 or lenList == 0:
        return True

    # Recursion (the fuck is this ?) applied till last element
    return intList[0] >= intList[1] and revSortedOrNot(intList[-1:])

print("Enter as many numbers as you want")
print("Please, be careful to separate eah number by a space")
# result example ---> "10 20 30"
userInput = input()

# result example ---> ['10', '20', '30']
intList = userInput.rsplit()

# Display the result
if sortedOrNot(intList):
    print(" This shit is really sorted now ?")
elif revSortedOrNot(intList):
    print("Sorted but in reverse")
else:
    print("fuck this shit, I'm out !")

#--------------------------------------------------------------------------------------------------------------------------------------------
# now I must find a way to analyze this shit.
# idea is " for a length L " ---> " if array.index I is superior to I+" and " if I+ is superior to I++" ---> " list is in order"
"""
    # for 2 numbers
if intList[0] <= intList[1]:
    print("2 in ascending order !!!")
elif intList[0] >= intList[1]:
    print("2 in descending order!!!")
# for 3 numbers
elif intList[0] >= intList[1] and intList[1] <= intList[2]:
    print("3 in ascending order !!!")
elif intList[0] >= intList[1] and intList[1] >= intList[2]:
    print("3 in descending order !!!")
# for 4 numbers
elif intList[0] >= intList[1] and intList[1] <= intList[2] and intList[2] <= intList[3]:
    print("4 in ascending order !!!")
elif intList[0] >= intList[1] and intList[1] >= intList[2] and intList[2] <= intList[3]:
    print("4 in descending order !!!")
# for 5 numbers
elif intList[0] >= intList[1] and intList[1] <= intList[2] and intList[2] <= intList[3] and intList[3] <= intList[4]:
    print("5 in ascending order !!!")
elif intList[0] >= intList[1] and intList[1] >= intList[2] and intList[2] <= intList[3] and intList[3] <= intList[4]:
    print("5 in descending order !!!")
else:
    print("HEEEEEEEEELLLLLLP !!!")
"""