# Template for code submission
# Name       :Alyssa Chonko
# Email      :alc258@pitt.edu
# Date       :09/06.16
# Class      :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Ch 3 exercise 7 from online courseweb exercises posted
# Example: Starting with Python, Chapter 1, Exercise 3
#
# Notes:
# any notes to the instructor and/or TA goes here

# ...and now let's program with Python

#ask user how many miles they drove
miles=input("How many miles have you driven? ")
#ask user how many gallons of gas they've used
gallons=input("How many gallons of gas have you used? ")
#convert miles to kilometers
kilometers=float(miles*1.6)
#convert gallons to liters
liters= float(gallons*3.785)
#calculate the fuel consumption
fuel_consumption= float(100*liters/kilometers)
#print how many liters the users car consumed
print("Your car has consumed " + str(fuel_consumption) + " liters per 100km of gas")
