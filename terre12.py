""" 12 to 24 """

# Créer un programme qui transforme une heure affichée en format 12h au format 24h
# Attention à midi et minuit.

import array as arr
import sys

try:
    myHour = int(sys.argv[1])
    myMinute = int(sys.argv[2])
    symbol = ":"
    indicator = str(sys.argv[3])  # automate this to define if it is AM or PM ?
    sillyGrade = indicator.upper()
    newTime = [myHour, symbol, myMinute, sillyGrade]  # that is the working base

    morningHours = arr.array("i", [00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    eveningHours = arr.array("i", [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

    #This part analyse the input and convert the hour (only the number)
    if sillyGrade == "AM":
        for x in morningHours:
            if myHour == morningHours.index(x):
                newTime[0] = morningHours.index(myHour)

    if sillyGrade == "PM":
        for x in eveningHours:

            if myHour != eveningHours.index(x):

                if myHour == 12:
                    newTime[0] = eveningHours[0]

                if myHour == 1:
                    newTime[0] = eveningHours[1]

                if myHour == 2:
                    newTime[0] = eveningHours[2]

                if myHour == 3:
                    newTime[0] = eveningHours[3]

                if myHour == 4:
                    newTime[0] = eveningHours[4]

                if myHour == 5:
                    newTime[0] = eveningHours[5]

                if myHour == 6:
                    newTime[0] = eveningHours[6]

                if myHour == 7:
                    newTime[0] = eveningHours[7]

                if myHour == 8:
                    newTime[0] = eveningHours[8]

                if myHour == 9:
                    newTime[0] = eveningHours[9]

                if myHour == 10:
                    newTime[0] = eveningHours[10]

                if myHour == 11:
                    newTime[0] = eveningHours[11]

    #This part of the code here define the AM or PM
    if sillyGrade == "AM":
        # remove AM
        newTime.pop(3)
    elif sillyGrade == "PM":
        # remove PM
        newTime.pop(3)
    elif sillyGrade != "AM" or sillyGrade != "PM":
        newTime.clear()
        print("which moment of the day is this ?  :-)")

    #Display the final result !
    # turn the array into a string, more eye-friendly to read.
    displayTime = " ".join([str(elem) for elem in newTime])
    # after all that mess, this display the converted hour into the console
    print(displayTime)
    # end !

except ValueError:
    print(" Wrong input ! ")
















# alternative with the "input" statement
"""
myHour = int(input())
myMinute = int(input())
symbol = ":"
indicator = input() # automate this to define if it is AM or PM ?
sillyGrade = indicator.upper()
newTime = [myHour, symbol, myMinute, sillyGrade ] # that is the working base

morningHours = arr.array('i',[
    00,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11
])

eveningHours = arr.array('i',[
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23
])


###This part analyse the input and convert the hour (only the number)
if sillyGrade == "AM":
    for x in morningHours:
        if myHour == morningHours.index(x):
            newTime[0] = morningHours.index(myHour)

if sillyGrade == "PM":
    for x in eveningHours:

        if myHour != eveningHours.index(x):

            if myHour == 12:
                newTime[0] = eveningHours[0]

            if myHour == 1:
                newTime[0] = eveningHours[1]

            if myHour == 2:
                newTime[0] = eveningHours[2]

            if myHour == 3:
                newTime[0] = eveningHours[3]

            if myHour == 4:
                newTime[0] = eveningHours[4]

            if myHour == 5:
                newTime[0] = eveningHours[5]

            if myHour == 6:
                newTime[0] = eveningHours[6]

            if myHour == 7:
                newTime[0] = eveningHours[7]

            if myHour == 8:
                newTime[0] = eveningHours[8]

            if myHour == 9:
                newTime[0] = eveningHours[9]

            if myHour == 10:
                newTime[0] = eveningHours[10]

            if myHour == 11:
                newTime[0] = eveningHours[11]


###This part of the code here define the AM or PM 
if sillyGrade == "AM":
    #remove AM
    newTime.pop(3)
elif sillyGrade == "PM":
    #remove PM
    newTime.pop(3)


###Display the final result !
# turn the array into a string, more eye-friendly to read.
displayTime = ' '.join([str(elem) for elem in newTime])
# after all that mess, this display the converted hour into the console
print(displayTime)
# end !
"""

# The code is working BUT...
# ... I could implement some user imput verification...
# ... an make a sacrific by a fullmoon night to know how to automate some part of the code TT___TT
