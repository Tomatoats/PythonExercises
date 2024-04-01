principal  = input("Enter Principal ")
rate = input("Enter rate of interest as a percentage but without the % ")
years = input("Enter years waiting ")
times = input("Enter amount of times compounded per year? ")
anter = str(round(int(principal)*(1 + (float(rate)/100)/int(times))**(int(times)*int(years)),2))

print("After {0} years at {1}% compunded {2} times per year, the investment will be worth ${3}.".format(years,rate,times,anter))