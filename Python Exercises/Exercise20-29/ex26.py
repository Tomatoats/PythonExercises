import math
bal = input("What is your balance? ")
apr = input("What is the apr on the card(as a percent?) ")
monthly = input ("What is the monthly payment you can make? ")
output = "It will take you {0} months to pay this card."
daily = (float(apr)/100)/365
part = 1 + (float(bal)/float(monthly)) * (1 - (1 + daily)**30)
partly = math.log10(part)

months = round((-1/30) * partly / math.log(1+daily,10),0) +1
print(output.format(months))