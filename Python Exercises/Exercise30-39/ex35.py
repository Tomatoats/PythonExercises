import random
flag = False
names = []
while flag == False:
    toAdd = input("Enter a name: ")
    if toAdd == "":
        flag = True
    else:
        names.append(toAdd)

name = random.choice(names)

output = "The winner is... {0}!"
print(output.format(name))
