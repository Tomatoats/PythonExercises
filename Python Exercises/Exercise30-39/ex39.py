from prettytable import PrettyTable

def Person(num):
    fName = ["John","Tou","Michaela","Jake","Jacquelyn","Sally"]
    lName = ["Johnson","Xiong","Michaelson","Jacobson","Jackson","Webber"]
    position = ["Manager","Software Engineer","District Manager","Programmer","DBA","Web Devoloper"]
    sepdate = ["2016-12-31","2016-10-05","2015-12-19","","","2015-12-18"]
    person = [fName[num],lName[num],position[num],sepdate[num]]
    return person

num = 6
quot = []
table = PrettyTable()
table.field_names = ["Name","Position","Seperation Date"]
for x in range(num):
    per = Person(x)
    table.add_row([per[0] +" " + per[1], per[2],per[3]])
print(table)

