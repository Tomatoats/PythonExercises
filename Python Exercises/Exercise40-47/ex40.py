from prettytable import PrettyTable
def Person(num):
    id0 = ["John Johnson","Manager","2016-12-31"]
    id1 = ["Tou Xiong","Software Engineer","2016-10-05"]
    id2 = ["Michaela Michaelson","District Manager","2015-12-19"]
    id3 = ["Jake Jacobson","Programmer",""]
    id4 = ["Jacquelyn Jackson","DBA",""]
    id5 = ["Sally Webber","Web Deveolper","2015-12-18"]
    match num:
        case 0: return id0
        case 1: return id1
        case 2: return id2
        case 3: return id3 
        case 4: return id4
        case 5: return id5

def results(toFind, total,num):
    numbers = []
    toMake = []
    for x in range(5):
        listing = Person(x)
        if any(toFind in word for word in listing):
            numbers.append(x)
        else:
            numbers.append(-1)
    for x in numbers:
        if x != -1:
            toMake.append(numbers.index(x))
    print(numbers)
    print(toMake)
    refined = list(map(Person,toMake))
    printTable(refined)
    


def printTable(total):
    table = PrettyTable()
    table.field_names = ["Name","Position","Seperation Date"]
    for x in total:
        table.add_row(x)
    print(table)


num = 5
total = list(map(Person, range(num)))

printTable(total)

toFind = input("Enter a search string ")

print("Results:")

results(toFind,total,num)

    