import math
from statistics import stdev

def average(numbers):
    total = 0
    for x in numbers:
        total = total + float(x)
    divide = len(numbers)
    avg = total / divide
    return avg

def maximum(numbers):
    return max(numbers)

def minimum(numbers):
    return min(numbers)

def std(numbers):
    return stdev(numbers)

def validate(toAdd):
    try:
        float(toAdd)
    except ValueError:
        print("That is not a number")
        toAdd = -1
    return toAdd

def printNumbers(numbers):
    print("Numbers:")
    for x in numbers:
        print(x)
    print("The average is",average(numbers))
    print("the minimum is",minimum(numbers))
    print("the maximum is",maximum(numbers))
    #print("the standard deviation is",std(numbers))

def toNumb(numbers):
    newNumb = []
    for x in numbers:
        float(x)
        newNumb.append(x)
    return newNumb

numbers = []
flag = False
while flag == False:
    toAdd = input("Enter a number ")
    if toAdd == "done":
        numbers = toNumb(numbers)
        flag = True
    else: 
        number = validate(toAdd)
        if number != -1:
            numbers.append(number)

printNumbers(numbers)
