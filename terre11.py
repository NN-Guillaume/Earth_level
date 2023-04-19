""" 24 to 12 """

# Créer un programme qui transforme une heure affichée en format 24h au format 12h
# Attention à midi et minuit.

# the idea is to get this:
# morning ---> from "10:30" to "10:30 AM"
# evening ---> from "21:45" to "09:45 AM"

# the danger:
# morning ---> from "12:00" to "12:00 AM"
# evening ---> from "00:15" to "12:15 AM"
print("Please, respect the following hour scheme --->   hh:mm   ")
myHour = input("enter your hour here: ")

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

hourTable = { goodHour:sillyHour }
"""
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


for val in hourTable:
    if myHour == val.keys(): #AttributeError: 'str' object has no attribute 'keys'
        print("it seems to works up there !")
        #print(val.keys())
        #print(val.values())
        #weirdHour = val.values()
        #print(weirdHour)