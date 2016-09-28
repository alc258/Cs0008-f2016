# Template for code submission
# Name       :Alyssa Chonko
# Email      :alc258@pitt.edu
# Date       :09/30/16
# Class      :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Assignment 1
# Notes:

# ...and now let's program with Python

unit=input("Are you using USC? ")                             ##ask user if they are using USC
if unit=="yes":                                               #if user is using usc
    distance=input("How many miles have you driven? ")        #ask user to input the distance driven
    gas=input("How many gallons have you used? ")             #ask user to input the amount of gas used
    kilometers=distance*1.60924                               #convert miles to cm
    liter=3.78541                                             #convert gallons to liters
    cm=(liter/100)*kilometers                                 #find cm to find efficiency later
if unit=="no":
    distance=input("How many kilometers have you driven? ")   #ask user to input the distance driven in metric
    gas=input("How many liters have you used? ")              #ask user to input gas used in metric
    miles=distance*.264172                                    #convert km to miles
    gallons=gas*.621371                                       #convert liters to gallons
    cm=(gas/100)*distance                                     #calculate cm for efficiency
if cm>20:                                                     #assagin cm to fuel consumption rating
    efficiency="extremely poor"
elif 15<cm>=20:
    efficiency="poor"
elif 10<cm>=15:
    efficiency="average"
elif 8<cm>=10:
    efficiency="good"
elif cm<=8:
    efficiency="excellent"


