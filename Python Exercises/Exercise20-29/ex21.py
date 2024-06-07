flag1 = False
while flag1 == False:
    number = input("Please enter the number of the month ")
    try:
        int(number)
    except ValueError:
        print("ayo mate i need numbers.")
    
    else:
        flag1 = True

    