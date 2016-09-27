# Template for code submission
# Name       :Alyssa Chonko
# Email      :alc258@pitt.edu
# Date       :09/19/16
# Class      :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Ch 3 exercise 7 page 116
# Notes:
# any notes to the instructor and/or TA goes here

# ...and now let's program with Python

#ask user to enter color1
color1=input("What is your first primary color? ")

#ask user to input color2
color2=input("What is your second primary color? ")
#make sure color1 and color2 are primary colors
if color1!="red" and color1!="blue" and color1!="yellow":
    print("Error color 1 is not a primary color")
if color2!="red" and color2!="blue" and color2!="yellow":
    print("Error color 2 is not a primary color.")
#Print the mixtures of the primary colors
if color1== "blue" and color2== "red":
    print("This makes purple")
elif color1=="red" and color2=="blue":
    print("This makes purple")
elif color1=="yellow" and color2=="blue":
    print("This makes green")
elif color1=="blue" and color2=="yellow":
    print("This makes green")
elif color1=="red" and color2=="yellow":
    print("This makes orange")
elif color1=="yellow" and color2=="red":
    print("this makes orange")
