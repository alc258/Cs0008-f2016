years=input("How many years?")
for rain in range(years):
    total=0.0
    for months in range(12):
        rainfall=input("Enter the amount of rainfall this month: ")
        month=total+months
        total_rainfall=rainfall/2
        print(str(months) + ":" + str(rainfall) + ":" + str(total_rainfall))


