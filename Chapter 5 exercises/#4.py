def main():
    loan_input=input("Enter the amount you spend a month on you cars loan payment: ")
    insurance_input=input("Enter the amount you spend a month on car insurance: ")
    gas_input=input("Enter the amount you spend on gas every month: ")
    oil_input=input("Enter the amount you spend on car oil every month: ")
    tire_input=input("Enter the amount you spend every month on your cars tires: ")
    maintenance_input=input("Enter the amount you spend every month on car maintenance: ")
    monthly_sum(loan_input,insurance_input,gas_input,oil_input,tire_input,maintenance_input)
    annual_sum(loan_input,insurance_input,gas_input,oil_input,tire_input,maintenance_input)
def monthly_sum(monthly_loan,monthly_insurance,monthly_gas,monthly_oil,monthly_tire,monthly_maintenance):
    monthly=monthly_loan+monthly_insurance+monthly_gas+monthly_oil+monthly_tire+monthly_maintenance
    print("The monthly amount you spend on your car is "+str(monthly)+" dollars")
def annual_sum(monthly_loan,monthly_insurance,monthly_gas,monthly_oil,monthly_tire,monthly_maintenance):
    annual=(12*monthly_loan)+(12*monthly_insurance)+(12*monthly_gas)\
           +(12*monthly_oil)+(12*monthly_tire)+(12*monthly_maintenance)
    print("The annual amount you spend on your car is  "+str(annual)+" dollars")
main()