def main():
    replace_price = input("Enter the replacement price of your building or home: ")
    minimum_insurance(replace_price)
def minimum_insurance(amount):
    insurance = amount *.80
    print("You should purchase at least "+str(insurance)+" dollars in insurance")
main()