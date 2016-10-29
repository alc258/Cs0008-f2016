#max number of days
max=5
#initialize an accumulator
total=0
print("This program calculates the total number of bugs collected")
#Get number of bugs and accumulate them
for counter in range(max):
    bugs=int(input("Enter the number of bugs collected today "))
    total=total+bugs
#print the total number of bugs
print("The total number of bugs you collected is", total)