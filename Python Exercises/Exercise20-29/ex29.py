flag = False
flag1 = False
flag2 = False
while flag == False:
    rate = input("What is the rate of return? ")
    try:
        float(rate)
    except ValueError:
        print("Sorry that's not a valid input.")
        continue
    else:
        flag1 = True
    if float(rate) == 0:
        print("Sorry, that is not a valid input.")
    else: 
        flag2 = True

    if flag1 == True and flag2 == True:
        flag = True

years = 72/float(rate)

print("It will take",years," years to double your initial investment.")