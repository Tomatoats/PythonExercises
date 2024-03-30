gallon = 350

length = input("what da length be ")
width = input("What da width be ")

area = str(int(length) *int(width))

if int(area) % 350 == 0:
    gallons = str(int(area) // gallon)

else:
    gallons = str((int(area) // gallon) + 1)

print("You need " + gallons + " gallons of paint for  an area of "+ area + " feet.")