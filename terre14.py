""" Trier, ou pas ! """

# Créer un programme qui détermine si une liste d'entiers est triée ou non.

# exemples:
#  9   8   3        --->    pas triée !
#  3   8   9  12    --->    triée !
# Yolooo            --->    nope, erreur !


try:
    # Recursive approach to check if an array is sorted or not
    "NORMALY SORTED LIST - Function return 0 is a pair is found unsorted"

    def sortedOrNot(intList):

        # get the length
        lenList = len(intList)

        # Array has one or no element OR the rest is already checked and approved
        if lenList == 1 or lenList == 0:
            return True

        # Recursion (the fuck is this ?) applied till last element
        return intList[0] <= intList[1] and sortedOrNot(intList[1:])

    "REVERSE SORTED LIST - Function return 0 is a pair is found unsorted"

    def revSortedOrNot(intList):

        # get the length
        lenList = len(intList)

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

except ValueError:
    print(" NOOOOOOPE ! ")


# Gives instructions inside the console (doesn't works)
"""
import sys

# Recursive approach to check if an array is sorted or not
###NORMALY SORTED LIST - Function return 0 is a pair is found unsorted
def sortedOrNot(intList):
    
    # get the length
    lenList =len(intList)

    # Array has one or no element OR the rest is already checked and approved
    if lenList == 1 or lenList == 0:
        return True

    # Recursion (the fuck is this ?) applied till last element
    return intList[0] <= intList[1] and sortedOrNot(intList[1:])

###REVERSE SORTED LIST - Function return 0 is a pair is found unsorted
def revSortedOrNot(intList):
    
    # get the length
    lenList =len(intList)

    # Array has one or no element OR the rest is already checked and approved
    if lenList == 1 or lenList == 0:
        return True

    # Recursion (the fuck is this ?) applied till last element
    return intList[0] >= intList[1] and revSortedOrNot(intList[-1:])

#print("Enter as many numbers as you want")
#print("Please, be careful to separate eah number by a space")
# result example ---> "10 20 30"
#userInput = input()
userInput = sys.argv[1]

# result example ---> ['10', '20', '30']
intList = userInput.rsplit()

print(intList) # just to check

# Display the result
if sortedOrNot(intList):
    print(" This shit is sorted")
elif revSortedOrNot(intList):
    print("Sorted but in reverse")
else:
    print("Fuck this shit, I'm out !")
"""
