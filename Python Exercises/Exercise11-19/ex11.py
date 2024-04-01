
euros = input("How many euros do you have? ")
rate =  input("What is the currency rate? ")
dollar = str(round(float(euros) * float(rate),2))
print("{0} euros at a rate of {1} is {2} U.S Dollars".format(euros,rate,dollar)) 