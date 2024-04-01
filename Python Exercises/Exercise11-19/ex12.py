principal  = input("Enter Principal ")
rate = input("Enter rate of interest as a percentage but without the % ")
years = input("Enter years waiting ")
anter = str(round(int(principal)*(1 + (float(rate)/100)*float(years)),2))

print("After {0} years at {1}%, the investment will be worth ${2}.".format(years,rate,anter))