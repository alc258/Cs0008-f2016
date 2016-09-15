#ask user how many miles they drove
miles=input("How many miles have you driven? ")
#ask user how many gallons of gas they've used
gallons=input("How many gallons of gas have you used? ")
#convert miles to kilometers4
kilometers=float(miles*1.6)
#convert gallons to liters
liters= float(gallons*3.785)
#calculate the fuel consumption
fuel_consumption= float(100*liters/kilometers)
print("Your car has consumed " + str(fuel_consumption) + " liters per 100km of gas")
