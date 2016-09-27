# Template for code submission
# Name       :Alyssa Chonko
# Email      :alc258@pitt.edu
# Date       :09/06.16
# Class      :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Ch 3 exercise 3 page 115
# Notes:
# any notes to the instructor and/or TA goes here

# ...and now let's program with Python

#ask user for their age
age=input("What is your age? ")
#determine what that age classifies the user as
if age<=1:
    print("You are an infant.")
elif 1<age<13:
    print("You are a child.")
elif 13<=age<20:
    print("You are a teenager.")
elif age>=20:
    print("You are an adult.")
