def main():
    kilometers_entered = float(input("Enter your distance in miles: "))
    kilometers_to_miles(kilometers_entered)
def kilometers_to_miles(kilometers):
    miles = kilometers * .6214
    print("Your distance in miles is "+str(miles)+"")
main()


