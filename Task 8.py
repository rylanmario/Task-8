# Name: Task 8.py
# Author: Rylan Fessey
# Date created: November 22nd, 2022
# Date last modified: November 22nd, 2022
# Purpose: The purpose of this program is to take user input on temperture or speed and convert to another format.
#This is version 2.0, which includes bug fixes and improvements over version 1.0


convertion = int(input("Would you like to convert speed or temperture? Type 1 for temperture or 2 for speed: "))
while  not(convertion == 1 or convertion == 2):
    convertion=int(input("Please enter a valid option, 1 or 2: "))
#This is the start of the program and contains the loop for when an invalid value is submitted

def temperture():
    tempConvert = int(input("Type 1 to convert to Farenheit or 2 to convert to Celsius: "))
    if tempConvert == 1:
        tempC = float(input("What is the temperture you are converting from in Celsius?: "))
        cConvertion = (tempC * 9/5) + 32
        print(tempC, "degrees C converted is", round(cConvertion,2), "degrees F")
    elif tempConvert == 2:
        tempF = float(input("What is the temperture you are converting from in Farenheit?: "))
        fConvertion = (tempF - 32) * 5/9
        print(tempF, "degrees F, converted is", round(fConvertion,2), "degrees C")
    else:
        print("Please enter a valid option. Valid options are 1 or 2.")
#Defines the tempurture convertion function

def speed():
    speedConvert = int(input("Type 1 to convert KM/h to MPH, or type 2 to convert MPH to KM/h: "))
    if speedConvert == 1:
        speedKPH = float(input("What is the speed in kilometers?: "))
        KPHConvert = speedKPH / 1.609
        print(speedKPH, "KM/h converted is", round(KPHConvert,2), "MPH")
    elif speedConvert == 2:
        speedMPH = float(input("What is the speed in miles?: "))
        MPHConvert = speedMPH * 1.609
        print(speedMPH, "MPH converted is", round(MPHConvert,2), "Km/h.")
#Defines the speed convertion function

if convertion == 1:
    temperture()
#Calls the temp conversion based on the user input
elif convertion == 2:
    speed()
#Calls the speed conversion based on user input


input("Press enter to exit:")
exit()
#Exit menu for program