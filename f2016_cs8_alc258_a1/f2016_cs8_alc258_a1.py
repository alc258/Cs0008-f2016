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

unit=input("Are you using USC? Answer 'no' if using Metric. ") #ask user if they are using USC
if unit=="yes":                                               #if user is using usc
    distance=input("How many miles have you driven? ")        #ask user to input the distance driven
    gas=input("How many gallons have you used? ")             #ask user to input the amount of gas used
    miles=distance                                            #assaiging distance input to miles variable
    gallons=gas                                               #assaigning gas input to gallons variable
    kilometers=distance*1.60924                               #convert miles to km
    liters=3.78541*gallons                                    #convert gallons to liters
    mpg=(miles/gallons)                                       #calculate consumption in USC
    lpkm=100*(liters/kilometers)                              #calculate fuel consumption in metric
if unit=="no":                                                #if user answers that they are using metric
    distance=input("How many kilometers have you driven? ")   #ask user to input the distance driven in metric
    gas=input("How many liters have you used? ")              #ask user to input gas used in metric
    kilometers=distance                                       #assaign distance input to kilometers
    liters=gas                                                #assaign gas input to liters
    miles=distance*.264172                                    #convert km to miles
    gallons=gas*.621371                                       #convert liters to gallons
    mpg=(miles/gallons)                                       #calculate consumption in USC
    lpkm=100*(liters/kilometers)                              #calculate consumption in metric
if kilometers>20:                                             #Set conditions/parameters for fuel efficiency
    efficiency="extremely poor"                               #assaigns efficiency to a string for the print function
elif 15<kilometers>=20:
    efficiency="poor"
elif 10<kilometers>=15:
    efficiency="average"
elif 8<kilometers>=10:
    efficiency="good"
elif kilometers<=8:
    efficiency="excellent"
                                                            #prints the results given the users input and formats them
                                                            #so they are in 3 columns and each number has a width of 6
                                                            #and 3 decimal places
print("                             ", "USC     ",                  "Metric")
print("Distance______________:",format(miles, "10.3f"),format(kilometers, "10.3f"))
print("Gas___________________:",format(gallons, "10.3f"),format(liters, "10.3f"))
print("consumption___________:",format(mpg, "10.3f"), format(lpkm, "10.3f"))
print("Gas consumption rating: "+ str(efficiency)+" ")


