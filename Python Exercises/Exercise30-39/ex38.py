def filterEvenNumbers(arr):
    even = []
    toAdd = ""
    for x in arr:
        if int(x) %2 == 0:
            toAdd = x + " "
            even.append(toAdd)
    return even


numbers = input("Enter a list of numbers, seperated by spaces ")
arr = numbers.split(" ")
even = filterEvenNumbers(arr)
actual = "".join(str(x) for x in even)
output = "The even numbers are {0}"
print(output.format(actual))