""" 24 to 12 """

# Créer un programme qui transforme une heure affichée en format 24h au format 12h
# Attention à midi et minuit.

import array as arr
import sys

try:
    myHour = int(sys.argv[1])
    myMinute = int(sys.argv[2])
    symbol = ":"
    newTime = [myHour, symbol, myMinute] # that is the working base
    sillyHour = arr.array('i',[
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
        11,
        12,
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


    """ This part analyse the input and convert the hour (only the number) """
    for x in sillyHour:    
        if myHour == sillyHour.index(x):
            #print("sillyHour value is matching !") # ne fonctionne pas à partir de 13h mais detecte deux fois le type 01hxx
            newTime[0] = sillyHour.index(myHour)


        elif myHour != sillyHour.index(x):
            #print("sillyHour value is NOT matching !") # ne fonctionne pas à partir de 13h mais detecte deux fois le type 01hxx

            # haven't found how to simplify this part...  :-(
            if myHour == 13:
                newTime[0] = sillyHour[13]

            elif myHour == 14:
                newTime[0] = sillyHour[14]

            elif myHour == 15:
                newTime[0] = sillyHour[15]

            elif myHour == 16:
                newTime[0] = sillyHour[16]

            elif myHour == 17:
                newTime[0] = sillyHour[17]

            elif myHour == 18:
                newTime[0] = sillyHour[18]

            elif myHour == 19:
                newTime[0] = sillyHour[19]

            elif myHour == 20:
                newTime[0] = sillyHour[20]

            elif myHour == 21:
                newTime[0] = sillyHour[21]

            elif myHour == 22:
                newTime[0] = sillyHour[22]

            elif myHour == 23:
                newTime[0] = sillyHour[23]

    if myHour <= 11:
        #add index[5] to print "AM"
        newTime.append(" AM")
    elif myHour >= 12:
        #add index[5] to print "PM"
        newTime.append(" PM")


    #Display the final result ! 
    # turn the array into a string, more eye-friendly to read.
    displayTime = ' '.join([str(elem) for elem in newTime])
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
newTime = [myHour, symbol, myMinute] # that is the working base
sillyHour = arr.array('i',[
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
    11,
    12,
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


#This part analyse the input and convert the hour (only the number)
for x in sillyHour:    
    if myHour == sillyHour.index(x):
        #print("sillyHour value is matching !") # ne fonctionne pas à partir de 13h mais detecte deux fois le type 01hxx
        newTime[0] = sillyHour.index(myHour)


    elif myHour != sillyHour.index(x):
        #print("sillyHour value is NOT matching !") # ne fonctionne pas à partir de 13h mais detecte deux fois le type 01hxx

        # haven't found how to simplify this part...  :-(
        if myHour == 13:
            newTime[0] = sillyHour[13]

        elif myHour == 14:
            newTime[0] = sillyHour[14]

        elif myHour == 15:
            newTime[0] = sillyHour[15]

        elif myHour == 16:
            newTime[0] = sillyHour[16]

        elif myHour == 17:
            newTime[0] = sillyHour[17]

        elif myHour == 18:
            newTime[0] = sillyHour[18]

        elif myHour == 19:
            newTime[0] = sillyHour[19]

        elif myHour == 20:
            newTime[0] = sillyHour[20]

        elif myHour == 21:
            newTime[0] = sillyHour[21]

        elif myHour == 22:
            newTime[0] = sillyHour[22]

        elif myHour == 23:
            newTime[0] = sillyHour[23]


#This part of the code here define the AM or PM 
if myHour <= 11:
    #add index[5] to print "AM"
    newTime.append(" AM")
elif myHour >= 12:
    #add index[5] to print "PM"
    newTime.append(" PM")


#Display the final result ! 
# turn the array into a string, more eye-friendly to read.
displayTime = ' '.join([str(elem) for elem in newTime])
# after all that mess, this display the converted hour into the console
print(displayTime)
# end !
"""
# The code is working BUT...
#... I could implement some user imput verification...
#... an make a sacrifice by a fullmoon night to know how to automate some part of the code TT___TT

#--------------------------------------------------------------------------------------------------------------------------
""" Those parts below were failing attempt to build the program """

"""
goodHour = [
    "00:00",
    "01:00",
    "02:00",
    "03:00",
    "04:00",
    "05:00",
    "06:00",
    "07:00",
    "08:00",
    "09:00",
    "10:00",
    "11:00",
    "12:00",
    "13:00",
    "14:00",
    "15:00",
    "16:00",
    "17:00",
    "18:00",
    "19:00",
    "20:00",
    "21:00",
    "22:00",
    "23:00"
]

sillyHour = [
    "00:00 AM",
    "01:00 AM",
    "02:00 AM",
    "03:00 AM",
    "04:00 AM",
    "05:00 AM",
    "06:00 AM",
    "07:00 AM",
    "08:00 AM",
    "09:00 AM",
    "10:00 AM",
    "11:00 AM",
    "12:00 PM",
    "13:00 PM",
    "14:00 PM",
    "15:00 PM",
    "16:00 PM",
    "17:00 PM",
    "18:00 PM",
    "19:00 PM",
    "20:00 PM",
    "21:00 PM",
    "22:00 PM",
    "23:00 PM"
]

#hourTable = { goodHour:sillyHour }

hourTable = {
    "00:00" : "00:00 AM",
    "01:00" : "01:00 AM",
    "02:00" : "02:00 AM",
    "03:00" : "03:00 AM",
    "04:00" : "04:00 AM",
    "05:00" : "05:00 AM",
    "06:00" : "06:00 AM",
    "07:00" : "07:00 AM",
    "08:00" : "08:00 AM",
    "09:00" : "09:00 AM",
    "10:00" : "10:00 AM",
    "11:00" : "11:00 AM",
    "12:00" : "12:00 PM",
    "13:00" : "01:00 PM",
    "14:00" : "02:00 PM",
    "15:00" : "03:00 PM",
    "16:00" : "04:00 PM",
    "17:00" : "05:00 PM",
    "18:00" : "06:00 PM",
    "19:00" : "07:00 PM",
    "20:00" : "08:00 PM",
    "21:00" : "09:00 PM",
    "22:00" : "10:00 PM",
    "23:00" : "11:00 PM"
}
"""