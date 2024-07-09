from prettytable import PrettyTable

def printTable(listed):
    table = PrettyTable()
    table.field_names = ["Last","First","Salary"]
    for x in listed:
        table.add_row(x)
    print(table)
    mystring = table.get_string()
    return mystring

def printtoFile(tableString):
    fileOut = open("Exercise40-50\ex42\ex42_out.txt","w")
    fileOut.write(tableString)
    fileOut.close


filein = open("Exercise40-50\ex42\ex42_in.txt","r")
names = filein.readlines()
filein.close()
sep = []
listed = []
for x in names:
    sep = list(x.split(","))
    if "\n" in sep[2]:
        sep[2] = sep[2].replace("\n","")
    listed.append(sep)

tableString = printTable(listed)
printtoFile(tableString)
