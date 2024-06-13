import re
first = input("Enter your first name ")
second = input("Enter your last name ")
zip = input("Enter your zip code ")
id = input("Enter your  ID  ")

def validatename(string):
    if len(string) > 1:
        return True
    else:
        return False
    
def validateID(string):
    x = re.findall("[A-Z][A-Z]-[0-9][0-9][0-9][0-9]",string)
    if len(x) > 0 and len(string) == 7: return True
    else: return False

def validateZip(string):
    x = re.findall("\d",string)
    if len(x) == 5 and len(string) == 5: return True
    else: return False

def validateInputs(string1,string2,string3,string4):
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    if validatename(string1) == True:
        flag1 = True
    else:
        print("The first name must be at least 2 characters long.")

    if validatename(string2) == True:
        flag2 = True
    else:
        print("The last name must be at least 2 characters long.")

    if validateZip(string3) == True:
        flag3 = True
    else:
        print("zip codes must be 5 numbers long.")
    
    if validateID(string4) == True:
        flag4 = True 
    else:
        print("The employee ID must be in the format of AA-1234")   
    
    if flag1 == True and flag2 == True and flag3 == True and flag4 == True:
        print("There were no errors found.")

validateInputs(first,second,zip,id)
