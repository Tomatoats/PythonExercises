#from prettytable import PrettyTable 
from tabulate import tabulate
thislist = []

rows = 12
cols = 12
arr = [[ ((j*12)+(i+1)) for i in range(cols)] for j in range(rows)]
#print(arr)

print(tabulate(arr, tablefmt = "grid"))


#myTable = PrettyTable(["Test1","Test2","Test3","Test4","Test5","Test6","Test7","Test8","Test9","Test10","Test11","Test12"])


#yTable.add_row([arr[0]])
#myTable.add_row([arr[1]])
#print(myTable)
#myTable = PrettyTable(["","","","","","","","","","","",""])
#for y in range(12):
#    for x in range(12):
#        listing = list.append((y*12) +(x+1))
#        myTable.add_row([list])
#        listing = list.clear
#print(myTable)
#arr = [[0]*cols]*rows
#print(arr)
#count = 0
#for y in range(12):
#    for x in range(12):
#        thislist.append((y*12)+(x+1))
#        arr[count][x] = ((y*12)+(x+1))
#        print(arr[y][x])
#mydata = [
#    [arr[0]], [arr[1]], [arr[2]], [arr[3]], [arr[4]], [arr[5]], [arr[6]], [arr[7]], [arr[8]], [arr[9]], [arr[10]], [arr[11]]
#]

