def remove(employees):
    flag = False
    while flag == False:
        name = input("Enter an employee name to remove: ")

        if name in employees:
            employees.remove(name)
            flag = True
        else:
            print("That name is not in the list.")

def printNames(employees):
    for x in employees: 
        print(x)

print("There are 5 employees:")
employees = ["John Smith","Jackie Jackson", "Chris Jones", "Amanda Cullen"]
employees.append("Jeremy Goodwin")

printNames(employees)

remove(employees)

print("There are ",len(employees)," employees: ")
printNames(employees)
