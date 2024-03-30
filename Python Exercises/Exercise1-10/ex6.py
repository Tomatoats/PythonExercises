import datetime
age = input("how old ye be ")
retire = input ("How old ye not wanna work ")
current = datetime.datetime.now()
year = int(current.year)
years_to_retire = int(retire) - int(age)
retire_year = int(year) + int(years_to_retire)

line1 = "You have " + str(years_to_retire) + " till you can retire."
line2 = "It's " + str(year) + ", so you can retire in " + str(retire_year)
output = line1 + "\n" + line2
print(output)