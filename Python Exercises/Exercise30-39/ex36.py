import math
import numpy as np

def average(numbers):
    total = 0
    for x in numbers:
        total = total + float(x)
    divide = len(numbers)
    avg = total / divide
    return avg

def maximum(numbers):
    largest = 1
    for x in numbers:
        if int(x) > largest:
            largest = int(x)
    return largest

def minimum(numbers):
    return min(numbers)

def std(numbers):
    avg = average(numbers)
    sq_diff = [(float(x) - avg) ** 2 for x in numbers] #this is wizardry
    variance = sum(sq_diff) / (len(sq_diff))
    stddev = variance ** 0.5
    return stddev

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
    print("the standard deviation is",round(std(numbers),2))

def toNumb(numbers):
    newNumb = []
    for x in numbers:
        float(x)
        newNumb.append(x)
    return newNumb

hold = []
flag = False
while flag == False:
    toAdd = input("Enter a number ")
    if toAdd == "done":
        numbers = toNumb(hold)
        flag = True
    else: 
        number = validate(toAdd)
        if number != -1:
            hold.append(number)

printNumbers(numbers)
