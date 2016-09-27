# Template for code submission
# Name       :Alyssa Chonko
# Email      :alc258@pitt.edu
# Date       :09/06.16
# Class      :CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Ch 3 exercise 2 page 115
#
# Notes:
# any notes to the instructor and/or TA goes here

# ...and now let's program with Python

#ask user for the length and width of the first rectangle
width1=input("What is the width of the first rectangle? ")
height1=input("What is the height of the first rectangle? ")
#ask user for length and width of second triangle
width2=input("What is the width of the second rectangle? " )
height2=input("what is the height of the second rectangle? ")
#calculate area of rectangle 1
area1=width1*height1
#calculate area of rectangle 2
area2=width2*height2
if area1>area2:
    print("Rectangle 1 has a greater area")
else:
    if area2>area1:
        print("Rectangle 2 has a greater area")
    else:
        if area1==area2:
            print("Rectangle 1 and 2 have equal areas")

