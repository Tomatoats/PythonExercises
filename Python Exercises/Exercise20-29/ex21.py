flag = False
month = ""
while flag == False:
    number = input("Please enter the number of the month ")

    match number:
        case '1':
            month = "January"
            flag = True
        case '2':
            month = "February"
            flag = True
        case '3':
            month = "March"
            flag = True
        case '4':
            month = "April"
            flag = True
        case '5':
            month = "May"
            flag = True
        case '6':
            month = "June"
            flag = True
        case '7':
            month = "July"
            flag = True
        case '8':
            month = "August"
            flag = True
        case '9':
            month = "September"
            flag = True
        case '10':
            month = "October"
            flag = True
        case '11':
            month = "November"
            flag = True
        case '12':
            month = "December"
            flag = True
        case _:
            flag = False
            print("Please give me a number inbetween 1 and 12.")
output = "The name of the month is {0}."
print(output.format(month))
