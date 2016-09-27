# Template for code submission
# Name       :Alyssa Chonko
# Email      :alc258@pitt.edu
# Date       :09/19/16
# Class      :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Ch 3 exercise 4 page 116
# Notes:
# any notes to the instructor and/or TA goes here

# ...and now let's program with Python

#ask user to enter a number
x=input("Enter a number between 1 and 10. ")
#assaign x to a roman numeral
if x==1:
    print("I")
elif x==2:
    print("II")
elif x==3:
    print("III")
elif x==4:
    print("IV")
elif x==5:
    print("X")
elif x==6:
    print("VII")
elif x==7:
    print("VII")
elif x==8:
    print("VIII")
elif x==9:
    print("IX")
elif x==10:
    print("X")
#Make an error if number is not between 1 and 10
if x<1:
    print("Error number is not between 1 and 10.")
else:
        if x>10:
            print("Error number is not between 1 and 10")
