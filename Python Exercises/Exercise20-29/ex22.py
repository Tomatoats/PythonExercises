numb1,numb2,numb3 = input("Enter 3 numbers, seperated by a comma ").split(',')

large = 0
n1 = int(numb1)
n2 = int(numb2)
n3 = int(numb3)
if n1 > n2:
    if n1 > n3:
        large = n1
    else:
        if n3 > n2:
            large = n3
        else:
            large = n2
else:
    if n2 > n3:
        large = n2
    else:
        if n3 > n1:
            large = n3
        else:
            large = n1
output = "the largest number is {0}"
print(output.format(large))