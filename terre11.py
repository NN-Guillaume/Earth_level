""" 24 to 12 """

import array as arr

# Créer un programme qui transforme une heure affichée en format 24h au format 12h
# Attention à midi et minuit.

myHour = int(input())
myMinute = int(input())
symbol = ":"
newTime = [myHour, symbol, myMinute] # working base
#displayTime = ' '.join([str(elem) for elem in newTime])
#displayTime = "basic hour print=  %d : %d " % (myHour, myMinute) # will be displayed in the console

#print(newTime)
#print(displayTime)

#--------------------------------------------------------------------------------------------------------------------------
# goodHour was used to build the program
goodHour = arr.array('i',[
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

#--------------------------------------------------------------------------------------------------------------------------
""" This part was used to build the program """
"""
for x in goodHour :
    if myHour == goodHour.index(x):
        #print("goodHour value is matching !") # FONCTIONNE !!! ce print confirme la condition au dessus  :-)
        pass
    else:
        pass
"""

for x in sillyHour:    
    if myHour == sillyHour.index(x):
        #print("sillyHour value is matching !") # ne fonctionne pas à partir de 13h mais detecte deux fois le type 01hxx
        newTime[0] = sillyHour.index(myHour)


    elif myHour != sillyHour.index(x):
        #print("sillyHour value is NOT matching !") # ne fonctionne pas à partir de 13h mais detecte deux fois le type 01hxx

        if myHour == 13:
            newTime[0] = sillyHour[13]
            #print(newTime)

        elif myHour == 14:
            newTime[0] = sillyHour[14]
            #print(newTime)

        elif myHour == 15:
            newTime[0] = sillyHour[15]
            #print(newTime)

        elif myHour == 16:
            newTime[0] = sillyHour[16]
            #print(newTime)

        elif myHour == 17:
            newTime[0] = sillyHour[17]
            #print(newTime)

        elif myHour == 18:
            newTime[0] = sillyHour[18]
            #print(newTime)

        elif myHour == 19:
            newTime[0] = sillyHour[19]
            #print(newTime)

        elif myHour == 20:
            newTime[0] = sillyHour[20]
            #print(newTime)

        elif myHour == 21:
            newTime[0] = sillyHour[21]
            #print(newTime)

        elif myHour == 22:
            newTime[0] = sillyHour[22]
            #print(newTime)

        elif myHour == 23:
            newTime[0] = sillyHour[23]


# to apply AM or PM
if myHour <= 11:
    #add index 5 to print "AM"
    newTime.append(" AM")
    #pass
elif myHour >= 12:
    #add index 5 to print "PM"
    newTime.append(" PM")
    #pass

#print(newTime)
displayTime = ' '.join([str(elem) for elem in newTime])
print(displayTime)

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