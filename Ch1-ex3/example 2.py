# Name       :Alyssa Chonko
# Email      :alc258@pitt.edu
# Date       :09/06.16
# Class      :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# description of this file goes here
# Example: Starting with Python, Chapter 1, Exercise 3
#
# Notes:
# ch 2 ex.7

kilometers=input('How many kilometers have you driven? ') #asking how many miles the user has driven
gas=input('How many liters of gas have you used? ') # asking how many liters of gas they have used
fuel_consumption=float(100*gas/kilometers) #fuel consumption equation
print("Your car has consumed " + str(fuel_consumption) + " Liters of gas") #telling them how much gas theyve used
