#calculate calories burned for five different times 10-30
#first workout time
start=10
#last workout time
last=31
#Increment workout times are increased by
increment=5
#how many calories are burned per minute
conversion=4.2
#print the table headings
print("Workout time\tCalories Burned")
print("-----------------------------")
#print the calories burned
for time in range(start,last,increment):
    calories=time*conversion
    print(+ time +  + calories+)