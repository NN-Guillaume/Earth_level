""" Trier, ou pas ! """

# Créer un programme qui détermine si une liste d'entiers est triée ou non.

#exemples:   
#  9   8   3        --->    pas triée !
#  3   8   9  12    --->    triée !
# Yolooo            --->    nope, erreur !

""" Input the list of values """
"""
# I will need to be able to mess with several arguments (no precise number ???) 
#let's start this shit with 3 values
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
intList = [a, b, c]
"""

""" Condition to determine which value is in the MIDDLE """
"""
# if the 3 values are the same, gives a error message:
if a <= b and b <= c:
    print("the list is in order")
elif a >= b and b >= c:
    print("the list is in order")

else:
    print("NOPE ! this is not in order at all")
"""
#---------------------------------------------------------------------------------------------------------------------

"""
# now I must find a way to analyze this shit.

# idea is " for a length L " ---> " if array.index I is superior to I+" and " if I+ is superior to I++" ---> " list is in order"
for x in intList:
        if intList[0] <= intList[1]:
            print("do something !!!")
        else:
            print("Fuuuuuuuuck !!!")
"""

#---------------------------------------------------------------------------------------------------------------------
print("Enter as many numbers as you want")
print("Please, be careful to separate eah number by a space")
userInput = input()
# result example ---> "10 20 30"

intList = userInput.rsplit(" ")
# result example ---> ['10', '20', '30']

print(intList)

#lenList =len(intList)

# now I must find a way to analyze this shit.
# idea is " for a length L " ---> " if array.index I is superior to I+" and " if I+ is superior to I++" ---> " list is in order"

for x in intList:
    if intList[0] <= intList[1]:
        print("do something !!!")
    elif intList[0] >= intList[1]:
        print("do something else !!!")
    #elif intList[0] <= len(intList) <= intList[-1]:
    #    print(" Someone help me, this shit is driving me crazy !!!!   :-O ")
    #elif intList[0] >= len(intList) >= intList[-1]:
    #    print(" Je test n'importe quoi !!!!   :-O ")
    elif intList[0] <= intList[+1]:
        print(" WAZZUP !!!!!  :-D ")
    elif intList[0] >= intList[+1]:
        print(" PUTAIN DE MERDE !!!!  >:-O ")
    else:
        print("Fuuuuuuuuck !!!")

"""
for y in intList[0]:
    while y < lenList:
        if y <= y+1:
            print("test 'd'infériorité ! Liste croissante !")
        elif y >= y+1:
            print("test de supériorité ! Liste décroissante ! ")
"""